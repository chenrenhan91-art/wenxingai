# 问星AI SEO/GEO 全面深度优化方案与自动化运行系统

> 本方案基于《AI 驱动的 SEO_GEO 优化方案.md》整理，并按问星AI当前仓库能力落地：`robots.txt`、`llms.txt`、`.well-known/ai.txt`、`sitemap.xml`、热点内容流水线、Buffer 分发、结构化页面与 GitHub Actions。

## 一、目标与原则

### 1. 核心目标

1. **传统 SEO**：提升 Google/Bing 对首页、热点页、FAQ、术语页、二十四节气页、深度文章的收录与长尾曝光。
2. **生成式引擎优化 GEO**：让 ChatGPT、Perplexity、Claude、Gemini 等 AI 检索系统能准确识别“问星AI是什么、由谁研发、支持哪些功能、适合谁使用”。
3. **回答引擎优化 AEO**：让 FAQ、术语页、节气页和热点深度文章能被直接摘录为答案，覆盖“AI命理是什么”“紫微斗数AI排盘”“AI算命准确吗”等问答型意图。
4. **自动化运营**：每天更新热点与新鲜度，每周更新 AI 知识库热点区块，每次运行生成 SEO/GEO 健康报告。

### 2. 执行原则

- **事实优先**：用明确数据、功能边界、更新时间、来源链接替代营销形容词。
- **一页一实体**：用 `facts/wenxing-ai.html` 作为问星AI实体锚定页，给 AI RAG 系统稳定 grounding source。
- **显性结构优先**：关键事实写在用户可见 HTML 中，尤其是 `<dl><dt><dd>` 定义网格；JSON-LD 只做镜像补充。
- **自然语言优先**：不为 AI 伪造机器文风，不做关键词堆砌，不制造虚假第三方提及。
- **自动化可验证**：每个动作对应脚本、产物或报告，避免只停留在运营建议。

## 二、站点资产分层

| 层级 | 现有/新增资产 | 作用 | 自动化方式 |
|---|---|---|---|
| 实体锚定层 | `facts/wenxing-ai.html` | 给 AI 系统提供问星AI唯一实体事实源 | 每日纳入 freshness 与 SEO/GEO 审计 |
| AI 摘要层 | `llms.txt`、`llms-full.txt`、`.well-known/ai.txt` | 给 LLM 快速读取产品定义、引用规范与热点知识 | 每周更新 `llms-full.txt` 热点区块 |
| 核心转化层 | `index.html`、`pro.html`、`wenxing.html` | 承接品牌词、产品词与转化意图 | 每日审计 metadata/JSON-LD/新鲜度 |
| 答案层 | `geo-answers.html`、`glossary.html` | 覆盖 FAQ、术语、AEO 直接答案 | 每日更新 modified time，每月扩展问题与术语 |
| 专题层 | `24jieqi/` | 覆盖节气长尾、流年、八字月令相关查询 | sitemap 固定收录，节气前人工强化 |
| 热点层 | `mingli-xuanxue-news.html`、`articles/`、`generated/articles/` | 抢每日热点、社交分发、长尾文章；公开 HTML 在 `articles/`，Markdown 源文在 `generated/articles/` | GitHub Actions 每日运行内容流水线 |
| 监控层 | `generated/seo-geo-report.*` | 记录可抓取性、结构化数据、实体页与流水线状态 | `scripts/run_seo_geo_automation.py` 每日生成 |

## 三、SEO/GEO 深度优化路线

### 阶段 1：技术底座与实体消歧

1. **开放爬虫通路**
   - 保持 `robots.txt` 对 GPTBot、ClaudeBot、PerplexityBot、Google-Extended、Bingbot 等主流机器人开放。
   - 保留 `Sitemap`、`AI-Policy`、`LLMs` 入口，方便爬虫发现 AI 文档。
2. **建立问星AI实体事实页**
   - 使用 `facts/wenxing-ai.html` 作为单一权威实体页。
   - H1 只写“问星AI”，首段给出单句定义，避免混入营销口号。
   - 用 `<dl>` 写清：产品名、英文名、研发者、入口、平台、价格、目标用户、Verified 日期。
   - JSON-LD 镜像页面事实，绑定 `SoftwareApplication`、`WebPage`、`BreadcrumbList`。
3. **消歧与边界声明**
   - 明确问星AI不同于通用聊天机器人、传统模板排盘站和线下算命馆。
   - 明确输出为文化、娱乐与个人反思参考，不提供医疗、法律、投资等承诺。

### 阶段 2：核心页面 AI 可引用改造

1. **首页**
   - 保持产品定义、核心功能、创作者、入口、社交渠道、FAQ 的 JSON-LD 与可见文本一致。
   - Footer 暴露 `facts/wenxing-ai.html`、`llms.txt`、`llms-full.txt`、`sitemap.xml`，降低 AI 发现成本。
2. **FAQ 页**
   - 继续用 FAQPage JSON-LD 覆盖高频问题。
   - 增补“AI命理和传统命理有什么边界”“问星AI如何处理隐私”“AI结果如何理性使用”等信任问题。
3. **术语页**
   - 术语定义保持短句、可摘录、无夸张形容词。
   - 对紫微斗数、八字、六爻、流年、大运、化忌、化禄等建立内链到 FAQ 与节气页。
4. **专题页**
   - 二十四节气页适合做传统 SEO 长尾，标题保留“节气 + 命理 + 运势/八字/月令”。
   - 节气临近前一周，人工补充当年年份、五行趋势、常见问题。

### 阶段 3：热点内容与深度文章 GEO 强化

1. **内容生成要求**
   - 每篇深度文章至少包含 3 个具体事实点：日期、来源、热点主题、公开讨论语境。
   - 每个主要 `<h2>` 尽量带主体前缀，如“问星AI观察：流年讨论为何会被放大”。
   - 加入 1 个事实定义块或 `<dl>` 小节，便于 RAG 抽取。
   - 文章结尾添加 FAQ 与内链，链接到首页、热点页、FAQ、术语页、实体事实页。
2. **避免项**
   - 不写“必然”“注定”“百分百准确”。
   - 不制造虚假专家引用或伪造媒体来源。
   - 不做关键词堆砌，不为了 AI 强行切碎段落。
3. **外部赢得媒体**
   - 每月挑选 2-4 个真实话题投放到 Threads、Instagram、X 或博客平台。
   - 优先发布“事实解释型内容”：AI命理如何避免模板化、紫微斗数和八字差异、AI算命隐私边界。
   - 外部内容统一回链到 `facts/wenxing-ai.html` 或专题页，而不是只回首页。

## 四、自动化运行系统

### 1. GitHub Actions 主调度

当前工作流：`.github/workflows/update-hot-news.yml`

运行节奏：

- 每日 UTC 03:00 与 13:00 自动运行，对应北京时间 11:00 与 21:00。
- 手动 `workflow_dispatch` 可强制刷新 AI 内容与 Buffer 分发。

执行链路：

1. `scripts/run_content_pipeline.py`
   - 抓取热点。
   - 判断热点签名是否变化。
   - 生成 Gemini/DashScope 内容包。
   - 审校、规则质检、Buffer 分发。
   - 成功后生成深度文章。
2. `scripts/update_llms_weekly.py`
   - 每周一更新 `llms-full.txt` 的近期热点区块。
   - 同步 sitemap 中 `llms.txt` 与 `llms-full.txt` 的 lastmod。
3. `scripts/update_geo_signals.py`
   - 每日更新核心 HTML 的 `article:modified_time`、JSON-LD `dateModified` 与 sitemap `lastmod`。
4. `scripts/run_seo_geo_automation.py`
   - 生成 `generated/seo-geo-report.json` 与 `generated/seo-geo-report.md`。
   - 检查 canonical、meta description、robots、JSON-LD、实体锚定页、AI 文档、sitemap 与内容流水线产物。

### 2. 本地 Cron 方案

本地电脑需要参与时，可使用：

```bash
bash run_daily.sh
```

推荐 crontab：

```cron
0 8 * * * /bin/bash /Users/apple/Desktop/wenxingai-main/run_daily.sh >> /Users/apple/Desktop/wenxingai-main/logs/run_daily.log 2>&1
```

本地脚本负责：热点抓取、每周 llms 更新、GEO 新鲜度更新、SEO/GEO 自动审计报告。

### 3. 自动化产物

| 产物 | 用途 |
|---|---|
| `generated/pipeline-report.md` | 每日内容流水线状态、热点变化、分发结果 |
| `generated/gemini-audit-report.md` | AI 内容质量审计 |
| `generated/distribution-package.md` | 社交分发包与 UTM 链接 |
| `generated/articles-report.md` | 深度文章生成结果 |
| `generated/seo-geo-report.md` | SEO/GEO 可抓取性、结构化数据、实体事实页健康报告 |

## 五、KPI 与复盘节奏

| 周期 | 指标 | 工具/来源 | 行动 |
|---|---|---|---|
| 每日 | 热点页是否更新、SEO/GEO 报告是否有 fail | GitHub Actions、`generated/seo-geo-report.md` | 修复失败项，必要时手动重跑 |
| 每周 | `llms-full.txt` 热点是否更新、哪些热点带来社交流量 | Pipeline report、Buffer、GA4/Plausible | 调整热点源与提示词 |
| 每月 | Search Console 展示/点击、Bing 收录、AI 引用表现 | GSC、Bing Webmaster、人工 AI prompt 测试 | 扩 FAQ、术语页与专题页 |
| 每季度 | 品牌实体一致性、第三方提及、转化链路 | AI 搜索手测、社交后台、咨询归因 | 做外部媒体/博客/社区内容投放 |

## 六、人工 Prompt 测试清单

每月在 ChatGPT、Perplexity、Claude、Gemini 中测试以下问题，并记录是否引用或提到问星AI：

1. “中文 AI 命理应用有哪些？”
2. “问星AI是什么？”
3. “有没有支持紫微斗数和八字的 AI 工具？”
4. “AI 算命和传统算命有什么区别？”
5. “紫微斗数 3D 排盘是什么？”
6. “大运 K 线图是什么意思？”
7. “AI 命理应用如何保护出生信息隐私？”

记录维度：是否出现问星AI、是否链接官网、是否描述准确、是否引用事实页、是否混淆品牌。

## 七、优先级路线图

### 7 天内

- 确认 `facts/wenxing-ai.html` 已被 sitemap 收录。
- 检查 `generated/seo-geo-report.md` 无 fail 项。
- 在首页、FAQ、术语页 footer 保留实体事实页入口。

### 30 天内

- 给 `geo-answers.html` 增补 5-8 个信任型问题。
- 每周至少生成 2 篇热点深度文章，并确保文章被 sitemap 或站内索引页发现。
- 用 Search Console 提交 `sitemap.xml`。

### 60 天内

- 做 3-5 篇外部博客/社交长帖，主题围绕 AI 命理方法论、隐私边界、传统命理与 LLM 的差异。
- 建立 AI 引用手测表，跟踪 ChatGPT、Perplexity、Gemini、Claude 的品牌描述准确率。

### 90 天内

- 将高转化 FAQ 扩展成独立专题页。
- 根据 Search Console 查询词，补齐“紫微斗数AI”“八字AI排盘”“六爻AI解卦”“AI合盘”等页面或章节。
- 对外部赢得媒体提及做月度复盘，优先加深真实、有来源、非营销化的第三方内容。

## 八、维护边界

- `llms.txt` 和 `llms-full.txt` 是辅助文档，不替代常规 HTML 页面。
- JSON-LD 必须与页面可见事实一致，不能塞入用户看不到或不可验证的 claim。
- 每次新增页面都要同步：canonical、meta description、robots、JSON-LD、sitemap、至少一个站内入口。
- 自动化报告出现 fail 时先修技术发现性，再修内容表达；AI 找不到页面时，内容写得再好也不会被引用。