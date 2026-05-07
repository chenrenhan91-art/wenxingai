-- =============================================================
-- 问星AI · Supabase 数据库初始化
-- 执行方式：Supabase Dashboard > SQL Editor > 粘贴运行
--          或 supabase db push
-- =============================================================

-- ── profiles 表 ──
-- 每个注册用户对应一行，存储额度和专业版状态
create table if not exists public.profiles (
  user_id        uuid primary key references auth.users(id) on delete cascade,
  is_pro         boolean   not null default false,
  remaining_quota integer  not null default 3,   -- 免费额度，注册时赠送 3 次
  total_quota    integer   not null default 3,
  created_at     timestamptz not null default now(),
  updated_at     timestamptz not null default now()
);

-- 自动更新 updated_at
create or replace function public.set_updated_at()
returns trigger language plpgsql as $$
begin
  new.updated_at = now();
  return new;
end;
$$;

drop trigger if exists profiles_updated_at on public.profiles;
create trigger profiles_updated_at
  before update on public.profiles
  for each row execute procedure public.set_updated_at();

-- ── Row Level Security ──
alter table public.profiles enable row level security;

-- 用户只能读取自己的 profile（前端直接查询时使用）
drop policy if exists "users can read own profile" on public.profiles;
create policy "users can read own profile"
  on public.profiles for select
  using (auth.uid() = user_id);

-- 写操作由 service_role（Edge Function）负责，普通用户不能自行修改额度
-- （Edge Function 使用 service_role key，绕过 RLS）

-- ── 自动创建 profile 的触发器 ──
-- 每当 auth.users 新增一行时，自动插入 profiles 默认记录
create or replace function public.handle_new_user()
returns trigger language plpgsql security definer as $$
begin
  insert into public.profiles (user_id, is_pro, remaining_quota, total_quota)
  values (new.id, false, 3, 3)
  on conflict (user_id) do nothing;
  return new;
end;
$$;

drop trigger if exists on_auth_user_created on auth.users;
create trigger on_auth_user_created
  after insert on auth.users
  for each row execute procedure public.handle_new_user();
