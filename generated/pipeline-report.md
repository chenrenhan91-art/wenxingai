# 问星AI 内容自动化运行报告 2026年6月5日 00:21

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：de1a80d0aa57cc05046922094936fad3aa487961
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 身邊有人在暗戀你嗎？新人還是舊人？ta是過客還是緣分？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 看到有些年輕的紫微斗數命理師們嘗試著要把馬斯克、巴菲特等「巨頭」的命盤打出來，精神可佩！可惜在他們的養成教育當中缺乏一些環節，這種努力恐怕都要做白工，非常可惜！ 紫微斗數、八字等中國傳統術數的先天缺陷：
- [新聞] 鬼門開遇日全蝕超凶？命理師引述古籍：
- 命理師揭下半年運勢！「乳製品」恐短缺？
- 2026芒種節氣到！命理師揭「兩大開運秘訣」 2生肖女性大掃除有助旺財

## 新增标题
- 身邊有人在暗戀你嗎？新人還是舊人？ta是過客還是緣分？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 看到有些年輕的紫微斗數命理師們嘗試著要把馬斯克、巴菲特等「巨頭」的命盤打出來，精神可佩！可惜在他們的養成教育當中缺乏一些環節，這種努力恐怕都要做白工，非常可惜！ 紫微斗數、八字等中國傳統術數的先天缺陷：
- 命理師揭下半年運勢！「乳製品」恐短缺？

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月5日 00:21
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
