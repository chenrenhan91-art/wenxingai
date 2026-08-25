# 问星AI 内容自动化运行报告 2026年8月25日 11:20

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：6745602cecadba2a2bf3cc934c1cf459abff82b4
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他心裡有別人嗎？你是不是他的唯一？他對你和對別人有什麼區別？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 塔羅牌與占星洞察相互交會，便形成了「塔羅星座運勢」（Tarotscope）。2026年8月24日至30日這一週，十二星座將迎來什麼課題？以下透過每個星座對應的一張塔羅牌，解讀本週值得留意的情緒、關係與人生方向。
- [新聞]台灣命理師說「北京沒冰箱」中國網友群嘲
- 【鬼月最重要一天來了！命理師示警「4種人」當心 最簡單開運法曝光】 就在這個星期四～（#豬頭皮）
- 鬼月最重要一天來了！命理師示警「4種人」當心 最簡單開運法曝光

## 新增标题
- 他心裡有別人嗎？你是不是他的唯一？他對你和對別人有什麼區別？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 塔羅牌與占星洞察相互交會，便形成了「塔羅星座運勢」（Tarotscope）。2026年8月24日至30日這一週，十二星座將迎來什麼課題？以下透過每個星座對應的一張塔羅牌，解讀本週值得留意的情緒、關係與人生方向。

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年8月25日 11:21
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
