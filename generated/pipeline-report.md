# 问星AI 内容自动化运行报告 2026年7月20日 23:13

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：0d6640e78abcbe514b8780bcfb5fb396b32fbce9
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【神預言】愛神給你的傳訊：屬於你的愛情桃花正在降臨！|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 命理師有時候，比心理師還安靜。 很多人以為。 算命就是一直講。 其實不是。 很多時候。 我反而都在聽。 聽一個人。 怎麼把委屈藏了十幾年。 怎麼一直替別人活。 怎麼一直覺得自己不夠好。 很多人來找我。 真正想要的。 不是一句： 「你今年財運很好。」 而是有人願意聽他
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 2026大暑最強開運法！命理師曝3招開運、2風水法調氣場：財運最旺生肖、8大禁忌全公開
- 本週12生肖運勢！命理師點名「3生肖」好運擋不住 屬羊需保守

## 新增标题
- 【神預言】愛神給你的傳訊：屬於你的愛情桃花正在降臨！|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 2026大暑最強開運法！命理師曝3招開運、2風水法調氣場：財運最旺生肖、8大禁忌全公開
- 本週12生肖運勢！命理師點名「3生肖」好運擋不住 屬羊需保守

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年7月20日 23:14
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
