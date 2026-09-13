# 问星AI 内容自动化运行报告 2026年9月13日 21:13

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：f5f90ecbe291a13cbb73c853063778be4b8ac2e5
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他今天想你了嗎？怎麼想的？想了什麼？對你的感情、對關係的想法|曖昧|愛情|戀愛|桃花|塔羅占卜
- 今天的塔羅占卜改明後天開台喔 忙碌兩天做餅全身痠痛 有點累等身體好點再占占唷🙏
- [問卦] 中醫 是醫學還是玄學？
- 入秋運勢變化了！命理師曝「3生肖」最旺 屬牛財運、貴人全都有
- 孫安佐遭羈押禁見！命理師2年前預言「今年走死神流年」：難逃牢獄之災

## 新增标题
- 他今天想你了嗎？怎麼想的？想了什麼？對你的感情、對關係的想法|曖昧|愛情|戀愛|桃花|塔羅占卜
- 今天的塔羅占卜改明後天開台喔 忙碌兩天做餅全身痠痛 有點累等身體好點再占占唷🙏
- 入秋運勢變化了！命理師曝「3生肖」最旺 屬牛財運、貴人全都有
- 孫安佐遭羈押禁見！命理師2年前預言「今年走死神流年」：難逃牢獄之災

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月13日 21:13
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
