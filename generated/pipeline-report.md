# 问星AI 内容自动化运行报告 2026年4月7日 13:10

- 总体状态：failed_distribution
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：3f29e4c2213f0ac4cfb6f3e667ed5130b8744f03
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 你在他腦海裡的頻率，想到你的心情感受，他對你們關係的期待|曖昧|愛情|戀愛|桃花|塔羅占卜|
- [ 易經６４卦算流年 初班0317 ] #火風鼎 木上有火鼎君子以正位凝命 #易卦大成卦六十四卦 #巽卦命 #2026丙午馬年 #算流年唔駛用八字 #算流年唔駛用紫斗 #自己運程自己推算 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流
- [ 風水布局實戰班0312 ] 乾坤國寶 庫池水 #庫池水 #乾坤國寶 #正三元水法 #三天水法 #先後天水法 #龍門八局 #正局水法 #揀樓為主布局為輔 #宅命相配 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇
- 清明「能量爆發」轉運時機來了！命理師曝12生肖「開運儀式」方法一次看
- 清明運勢來了！命理師曝「財運最旺星座」 獅子有望加薪

## 新增标题
- 你在他腦海裡的頻率，想到你的心情感受，他對你們關係的期待|曖昧|愛情|戀愛|桃花|塔羅占卜|

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月7日 13:10
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月7日 13:10 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
