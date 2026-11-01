# 问星AI 内容自动化运行报告 2026年11月1日 11:10

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：e0114aa15ccf16479643fd57502b30eceeb0f4d4
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 時光機：明年今日你是他的誰？愛不愛你？你和他各對感情的感受看法？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 今天萬聖節 來分享幾個 八字十神的恐怖故事 比肩： 朋友說一起創業 結果兩個人都想當老闆 劫財： 月底打開銀行帳戶 發現錢不知道去哪了 食神： 半夜說只吃一口 結果整包零食不見了 傷官： 主管說了一句話 腦袋已經準備好八百字反駁 正財： 記帳記得很認真 但看到購
- [問卦] 中醫 是醫學還是玄學？
- 寒露要來了！命理師示警2生肖和「這類人」恐出事 開運招曝光
- 百歲流年看台北戰局！命理師點名「他」迎掌權：後勢看好

## 新增标题
- 今天萬聖節 來分享幾個 八字十神的恐怖故事 比肩： 朋友說一起創業 結果兩個人都想當老闆 劫財： 月底打開銀行帳戶 發現錢不知道去哪了 食神： 半夜說只吃一口 結果整包零食不見了 傷官： 主管說了一句話 腦袋已經準備好八百字反駁 正財： 記帳記得很認真 但看到購

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月1日 11:10
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
