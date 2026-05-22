# 问星AI 内容自动化运行报告 2026年5月22日 14:08

- 总体状态：failed_generate
- 本轮是否强制刷新：否
- 热点是否变化：是
- 变更签名：45d089af4f1526bf7fe5d304fea5847fc0771713
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 脫單時間預告！下一任會是誰？ta的特徵、出現時間、是誰主動的？|曖昧|愛情|戀愛|桃花|塔羅占卜|
- [ 數字能量學0511 ] 電話號碼催財運 #催財 #揀電話號碼 #自己號碼自己揀 #電話號碼 #搵個靚冧巴 #催旺化煞 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年批命 #擇吉日擇時辰 #改名 #占卜問事 #揀電話號碼揀冧巴
- [問卦] 戶田惠梨香:命理師說我38歲會死掉
- 6月份12生肖運勢曝光 命理師建議「穩中求進」才是關鍵
- 小滿4大禁忌曝光！命理師警告「別加班熬夜」 4生肖運勢兩樣情

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月22日 14:08
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[ok] DashScope fallback model selected: qwen3.6-flash-2026-04-16
Gemini content generation failed: invalid Gemini response: missing zh_cn.social_posts
