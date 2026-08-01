# 问星AI 内容自动化运行报告 2026年8月1日 21:33

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：2553bfeb55a45a17a33c6ba0492801a094e7f8f3
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 只有屬龍人才有的命格！辰逢申月三合成局，「天祿貴人」加持，8月大財小財不斷！#屬龍運勢#生肖龍#2026年運勢#辰申三合#天祿貴人#命理分析#開運指南#貴人運#財運爆發
- 官祿宮反映你的事業運勢、工作天賦、升遷機會與職場人際關係。 ✦ 吉星入宮：事業順遂，容易獲得賞識和升遷 ✦ 主星影響：紫微入宮→適合管理職；天機入宮→適合策劃分析 ✦ 化祿入宮：財運與事業雙豐收的好兆頭 #紫微斗數 #官祿宮 #命盤解析 #事業運勢 #命運屋 #Fa
- [問卦] 敵基督 vs 紫微聖人 誰會贏
- 2026年8月7日迎立秋！命理專家公開6大開運法，3件事別做小心影響運勢| 生活發現
- 觀音成道日來了！命理師揭開運法：「做5件事」累積福報

## 新增标题
- 只有屬龍人才有的命格！辰逢申月三合成局，「天祿貴人」加持，8月大財小財不斷！#屬龍運勢#生肖龍#2026年運勢#辰申三合#天祿貴人#命理分析#開運指南#貴人運#財運爆發
- 2026年8月7日迎立秋！命理專家公開6大開運法，3件事別做小心影響運勢| 生活發現

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年8月1日 21:33
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
