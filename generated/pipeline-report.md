# 问星AI 内容自动化运行报告 2026年11月21日 21:08

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：dfa931e739fd65278af70596d51d2f0f64ca6203
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【紫微斗数】天相星落在哪裏更容易遇到貴人？從紫微命盤看你的人脈與資源變現機會！#紫微斗数#天相星#贵人运#命盘解析#十二宫#事业运势#命理科普#紫微教学#印星#流年运势
- 怎樣學好算命？是這樣的，我講個故事給你聽。 以前，有位飛星派的命理師，跟老師學了好多年，也就記下了一些口訣，根本不太會算。 但有一次，自己欠了巨額的債，完全還不上，債主到處找他，他每天東躲西藏，活得提心吊膽。那時，他想起自己學過算命，就每天躲在什
- [新聞] 神機妙算！沈伯洋塔羅牌抽「死神牌」有反
- 擺脫內耗！命理師揭下週12星座運勢：迎重大轉折
- 台股崩跌！命理師祭「3不原則」 曝2027年運勢：還有獲利空間

## 新增标题
- 【紫微斗数】天相星落在哪裏更容易遇到貴人？從紫微命盤看你的人脈與資源變現機會！#紫微斗数#天相星#贵人运#命盘解析#十二宫#事业运势#命理科普#紫微教学#印星#流年运势
- 擺脫內耗！命理師揭下週12星座運勢：迎重大轉折
- 台股崩跌！命理師祭「3不原則」 曝2027年運勢：還有獲利空間

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月21日 21:09
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
