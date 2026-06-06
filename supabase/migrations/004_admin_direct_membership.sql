-- =============================================================
-- 问星AI · 管理员直接开通/取消会员
-- 逻辑：用户不再输入邀请码；专业版状态只由管理员后台更新 profiles.is_pro。
-- =============================================================

-- 关闭旧的用户自助邀请码兑换入口，避免用户绕过前端继续调用 RPC 升级。
drop function if exists public.redeem_invite_code(text);

-- 新用户注册时只创建额度与会员状态，不再生成邀请码。
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer as $$
begin
  insert into public.profiles (user_id, is_pro, remaining_quota, total_quota)
  values (new.id, false, 3, 3)
  on conflict (user_id) do nothing;
  return new;
end;
$$;

-- 管理员视图不再返回 invite_code，只供 Edge Function 使用。
drop view if exists public.profiles_admin;

alter table public.profiles
  drop constraint if exists profiles_invite_code_key;

alter table public.profiles
  drop column if exists invite_code;

create view public.profiles_admin as
select
  u.email,
  p.is_pro,
  p.remaining_quota,
  p.total_quota,
  p.user_id,
  p.created_at,
  p.updated_at
from public.profiles p
join auth.users u on u.id = p.user_id
order by p.created_at desc;

revoke all on public.profiles_admin from anon, authenticated;
grant select on public.profiles_admin to service_role;
