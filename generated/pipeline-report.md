# 问星AI 内容自动化运行报告 2026年8月30日 11:14

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：d44385d1843496518bee66b87979321e76099ddf
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- [問卦] 中醫 是醫學還是玄學？
- [新聞] 台灣命理師脫口「北京沒冰箱」陸國台辦
- [新聞] 台派命理師扯「北京沒冰箱」 遭陸網群嘲
- [閒聊] 雙魚/巨蟹是最傻的星座嗎？
- [問卦] 俗話說科學的盡頭是玄學，那文科呢？

## 新增标题
- [問卦] 中醫 是醫學還是玄學？
- [新聞] 台灣命理師脫口「北京沒冰箱」陸國台辦
- [新聞] 台派命理師扯「北京沒冰箱」 遭陸網群嘲
- [閒聊] 雙魚/巨蟹是最傻的星座嗎？
- [問卦] 俗話說科學的盡頭是玄學，那文科呢？

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
updated 8 hot news items at 2026年8月30日 11:17
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
