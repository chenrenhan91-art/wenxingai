-- =============================================================
-- 问星AI · 用户专属邀请码（替换 002 的公共码池方案）
-- 逻辑：每个用户注册时自动生成唯一邀请码存入 profiles，
--       管理员后台查看 profiles_admin 视图（邮箱+邀请码），
--       付款后将该用户的邀请码发给他，用户输入后升级专业版。
-- =============================================================

-- ── 1. 废弃旧的公共邀请码池 ──
drop table if exists public.invite_codes;

-- ── 2. profiles 表新增 invite_code 列 ──
alter table public.profiles
  add column if not exists invite_code text;

-- 为已有用户回填邀请码（每人唯一）
update public.profiles
set invite_code = 'WXAI-' || upper(substring(replace(gen_random_uuid()::text, '-', ''), 1, 8))
where invite_code is null;

-- 设为非空 + 唯一
alter table public.profiles
  alter column invite_code set not null;

alter table public.profiles
  drop constraint if exists profiles_invite_code_key;
alter table public.profiles
  add constraint profiles_invite_code_key unique (invite_code);

-- ── 3. 注册触发器：新用户自动生成邀请码 ──
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer as $$
begin
  insert into public.profiles (user_id, is_pro, remaining_quota, total_quota, invite_code)
  values (
    new.id,
    false,
    3,
    3,
    'WXAI-' || upper(substring(replace(gen_random_uuid()::text, '-', ''), 1, 8))
  )
  on conflict (user_id) do nothing;
  return new;
end;
$$;

-- ── 4. 兑换函数：验证该用户自己的邀请码 ──
create or replace function public.redeem_invite_code(p_code text)
returns json
language plpgsql
security definer
set search_path = public
as $$
declare
  v_uid uuid := auth.uid();
begin
  if v_uid is null then
    return json_build_object('success', false, 'error', 'UNAUTHORIZED');
  end if;

  if exists (select 1 from public.profiles where user_id = v_uid and is_pro = true) then
    return json_build_object('success', false, 'error', 'ALREADY_PRO');
  end if;

  -- 验证输入的码与该用户自己的 invite_code 是否匹配
  if not exists (
    select 1 from public.profiles
    where user_id = v_uid
      and invite_code = upper(trim(p_code))
  ) then
    return json_build_object('success', false, 'error', 'INVALID_CODE');
  end if;

  update public.profiles
     set is_pro = true
   where user_id = v_uid;

  return json_build_object('success', true);
end;
$$;

revoke execute on function public.redeem_invite_code(text) from public;
grant  execute on function public.redeem_invite_code(text) to authenticated;

-- ── 5. 管理员视图：邮箱 + 邀请码 + 状态（供后台查询） ──
create or replace view public.profiles_admin as
select
  u.email,
  p.invite_code,
  p.is_pro,
  p.remaining_quota,
  p.total_quota,
  p.user_id,
  p.created_at,
  p.updated_at
from public.profiles p
join auth.users u on u.id = p.user_id
order by p.created_at desc;
