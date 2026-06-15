-- =============================================================
-- 问星AI · AI 调用风控限流
-- 按用户维度限制调用频率，防止脚本刷接口消耗 Token
-- =============================================================

create table if not exists public.ai_rate_limits (
  user_id       uuid primary key references auth.users(id) on delete cascade,
  last_call_at  timestamptz,
  minute_bucket timestamptz not null default date_trunc('minute', now()),
  minute_count  integer not null default 0,
  hour_bucket   timestamptz not null default date_trunc('hour', now()),
  hour_count    integer not null default 0,
  day_bucket    date not null default (now() at time zone 'utc')::date,
  day_count     integer not null default 0,
  updated_at    timestamptz not null default now()
);

alter table public.ai_rate_limits enable row level security;

-- 仅 Edge Function（service_role）可读写
revoke all on public.ai_rate_limits from anon, authenticated;
grant select, insert, update, delete on public.ai_rate_limits to service_role;

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
  v_hour timestamptz := date_trunc('hour', v_now);
  v_day date := (v_now at time zone 'utc')::date;
  v_cooldown interval;
  v_max_minute int;
  v_max_hour int;
  v_max_day int;
  r public.ai_rate_limits%rowtype;
  v_retry_after int;
begin
  if p_is_pro then
    v_cooldown := interval '3 seconds';
    v_max_minute := 8;
    v_max_hour := 60;
    v_max_day := 200;
  else
    v_cooldown := interval '10 seconds';
    v_max_minute := 2;
    v_max_hour := 3;
    v_max_day := 3;
  end if;

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
  if r.hour_bucket is distinct from v_hour then
    r.hour_count := 0;
    r.hour_bucket := v_hour;
  end if;
  if r.day_bucket is distinct from v_day then
    r.day_count := 0;
    r.day_bucket := v_day;
  end if;

  if r.last_call_at is not null and v_now - r.last_call_at < v_cooldown then
    v_retry_after := greatest(1, ceil(extract(epoch from (v_cooldown - (v_now - r.last_call_at))))::int);
    return jsonb_build_object(
      'allowed', false,
      'error', 'COOLDOWN',
      'message', '请求过于频繁，请稍后再试。',
      'retry_after', v_retry_after
    );
  end if;

  if r.minute_count >= v_max_minute then
    return jsonb_build_object(
      'allowed', false,
      'error', 'RATE_LIMIT_MINUTE',
      'message', '本分钟调用次数已达上限，请稍后再试。',
      'retry_after', 60
    );
  end if;

  if r.hour_count >= v_max_hour then
    return jsonb_build_object(
      'allowed', false,
      'error', 'RATE_LIMIT_HOUR',
      'message', '本小时调用次数已达上限，请稍后再试。',
      'retry_after', 3600
    );
  end if;

  if r.day_count >= v_max_day then
    return jsonb_build_object(
      'allowed', false,
      'error', 'RATE_LIMIT_DAY',
      'message', '今日调用次数已达上限，请明天再试。',
      'retry_after', 86400
    );
  end if;

  update public.ai_rate_limits
  set
    last_call_at = v_now,
    minute_count = r.minute_count + 1,
    hour_count = r.hour_count + 1,
    day_count = r.day_count + 1,
    minute_bucket = v_minute,
    hour_bucket = v_hour,
    day_bucket = v_day,
    updated_at = v_now
  where user_id = p_user_id;

  return jsonb_build_object('allowed', true);
end;
$$;

revoke all on function public.consume_ai_rate_limit(uuid, boolean) from public;
grant execute on function public.consume_ai_rate_limit(uuid, boolean) to service_role;
