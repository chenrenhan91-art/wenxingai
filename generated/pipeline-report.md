# 问星AI 内容自动化运行报告 2026年10月6日 21:18

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：8933a30374a9bd0fa6b7ef8a79bb1f69631fd20f
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他對你動心or走腎？心動程度有多少？更在意什麼？怎麼看待關係的？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 天色漸漸光啦！ 青鳥發文說沈伯洋演講「出現聖光」，文章破4萬讚，一堆青鳥喊太神啦！ 更有命理師指出，雲層裂開，一道道金光穿雲而出，玄學的角度有「撥雲見日」的意象。 還有青鳥聽完命理師的分析驚呼：「我在光裡看到大佛！」 我猜沈伯洋出生的那天，天上一定是
- [問卦] 中醫 是醫學還是玄學？
- 寒露10/8到了！命理師點名「3類人」運勢動盪要小心，開運「3招」先整理帳目
- 獨家／寒露10月8日到！日夜溫差轉大 命理師點名「4生肖」運勢有變化

## 新增标题
- 他對你動心or走腎？心動程度有多少？更在意什麼？怎麼看待關係的？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 寒露10/8到了！命理師點名「3類人」運勢動盪要小心，開運「3招」先整理帳目
- 獨家／寒露10月8日到！日夜溫差轉大 命理師點名「4生肖」運勢有變化

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月6日 21:18
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
