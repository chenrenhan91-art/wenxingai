# 问星AI Buffer 自动化运营方案

## 目标

- 拉新：把玄学热点流量引到 `wenxingai.top`
- SEO：持续更新热点页，扩大命理 / 玄学 / 塔罗相关长尾覆盖
- 品牌曝光：在 `X / Threads / Instagram` 建立稳定的日更节奏
- 转化：把热点讨论自然导向微信咨询与付费咨询

## 当前项目里已经具备的能力

- `scripts/update_hot_news.py`
  - 抓取 Google News、PTT、YouTube、X、Reddit 等热点
  - 回写 [index.html](/Users/apple/Desktop/运营自动化/wenxingai-main/index.html) 和 [mingli-xuanxue-news.html](/Users/apple/Desktop/运营自动化/wenxingai-main/mingli-xuanxue-news.html)
- `scripts/generate_daily_content.py`
  - 用 Gemini 生成双语内容包
  - 输出 `zh_cn` 与 `zh_hant`
- `scripts/distribute_daily_content.py`
  - 按平台语言配置生成 Buffer 入队任务
  - 生成带 UTM 的落地页链接
- `scripts/run_content_pipeline.py`
  - 统一编排抓取、生成、入队
  - 热点没有实质变化时自动跳过 Gemini 与 Buffer

## 推荐渠道策略

- `Threads`
  - 语言：`zh_hant`
  - 作用：承接台湾 / 香港 / 海外华语玄学讨论
  - 内容类型：观点型、趋势型、节气型
- `X`
  - 语言：`zh_cn`
  - 作用：抢热点、做短平快传播、带动站内新访客
  - 内容类型：结论型、提醒型、冲突点型
- `Instagram`
  - 语言：`zh_hant`
  - 作用：做品牌氛围、咨询导流、沉淀视觉内容
  - 内容类型：简短总结、节气提醒、命理观点卡片文案

## 自动化主流程

1. `update_hot_news.py`
   - 每天抓取热点源
   - 更新首页热点模块和热点专题页
   - 更新 `hot-news-data.json` 与 `sitemap.xml`
2. `run_content_pipeline.py`
   - 比较本轮热点签名和上次成功签名
   - 没有显著变化就停止发布链路
3. `generate_daily_content.py`
   - 把热点快照送入 Gemini
   - 生成 `zh_cn / zh_hant` 双语内容包
4. `distribute_daily_content.py`
   - 依据平台语言配置挑选对应版本文案
   - 追加 UTM 链接
   - 入队 Buffer
5. `generated/pipeline-report.md`
   - 输出本轮是否发布、发布了什么、跳过原因是什么

## 内容来源建议

- 主抓取层：项目已接入的 Google News、PTT、YouTube、X、Reddit
- 建议保留人工巡检：
  - 小红书
  - Threads 玄学博主
  - Instagram 玄学内容账号
- 选题优先级：
  - 节气 / 流年 / 星座 / 生肖
  - 社区高讨论度命理争议
  - AI 算命、命理师观点对撞
  - 容易自然导向咨询的“提醒型话题”

## Buffer 配置建议

推荐环境变量：

```env
BUFFER_API_KEY=你的_key
BUFFER_THREADS_PROFILE_ID=你的_threads_profile_id
BUFFER_X_PROFILE_ID=你的_x_profile_id
BUFFER_INSTAGRAM_PROFILE_ID=你的_instagram_profile_id

SOCIAL_ENABLED_PLATFORMS=threads,x,instagram
SOCIAL_THREADS_LOCALE=zh_hant
SOCIAL_X_LOCALE=zh_cn
SOCIAL_INSTAGRAM_LOCALE=zh_hant
SOCIAL_LANDING_URL=https://wenxingai.top/
```

推荐发布时间：

- `Threads`：09:30
- `X`：12:30
- `Instagram`：20:30

说明：

- 早上用 `Threads` 发观点帖，适合深度阅读
- 中午用 `X` 抢即时传播
- 晚上用 `Instagram` 承接咨询与私域导流

## 效果追踪方案

当前仓库已经做到：

- 每条外发链接自动带：
  - `utm_source`
  - `utm_medium=social`
  - `utm_campaign`
  - `utm_content`
- 每次排队结果记录到：
  - `generated/distribution-jobs.json`
  - `generated/distribution-state.json`
  - `generated/pipeline-report.md`

建议你下一步补齐两层归因：

1. 网站侧接入统计工具
   - `GA4` 或 `Plausible`
   - 核心维度看 `source / campaign / content`
2. 咨询侧接入来源透传
   - 微信落地页保留 `utm_*`
   - 表单或 CRM 保存首触来源

建议追踪的核心指标：

- 社交访问量
- 热点页访问量
- 热点页停留时长
- 微信咨询点击量
- 咨询转化率
- 每个平台的有效咨询成本

## 日常运营 SOP

- 每天早上：检查 `generated/pipeline-report.md`
- 每周一次：看哪类热点最容易引发咨询
- 每周一次：调整 Gemini 提示词，减少低转化话题
- 每月一次：复盘平台语言配置是否需要调整

## GitHub Actions 调度

当前仓库工作流默认会在 GitHub Actions 上按北京时间每日运行两次：

- `11:00`
- `21:00`

只要 GitHub 仓库里的 Secrets 和 Variables 配置完整，就不需要本地电脑开机。

## 本项目的默认假设

- `X` 用简体中文跑更广泛中文流量
- `Threads / Instagram` 用繁體中文更适合台湾和海外华语受众
- 默认落地到热点专题页，而不是直接跳外站

如果你后面要继续，我建议下一步直接做这两件事：

1. 接入你真实的 `BUFFER_*` 和 `GEMINI_API_KEY`
2. 再把站内 CTA 和微信咨询页也纳入同一套 UTM 归因链路
