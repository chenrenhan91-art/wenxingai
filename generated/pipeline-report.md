# 问星AI 内容自动化运行报告 2026年10月22日 21:17

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：19ad91a1b86529940af1ae808df212c396f8f9f6
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 假如你疏遠他，他會怎麼樣、感受、想法、行動力是如何的？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 有時候幫客人看感情合盤 真的很像在看兩個人吵架的監視器🤣 客人： 「老師 我們八字合很多 是不是代表很適合？」 我： 「那你們平常怎麼相處？」 客人： 「就很常吵架啊」 「但我們八字很合耶！」 等一下 你是不是把天干地支的合 當成結婚保證書了 八字裡的合 有可能是吸
- [問卦] 中醫 是醫學還是玄學？
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光
- 討論牆 | 蘇巧慧、李四川新北大激戰！命理師解鎖「面相+流年」秒點名這人

## 新增标题
- 有時候幫客人看感情合盤 真的很像在看兩個人吵架的監視器🤣 客人： 「老師 我們八字合很多 是不是代表很適合？」 我： 「那你們平常怎麼相處？」 客人： 「就很常吵架啊」 「但我們八字很合耶！」 等一下 你是不是把天干地支的合 當成結婚保證書了 八字裡的合 有可能是吸
- 討論牆 | 蘇巧慧、李四川新北大激戰！命理師解鎖「面相+流年」秒點名這人

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月22日 21:17
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
