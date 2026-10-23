# 问星AI 内容自动化运行报告 2026年10月23日 11:15

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：f6e15e374e1e2b7c3cc9044395aab59ef5f908b1
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他對你最新的想法打算不想讓你知道事兒希望你怎麼做曖昧愛情戀愛桃花塔羅占卜
- 🐯 虎嚕命理 𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.10.22（四）己巳日 🔮 🔔 凡事皆有裂痕，那是光照進來的地方。 🌾 巳火生己土，今天容易重新看見某些傷口，也可能忽然明白：原來當初讓你難過的事，正在教你如何保護自己。 有裂痕不代表你壞掉了 只是光終於找到入口 ✨ 十神開運指
- [問卦] 中醫 是醫學還是玄學？
- 【手機桌布也會影響運勢！命理師曝「這三種別放」：恐進入低頻狀態】 桌布不要亂放 （#起啵）
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光

## 新增标题
- 他對你最新的想法打算不想讓你知道事兒希望你怎麼做曖昧愛情戀愛桃花塔羅占卜
- 🐯 虎嚕命理 𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.10.22（四）己巳日 🔮 🔔 凡事皆有裂痕，那是光照進來的地方。 🌾 巳火生己土，今天容易重新看見某些傷口，也可能忽然明白：原來當初讓你難過的事，正在教你如何保護自己。 有裂痕不代表你壞掉了 只是光終於找到入口 ✨ 十神開運指
- 【手機桌布也會影響運勢！命理師曝「這三種別放」：恐進入低頻狀態】 桌布不要亂放 （#起啵）

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月23日 11:15
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
