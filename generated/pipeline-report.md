# 问星AI 内容自动化运行报告 2026年9月3日 21:16

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：a58c4a9f6ec4dd1d3d08599db8153f03eedfcb0e
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- [極致反差]他眼中vs心底的你！什麼出乎意料的割裂反差？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 線下看了一個命理師，本來看著玩，結果把我前面的都說的非常准，還說我工作變動大會轉行（實話），我現在在幹啥都說的很準。然後我問了未來財運，他說會有人給我錢花……？？？這啥意思？
- [問卦] 中醫 是醫學還是玄學？
- 【12星座本週運勢】8/31至9/6最旺星座TOP3，12星座整體運勢、工作運、桃花運一次看
- 塔羅星座- 副刊

## 新增标题
- 線下看了一個命理師，本來看著玩，結果把我前面的都說的非常准，還說我工作變動大會轉行（實話），我現在在幹啥都說的很準。然後我問了未來財運，他說會有人給我錢花……？？？這啥意思？
- 【12星座本週運勢】8/31至9/6最旺星座TOP3，12星座整體運勢、工作運、桃花運一次看
- 塔羅星座- 副刊

## 次日运营建议
- 明日优先延展「塔罗星象」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月3日 21:16
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
