# 问星AI 内容自动化运行报告 2026年10月29日 21:12

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：c1e7d5757a5684a49b06a550180590ec59e706e5
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他對他對你是否還有留戀？為什麼不主動？他是真不在意，還是裝冷漠偷偷想你？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 🐯 虎嚕命理 𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.10.27（二）甲戌日 🔮 🔔 不要因為走得太遠，而忘記了自己為什麼出發。 🌳 甲木遇戌土，今天容易忙著完成目標、證明自己，卻忘了當初真正想守住的是什麼。 走得快很厲害 但方向對，才不會努力半天跑去別人家 ✨ 十神開運指南｜請對
- [問卦] 中醫 是醫學還是玄學？
- 霜降到！命理師點名5生肖運勢大翻盤…開運致富關鍵曝光
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光

## 新增标题
- 他對他對你是否還有留戀？為什麼不主動？他是真不在意，還是裝冷漠偷偷想你？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月29日 21:12
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
