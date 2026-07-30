# 问星AI 内容自动化运行报告 2026年7月30日 21:38

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：73ab2c4d91a3c004932a35b863a57310ce86ddce
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 屬虎、馬、狗的朋友接喜！「寅午戌三合」8月火力全開，三大生肖聯手旺財，貴人財氣滾滾來！#屬虎運勢#屬馬運勢#屬狗運勢#寅午戌三合#生肖命理#八字開運#農曆八月#貴人運#財庫
- 官祿宮反映你的事業運勢、工作天賦、升遷機會與職場人際關係。 ✦ 吉星入宮：事業順遂，容易獲得賞識和升遷 ✦ 主星影響：紫微入宮→適合管理職；天機入宮→適合策劃分析 ✦ 化祿入宮：財運與事業雙豐收的好兆頭 #紫微斗數 #官祿宮 #命盤解析 #事業運勢 #命運屋 #Fa
- [問卦] 八字到底準不準？
- 大暑到！命理師曝4招開運法 5生肖運勢大翻轉
- 8／1觀音成道日！命理師揭「最強開運法」 做「5件事」增福報

## 新增标题
- 屬虎、馬、狗的朋友接喜！「寅午戌三合」8月火力全開，三大生肖聯手旺財，貴人財氣滾滾來！#屬虎運勢#屬馬運勢#屬狗運勢#寅午戌三合#生肖命理#八字開運#農曆八月#貴人運#財庫
- 官祿宮反映你的事業運勢、工作天賦、升遷機會與職場人際關係。 ✦ 吉星入宮：事業順遂，容易獲得賞識和升遷 ✦ 主星影響：紫微入宮→適合管理職；天機入宮→適合策劃分析 ✦ 化祿入宮：財運與事業雙豐收的好兆頭 #紫微斗數 #官祿宮 #命盤解析 #事業運勢 #命運屋 #Fa

## 次日运营建议
- 明日优先延展「八字紫微」相关选题（当前占比 3/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年7月30日 21:38
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
