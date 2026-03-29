# Buffer 分发接入说明

当前仓库已经预埋了多平台分发层，默认会生成分发任务文件；配置 Buffer 后可自动排期发布。

## 当前已完成

- 新增 `scripts/distribute_daily_content.py`
- 每次 Gemini 内容包生成后，自动产出：
  - `generated/distribution-jobs.json`
  - `generated/distribution-package.md`
  - `generated/social-posts/*.md`
- 配置 `BUFFER_API_KEY` 后，可把 Threads、X、Facebook、Instagram 的文案自动排入 Buffer
- 已加入 `generated/distribution-state.json`，避免同一天同一条内容重复入队

## 需要的配置

- `BUFFER_API_KEY`
- 可选：
  - `BUFFER_THREADS_PROFILE_ID`
  - `BUFFER_X_PROFILE_ID`
  - `BUFFER_FACEBOOK_PROFILE_ID`
  - `BUFFER_INSTAGRAM_PROFILE_ID`
  - `SOCIAL_LANDING_URL`

## 默认站外落地页

如果不单独设置 `SOCIAL_LANDING_URL`，分发脚本会默认把社交流量引到：

- `https://karmaisacat.top/`

## 建议做法

如果你的 Buffer 里同一平台只接了一个账号，可以先只配 `BUFFER_API_KEY`。

如果同一平台接了多个账号，必须补对应的 `BUFFER_*_PROFILE_ID`，否则脚本会跳过该平台，避免发错号。
