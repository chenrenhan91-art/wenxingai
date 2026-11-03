# 问星AI 内容自动化运行报告 2026年11月3日 11:09

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：34c5a74b1bf4966d1ad1cdfcdc24ea4b63f7352f
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 【紫微斗数】天相星落在哪裏更容易遇到貴人？從紫微命盤看你的人脈與資源變現機會！#紫微斗数#天相星#贵人运#命盘解析#十二宫#事业运势#命理科普#紫微教学#印星#流年运势
- GitHub 熱榜上居然有人在排紫微斗數 專案叫 ziwei-doushu 照倪海廈《天紀》那套體系寫的 排盤、四化、格局判斷、古籍原文，全部開源 這幾天一天漲一千多顆星，現在破 1.2 萬 作者說前 1 萬顆星花了 180 天 最後 1000 顆只用了 16 個小時 而且作者是一個人用 AI 把整
- [問卦] 中醫 是醫學還是玄學？
- 立冬開運！12生肖掌握「旺點」 命理師急喊：這事沒做別亂衝
- 2026下午立冬暖烘烘！命理師授「立冬開運4招」必吃1水果

## 新增标题
- GitHub 熱榜上居然有人在排紫微斗數 專案叫 ziwei-doushu 照倪海廈《天紀》那套體系寫的 排盤、四化、格局判斷、古籍原文，全部開源 這幾天一天漲一千多顆星，現在破 1.2 萬 作者說前 1 萬顆星花了 180 天 最後 1000 顆只用了 16 個小時 而且作者是一個人用 AI 把整
- 立冬開運！12生肖掌握「旺點」 命理師急喊：這事沒做別亂衝
- 2026下午立冬暖烘烘！命理師授「立冬開運4招」必吃1水果

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年11月3日 11:09
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 404: Not Found
