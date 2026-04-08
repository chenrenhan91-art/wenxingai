# 问星AI 内容自动化运行报告 2026年4月8日 13:12

- 总体状态：failed_distribution
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：5c59e9166ca7816f94872ac67c0dc3029482f762
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 你們之間，還有沒說完的話嗎？他什麼時候會說？會怎麼表達？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 掌相學 Chirology #掌相學 #Palmistry #PalmReading #Chirology #Palmist #Chirologists #LifeLine #HeadLine #HeartLine #FateLine #SunLine #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名
- [ 玄學 ☯ 歌訣 ] 桃花歌訣 寅午戌桃花兔裡出 巳酉丑騎馬浪漫走 亥卯未 子鼠當頭忌 申子辰雞叫亂淫倫 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名 #占卜問事 #揀電話號碼揀冧巴 #FOH #
- 清明運勢來了！命理師曝「財運最旺星座」 獅子有望加薪
- 討論牆 | 命理師潘智航:清明節氣可開運

## 新增标题
- 你們之間，還有沒說完的話嗎？他什麼時候會說？會怎麼表達？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 討論牆 | 命理師潘智航:清明節氣可開運

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月8日 13:12
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月8日 13:12 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
