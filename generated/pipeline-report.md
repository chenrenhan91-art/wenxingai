# 问星AI 内容自动化运行报告 2026年11月6日 21:09

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：c7ef899fbb01ec7ea0ebcbf7f2b1ea12d33e0222
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【紫微斗数】天相星落在哪裏更容易遇到貴人？從紫微命盤看你的人脈與資源變現機會！#紫微斗数#天相星#贵人运#命盘解析#十二宫#事业运势#命理科普#紫微教学#印星#流年运势
- 每次有人聽到八字裡有「剋」 第一個反應通常都是 「老師 那是不是不好？」 先不要緊張🤣 五行相剋 不代表一定是壞事 例如木剋土 土剋水 水剋火 火剋金 金剋木 這是五行之間 相互制約的關係 就像一棵樹 如果只知道一直長 卻完全沒有修剪 也不一定能長得漂亮 命盤也是
- [問卦] 中醫 是醫學還是玄學？
- 2026立冬運勢全解析！翻轉財運3大關鍵、事業人際洗牌，命理師教你拜拜開運色穿搭
- 神準！韓命理師3個月前預言台股「這時段」震盪 網驚：以後不分析、直接算命

## 新增标题
- 每次有人聽到八字裡有「剋」 第一個反應通常都是 「老師 那是不是不好？」 先不要緊張🤣 五行相剋 不代表一定是壞事 例如木剋土 土剋水 水剋火 火剋金 金剋木 這是五行之間 相互制約的關係 就像一棵樹 如果只知道一直長 卻完全沒有修剪 也不一定能長得漂亮 命盤也是
- 神準！韓命理師3個月前預言台股「這時段」震盪 網驚：以後不分析、直接算命

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月6日 21:10
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
