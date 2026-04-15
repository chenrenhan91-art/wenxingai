# 问星AI 内容自动化运行报告 2026年4月15日 13:25

- 总体状态：failed_distribution
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：a70df8304f7f952260368eaf484e28763b7f2dd5
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 他最想對你做的事：聽聽她內心深處不敢說出口的那個秘密幻想|曖昧|愛情|戀愛|桃花|塔羅占卜|
- [ 玄學 ☯ 歌訣 ] 五虎遁歌訣 甲己之年丙作首乙庚之歲戊為頭 丙辛歲首尋庚上丁壬壬水順水流 試問戊癸何方發甲寅之上好追求 #五虎遁元 #五虎遁月 #五虎遁 #天天背口訣 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流
- [ 玄學 ☯ 歌訣 ] 文昌歌訣 甲乙巳午文昌位丙戊申宮丁己雞 庚豬辛鼠壬逢虎癸人見卯上雲梯 #天天背口訣 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名 #占卜問事 #揀電話號碼揀冧巴 #FOH
- 媽祖生日運勢大爆發！命理師點名3生肖財運暴衝
- 4／20迎穀雨！命理師揭7大禁忌超簡易開運法公開| 生活

## 新增标题
- 他最想對你做的事：聽聽她內心深處不敢說出口的那個秘密幻想|曖昧|愛情|戀愛|桃花|塔羅占卜|

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 4/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月15日 13:25
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月15日 13:25 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
