# 问星AI 内容自动化运行报告 2026年7月30日 12:02

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：8a7d061cd5358d733b946135ccec50b5203b2d59
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 《紅線另一端牽著誰》⏳共時，是此刻與訊息相遇。⏳任何日期可抽牌❤️適用任何時間季節🔮塔羅占卜❤️愛情占卜🔮愛情解析🔮戀愛心事🔮塔羅學習
- 虎嚕消失三天。 不是閉關。 不是改運。 也不是被天庭抓去開會。 是真的忙到連每日運勢都沒有發。 這幾天每天睜開眼睛都想： 「晚一點來發文。」 然後下一次想起來， 已經是準備睡覺的時間。 所以今天先正式復活。 沒有補發三天運勢。 過去的就讓它過去。 畢竟連命理師
- [問卦] 八字到底準不準？
- 大暑到！命理師曝4招開運法 5生肖運勢大翻轉
- 8／1觀音成道日！命理師揭「最強開運法」 做「5件事」增福報

## 新增标题
- 《紅線另一端牽著誰》⏳共時，是此刻與訊息相遇。⏳任何日期可抽牌❤️適用任何時間季節🔮塔羅占卜❤️愛情占卜🔮愛情解析🔮戀愛心事🔮塔羅學習
- [問卦] 八字到底準不準？
- 8／1觀音成道日！命理師揭「最強開運法」 做「5件事」增福報

## 次日运营建议
- 明日优先延展「塔罗星象」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年7月30日 12:03
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
