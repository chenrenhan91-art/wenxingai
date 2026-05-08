/**
 * Cloudflare Pages Function: /proxy/* → vyumtwiwwuqqcipdskis.supabase.co/*
 *
 * 作用：代理所有 Supabase 请求（auth / rest / functions），
 * 解决 supabase.co 在中国大陆被 GFW 屏蔽的问题。
 * Cloudflare 边缘节点可正常访问 Supabase，且对中国用户可达。
 */

const SUPABASE_BASE = 'https://vyumtwiwwuqqcipdskis.supabase.co';

// 需要透传给 Supabase 的请求头白名单
const FORWARD_REQ_HEADERS = new Set([
    'content-type',
    'apikey',
    'authorization',
    'prefer',
    'x-client-info',
    'x-upsert',
    'cache-control',
    'range',
]);

// 需要从 Supabase 响应透传回客户端的响应头
const FORWARD_RES_HEADERS = [
    'content-type',
    'content-range',
    'x-total-count',
    'location',
];

function corsHeaders() {
    return {
        'access-control-allow-origin': '*',
        'access-control-allow-methods': 'GET,POST,PUT,PATCH,DELETE,OPTIONS',
        'access-control-allow-headers':
            'Content-Type,apikey,Authorization,Prefer,X-Client-Info,Range',
        'access-control-max-age': '86400',
    };
}

export async function onRequest({ request, params }) {
    // CORS preflight
    if (request.method === 'OPTIONS') {
        return new Response(null, { status: 204, headers: corsHeaders() });
    }

    // 构造目标 URL：/proxy/auth/v1/token → supabase.co/auth/v1/token
    const pathParts = params.path || [];
    const path = pathParts.join('/');
    const search = new URL(request.url).search;
    const targetUrl = `${SUPABASE_BASE}/${path}${search}`;

    // 只转发白名单内的请求头，避免把 Cloudflare 内部头带给 Supabase
    const fwdHeaders = new Headers();
    for (const [k, v] of request.headers.entries()) {
        if (FORWARD_REQ_HEADERS.has(k.toLowerCase())) {
            fwdHeaders.set(k, v);
        }
    }

    const hasBody = !['GET', 'HEAD'].includes(request.method);
    let upstream;
    try {
        upstream = await fetch(targetUrl, {
            method: request.method,
            headers: fwdHeaders,
            body: hasBody ? request.body : undefined,
        });
    } catch (err) {
        return new Response(
            JSON.stringify({ error: 'proxy_fetch_failed', detail: String(err) }),
            { status: 502, headers: { 'content-type': 'application/json', ...corsHeaders() } }
        );
    }

    // 构造响应头：CORS + 选择性透传 Supabase 响应头
    const resHeaders = new Headers(corsHeaders());
    for (const h of FORWARD_RES_HEADERS) {
        const val = upstream.headers.get(h);
        if (val) resHeaders.set(h, val);
    }

    return new Response(upstream.body, {
        status: upstream.status,
        headers: resHeaders,
    });
}
