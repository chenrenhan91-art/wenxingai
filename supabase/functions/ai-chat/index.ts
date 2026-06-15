// Supabase Edge Function: ai-chat
const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};
const AI_API_URL = 'https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions';
// 模型按优先级排列：额度耗尽(403 AllocationQuota)时自动降级到下一个
const AI_MODELS = [
  'deepseek-v4-flash',          // 主力：100万免费token，到2026/07/24
  'qwen3.6-flash-2026-04-16',   // 备用1：100万免费token，到2026/07/17
  'qwen3.5-flash',              // 备用2：100万免费token，到2026/05/25
  'qwen-turbo',                 // 兜底：付费，始终可用
];
const MAX_PROMPT_CHARS = 6000;
const MAX_SYSTEM_CHARS = 12000;

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: CORS_HEADERS });
  }
  try {
    const supabaseUrl    = Deno.env.get('SUPABASE_URL');
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY');
    const aiApiKey   = Deno.env.get('DASHSCOPE_API_KEY');

    const authHeader = req.headers.get('Authorization');
    if (!authHeader || !authHeader.startsWith('Bearer ')) {
      return json({ error: 'UNAUTHORIZED' }, 401);
    }
    const token = authHeader.slice(7);

    const userResp = await fetch(supabaseUrl + '/auth/v1/user', {
      headers: { 'Authorization': 'Bearer ' + token, 'apikey': serviceRoleKey },
    });
    if (!userResp.ok) return json({ error: 'UNAUTHORIZED' }, 401);
    const userJson = await userResp.json();
    const userId = userJson && userJson.id;
    if (!userId) return json({ error: 'UNAUTHORIZED' }, 401);

    const body = await req.json().catch(() => ({}));
    const prompt = (body && body.prompt) || '';
    const systemInstruction = (body && body.systemInstruction) || '';
    if (!prompt.trim()) return json({ error: 'BAD_REQUEST' }, 400);
    if (prompt.length > MAX_PROMPT_CHARS || systemInstruction.length > MAX_SYSTEM_CHARS) {
      return json({
        error: 'PAYLOAD_TOO_LARGE',
        message: `请求内容过长，请缩短问题后重试（问题≤${MAX_PROMPT_CHARS}字）。`,
      }, 413);
    }
    if (!aiApiKey) return json({ error: 'CONFIG_ERROR' }, 500);

    const profileResp = await fetch(
      supabaseUrl + '/rest/v1/profiles?user_id=eq.' + userId + '&select=is_pro,remaining_quota',
      { headers: { 'Authorization': 'Bearer ' + serviceRoleKey, 'apikey': serviceRoleKey } },
    );
    if (!profileResp.ok) return json({ error: 'PROFILE_NOT_FOUND' }, 404);
    const profiles = await profileResp.json();
    const profile = profiles && profiles[0];
    if (!profile) return json({ error: 'PROFILE_NOT_FOUND' }, 404);
    if (!profile.is_pro && profile.remaining_quota <= 0) {
      return json({ error: 'NO_QUOTA', message: '免费额度已用完，请升级专业版。' }, 402);
    }

    const rateLimit = await consumeRateLimit(supabaseUrl, serviceRoleKey, userId, !!profile.is_pro);
    if (!rateLimit.allowed) {
      return json({
        error: 'RATE_LIMITED',
        code: rateLimit.error,
        message: rateLimit.message,
        retry_after: rateLimit.retry_after,
      }, 429);
    }

    if (!profile.is_pro) {
      await fetch(supabaseUrl + '/rest/v1/profiles?user_id=eq.' + userId, {
        method: 'PATCH',
        headers: {
          'Authorization': 'Bearer ' + serviceRoleKey,
          'apikey': serviceRoleKey,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ remaining_quota: profile.remaining_quota - 1 }),
      });
    }

    const messages = [];
    if (systemInstruction.trim()) messages.push({ role: 'system', content: systemInstruction });
    messages.push({ role: 'user', content: prompt });

    let text = '';
    let lastError = '';
    for (const model of AI_MODELS) {
      const aiResp = await fetch(AI_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + aiApiKey,
        },
        body: JSON.stringify({ model, messages, max_tokens: 1500, temperature: 0.7 }),
      });

      if (aiResp.ok) {
        const data = await aiResp.json();
        text = (data && data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content) || '星象模糊，无法解读。';
        console.log('AI model used:', model);
        break;
      }

      const errText = await aiResp.text().catch(() => '');
      console.error('model', model, 'error:', aiResp.status, errText.slice(0, 200));
      // 403 AllocationQuota = 免费额度耗尽，继续尝试下一个模型
      if (aiResp.status === 403 && errText.includes('AllocationQuota')) {
        lastError = errText;
        continue;
      }
      // 其他错误直接返回
      return json({ error: 'AI_ERROR', message: 'AI 服务暂时不可用，请稍后再试。' }, 502);
    }

    if (!text) {
      console.error('All models exhausted. Last error:', lastError.slice(0, 200));
      return json({ error: 'AI_ERROR', message: 'AI 服务暂时不可用，请稍后再试。' }, 502);
    }
    return json({ text }, 200);
  } catch (e) {
    console.error('unexpected error:', e);
    return json({ error: 'INTERNAL_ERROR' }, 500);
  }
});

async function consumeRateLimit(
  supabaseUrl: string,
  serviceRoleKey: string,
  userId: string,
  isPro: boolean,
) {
  const resp = await fetch(supabaseUrl + '/rest/v1/rpc/consume_ai_rate_limit', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer ' + serviceRoleKey,
      'apikey': serviceRoleKey,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ p_user_id: userId, p_is_pro: isPro }),
  });

  if (!resp.ok) {
    const err = await resp.text().catch(() => '');
    console.error('rate limit rpc error:', resp.status, err.slice(0, 200));
    return {
      allowed: false,
      error: 'RATE_LIMIT_UNAVAILABLE',
      message: '风控校验失败，请稍后再试。',
      retry_after: 30,
    };
  }

  const result = await resp.json().catch(() => ({}));
  return {
    allowed: !!result.allowed,
    error: result.error || 'RATE_LIMITED',
    message: result.message || '请求过于频繁，请稍后再试。',
    retry_after: Number(result.retry_after) || 30,
  };
}

function json(body, status) {
  return new Response(JSON.stringify(body), {
    status,
    headers: Object.assign({}, CORS_HEADERS, { 'Content-Type': 'application/json' }),
  });
}
