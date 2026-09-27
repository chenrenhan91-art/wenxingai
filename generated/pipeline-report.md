# 问星AI 内容自动化运行报告 2026年9月27日 21:13

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：67be073f38124f64264fe5087540758579af68dd
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- ゼロから学ぶ紫微斗数｜命盤の基礎から、仕事・財運・人間関係・流年まで読み解く実践講座
- #歲次乙未2015年回顧詩展_羊仙詩卷_站著寫詩_AIG+26卷 最新創作對手出現在眼前高108公分這張木桌勁敵 時間不限而空間只會不斷無限延伸展示人存在當下可能性 此刻108顆紫微斗數星盤想區域跨界到哪邊呢 詩者寫上作品題名後開始走來晃去七步百步腳印佈滿
- [問卦] 中醫 是醫學還是玄學？
- 中秋節後運勢翻轉！命理師點名「4生肖」擺脫包袱、迎接新轉機| 星座
- 中秋節後運勢翻轉！命理師點名「4生肖」迎好運 屬馬行動力大增

## 新增标题
- ゼロから学ぶ紫微斗数｜命盤の基礎から、仕事・財運・人間関係・流年まで読み解く実践講座
- 中秋節後運勢翻轉！命理師點名「4生肖」擺脫包袱、迎接新轉機| 星座
- 中秋節後運勢翻轉！命理師點名「4生肖」迎好運 屬馬行動力大增

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年9月27日 21:14
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
