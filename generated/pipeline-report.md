# 问星AI 内容自动化运行报告 2026年6月27日 14:29

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：262bf79234aad7a5513dee55abd8445cc8b43f3c
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 摩羯座｜這季只要全然相信自己可以宇宙會給你意料之外的驚喜｜季能量運勢牌卡解讀｜20260626發佈｜#塔羅占卜#運勢 #星座
- #匿名發言6207 99： 最近向開始做塔羅占卜想問問大家會希望的收費價位和占卜的方式
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 今天夏至別踩雷！命理師曝開運關鍵：吃麵配「這水果」最旺運，穿錯顏色恐影響運勢
- 孫協志逼問：5566未來會亡嗎？ 命理師看運勢鐵口直斷給答案 | 娛樂 | CTWANT

## 新增标题
- 摩羯座｜這季只要全然相信自己可以宇宙會給你意料之外的驚喜｜季能量運勢牌卡解讀｜20260626發佈｜#塔羅占卜#運勢 #星座

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月27日 14:30
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[ok] DashScope fallback model selected: qwen3.6-flash-2026-04-16
Gemini content generation failed: invalid Gemini response: missing zh_cn.site_article.excerpt
