# 问星AI 内容自动化运行报告 2026年8月26日 21:24

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：3e92b57a67c66bea8b0bab279756fc5314d66225
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【#2503】【塔罗·字卡·占卜】他/她對你有多心動呢？ | 浮世塔羅牌| 小確幸勵志卡| 天使祈禱神諭卡(無時間限制)
- 🐯 虎嚕命理𝐃𝐚𝐲 𝐆𝐮𝐢𝐝𝐞 🗓️ 2026.08.26（三）壬申日🔮 🔔 先穩住自己，才能穩穩接住好運。 壬水遇申金，思緒靈活、行動力提升✨ 今天適合掌握資訊與機會，但別因心急而起衝突。 ✨ 十神開運指南｜請對照日主 🌳甲木｜偏印：遠離暗中是非 🌿乙木｜正印：貴人及時相助
- [新聞]台灣命理師說「北京沒冰箱」中國網友群嘲
- 【鬼月最重要一天來了！命理師示警「4種人」當心 最簡單開運法曝光】 就在這個星期四～（#豬頭皮）
- 鬼月最重要一天來了！命理師示警「4種人」當心 最簡單開運法曝光

## 新增标题
- 【#2503】【塔罗·字卡·占卜】他/她對你有多心動呢？ | 浮世塔羅牌| 小確幸勵志卡| 天使祈禱神諭卡(無時間限制)

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 7/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年8月26日 21:24
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
