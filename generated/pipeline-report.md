# 问星AI 内容自动化运行报告 2026年6月20日 23:04

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：61c7d3361c5bd2ec9411b87e6aeabec773805f9a
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- [新聞] 「九紫離火運」全面啟動 命理師：AI產業
- [問卦] 目前人生都照紫微斗數命盤走 要信嗎？
- [新聞] 命理師驚揭黃仁勳擁 「帝王面相」！
- [問卦] 東方紫微聖人是三小？

## 新增标题
- [新聞] 「九紫離火運」全面啟動 命理師：AI產業
- [問卦] 目前人生都照紫微斗數命盤走 要信嗎？
- [新聞] 命理師驚揭黃仁勳擁 「帝王面相」！
- [問卦] 東方紫微聖人是三小？

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。
- 媒体新闻信号偏少，建议补充权威媒体来源以稳定可信度。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Google News zh-TW · 命理: HTTP Error 503: Service Unavailable
[warn] failed to fetch Google News zh-TW · 玄學: HTTP Error 503: Service Unavailable
[warn] failed to fetch Google News zh-TW · 塔羅: HTTP Error 503: Service Unavailable
[warn] failed to fetch Google News zh-TW · 風水: HTTP Error 503: Service Unavailable
[warn] failed to fetch YouTube Search: HTTP Error 503: Service Unavailable
[warn] failed to fetch X Recent Search: HTTP Error 503: Service Unavailable
[warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月20日 23:07
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
