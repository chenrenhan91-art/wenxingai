# 问星AI 内容自动化运行报告 2026年11月18日 21:09

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：e2273101d75ff070935d60cc1599df07d59f4631
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 小雪節氣「3生肖」運勢拉警報！命理師示警「這生肖」最要小心！ #shorts #手面相#風水 #紫微#星座 #命理 #開運
- 怎樣學好算命？是這樣的，我講個故事給你聽。 以前，有位飛星派的命理師，跟老師學了好多年，也就記下了一些口訣，根本不太會算。 但有一次，自己欠了巨額的債，完全還不上，債主到處找他，他每天東躲西藏，活得提心吊膽。那時，他想起自己學過算命，就每天躲在什
- [新聞] 神機妙算！沈伯洋塔羅牌抽「死神牌」有反
- 黃仁勳桃花劫 命理師解析面相「晚年運勢」大分歧
- 獨家／週末小雪下元節接力來！3生肖年底運勢拉警報 命理師1招求平安

## 新增标题
- 小雪節氣「3生肖」運勢拉警報！命理師示警「這生肖」最要小心！ #shorts #手面相#風水 #紫微#星座 #命理 #開運
- 獨家／週末小雪下元節接力來！3生肖年底運勢拉警報 命理師1招求平安

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月18日 21:10
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
