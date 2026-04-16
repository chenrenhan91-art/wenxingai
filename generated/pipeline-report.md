# 问星AI 内容自动化运行报告 2026年4月16日 13:31

- 总体状态：failed_distribution
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：eb8d2923dcb83fcf57a6d28ddebfe66ce90cbbb7
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 他內心有多在意你？你會牽動他的情緒嗎？想起你他的感覺如何？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 揭開玄學秘密! 想了解: 數字能量學、電話號碼、流年運程、風水布局、改名方法、占卜、解卦、擇日要訣..... 多個課程等你選擇: 【數字能量學：電話號碼及算流年綜合課程】【流年算命＋流年風水布局班】【實用改名班】【擇日實戰班】【玄空大卦擇日班】【玄空風水班】【揀樓風水班
- 【 挑戰 "生鐵鑊" 系列 】 本人成功用生鐵鑊薑蔥煎金蠔 唔黐底 #生鐵鑊唔黐底 #薑蔥煎金蠔 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名 #占卜問事 #揀電話號碼揀冧巴 #FOH #FutureOnH
- 穀雨一到運勢大洗牌「7大禁忌曝光」 命理師警告：做錯恐衰整季
- 今上帝公聖誕！開運攻略一次看 命理師曝4招打小人：1狀況恐反噬

## 新增标题
- 他內心有多在意你？你會牽動他的情緒嗎？想起你他的感覺如何？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 揭開玄學秘密! 想了解: 數字能量學、電話號碼、流年運程、風水布局、改名方法、占卜、解卦、擇日要訣..... 多個課程等你選擇: 【數字能量學：電話號碼及算流年綜合課程】【流年算命＋流年風水布局班】【實用改名班】【擇日實戰班】【玄空大卦擇日班】【玄空風水班】【揀樓風水班
- 【 挑戰 "生鐵鑊" 系列 】 本人成功用生鐵鑊薑蔥煎金蠔 唔黐底 #生鐵鑊唔黐底 #薑蔥煎金蠔 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名 #占卜問事 #揀電話號碼揀冧巴 #FOH #FutureOnH
- 穀雨一到運勢大洗牌「7大禁忌曝光」 命理師警告：做錯恐衰整季
- 今上帝公聖誕！開運攻略一次看 命理師曝4招打小人：1狀況恐反噬

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月16日 13:32
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月16日 13:32 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
