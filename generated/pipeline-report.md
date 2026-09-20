# 问星AI 内容自动化运行报告 2026年9月20日 11:15

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：5fe35776d00e6ba1358026d04592ceecd6a4bfea
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【客觀評價】他對你有幾分真心？對關係有幾分認真？他最最真實的想法|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 自學紫微斗數幾個月，是一個辛苦的心路歷程。看著自己的命盤，看到的是走過的荊棘路。至於預測未來，我尚未掌握這份功力 我的命盤很“硬”，被名字霸氣的星燿占據；都是武、軍、殺之流的。但剛中藏柔：雖是金命，但不是粗狂剛出土的狗頭金，而是歷經鐵匠千錘百煉的
- [問卦] 中醫 是醫學還是玄學？
- 中秋招財、求姻緣錯過等一年！命理師揭「未婚男女晚睡」開運法- 娛樂
- 秋分到好運來！命理師揭「做3事」助開運 生肖龍事業遇貴人

## 新增标题
- 【客觀評價】他對你有幾分真心？對關係有幾分認真？他最最真實的想法|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 自學紫微斗數幾個月，是一個辛苦的心路歷程。看著自己的命盤，看到的是走過的荊棘路。至於預測未來，我尚未掌握這份功力 我的命盤很“硬”，被名字霸氣的星燿占據；都是武、軍、殺之流的。但剛中藏柔：雖是金命，但不是粗狂剛出土的狗頭金，而是歷經鐵匠千錘百煉的

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月20日 11:15
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
