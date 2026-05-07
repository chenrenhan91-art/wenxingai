# 问星AI 内容自动化运行报告 2026年5月7日 00:14

- 总体状态：failed_distribution
- 本轮是否强制刷新：否
- 热点是否变化：是
- 变更签名：26a9c725b527931bd1fdd58e6ed7b45b82c8f0ca
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 流年運勢你算了嗎? #開運軍師尹森#風水尹森#流年 #算命 #紫微斗數#八字 #命盤#尹森老師#尹森#命理師#命理師推薦#風水師推薦#2026運勢 #https #家居風水宜忌
- 🔥習近平運勢終結?! 三個命理師同樣預言
- [新聞] 沈伯洋「地風升」！台北市長選戰火性強烈 命理師卜卦大膽預
- 立夏交節氣運勢洗牌…命理師示警2生肖恐破財 忌高風險操作
- 立夏後16天運勢起飛！命理師曝「6大生肖」氣場升溫率先翻盤登頂| 星座命理| 生活

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月7日 00:14
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年5月7日 00:14 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
