# 问星AI 内容自动化运行报告 2026年5月17日 14:23

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：bfc23037aedece45799e7f6118c481c21542e004
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 最近他想你了嗎？有多想？想到你的心情感受如何？以及你們近期的發展|曖昧|愛情|戀愛|桃花|塔羅占卜
- 我們的塔羅占卜改到明天 今天體力有點不支 沒辦法很好的幫大家占卜 也祝大家有個開心的母親節 狐狐也來陪伴狐媽啦🙏
- [新聞] 沈伯洋「地風升」！台北市長選戰火性強烈 命理師卜卦大膽預
- 算命文化盛行反映現代人對未來的不安 命理師：命運仍掌握在己
- 發財「3舊物」別丟棄!命理師示警： 可能導致運勢下滑

## 新增标题
- 最近他想你了嗎？有多想？想到你的心情感受如何？以及你們近期的發展|曖昧|愛情|戀愛|桃花|塔羅占卜
- 發財「3舊物」別丟棄!命理師示警： 可能導致運勢下滑

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月17日 14:24
- generate_daily_content.py | failed | Gemini content generation failed: invalid Gemini response: missing zh_cn.video_script
