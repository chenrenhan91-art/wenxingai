// Supabase Edge Function: admin-list
// 用途：管理员后台查询所有用户（邮箱 + 邀请码 + 专业版状态 + 额度）
// 安全：验证 ADMIN_SECRET 环境变量，Service Role Key 不暴露到前端

const CORS_HEADERS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'content-type, x-admin-secret',
};

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: CORS_HEADERS });
  }

  try {
    const adminSecret = Deno.env.get('ADMIN_SECRET');
    if (!adminSecret) {
      return json({ error: 'ADMIN_SECRET not configured' }, 500);
    }

    // 从请求头或请求体中获取密码
    const providedSecret =
      req.headers.get('x-admin-secret') ||
      (await req.json().catch(() => ({}))).secret || '';

    if (providedSecret !== adminSecret) {
      return json({ error: 'UNAUTHORIZED' }, 401);
    }

    const supabaseUrl    = Deno.env.get('SUPABASE_URL')!;
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!;

    // 查询 profiles_admin 视图（包含 email + invite_code + is_pro + quota）
    const resp = await fetch(
      supabaseUrl + '/rest/v1/profiles_admin?select=email,invite_code,is_pro,remaining_quota,total_quota,created_at&order=created_at.desc',
      {
        headers: {
          'apikey': serviceRoleKey,
          'Authorization': 'Bearer ' + serviceRoleKey,
          'Accept': 'application/json',
        },
      }
    );

    if (!resp.ok) {
      const err = await resp.text();
      console.error('profiles_admin query error:', resp.status, err);
      return json({ error: 'QUERY_FAILED', detail: err }, 502);
    }

    const rows = await resp.json();
    return json({ data: rows }, 200);
  } catch (e) {
    console.error('admin-list error:', e);
    return json({ error: 'INTERNAL_ERROR' }, 500);
  }
});

function json(body: unknown, status: number) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
  });
}
