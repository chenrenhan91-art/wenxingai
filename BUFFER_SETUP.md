# Buffer 分发接入说明

当前仓库已经预埋了多平台分发层，默认会生成分发任务文件；配置 Buffer 后可自动排期发布。现在的默认目标平台是 `X / Threads / Instagram`，并支持按平台选择简体中文或繁體中文版本。

注意：Instagram 在 API 场景下通常需要“媒体 + 文案（caption）”。本仓库分发脚本已默认对 Instagram 走媒体发布路径，默认媒体为站点封面图 `https://wenxingai.top/share-cover.jpg`，可通过 `SOCIAL_INSTAGRAM_MEDIA_URL` 覆盖。
如果你希望每天多条 Instagram 自动轮播不同素材，可使用 `SOCIAL_INSTAGRAM_MEDIA_URLS`（逗号分隔多个图片 URL）。

## 当前已完成

- `scripts/distribute_daily_content.py`
- `scripts/run_content_pipeline.py`
- 每次 Gemini 内容包生成后，自动产出：
  - `generated/distribution-jobs.json`
  - `generated/distribution-package.md`
  - `generated/social-posts/*.md`
- 配置 `BUFFER_API_KEY` 后，可把 Threads、X、Instagram 的文案自动排入 Buffer
- 已加入 `generated/distribution-state.json`，避免同一天同一平台同一语言版本重复入队
- 已加入 `generated/pipeline-state.json`，避免热点内容没有变化时重复生成和重复发布

## 需要的配置

- `BUFFER_API_KEY`
- 可选：
  - `BUFFER_THREADS_PROFILE_ID`
  - `BUFFER_X_PROFILE_ID`
  - `BUFFER_INSTAGRAM_PROFILE_ID`
  - `SOCIAL_ENABLED_PLATFORMS`
  - `SOCIAL_DEFAULT_LOCALE`
  - `SOCIAL_THREADS_LOCALE`
  - `SOCIAL_X_LOCALE`
  - `SOCIAL_INSTAGRAM_LOCALE`
  - `SOCIAL_LANDING_URL`
  - `SOCIAL_THREADS_LANDING_URL`
  - `SOCIAL_X_LANDING_URL`
  - `SOCIAL_INSTAGRAM_LANDING_URL`
  - `SOCIAL_INSTAGRAM_MEDIA_URL`
  - `SOCIAL_INSTAGRAM_MEDIA_URLS`

## 默认落地页

如果不单独设置 `SOCIAL_LANDING_URL`，分发脚本会默认把社交流量引到：

- `https://wenxingai.top/`

并自动附加：

- `utm_source`
- `utm_medium=social`
- `utm_campaign`
- `utm_content`

## 建议做法

如果你的 Buffer 里同一平台只接了一个账号，可以先只配 `BUFFER_API_KEY`。

如果同一平台接了多个账号，必须补对应的 `BUFFER_*_PROFILE_ID`，否则脚本会跳过该平台，避免发错号。

推荐先用下面这组配置：

```env
SOCIAL_ENABLED_PLATFORMS=threads,x,instagram
SOCIAL_THREADS_LOCALE=zh_hant
SOCIAL_X_LOCALE=zh_cn
SOCIAL_INSTAGRAM_LOCALE=zh_hant
SOCIAL_LANDING_URL=https://wenxingai.top/
SOCIAL_INSTAGRAM_MEDIA_URL=https://wenxingai.top/share-cover.jpg
SOCIAL_INSTAGRAM_MEDIA_URLS=https://wenxingai.top/share-cover.jpg,https://wenxingai.top/apple-touch-icon.png
```

这套默认意味着：

- `Threads` 发繁體中文，承接台湾/香港/海外华语用户
- `X` 发简体中文，承接更广泛中文讨论流量
- `Instagram` 发繁體中文，承接视觉内容与私域咨询
