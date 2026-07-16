# 问星AI 内容自动化运行报告 2026年7月16日 13:41

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：60a63a6d46508ec7421f617a1fc10fdbdcdc0165
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 50分鐘讀透紫微經典《太微賦》：你的命盤格局藏著怎樣的先天大運？學會古人流傳至今的“命理天規”！#太微賦#紫微斗數#絕處逢生#凋而不落#深夜聽書#順時而動#司馬懿 #大運格局#命理天規
- 認真，如果超越倫呢真係要開檔做生意 我真心覺得佢有幾項生意，佢真係可以做得風生水起 1.美甲店 2.占卜塔羅牌店 3.香水化妝品店
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 虎爺生日快到了！命理師曝3招開運法 旺財又防小人
- 2026下半年3星座運勢拉警報！水瓶當心破財慘賠 命理師教1招解套

## 新增标题
- 50分鐘讀透紫微經典《太微賦》：你的命盤格局藏著怎樣的先天大運？學會古人流傳至今的“命理天規”！#太微賦#紫微斗數#絕處逢生#凋而不落#深夜聽書#順時而動#司馬懿 #大運格局#命理天規
- 認真，如果超越倫呢真係要開檔做生意 我真心覺得佢有幾項生意，佢真係可以做得風生水起 1.美甲店 2.占卜塔羅牌店 3.香水化妝品店

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年7月16日 13:41
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
