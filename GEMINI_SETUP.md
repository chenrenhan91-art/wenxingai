# Gemini 接入说明

当前仓库已经预埋了 Gemini 内容生成层，但默认不会影响现有热点更新。

## 当前已完成

- 保留原有 `scripts/update_hot_news.py` 热点抓取与页面回写
- 新增 `scripts/generate_daily_content.py`
- 新增提示词模板 `prompts/gemini_daily_content_prompt.txt`
- GitHub Actions 已预留 Gemini 执行步骤
- 未配置 `GEMINI_API_KEY` 时，工作流会自动跳过 Gemini 生成，不会报错

## 你之后要给我的信息

- `GEMINI_API_KEY`
- 可选：`GEMINI_MODEL`

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

## 下一步建议

给出 API 后，优先做这两件事：

1. 把 `generated/gemini-content-bundle.json` 接到站内实际页面
2. 再接多平台自动分发与排期发布
