// Supabase Edge Function: ai-chat
const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
};
const AI_API_URL = 'https://api.deepseek.com/chat/completions';
// DeepSeek 官方账户当前可用模型，按优先级自动降级
const AI_MODELS = [
  'deepseek-v4-flash',
  'deepseek-v4-pro',
];
// 命盘上下文可能较长，仅拦截异常超大请求（防脚本灌包）
const MAX_TOTAL_CHARS = 80000;

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: CORS_HEADERS });
  }
  try {
    const supabaseUrl    = Deno.env.get('SUPABASE_URL');
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY');
    // 兼容现有 Supabase Secret 名称，方便无中断迁移到 DEEPSEEK_API_KEY。
    const aiApiKey = Deno.env.get('DEEPSEEK_API_KEY') || Deno.env.get('DASHSCOPE_API_KEY');

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
    if ((prompt.length + systemInstruction.length) > MAX_TOTAL_CHARS) {
      return json({
        error: 'PAYLOAD_TOO_LARGE',
        message: '请求内容异常过长，请缩短后重试。',
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
  try {
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
      console.error('rate limit rpc error (fail-open):', resp.status, err.slice(0, 200));
      return { allowed: true };
    }

    const result = await resp.json().catch(() => ({}));
    if (result.allowed) return { allowed: true };
    return {
      allowed: false,
      error: result.error || 'RATE_LIMITED',
      message: result.message || '请求过于频繁，请稍后再试。',
      retry_after: Number(result.retry_after) || 30,
    };
  } catch (e) {
    console.error('rate limit rpc exception (fail-open):', e);
    return { allowed: true };
  }
}

function json(body, status) {
  return new Response(JSON.stringify(body), {
    status,
    headers: Object.assign({}, CORS_HEADERS, { 'Content-Type': 'application/json' }),
  });
}
