-- =============================================================
-- 问星AI · 邀请码系统
-- 用途：管理员在 Supabase Dashboard 手动插入邀请码行，
--       付费用户填入后调用 redeem_invite_code() 升级为专业版。
-- =============================================================

-- ── invite_codes 表 ──
create table if not exists public.invite_codes (
  code        text         primary key,
  is_used     boolean      not null default false,
  used_by     uuid         references auth.users(id) on delete set null,
  used_at     timestamptz,
  created_at  timestamptz  not null default now()
);

-- ── Row Level Security ──
alter table public.invite_codes enable row level security;

-- 普通用户无法浏览邀请码表（所有读写由 security definer 函数完成）
-- 无需创建任何面向用户的 policy

-- ── 兑换邀请码函数 ──
-- 原子操作：校验码 → 标记已用 → 升级用户
-- 返回 JSON: {"success": true} 或 {"success": false, "error": "..."}
create or replace function public.redeem_invite_code(p_code text)
returns json
language plpgsql
security definer   -- 以函数 owner 权限执行，绕过 RLS
set search_path = public
as $$
declare
  v_uid uuid := auth.uid();
begin
  -- 必须已登录
  if v_uid is null then
    return json_build_object('success', false, 'error', 'UNAUTHORIZED');
  end if;

  -- 用户已是专业版，无需重复兑换
  if exists (select 1 from public.profiles where user_id = v_uid and is_pro = true) then
    return json_build_object('success', false, 'error', 'ALREADY_PRO');
  end if;

  -- 原子更新：只更新未使用的目标行，防止并发竞争
  update public.invite_codes
     set is_used = true,
         used_by = v_uid,
         used_at = now()
   where code = p_code
     and is_used = false;

  if not found then
    return json_build_object('success', false, 'error', 'INVALID_CODE');
  end if;

  -- 升级用户为专业版
  update public.profiles
     set is_pro = true
   where user_id = v_uid;

  return json_build_object('success', true);
end;
$$;

-- 撤销公开执行权限，再显式授予 authenticated 角色
revoke execute on function public.redeem_invite_code(text) from public;
grant  execute on function public.redeem_invite_code(text) to authenticated;
