# 问星AI 内容自动化运行报告 2026年9月16日 21:15

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：1134d06725b8c23b5f99c8d3831eefc25205cec5
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 他怎麼評價你？他對你的感覺？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 今天的塔羅占卜改明後天開台喔 忙碌兩天做餅全身痠痛 有點累等身體好點再占占唷🙏
- 🐯 虎嚕命理 𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.09.09（三）丙戌日 🔮 🐯 今日虎嚕語錄： 「別把同事當底牌，也別把主管當靠山。」 🔥 丙戌日容易把職場情義看得太重。 同事可以合作 主管可以尊重 但真正的底牌，還是自己手上的能力與選擇權。 ✨ 十神開運指南｜請對照日主 🌳甲木｜
- 秋季運勢亮紅燈！命理師曝3生肖當心「健康出大事」
- 中秋賞月恐影響運勢？命理師點名「4大生肖」遇極陰日 宜躲月防煞 | 生活 | CTWANT

## 新增标题
- 🐯 虎嚕命理 𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.09.09（三）丙戌日 🔮 🐯 今日虎嚕語錄： 「別把同事當底牌，也別把主管當靠山。」 🔥 丙戌日容易把職場情義看得太重。 同事可以合作 主管可以尊重 但真正的底牌，還是自己手上的能力與選擇權。 ✨ 十神開運指南｜請對照日主 🌳甲木｜
- 中秋賞月恐影響運勢？命理師點名「4大生肖」遇極陰日 宜躲月防煞 | 生活 | CTWANT

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch PTT Gossiping: HTTP Error 500: Internal Server Error
[warn] failed to fetch PTT WomenTalk: HTTP Error 500: Internal Server Error
[warn] failed to fetch PTT marvel: HTTP Error 500: Internal Server Error
[warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月16日 21:15
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
