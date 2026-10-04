# 问星AI 内容自动化运行报告 2026年10月4日 12:15

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：d6ecbd5e6ddd2f9cea6a40061db00db5d3d78be5
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他對你動心or走腎？心動程度有多少？更在意什麼？怎麼看待關係的？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 「西邊的太陽快要」的第二集 已經開始⋯⋯ 我作為命理師 只負責提前預測 不幹落井下石的事 何況我跟金文聲老先生的⋯⋯ 綜上 我聊郭德綱那期油管節目 已經私藏下架 等今年熱點過去了 再提供以學習為目的的觀看 還是那句話 郭德綱早期的一些活 後來寫的一些書 都很
- [問卦] 中醫 是醫學還是玄學？
- 獨家／中秋後3生肖運勢轉衰 命理師曝「開運破解法」：穩住身心最重要
- 蘇巧慧、李四川新北大激戰！命理師解鎖「面相+流年」秒點名這人

## 新增标题
- 他對你動心or走腎？心動程度有多少？更在意什麼？怎麼看待關係的？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 蘇巧慧、李四川新北大激戰！命理師解鎖「面相+流年」秒點名這人

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月4日 12:15
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
