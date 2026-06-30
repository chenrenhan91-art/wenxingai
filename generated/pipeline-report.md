# 问星AI 内容自动化运行报告 2026年6月30日 14:56

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：addcadea1c19ec2830277fd322d44190f6f2a973
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 50分鐘讀透紫微經典《太微賦》：你的命盤格局藏著怎樣的先天大運？學會古人流傳至今的“命理天規”！#太微賦#紫微斗數#絕處逢生#凋而不落#深夜聽書#順時而動#司馬懿 #大運格局#命理天規
- 聽大眾戀愛占卜但心中對象想的是老闆 塔羅師「這組看起來是在較勁，你覺得對方該有所回饋了、但對方覺得你做的還不夠時間還沒到⋯⋯真奇怪感覺像在看上司跟下屬⋯⋯這組該不會有人不是來看戀愛而是看工作的吧」 太準了老闆該幫我加薪了吧
- [新聞] 黑熊變國師！沈伯洋「塔羅牌算台北未來命
- 南投百年廟驚見「倒插香」！居民心驚：影響運勢、風水 命理師這樣看
- 恭喜生肖蛇！2026年6月“雙星入命”格局開啟，這15天不行動，財神轉身走人！#南懷瑾 #國學 #易經#開運 #招財#風水 #2026運勢#屬相#生肖運勢#生肖命理Student Finance (4TcGggAjQQ)

## 新增标题
- 南投百年廟驚見「倒插香」！居民心驚：影響運勢、風水 命理師這樣看
- 恭喜生肖蛇！2026年6月“雙星入命”格局開啟，這15天不行動，財神轉身走人！#南懷瑾 #國學 #易經#開運 #招財#風水 #2026運勢#屬相#生肖運勢#生肖命理Student Finance (4TcGggAjQQ)

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 3/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年6月30日 14:56
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[warn] DashScope model qwen3.6-flash-2026-04-16 failed; trying qwen3.5-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-flash failed; trying qwen3.5-35b-a3b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-35b-a3b failed; trying qwen3.5-27b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-27b failed; trying qwen3.5-122b-a10b. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
[warn] DashScope model qwen3.5-122b-a10b failed; trying deepseek-v4-flash. Reason: HTTP 400: {"error":{"message":"Access denied, please make sure your account is in good standing. For details, see: https://help.aliyun.com/zh/model-studio/error-code#overdue-payment","typ...
Gemini content generation failed: network or API error: HTTP Error 400: Bad Request
