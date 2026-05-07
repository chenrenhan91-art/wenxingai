Deno.serve(async (_req: Request): Promise<Response> => {
  return new Response(JSON.stringify({ ok: true }), {
    headers: { 'Content-Type': 'application/json' },
  });
});
