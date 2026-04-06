# 深度解读文章集

此目录为问星AI自动生成的深度解读文章。

## 文件结构

```
articles/
├── {slug}-zh_cn.html        # 简体中文文章（完整 HTML 页面）
├── {slug}-zh_cn.md          # 简体中文文章（Markdown 源）
├── {slug}-zh_hant.html      # 繁体中文文章（完整 HTML 页面）
├── {slug}-zh_hant.md        # 繁体中文文章（Markdown 源）
└── ...
```

## 文章自动生成流程

1. **输入**: `hot-news-data.json`（每日热点）
2. **处理**: `generate_daily_content.py`（生成社交 snippet）
3. **扩展**: `generate_article_from_snippets.py`（从 snippet 扩展为完整文章）
4. **输出**: 
   - HTML 页面（用于直接在浏览器打开）
   - Markdown 文件（便于版本控制和编辑）
   - JSON 索引（`articles-index.json`）

## 文章特点

✓ **SEO 优化**:
- 包含精心设计的 title, meta description, keywords
- 结构化数据 (JSON-LD): NewsArticle + FAQPage
- 内链建议: 指向首页和其他相关文章
- 响应式设计

✓ **内容质量**:
- 长文本: 2000-3000 字
- 多语言: 简体中文 + 繁体中文
- 自然叙述: 从热点 → 深度分析 → 产品定位
- FAQ 部分: 针对常见误解

✓ **转化优化**:
- 主 CTA: 鼓励访问问星AI体验
- 次 CTA: 补充建议
- UTM 参数追踪

## 发布指南

### 方式 1: 静态部署（推荐）

```bash
# 1. 构建文章
python3 scripts/generate_article_from_snippets.py

# 2. 文章已输出到 generated/articles/*.html
# 3. 部署到网站时，将整个 articles 文件夹复制到根目录
# 4. 更新首页导航指向 /articles/{slug}.html
```

### 方式 2: 集成到首页

在 `index.html` 中添加"深度文章"部分，向用户展示最新文章的链接。

参考代码:
```html
<section id="articles" class="articles-section">
  <h2>深度解读</h2>
  <ul id="articles-list"></ul>
</section>

<script>
  fetch('/generated/articles-index.json')
    .then(r => r.json())
    .then(data => {
      const list = document.getElementById('articles-list');
      data.articles.slice(0, 5).forEach(article => {
        const li = document.createElement('li');
        li.innerHTML = `<a href="${article.html_path}">${article.title}</a>`;
        list.appendChild(li);
      });
    });
</script>
```

## 常见问题

**Q: 文章需要手动审核吗？**
A: 建议部署前进行一次人工审核，检查内容的适当性和品牌对齐度。之后可以逐步自动化。

**Q: 如何更新现有文章？**
A: 编辑 `hot-news-data.json` 和相关热点源配置，然后重新运行生成流程即可。

**Q: 文章如何更新到网站？**
A: 通过 Git 提交、自动化构建工具 (GitHub Actions, etc.) 或直接 SFTP 上传。

## 相关脚本

- `generate_daily_content.py` - 生成社交内容包
- `generate_article_from_snippets.py` - 从 snippet 扩展为完整文章
- `run_content_pipeline.py` - 主流程编排
