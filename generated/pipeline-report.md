# 问星AI 内容自动化运行报告 2026年8月7日 21:30

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：388b1dbb9367627746bc017057dcea947771c64b
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 感情 #命理師#正能量#八字命理#十二属相#熱門 #流年運勢#家居風水宜忌#人生感悟#紫微斗數#易经#愛情 #婚姻 #補財庫旺財氣
- 驚天慘案：361位善良同胞被中共威逼投入1千多度沸騰的鋼水中！ 天佑台灣！神算命理師廖美然2026下半年預言：凶象重疊「最危險月份」來襲！ 鬼月遇上「子午大衝」，警告巨大地震與年輕人猝逝爆發期！ #琦玟街談巷說
- 中共把300多名法轮大法弟子，投入到北京首钢的炼钢炉内，化为青烟！中共及江泽民的邪恶，真的是宇宙级别的！——天佑台灣！神算命理師廖美然2026下半年預言：凶象重疊「最危險月份」來襲！鬼月遇上「子午大衝」，警告巨大地震與年輕人猝逝爆發期！#2026 #預..
- 太常算命恐「越算越薄」？命理師揭真相：真正毀運勢的是這事
- 今立秋運勢大翻盤！命理師點5生肖逆襲爆發、黑馬竄出| 星座命理| 生活

## 新增标题
- 感情 #命理師#正能量#八字命理#十二属相#熱門 #流年運勢#家居風水宜忌#人生感悟#紫微斗數#易经#愛情 #婚姻 #補財庫旺財氣
- 太常算命恐「越算越薄」？命理師揭真相：真正毀運勢的是這事

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年8月7日 21:30
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
