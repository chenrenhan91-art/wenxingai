# 问星AI 内容自动化运行报告 2026年5月31日 14:58

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：b21fe0ae9775e3765b56ec00c0291b1374618b5d
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 香灰千万别乱丢，这么做能招财！ #玄學 #國學 #風水 #香灰 #招財
- 揭秘內娛最甜婚姻真相，深扒浪姐唐藝昕命盤：甜妹皮囊下的「馴龍女王」，把張若昀調教成「純愛戰神」的神級馭夫術！《乘風2026》運勢大推演，女生必看... youtu.be/ArBvZDI78aY?si… 来自 @YouTube #唐艺昕 #浪姐 #乘风2026 #八字 #命理分析 #算命 #嫁豪门 #张若
- [新聞] 鬼門開遇日全蝕超凶？命理師引述古籍：
- 6／5芒種到！命理師教2招開運貴人、財氣雙旺- 好運到
- 2026九紫離火運｜命理師點名4大生肖 未來5年運勢大洗牌變化驚人

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月31日 14:59
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[ok] DashScope fallback model selected: qwen3.6-flash-2026-04-16
Gemini content generation failed: invalid Gemini response: missing zh_cn.site_article.excerpt
