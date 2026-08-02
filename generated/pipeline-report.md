# 问星AI 内容自动化运行报告 2026年8月2日 12:12

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：23fe3a074035bfb69214aecc713e0e0e8b474671
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 只有屬龍人才有的命格！辰逢申月三合成局，「天祿貴人」加持，8月大財小財不斷！#屬龍運勢#生肖龍#2026年運勢#辰申三合#天祿貴人#命理分析#開運指南#貴人運#財運爆發
- AI 算命行業思路還是太保守了 為什麼不能做一個 AI 改運助手 根據你的八字、大運和流年 每天提醒你幾點出門、穿什麼顏色、坐哪個位置 廣告語我都想好了： Don't fight your fate. Schedule it.
- [新聞] 土星逆行釀震盪！命理師示警：8月迎毒油
- 觀音成道日來了！命理師揭開運法：「做5件事」累積福報
- 2026年8月7日迎立秋！命理專家公開6大開運法，3件事別做小心影響運勢| 生活發現

## 新增标题
- AI 算命行業思路還是太保守了 為什麼不能做一個 AI 改運助手 根據你的八字、大運和流年 每天提醒你幾點出門、穿什麼顏色、坐哪個位置 廣告語我都想好了： Don't fight your fate. Schedule it.
- [新聞] 土星逆行釀震盪！命理師示警：8月迎毒油

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 7/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年8月2日 12:12
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
