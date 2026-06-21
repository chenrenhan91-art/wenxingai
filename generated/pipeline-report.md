# 问星AI 内容自动化运行报告 2026年6月21日 16:00

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：fbda404f123280e7f13e8a8a881548b9028843a5
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- shorts 開運物品都是假!? 要改命還不如投胎?!｜命理.算命.解密.何嘉文.張可昀.小賴.TIFFANY @我愛小明星大跟班
- 生日不要只許願。 因為很多願望， 如果你沒有看懂自己為什麼卡住， 明年還是會再許一次。 八字流年不是生日那天切換， 但生日是你命盤被啟動的日子。 很適合拿來問自己： 我這一年重複了什麼課題？ 我到底適合往哪裡走？ 我是不是又用同一種方式消耗自己？ 生日
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 【超罕見！端午節遇「三火疊加」 命理師曝3招開運】 「雙火」流年～～～～（#豬頭皮）
- 夏至「陽極換局」引運勢轉變！命理師揭下半年5大贏家生肖| 娛樂星聞

## 新增标题
- shorts 開運物品都是假!? 要改命還不如投胎?!｜命理.算命.解密.何嘉文.張可昀.小賴.TIFFANY @我愛小明星大跟班
- 生日不要只許願。 因為很多願望， 如果你沒有看懂自己為什麼卡住， 明年還是會再許一次。 八字流年不是生日那天切換， 但生日是你命盤被啟動的日子。 很適合拿來問自己： 我這一年重複了什麼課題？ 我到底適合往哪裡走？ 我是不是又用同一種方式消耗自己？ 生日
- 【超罕見！端午節遇「三火疊加」 命理師曝3招開運】 「雙火」流年～～～～（#豬頭皮）
- 夏至「陽極換局」引運勢轉變！命理師揭下半年5大贏家生肖| 娛樂星聞

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月21日 16:01
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
