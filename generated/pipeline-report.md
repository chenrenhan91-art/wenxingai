# 问星AI 内容自动化运行报告 2026年5月5日 13:44

- 总体状态：failed_audit
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：f9f1da6b70e27df4ebe1ceba82566ef422bdcd1a
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=failed, 分发=blocked, 文章=skipped

## 本轮热点标题
- 流年運勢你算了嗎? #開運軍師尹森#風水尹森#流年 #算命 #紫微斗數#八字 #命盤#尹森老師#尹森#命理師#命理師推薦#風水師推薦#2026運勢 #https #家居風水宜忌
- 🔥習近平運勢終結?! 三個命理師同樣預言
- [新聞] 沈伯洋「地風升」！台北市長選戰火性強烈 命理師卜卦大膽預
- 今天立夏小心破財！命理師警告：這個動作恐讓財運流失，「2做4不做」開運關鍵一次看
- 立夏將至!12生肖運勢一次看 命理師：6類人氣場全面升溫

## 新增标题
- 今天立夏小心破財！命理師警告：這個動作恐讓財運流失，「2做4不做」開運關鍵一次看
- 立夏將至!12生肖運勢一次看 命理師：6類人氣場全面升溫

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 7/8）。

## 失败脚本
- audit_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月5日 13:44
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年5月5日 13:44 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | failed | content audit failed
