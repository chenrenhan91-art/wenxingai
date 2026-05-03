# 问星AI 内容自动化运行报告 2026年5月3日 14:06

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：014112617d0dd25e0046b333dd07138314f15975
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 流年運勢你算了嗎? #開運軍師尹森#風水尹森#流年 #算命 #紫微斗數#八字 #命盤#尹森老師#尹森#命理師#命理師推薦#風水師推薦#2026運勢 #https #家居風水宜忌
- 【 挑戰 "生鐵鑊" 系列 】 碧玉內子命令本人蒜蓉炒呢堆嘢 本人成功用生鐵鑊炒靚呢堆嘢唔燶唔黐底 完美避免犯太座 #生鐵鑊炒嘢唔燶唔黐底 #犯太座 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰
- [新聞] 沈伯洋「地風升」！台北市長選戰火性強烈 命理師卜卦大膽預
- 赤馬年火氣旺! 命理師邱彥龍： 今年大年初一不一樣太急恐亂整年運勢
- 5/1明天記得拜財神！ 命理師曝「3招最強求財步驟」， 正財偏財開運旺整年

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月3日 14:06
- generate_daily_content.py | failed | Gemini content generation failed: network or API error: HTTP Error 503: Service Unavailable
