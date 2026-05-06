# 热点新闻深度文章生成系统

## 概述

本系统将每日生成的社交内容 snippet 自动扩展为完整的 **SEO 优化深解文章**，覆盖简体中文与繁体中文两个版本。

**核心特点**:
- ✓ 自动化生成 2000-3000 字的深度分析文章
- ✓ 每篇文章单独优化 SEO（title/description/keywords/schema）
- ✓ 包含 FAQ、内链、CTA 等转化要素
- ✓ 生成完整 HTML 页面和 Markdown 源文件
- ✓ 完整的流量追踪（UTM 参数）

---

## 架构流程

```
热点抓取
   ↓
社交内容生成 (Gemini)
   ↓
内容审校 (Gemini Review)
   ↓
质量检查 (Audit Gate)
   ↓
社交分发 (Buffer)
   ↓
[新] 深度文章生成 ← ← ← 本功能
   ├─ 简体中文版本
   ├─ 繁体中文版本
   └─ 文章索引
```

---

## 文件说明

### 1. 核心脚本

#### `scripts/generate_article_from_snippets.py`
- **作用**: 从 `gemini-content-bundle.json` 读取每日内容，使用 Gemini API 生成深度文章
- **输入**: 
  - `generated/gemini-content-bundle.json` (社交内容包)
  - `hot-news-data.json` (热点数据)
- **输出**:
  - `generated/articles/{slug}-zh_cn.html` (简体中文页面)
  - `generated/articles/{slug}-zh_cn.md` (简体中文 Markdown)
  - `generated/articles/{slug}-zh_hant.html` (繁体中文页面)
  - `generated/articles/{slug}-zh_hant.md` (繁体中文 Markdown)
  - `generated/articles-index.json` (文章索引)
  - `generated/articles-report.md` (生成报告)

### 2. Prompt 配置

#### `prompts/gemini_article_generation_prompt.txt`
- 指导 Gemini 如何生成高质量文章
- 包含 SEO 要求、内容规范、写作风格等

### 3. Pipeline 集成

#### `scripts/run_content_pipeline.py` (已更新)
- 在分发阶段之后自动运行文章生成
- 失败时优雅降级（不影响其他阶段）
- 在报告中展示文章生成状态

---

## 使用指南

### 方式 1: 自动运行（推荐）

完整流程会在每日运行时自动执行：

```bash
# 直接运行完整流程
python3 scripts/run_content_pipeline.py

# 或使用强制刷新
PIPELINE_FORCE_REFRESH=1 python3 scripts/run_content_pipeline.py
```

流程中自动执行：
1. 抓取热点 → 
2. 生成社交内容 → 
3. 审校内容 → 
4. 质量检查 → 
5. 分发社交 → 
6. **生成深度文章** ← 新增

### 方式 2: 单独运行

如果仅想重新生成文章（不刷新其他阶段）：

```bash
python3 scripts/generate_article_from_snippets.py
```

### 方式 3: 通过 GitHub Actions

编辑 `.github/workflows/update-hot-news.yml` 或等效的 CI/CD 配置，确保包含完整流程。

---

## 输出文件详解

### HTML 页面示例结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <!-- SEO Meta 标签 -->
    <title>清明转运秘诀：AI如何重新定义命理趋势分析 | 问星AI</title>
    <meta name="description" content="...">
    <meta name="keywords" content="清明, 运势, 命理, 转运, 玄学">
    
    <!-- Open Graph (社交分享) -->
    <meta property="og:title" content="...">
    <meta property="og:description" content="...">
    
    <!-- 结构化数据 -->
    <script type="application/ld+json">
    { "@type": "NewsArticle", ... }
    </script>
    <script type="application/ld+json">
    { "@type": "FAQPage", ... }
    </script>
</head>
<body>
    <article>
        <!-- 文章正文: 2000-3000 字 -->
        <h2>清明的真实命理意义</h2>
        <p>...</p>
        
        <!-- FAQ 部分 -->
        <section class="faq-section">
            <h3>常见问题</h3>
            <div class="faq-item">
                <strong>Q: AI命理与传统命理有何区别？</strong>
                <p>A: ...</p>
            </div>
        </section>
        
        <!-- CTA (行动号召) -->
        <div class="cta-box">
            <p>立即体验问星AI的AI命理分析</p>
            <a href="https://wenxingai.top/?utm_source=article&..." class="cta-button">
                立即体验问星AI
            </a>
        </div>
        
        <!-- 内链 -->
        <div class="internal-links">
            <a href="/mingli-xuanxue-news.html">查看更多热点新闻</a>
            <a href="/">返回首页</a>
        </div>
    </article>
</body>
</html>
```

### articles-index.json 格式

```json
{
  "generated_at": "2026-04-06T12:47:10.139112+08:00",
  "total_articles": 2,
  "articles": [
    {
      "slug": "daily-hot-news-2026-04-06-zh_cn",
      "title": "清明转运秘诀：AI如何重新定义命理趋势分析",
      "locale": "zh_cn",
      "html_path": "/articles/daily-hot-news-2026-04-06-zh_cn.html",
      "md_path": "/articles/daily-hot-news-2026-04-06-zh_cn.md",
      "keywords": ["清明", "转运", "命理", "AI", "流年"],
      "seo_title": "清明转运秘诀：AI如何重新定义命理趋势分析",
      "published_at": "2026年4月6日"
    },
    ...
  ]
}
```

---

## 在首页展示文章

### 方式 A：直接嵌入 HTML

从 `generated/articles-section.html` 复制片段代码，粘贴到 `index.html` 合适位置：

```html
<!-- 在 </main> 之前或适当位置插入 -->
<!-- 深度解读部分 (开始) -->
<section id="articles" class="articles-section">
    ...
    (完整代码见 articles-section.html)
</section>
<!-- 深度解读部分 (结束) -->
```

### 方式 B：动态加载

如果想通过 JavaScript 动态加载（不修改主 HTML）：

```javascript
// 在你的主页脚本中
fetch('/generated/articles-index.json')
  .then(r => r.json())
  .then(data => {
    // 构建文章列表 UI
    const articles = data.articles.slice(0, 6);
    // ... 渲染代码
  });
```

---

## 文章 SEO 优化要点

### 1. 关键词策略
- **一级关键词**: 命理、运势、流年、玄学（相对稳定）
- **二级关键词**: 根据当日热点自动调整（如"清明""塔罗""官非"）
- **品牌词**: 问星AI、AI命理

### 2. 标题优化
```
格式: [当日热点概念] + [理性视角] + [品牌承诺]
例: "清明转运秘诀：AI如何重新定义命理趋势分析"
    └─ 热点    └─ 差异化     └─ 品牌承诺
```

### 3. 内容结构
- H1: 文章标题（1 个）
- H2: 主要段落标题（3-5 个）
- P: 段落文本（20+ 个）
- Strong: 关键概念加粗
- Em: 引用新闻斜体

### 4. 内链策略
- **首页**: 品牌介绍
- **热点新闻页**: 完整热点列表
- **其他文章**: 相关主题

### 5. 结构化数据
- NewsArticle: 告诉 Google 这是新闻文章
- FAQPage: 在搜索结果中显示常见问题

---

## 性能与成本

### API 调用

| 操作 | 调用次数 | 成本 |
|------|---------|------|
| 生成社交内容 (1 次) | 1x `gemini-2.5-pro` | ~0.05-0.10 USD |
| 审校内容 (1 次) | 1x `gemini-2.5-pro` | ~0.05-0.10 USD |
| 生成 2 篇文章 (新) | 2x `gemini-2.5-pro` | ~0.10-0.20 USD |
| **每日总成本** | | **~0.20-0.40 USD** |

（基于 Gemini 2.5 Flash pricing，实际可能更低）

### 存储

| 元素 | 文件数量 | 大小 |
|------|---------|------|
| HTML 页面 | 2 (zh_cn, zh_hant) | ~100-150 KB |
| Markdown | 2 | ~50-80 KB |
| JSON 索引 | 1 | ~10 KB |
| **每日增量** | | **~200 KB** |

---

## 故障排查

### 问题 1: "Failed to load articles index"

**原因**: `articles-index.json` 还未生成

**解决**:
1. 确认 Gemini API Key 配置正确
2. 运行 `python3 scripts/generate_article_from_snippets.py`
3. 检查 `generated/articles-report.md` 中的错误

### 问题 2: 文章内容不好

**原因**: Prompt 需要调整或模型输出不稳定

**解决**:
1. 编辑 `prompts/gemini_article_generation_prompt.txt`
2. 重新运行文章生成
3. 人工审核后发布

### 问题 3: 文章没有在首页显示

**原因**: JavaScript 加载失败或路径错误

**解决**:
1. 检查浏览器控制台错误 (F12)
2. 验证 `/generated/articles-index.json` 是否可访问
3. 检查 CORS 配置（如果部署在不同域）

---

## 最佳实践

### 发布前检查清单

- [ ] 文章标题包含关键词且吸引人
- [ ] 首段开篇自然引入热点，不生硬
- [ ] 内容深度 2000+ 字，逻辑清晰
- [ ] FAQ 部分回答了真实用户的疑问
- [ ] 内链指向相关且有价值的页面
- [ ] CTA 文案清晰，指向 `/` 或带 UTM 参数
- [ ] 没有大量空泛词汇（"开启""洞察""掌握"等）
- [ ] 没有绝对预言表达（"一定会""注定"等）

### 定期优化

```bash
# 每 2 周审查一次
1. 查看文章点击率 (GA)
2. 检查排名变化 (GSC)
3. 读者反馈改进
4. 更新 Prompt 中的指导
```

---

## 下一步改进

1. **自动化内链**: 根据文章内容自动推荐链接
2. **A/B 标题测试**: 生成多个标题版本，选择最优
3. **视频脚本生成**: 从文章自动生成短脚本
4. **多语言扩展**: 添加日语、越南语等
5. **文章评分**: 基于 SEO 指标自动评分
6. **反向链接监测**: 追踪外部链接到文章的情况

---

## 参考资源

- [Google SEO Starter Guide](https://developers.google.com/search/docs/beginner/seo-starter-guide)
- [JSON-LD 文档](https://json-ld.org/)
- [Gemini API 文档](https://ai.google.dev/docs)
- [问星AI 产品文档](https://wenxingai.top/)
