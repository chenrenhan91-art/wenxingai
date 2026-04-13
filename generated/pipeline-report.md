# 问星AI 内容自动化运行报告 2026年4月13日 13:43

- 总体状态：failed_distribution
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：fbc0ff6424df9e8a2fe40f4cd58d4712b71e12a0
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=ok, 审校=ok, 质检=ok, 分发=failed, 文章=skipped

## 本轮热点标题
- 這兩天他想你了嗎？此刻對你的感覺，你給他的印象，想跟你做什麼？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 【 挑戰 "生鐵鑊" 系列 】 本人成功用生鐵鑊薑蔥煎金蠔 唔黐底 #生鐵鑊唔黐底 #薑蔥煎金蠔 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名 #占卜問事 #揀電話號碼揀冧巴 #FOH #FutureOnH
- [ 玄學 ☯ 歌訣 ] 五虎遁歌訣 甲己之年丙作首乙庚之歲戊為頭 丙辛歲首尋庚上丁壬壬水順水流 試問戊癸何方發甲寅之上好追求 #五虎遁元 #五虎遁月 #五虎遁 #天天背口訣 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流
- 你如果要給命理師幫你算命，他會不會問你一年出生的年月日？😜
- 赤馬紅羊年要注意什麼？九運離火加劇火災頻發社會易動盪命理師警告4個生肖最危險！【附化解教學】

## 新增标题
- 這兩天他想你了嗎？此刻對你的感覺，你給他的印象，想跟你做什麼？|曖昧|愛情|戀愛|桃花|塔羅占卜
- 赤馬紅羊年要注意什麼？九運離火加劇火災頻發社會易動盪命理師警告4個生肖最危險！【附化解教學】

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 3/8）。

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月13日 13:43
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月13日 13:43 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | prepared 6 distribution jobs; queued 4 jobs to Buffer; 2 jobs failed
distribution completed with 2 publishing failures
