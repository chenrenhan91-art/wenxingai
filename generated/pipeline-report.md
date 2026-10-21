# 问星AI 内容自动化运行报告 2026年10月21日 21:16

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：c5b717dfa5b9ba1a447824e7f9a2b334ea2be7f2
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【紫微斗數】流年遇到擎羊、陀羅、火星、鈴星，真的會倒黴嗎？四大煞星其實暗藏翻身機會！#紫微斗數#四大煞星#擎羊陀羅火星鈴星#流年運勢#命理 #改運#流年命盤#煞星化解#命理解析
- 2026年10月19日至25日這一週，十二星座將迎來哪些課題與轉折？以下透過每個星座對應的一張塔羅牌，解讀本週值得留意的情緒、關係與行動方向。 https://t.co/ogbx6ZJhz3
- [問卦] 中醫 是醫學還是玄學？
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光
- 手機桌布放「前任照」恐影響運勢！命理師皆「3類照片」禁忌

## 新增标题
- 【紫微斗數】流年遇到擎羊、陀羅、火星、鈴星，真的會倒黴嗎？四大煞星其實暗藏翻身機會！#紫微斗數#四大煞星#擎羊陀羅火星鈴星#流年運勢#命理 #改運#流年命盤#煞星化解#命理解析
- 手機桌布放「前任照」恐影響運勢！命理師皆「3類照片」禁忌

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月21日 21:17
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
