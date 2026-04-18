# 问星AI 内容自动化运行报告 2026年4月18日 22:02

- 总体状态：failed_audit
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：3713fbf78b2c06633721081a1de32e33af2f8881
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=failed, 分发=blocked, 文章=skipped

## 本轮热点标题
- 流年運勢你算了嗎? #開運軍師尹森#風水尹森#流年 #算命 #紫微斗數#八字 #命盤#尹森老師#尹森#命理師#命理師推薦#風水師推薦#2026運勢 #https #家居風水宜忌
- 揭開玄學秘密! 想了解: 數字能量學、電話號碼、流年運程、風水布局、改名方法、占卜、解卦、擇日要訣..... 多個課程等你選擇: 【數字能量學：電話號碼及算流年綜合課程】【流年算命＋流年風水布局班】【實用改名班】【擇日實戰班】【玄空大卦擇日班】【玄空風水班】【揀樓風水班
- [ 玄學 ☯ 歌訣 ] 五虎遁歌訣 甲己之年丙作首乙庚之歲戊為頭 丙辛歲首尋庚上丁壬壬水順水流 試問戊癸何方發甲寅之上好追求 #五虎遁元 #五虎遁月 #五虎遁 #天天背口訣 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流
- 玄天上帝生日7注意事項！命理師曝「開運、化解小人」祭拜秘訣
- 土地婆聖誕巧遇天赦日！ 命理師揭供品與祈願開運方式

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 5/8）。

## 失败脚本
- audit_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月18日 22:02
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月18日 22:02 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | failed | content audit failed
