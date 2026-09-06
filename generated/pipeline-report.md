# 问星AI 内容自动化运行报告 2026年9月6日 21:13

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：8728e374a1ae4a941cf3de222f1c5ead86e28d3c
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 對方最近對你的想法、感情，面對關係的心態如何？以及他的行動力|曖昧|愛情|戀愛|桃花|塔羅占卜
- 🐯 虎嚕命理 𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.09.06（日）癸未日 🔮 🐯 今日虎嚕語錄： 「別人怎麼輕賤你都不要緊，重要的是你別跟著輕賤自己。」 💧 癸未日容易把情緒壓在心裡，表面說著沒關係，腦袋卻已經偷偷重播八十遍。 別人的評價聽聽就好，別拿回家供著。 ✨ 十神開運指南
- [問卦] 中醫 是醫學還是玄學？
- 流年步入犧牲！蔣萬安「吊人牌苦行」 命理師驚吐連任之戰結局
- 運勢走下坡有徵兆！命理師揭3大警訊 「這舉動」是破財開始

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月6日 21:13
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
