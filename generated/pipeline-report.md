# 问星AI 内容自动化运行报告 2026年7月23日 21:37

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：13ff9b6f7e93dc8eb7c834ef9d10538aa8452925
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 誰即將走進你的生活？ta會給你帶來什麼？你和ta會有什麼故事？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 我真的懷疑。 是不是很多人都以為命理師有一個隱藏技能。 叫做： 「通靈Google。」 客人： 「老師，我要不要換工作？」 可以。 這很正常。 「老師，我跟他還有機會嗎？」 也很正常。 「老師，我最近一直掉頭髮，是不是流年不好？」 …… 嗯？ 「老師，我家的貓最近一直瞪我，是
- [問卦] 敵基督 vs 紫微聖人 誰會贏
- 大暑逢「三合火局」易斷理智線！命理師曝4大開運祕訣 3生肖運勢旺
- 大暑到！命理師曝4招開運法 5生肖運勢大翻轉

## 新增标题
- 誰即將走進你的生活？ta會給你帶來什麼？你和ta會有什麼故事？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 大暑到！命理師曝4招開運法 5生肖運勢大翻轉

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年7月23日 21:37
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
