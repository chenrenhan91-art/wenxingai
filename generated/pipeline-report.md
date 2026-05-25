# 问星AI 内容自动化运行报告 2026年5月25日 15:15

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：c5f65cadf589493f7ecdc0fb42de5076b93e2cc4
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【願望顯化】 2026下半年🌸你的戀愛運🔮他會回頭(復合)嗎？還是你將遇見💫新戀情｜愛情塔羅占卜🔮 舊人回歸？新人出現？復合機率＆新戀情預測
- 母女合盤：揭秘大運背離的宿命羈絆，警惕母愛變毒藥！命盤拆解：葉一茜與女兒森蝶運勢推演，切勿盲目雞娃，如何用八字為孩子規劃未來？“女憑夫貴、母憑子... youtu.be/qik_fs39buI?si… 来自 @YouTube #叶一茜 #浪姐 #乘风2026 #八字 #命理分析 #算命 #森蝶 #田
- [新聞] 狄鶯頭痛了！ 命理師曝孫安佐「皇帝命」
- 預言馬英九犯小人成真 命理師分析流年：未來2年健康是重點
- 早預言馬英九犯小人!命理師驚揭「流年走死神」： 恐有大變化

## 新增标题
- 【願望顯化】 2026下半年🌸你的戀愛運🔮他會回頭(復合)嗎？還是你將遇見💫新戀情｜愛情塔羅占卜🔮 舊人回歸？新人出現？復合機率＆新戀情預測
- 預言馬英九犯小人成真 命理師分析流年：未來2年健康是重點
- 早預言馬英九犯小人!命理師驚揭「流年走死神」： 恐有大變化

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月25日 15:16
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[ok] DashScope fallback model selected: qwen3.6-flash-2026-04-16
Gemini content generation failed: invalid Gemini response: missing zh_cn.site_article.seo_description
