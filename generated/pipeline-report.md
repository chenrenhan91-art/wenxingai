# 问星AI 内容自动化运行报告 2026年7月14日 22:56

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：9cf72231d8910f448f4952a0aa0fd51486b4b8d8
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他是值得的人嗎？你懂他對你的心意嗎？實際上他對你的感情如何？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 何篤霖離開主持了24年的《命運好好玩》，就連多位資深命理老師也看在眼裡，與何篤霖同進退，消極推辭通告，讓接棒的小賴和湯鎮瑋，面臨不少挑戰 【獨家！命理師推辭《命運好好玩》 小賴接棒何篤霖陷危機】 mirrormedia.mg/story/20260713…
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 虎爺誕辰日將至！命理師曝「開運秘訣」：正財偏財都來
- 大暑「三合火局」！命理師曝4招求財開運 這生肖慎防血光災

## 新增标题
- 何篤霖離開主持了24年的《命運好好玩》，就連多位資深命理老師也看在眼裡，與何篤霖同進退，消極推辭通告，讓接棒的小賴和湯鎮瑋，面臨不少挑戰 【獨家！命理師推辭《命運好好玩》 小賴接棒何篤霖陷危機】 mirrormedia.mg/story/20260713…

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年7月14日 22:56
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
