// Supabase Edge Function: admin-list
// 用途：管理员后台查询所有用户，并开通/取消专业版
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

    const body = await req.json().catch(() => ({}));

    // 从请求头或请求体中获取密码
    const providedSecret =
      req.headers.get('x-admin-secret') ||
      body.secret || '';

    if (providedSecret !== adminSecret) {
      return json({ error: 'UNAUTHORIZED' }, 401);
    }

    const supabaseUrl    = Deno.env.get('SUPABASE_URL')!;
    const serviceRoleKey = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')!;

    if (body.action === 'set_pro') {
      const userId = String(body.user_id || '').trim();
      if (!userId || typeof body.is_pro !== 'boolean') {
        return json({ error: 'BAD_REQUEST' }, 400);
      }

      const updateResp = await fetch(
        supabaseUrl + '/rest/v1/profiles?user_id=eq.' + encodeURIComponent(userId) + '&select=user_id',
        {
          method: 'PATCH',
          headers: {
            'apikey': serviceRoleKey,
            'Authorization': 'Bearer ' + serviceRoleKey,
            'Content-Type': 'application/json',
            'Prefer': 'return=representation',
          },
          body: JSON.stringify({ is_pro: body.is_pro }),
        },
      );

      if (!updateResp.ok) {
        const err = await updateResp.text();
        console.error('profiles update error:', updateResp.status, err);
        return json({ error: 'UPDATE_FAILED', detail: err }, 502);
      }

      const updatedRows = await updateResp.json().catch(() => []);
      if (!Array.isArray(updatedRows) || updatedRows.length === 0) {
        return json({ error: 'USER_NOT_FOUND' }, 404);
      }
    }

    const rows = await listUsers(supabaseUrl, serviceRoleKey);
    return json({ data: rows }, 200);
  } catch (e) {
    console.error('admin-list error:', e);
    return json({ error: 'INTERNAL_ERROR' }, 500);
  }
});

async function listUsers(supabaseUrl: string, serviceRoleKey: string) {
  // 查询 profiles_admin 视图（包含 email + user_id + is_pro + quota）
  const resp = await fetch(
    supabaseUrl + '/rest/v1/profiles_admin?select=email,user_id,is_pro,remaining_quota,total_quota,created_at&order=created_at.desc',
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
    throw new Error('QUERY_FAILED: ' + err);
  }

  return await resp.json();
}

function json(body: unknown, status: number) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...CORS_HEADERS, 'Content-Type': 'application/json' },
  });
}
