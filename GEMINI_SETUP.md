# Gemini 接入说明

当前仓库已经预埋了 Gemini 内容生成层，但默认不会影响现有热点更新。

## 当前已完成

- 保留原有 `scripts/update_hot_news.py` 热点抓取与页面回写
- 新增 `scripts/generate_daily_content.py`
- 新增 `scripts/run_content_pipeline.py`
- 新增提示词模板 `prompts/gemini_daily_content_prompt.txt`
- GitHub Actions 已预留 Gemini 执行步骤
- 未配置 `GEMINI_API_KEY` 时，工作流会自动跳过 Gemini 生成，不会报错

## 你之后要给我的信息

- `GEMINI_API_KEY`
- 可选：`GEMINI_MODEL`
- 可选：`GEMINI_REVIEW_MODEL`

## 配置位置

本地开发可放进：

- `.env.local`
- `.env`

GitHub Actions 线上可放进：

- Repository Secret：`GEMINI_API_KEY`
- Repository Variable：`GEMINI_MODEL`

## 生成结果

配置完成后，每次热点更新后会额外生成：

- `generated/gemini-content-bundle.json`
- `generated/gemini-content-package.md`

当前内容包已经升级为：

- `zh_cn`：简体中文网站文章、X / Threads / Instagram 文案、视频脚本
- `zh_hant`：繁體中文网站文章、X / Threads / Instagram 文案、视频脚本
- 审校层：会先由 `GEMINI_REVIEW_MODEL` 做一轮语病、语气、人性化修正

## 下一步建议

给出 API 后，优先做这两件事：

1. 先跑 `python3 scripts/run_content_pipeline.py`，确认热点变化时才会触发 Gemini 与 Buffer
2. 再把 `generated/gemini-content-bundle.json` 中的双语内容接入站内专题页或文章页
