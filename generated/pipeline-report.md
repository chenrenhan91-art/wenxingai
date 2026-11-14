# 问星AI 内容自动化运行报告 2026年11月14日 11:08

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：965bbe8880744c9bb452f13a5ca48cacd55f6307
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 江𤒹生Anson Kong 八字命盤分析︱2027大運流年相沖，小心出事？ 2031年起事業上高峰！︱陳俊燊師傅【陳俊燊風水命理EP240】
- @Baoliaogeming64 2027 丁未年「破財消災」（65 歲丁未年）紫微流年「巨門化忌」衝動戊午身宮，八字又是「丁未歲運并臨」。這代表 2027 年他將面臨輝達股價暴跌後引發的股東集體民事訴訟、SEC（美國證交會）資訊揭露調查，以及個人婚姻與家族信託的巨額財產重整，
- [新聞] 神機妙算！沈伯洋塔羅牌抽「死神牌」有反
- 2027年恐陷血光危機！命理師曝3大開運色保平安
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光

## 新增标题
- @Baoliaogeming64 2027 丁未年「破財消災」（65 歲丁未年）紫微流年「巨門化忌」衝動戊午身宮，八字又是「丁未歲運并臨」。這代表 2027 年他將面臨輝達股價暴跌後引發的股東集體民事訴訟、SEC（美國證交會）資訊揭露調查，以及個人婚姻與家族信託的巨額財產重整，
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月14日 11:09
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
