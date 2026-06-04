# 问星AI 内容自动化运行报告 2026年6月4日 15:24

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：a5b7df40a4d406b2641d418d26afa89723aa84be
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- ta對你的真實需求？ta到底想要讓你怎樣？深挖ta對你的想法！|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 早安安呀~🌸 生活中的煩惱戀愛中的困境 工作中的不如意❤️‍🔥 有時是需要一點點的魔法 放下自己的腳步來審視 交給嫟命老師來解惑吧(*´∀`)~♥ 昨天跟大家一起玩的了塔羅 真的好有趣哦☺️💕 下次再來幫你們占卜✨
- [新聞] 鬼門開遇日全蝕超凶？命理師引述古籍：
- 2026芒種節氣到！命理師揭「兩大開運秘訣」 2生肖女性大掃除有助旺財
- 早預言馬英九犯小人!命理師驚揭「流年走死神」： 恐有大變化

## 新增标题
- 2026芒種節氣到！命理師揭「兩大開運秘訣」 2生肖女性大掃除有助旺財
- 早預言馬英九犯小人!命理師驚揭「流年走死神」： 恐有大變化

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月4日 15:24
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
