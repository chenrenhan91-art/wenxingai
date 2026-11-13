# 问星AI 内容自动化运行报告 2026年11月13日 21:09

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：107c7d5b4604cdf0d38c97a4eefd78913b52ef5e
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 江𤒹生Anson Kong 八字命盤分析︱2027大運流年相沖，小心出事？ 2031年起事業上高峰！︱陳俊燊師傅【陳俊燊風水命理EP240】
- 晚上洗澡時，突然想起來前幾天在threads上看到有人說，如果沈伯洋要當選的話，一定要女性的幫助。 剛剛花了一點時間找到這一篇，結果發文的人晚上也再po文了。 雖然我看不懂紫微命盤，但是應該可以和小英這篇文做連結吧？ 空安應該沒想過小英實實文章的力量
- [新聞] 神機妙算！沈伯洋塔羅牌抽「死神牌」有反
- 2027年恐陷血光危機！命理師曝3大開運色保平安
- 桃園市長選戰！命理師綜合運勢、姓名、生肖分析：小心行險招- 生活

## 新增标题
- 江𤒹生Anson Kong 八字命盤分析︱2027大運流年相沖，小心出事？ 2031年起事業上高峰！︱陳俊燊師傅【陳俊燊風水命理EP240】
- 2027年恐陷血光危機！命理師曝3大開運色保平安

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月13日 21:10
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
