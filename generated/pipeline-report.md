# 问星AI 内容自动化运行报告 2026年6月16日 16:46

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：109cfa62a39a62e5c9c9bbf39fefe03d8de5c9a4
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 吉字占卜本月運勢！老天眷顧給錢花的人！｜#命運好好玩#shorts #手面相#風水 #紫微#星座 #命理 #開運
- 你好，我是山月知。 很多人聽說我從小對磁場和能量流動特別敏感，後來又死磕了十幾年玄學，經常會問我同一個問題：「既然你中西命理都精通，那出來幫人看盤，你到底更推崇占星還是八字？」 我的回答一向很直接：我都看，而且必須一起看。 #astrologer
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 【千萬別午睡！命理師曝「端午節最忌3行為」：恐影響下半年運勢】 （示意圖／ETtoday資料照）
- 2026端午節3大開運法！命理師：今年火能量極旺 午時水正確用法曝

## 新增标题
- 【千萬別午睡！命理師曝「端午節最忌3行為」：恐影響下半年運勢】 （示意圖／ETtoday資料照）
- 2026端午節3大開運法！命理師：今年火能量極旺 午時水正確用法曝

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月16日 16:46
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
