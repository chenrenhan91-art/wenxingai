# 问星AI 内容自动化运行报告 2026年10月15日 11:14

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：be84d50012d6fd635e68dddb59520bb87a35e639
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 十年大運不好，就要倒楣十年？#紫微斗數#命理 #流年運勢#趨吉避凶#算命 #財運 #感情 #人生選擇#魁哥OpenMic
- 學八字之前 以為天干地支就22個字 應該沒有很難吧 學八字之後 天干要看合 地支要看沖 還有刑害破 藏干打開 裡面又住了三個十神 我只是想了解自己 怎麼感覺誤入 一個大型家族恩怨現場🤣 但八字有趣的地方 就是你越學 越能發現每個人 思考和面對事情的方式都不同
- [問卦] 中醫 是醫學還是玄學？
- 寒露節氣2026｜命理師點名4生肖運勢低迷小心破財 教3招居家開運
- 重陽節想招財！命理師教拿午時水「擦這地方」 11招開運方法曝

## 新增标题
- 學八字之前 以為天干地支就22個字 應該沒有很難吧 學八字之後 天干要看合 地支要看沖 還有刑害破 藏干打開 裡面又住了三個十神 我只是想了解自己 怎麼感覺誤入 一個大型家族恩怨現場🤣 但八字有趣的地方 就是你越學 越能發現每個人 思考和面對事情的方式都不同
- 重陽節想招財！命理師教拿午時水「擦這地方」 11招開運方法曝

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年10月15日 11:15
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
