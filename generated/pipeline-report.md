# 问星AI 内容自动化运行报告 2026年4月11日 12:56

- 总体状态：failed_distribution
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：93b58792d782b26ed54287520c14f431035df803
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 這兩天他想你了嗎？此刻對你的感覺，你給他的印象，想跟你做什麼？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 有喜歡紫微斗數的捧油嗎！ 有一位親戚跟命理相性&紫微造詣很高，但不喜歡細說，只在重要事件發生前會提一下，補給部隊也有排命盤問過他，他也只說他們（小孩）命都比你好，你先顧好晚年健康吧。 雖然我不是迷信的人，但看看這些參考一下還是蠻有意思的對吧！
- ［路娜塔羅占卜］三選一：測驗你的戀愛腦指數喔
- 清明運勢來了！命理師曝「財運最旺星座」 獅子有望加薪
- 討論牆 | 命理師潘智航:清明節氣可開運

## 新增标题
- 這兩天他想你了嗎？此刻對你的感覺，你給他的印象，想跟你做什麼？|曖昧|愛情|戀愛|桃花|塔羅占卜
- ［路娜塔羅占卜］三選一：測驗你的戀愛腦指數喔

## 次日运营建议
- 明日优先延展「塔罗星象」相关选题（当前占比 3/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月11日 12:56
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月11日 12:56 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
