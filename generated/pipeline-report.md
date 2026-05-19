# 问星AI 内容自动化运行报告 2026年5月19日 14:49

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：33ada35a5e5c523bbf539b6475d792a2f8477048
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 看完麥可傑克森電影！王者的紫微斗數命盤，注定的「煞星」已訴說一切
- 做著週表邊聽塔羅占卜 : 你已經很棒了，先把自己當植物養。要照照陽光、多喝水 我: 對...變成自由居家工作的木頭，需要見一下陽光🤣
- [問卦] 戶田惠梨香:命理師說我38歲會死掉
- 孫安佐流年走入「死神」！命理師早預言「牢獄之災」皇帝命盤脾氣火爆
- 孫安佐持槍遭羈押！命理師2年前早預言：死神流年

## 新增标题
- 看完麥可傑克森電影！王者的紫微斗數命盤，注定的「煞星」已訴說一切
- [問卦] 戶田惠梨香:命理師說我38歲會死掉
- 孫安佐流年走入「死神」！命理師早預言「牢獄之災」皇帝命盤脾氣火爆

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月19日 14:49
- generate_daily_content.py | failed | Gemini content generation failed: network or API error: HTTP Error 403: Forbidden
