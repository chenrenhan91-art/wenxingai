# 问星AI 内容自动化运行报告 2026年9月1日 11:16

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：2f63f859d45b95230d1b3eb5d9d554c63ea32b9a
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他最近想你了嗎？想對你做什麼？希望你怎麼對待他？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 研究孫宇晨的八字，找了一批跟牠同樣價值觀的八字做對比，一個比孫宇晨「割學」，稍差一點的八字。 2028轉大運「傷官見官，為禍百端」，驚蟄就有事立秋最凶。再練練手，用鐵算心易和連山大定核實了一下，這一關闖不過去，極端情況下就跟郭文貴一樣了。具體是誰，應
- [問卦] 中醫 是醫學還是玄學？
- 2026年9月星座運勢出爐！命理師點名這3星座旺到翻，水瓶千萬別亂吃瓜！
- 鬼月最重要一天！4類人當心 命理師曝3大開運法

## 新增标题
- 研究孫宇晨的八字，找了一批跟牠同樣價值觀的八字做對比，一個比孫宇晨「割學」，稍差一點的八字。 2028轉大運「傷官見官，為禍百端」，驚蟄就有事立秋最凶。再練練手，用鐵算心易和連山大定核實了一下，這一關闖不過去，極端情況下就跟郭文貴一樣了。具體是誰，應

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月1日 11:17
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
