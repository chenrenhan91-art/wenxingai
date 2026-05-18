# 问星AI 内容自动化运行报告 2026年5月18日 14:57

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：ef51f7a578b7b7ae16e4da8a65414d2e6e3d4515
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 26下半年你的桃花運VS財運？會遇到正緣嗎？會暴富嗎？指引解析⭐有雷勿入|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 今日塔羅占卜暫停一次 還再點心帕魯 以時間估計應該是還忙不完 會把占卜延後週一或週二喔🙏
- [新聞] 沈伯洋「地風升」！台北市長選戰火性強烈 命理師卜卦大膽預
- 孫安佐持槍遭羈押！命理師2年前早預言：死神流年
- 孫安佐遭羈押禁見！命理師2年前預言「今年走死神流年」：難逃牢獄之災

## 新增标题
- 26下半年你的桃花運VS財運？會遇到正緣嗎？會暴富嗎？指引解析⭐有雷勿入|曖昧|愛情|戀愛|桃花|塔羅占卜|
- 孫安佐持槍遭羈押！命理師2年前早預言：死神流年
- 孫安佐遭羈押禁見！命理師2年前預言「今年走死神流年」：難逃牢獄之災

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月18日 14:57
- generate_daily_content.py | failed | Gemini content generation failed: invalid Gemini response: missing zh_cn.site_article.excerpt
