# 问星AI SEO/GEO 自动化运营执行手册

本手册用于把问星AI从“有 SEO 基础”推进到“持续扩大玄学、命理、AI命理、紫微斗数、八字、六爻等关键词覆盖，并逐步提高搜索引擎与生成式引擎抓取、收录、引用概率”。

## 一、当前核心判断

### 1. 已经具备的优势

- 站点已有首页、热点页、FAQ、术语页、二十四节气专题、`llms.txt`、`llms-full.txt`、AI policy 与 sitemap。
- 已有每日热点抓取、AI 内容生成、审校、分发、文章扩展的流水线。
- 已新增实体事实页 `facts/wenxing-ai.html`，可作为问星AI在 AI 搜索中的 grounding source。
- 已新增 SEO/GEO 健康报告，当前核心页面可抓取性与 JSON-LD 状态为 `ok`。

### 2. 之前最大的收录断点

深度文章脚本原本把 HTML 写入 `generated/articles/`，但 canonical 与链接指向 `/articles/...`。这会造成“内容生成了，但公开 URL 不稳定或不可被 sitemap 正确发现”的问题。

现在已调整为：

- 公开文章页：`/articles/{slug}.html`
- 公开文章索引：`/articles/`
- 公开文章数据：`/articles/index.json`
- 生成源文：`/generated/articles/{slug}.md`
- sitemap 自动写入 `/articles/` 与最新文章 URL

## 二、自动化系统结构

### 无人值守模式

现在的目标是让 SEO/GEO 优化尽量不依赖人工选题。系统会自动完成：

- 根据 `seo_geo_keywords.json` 生成 `/topics/` 主题专题页。
- 根据热点变化生成 `/articles/` 深度文章。
- 自动维护 `/articles/`、`/topics/`、实体事实页、FAQ、术语页、热点页的 sitemap 入口。
- 每日更新 freshness 信号。
- 每日生成 SEO/GEO 健康报告与内容运营 brief。
- 配置 `INDEXNOW_KEY` 后，自动向 IndexNow 提交 sitemap URL。

你只需要在关键词策略变化时更新 `seo_geo_keywords.json`；如果不更新，系统会按当前矩阵持续运行。

### 每日自动化

由 GitHub Actions 或 `run_daily.sh` 执行：

1. `scripts/run_content_pipeline.py`
   - 抓取命理玄学热点。
   - 判断热点签名是否变化。
   - 生成、审校、质检、分发内容。
   - 生成深度文章到 `/articles/`。
2. `scripts/update_geo_signals.py`
   - 更新核心页面 `article:modified_time`。
   - 更新 JSON-LD `dateModified`。
   - 更新 sitemap `lastmod`。
3. `scripts/run_seo_geo_automation.py`
   - 检查 canonical、meta、robots、JSON-LD、sitemap、AI 文档、实体事实页、文章索引。
   - 输出 `generated/seo-geo-report.md`。
4. `scripts/plan_seo_geo_content.py`
   - 读取 `seo_geo_keywords.json`。
   - 结合热点标题与文章库覆盖情况，输出今日/本周内容 brief。
   - 输出 `generated/seo-geo-content-plan.md`。
5. `scripts/generate_seo_geo_topic_pages.py`
   - 根据 `seo_geo_keywords.json` 自动生成 `/topics/` 主题专题页。
   - 将 `/topics/` 和各主题 URL 写入 sitemap。
6. `scripts/submit_indexnow.py`
   - 如果配置 `INDEXNOW_KEY`，自动把 sitemap URL 提交给 IndexNow。
   - 如果未配置 key，会自动跳过，不影响主流程。

### 每周自动化

- 周一运行 `scripts/update_llms_weekly.py`。
- 更新 `llms-full.txt` 的近期热点话题，让 AI 文档持续具备新鲜度。

### 每月人工复盘

- 检查 Google Search Console 与 Bing Webmaster。
- 手动测试 ChatGPT、Perplexity、Claude、Gemini 是否正确回答“问星AI是什么”。
- 根据 `generated/seo-geo-content-plan.md` 的主题评分，决定下月重点页面。

## 三、关键词主题矩阵

关键词配置文件：`seo_geo_keywords.json`

当前优先级：

| 主题 | 目标 | 主要承接页 |
|---|---|---|
| AI命理与AI算命 | 抢“AI命理/AI算命/命理AI”核心品类词 | 首页、实体事实页、FAQ、文章库 |
| 紫微斗数AI排盘 | 抢“紫微斗数AI/紫微斗数排盘”功能词 | 首页、术语页、FAQ、文章库 |
| 八字排盘与流年大运 | 抢“八字排盘/流年运势/大运K线”问题词 | FAQ、术语页、文章库 |
| 周易六爻AI解卦 | 抢“六爻AI/周易六爻/AI解卦”功能词 | FAQ、术语页、文章库 |
| 合盘与关系分析 | 抢“AI合盘/感情合盘/夫妻宫/桃花星”转化词 | 首页、FAQ、术语页、文章库 |
| 二十四节气命理 | 抢节气长尾和八字月令查询 | 24jieqi、FAQ、文章库 |
| 玄学热点与命理新闻 | 保持每日新鲜度与社交传播 | 热点页、文章库、术语页 |

## 四、内容生产策略

### 1. 每日内容

目标：提高新鲜度与长尾覆盖。

- 每日更新 `mingli-xuanxue-news.html`。
- 热点变化时生成 1-2 篇 `/articles/` 深度文章。
- 每篇文章必须具备：
  - 明确主关键词。
  - 3-5 个 FAQ。
  - 至少 1 个 `<dl>` 事实块。
  - 内链到实体事实页、FAQ、术语页、热点页。
  - 避免绝对化预测与夸张营销词。

### 2. 每周内容

目标：围绕核心关键词建立 topical authority。

- 每周至少强化 1 个核心主题：AI命理、紫微斗数AI、八字AI、六爻AI、AI合盘。
- 从 `generated/seo-geo-content-plan.md` 选择 score 最高的主题。
- 若已有页面承接，则更新 FAQ 或术语解释。
- 若没有页面承接，则生成新文章或新专题页。

### 3. 每月内容

目标：争取排名与 AI 引用。

- 扩展 3-5 个高转化问题：例如“AI算命准确吗”“紫微斗数AI排盘是什么”“大运K线图是什么意思”。
- 把表现好的文章升级为专题页。
- 对搜索展现高但点击低的页面重写 title/description。
- 对 AI 搜索回答不准确的问题，补充实体事实页或 FAQ。

## 五、收录提升动作

### 1. 发现性

- 保持 sitemap 包含：首页、实体事实页、文章索引、热点页、FAQ、术语页、24节气页、文章页。
- Footer 保留实体事实页、FAQ、术语页、热点页、AI 文档入口。
- 深度文章必须由 `/articles/` 索引页链接出来。

### 2. 可解析性

- 所有核心页保持 canonical 与实际 URL 一致。
- 所有 JSON-LD 必须能被 `json.loads` 解析。
- FAQ 和术语内容使用短句，方便搜索引擎提取摘要。

### 3. 新鲜度

- 每日更新 `article:modified_time` 与 sitemap `lastmod`。
- 每周更新 `llms-full.txt` 热点区块。
- 热点文章生成后自动写入 sitemap。

### 4. 实体一致性

- 所有页面统一使用：产品名“问星AI”、英文名“WenXing AI”、研发者“AIcoding”。
- 所有外部传播优先回链到 `/facts/wenxing-ai.html` 或相关专题页。

## 六、GEO 提升动作

### 1. 让 AI 明确识别实体

- `facts/wenxing-ai.html` 是首选实体锚定页。
- `llms.txt` 是快速摘要。
- `llms-full.txt` 是完整知识库。
- `.well-known/ai.txt` 声明允许 AI 抓取、总结和引用。

### 2. 让 AI 有内容可引用

优先生产这些内容类型：

- “问星AI是什么”定义型内容。
- “AI命理和传统命理区别”对比型内容。
- “紫微斗数AI排盘是什么”功能解释型内容。
- “AI算命准确吗”边界说明型内容。
- “大运K线图是什么意思”差异化功能内容。
- “节气如何影响八字月令”术语解释型内容。

### 3. 让 AI 不混淆品牌

- 页面反复出现稳定事实：官网、应用入口、创作者、功能范围、使用边界。
- 避免在实体事实页混入营销口号或不稳定 claims。
- 每月人工测试 AI 搜索回答，如果出现误解，回到实体页和 FAQ 修正。

## 七、排名提升节奏预期

### 0-2 周

- 技术发现性改善。
- sitemap 与实体事实页被重新抓取。
- Search Console 可能开始出现 `/facts/`、`/articles/`、FAQ/术语页曝光。

### 3-6 周

- 玄学热点、节气命理、AI命理长尾词开始积累展现。
- FAQ 与术语页更容易获得问答型查询曝光。
- AI 搜索对“问星AI是什么”的描述准确率提升。

### 2-3 个月

- 核心主题形成内容簇。
- 部分中长尾词有机会进入前几页。
- 外部社交与赢得媒体回链增加后，AI 引用概率提升。

## 八、无人值守 SOP

默认不需要人工执行。自动化系统会：

1. 每日生成 `/topics/` 主题专题页。
2. 热点变化时生成 `/articles/` 深度文章。
3. 每日更新 sitemap 与 freshness 信号。
4. 每日输出 `generated/seo-geo-report.md` 和 `generated/seo-geo-content-plan.md`。
5. 配置 `INDEXNOW_KEY` 后自动提交 IndexNow。

你只需要在看到 `generated/seo-geo-report.md` 出现 `fail` 时介入修复；正常 `ok` 状态无需手动操作。

## 九、关键指标

| 指标 | 目标 |
|---|---|
| sitemap 提交 URL 数 | 稳定增长，文章页持续进入 sitemap |
| Search Console 总展现 | 每周上升或至少关键词覆盖增加 |
| FAQ/术语页展现 | 覆盖“是什么/区别/准确吗/怎么看”等问题词 |
| `/articles/` 收录 | 每周新增文章被发现 |
| AI 搜索回答准确率 | “问星AI是什么”能准确提到官网、AIcoding、核心功能 |
| 社交 UTM 访问 | 热点内容能带来稳定 referral |

## 十、下一步优先事项

1. 接入 Google Search Console 和 Bing Webmaster，提交 `https://wenxingai.top/sitemap.xml`。
2. 每周按 `generated/seo-geo-content-plan.md` 执行至少 1 个核心主题。
3. 把高分主题扩展成专题页，而不只停留在每日文章。
4. 建立 AI 搜索手测表，记录 ChatGPT、Perplexity、Claude、Gemini 的回答变化。
5. 做真实第三方内容提及，避免虚假外链，把品牌事实自然沉淀到外部可信来源。

## 十一、需要你提供的配置

如果你希望完全自动化到“生成后通知搜索引擎”，需要补齐：

| 配置 | 类型 | 用途 | 是否必须 |
|---|---|---|---|
| `DASHSCOPE_API_KEY` | GitHub Secret | 自动生成每日内容和深度文章 | 已有流水线需要 |
| `DASHSCOPE_MODEL` | GitHub Secret 或 Variable | 指定内容生成主模型 | 已有流水线需要 |
| `DASHSCOPE_MODEL_FALLBACKS` | GitHub Secret 或 Variable | 主模型额度耗尽或不可用时自动切换 | 推荐 |
| `DASHSCOPE_REVIEW_MODEL` | GitHub Secret 或 Variable | 指定内容审校主模型 | 推荐 |
| `DASHSCOPE_REVIEW_MODEL_FALLBACKS` | GitHub Secret 或 Variable | 审校模型额度耗尽或不可用时自动切换 | 推荐 |
| `BUFFER_API_KEY` | GitHub Secret | 自动分发社交内容 | 可选 |
| `BUFFER_*_PROFILE_ID` | GitHub Variables | 指定 Threads/X/Instagram 账号 | 可选 |
| `INDEXNOW_KEY` | GitHub Secret | 自动向 Bing/IndexNow 生态提交 URL | 推荐 |
| `INDEXNOW_KEY_LOCATION` | GitHub Variable | IndexNow key 文件公开 URL | 推荐 |

IndexNow 的 key 文件必须能被公开访问。当前自动化会从 `INDEXNOW_KEY` 生成根目录 txt 文件；若 `INDEXNOW_KEY_LOCATION` 不配置，默认使用 `https://wenxingai.top/indexnow-key.txt`。如果你已经在 GitHub Secrets 填了 `INDEXNOW_KEY_LOCATION`，workflow 会按该 URL 的路径生成对应 txt 文件，并把文件内容写成 `INDEXNOW_KEY`。