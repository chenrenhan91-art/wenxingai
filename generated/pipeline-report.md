# 问星AI 内容自动化运行报告 2026年5月9日 13:49

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：a04b7de74afd1ca32555ae4c975cbe3fcd796d62
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 流年運勢你算了嗎? #開運軍師尹森#風水尹森#流年 #算命 #紫微斗數#八字 #命盤#尹森老師#尹森#命理師#命理師推薦#風水師推薦#2026運勢 #https #家居風水宜忌
- 臺灣命理師預測鄭麗文好運只能走到2026年(圖)
- [新聞] 沈伯洋「地風升」！台北市長選戰火性強烈 命理師卜卦大膽預
- 小滿「2生肖」開始走運！命理師揭3開運方法：多吃1種菜
- 立夏交節氣運勢洗牌…命理師示警2生肖恐破財 忌高風險操作

## 新增标题
- 臺灣命理師預測鄭麗文好運只能走到2026年(圖)
- 小滿「2生肖」開始走運！命理師揭3開運方法：多吃1種菜

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 7/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月9日 13:50
- generate_daily_content.py | failed | Gemini content generation failed: invalid Gemini response: missing zh_cn.video_script
