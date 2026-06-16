-- =============================================================
-- 问星AI · 放宽 AI 调用风控（仅防脚本_burst 刷接口）
-- =============================================================

create or replace function public.consume_ai_rate_limit(
  p_user_id uuid,
  p_is_pro boolean
)
returns jsonb
language plpgsql
security definer
set search_path = public
as $$
declare
  v_now timestamptz := now();
  v_minute timestamptz := date_trunc('minute', v_now);
  v_max_minute int;
  v_cooldown interval := interval '1 second';
  r public.ai_rate_limits%rowtype;
  v_retry_after int;
begin
  -- 专业版略宽松；免费版主要靠 remaining_quota 控总量
  v_max_minute := case when p_is_pro then 40 else 20 end;

  insert into public.ai_rate_limits (user_id)
  values (p_user_id)
  on conflict (user_id) do nothing;

  select * into r
  from public.ai_rate_limits
  where user_id = p_user_id
  for update;

  if r.minute_bucket is distinct from v_minute then
    r.minute_count := 0;
    r.minute_bucket := v_minute;
  end if;

  -- 极短冷却，仅防止连点/脚本毫秒级轰炸
  if r.last_call_at is not null and v_now - r.last_call_at < v_cooldown then
    v_retry_after := greatest(1, ceil(extract(epoch from (v_cooldown - (v_now - r.last_call_at))))::int);
    return jsonb_build_object(
      'allowed', false,
      'error', 'COOLDOWN',
      'message', '操作太快了，请稍等片刻。',
      'retry_after', v_retry_after
    );
  end if;

  -- 仅分钟级 burst 限制，拦截脚本高频刷接口
  if r.minute_count >= v_max_minute then
    return jsonb_build_object(
      'allowed', false,
      'error', 'RATE_LIMIT_MINUTE',
      'message', '当前请求过于密集，请 1 分钟后再试。',
      'retry_after', 60
    );
  end if;

  update public.ai_rate_limits
  set
    last_call_at = v_now,
    minute_count = r.minute_count + 1,
    minute_bucket = v_minute,
    updated_at = v_now
  where user_id = p_user_id;

  return jsonb_build_object('allowed', true);
end;
$$;

revoke all on function public.consume_ai_rate_limit(uuid, boolean) from public;
grant execute on function public.consume_ai_rate_limit(uuid, boolean) to service_role;
