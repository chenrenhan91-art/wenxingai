# 问星AI 内容自动化运行报告 2026年8月24日 11:23

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：cf1ecb97a1dbc42fdf3e8ef6e29d753b50047efc
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【金牛座】專注地朝向想要抵達的終點你最終的成績將會令人稱羨｜月能量運勢｜#塔羅占卜#運勢 #星座
- 我發現我好像一直沒把一件事講清楚。 我沒有自己開一堂「虎嚕八字班」。 現在跟著我學八字的學生， 正式課程是由專業老師上課。 而我的位置比較像—— 陪你一路學下去的上線。 上課聽不懂？ 可以來問我。 回家看命盤看到懷疑人生？ 可以來找我。 開始接觸案例，不
- [新聞]台灣命理師說「北京沒冰箱」中國網友群嘲
- 「處暑到」秋老虎發威！4生肖運勢亮紅燈…命理師：千萬別做2件事
- 周日迎處暑！命理師曝12生肖運勢、「這動物」貴人財運雙旺

## 新增标题
- 【金牛座】專注地朝向想要抵達的終點你最終的成績將會令人稱羨｜月能量運勢｜#塔羅占卜#運勢 #星座
- 我發現我好像一直沒把一件事講清楚。 我沒有自己開一堂「虎嚕八字班」。 現在跟著我學八字的學生， 正式課程是由專業老師上課。 而我的位置比較像—— 陪你一路學下去的上線。 上課聽不懂？ 可以來問我。 回家看命盤看到懷疑人生？ 可以來找我。 開始接觸案例，不

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年8月24日 11:23
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
