# 问星AI 内容自动化运行报告 2026年5月31日 22:49

- 总体状态：failed_generate
- 本轮是否强制刷新：是
- 热点是否变化：是
- 变更签名：3163ecf7bebbab293d193aaab4d096f92c5d453c
- Gemini 是否执行：是
- Gemini 审校是否执行：否
- 规则质检是否执行：否
- Gemini 内容包是否匹配本轮热点：否
- Buffer 是否执行：否
- 深度文章是否生成：否
- 阶段状态：抓取=ok, 生成=failed, 审校=blocked, 质检=blocked, 分发=blocked, 文章=skipped

## 本轮热点标题
- 香灰千万别乱丢，这么做能招财！ #玄學 #國學 #風水 #香灰 #招財
- 揭秘內娛最甜婚姻真相，深扒浪姐唐藝昕命盤：甜妹皮囊下的「馴龍女王」，把張若昀調教成「純愛戰神」的神級馭夫術！《乘風2026》運勢大推演，女生必看... youtu.be/ArBvZDI78aY?si… 来自 @YouTube #唐艺昕 #浪姐 #乘风2026 #八字 #命理分析 #算命 #嫁豪门 #张若
- [新聞] 鬼門開遇日全蝕超凶？命理師引述古籍：
- 早預言馬英九犯小人!命理師驚揭「流年走死神」： 恐有大變化
- 流年沖害破！命理師警告「3生肖破財」下半年慘了

## 新增标题
- 早預言馬英九犯小人!命理師驚揭「流年走死神」： 恐有大變化
- 流年沖害破！命理師警告「3生肖破財」下半年慘了

## 次日运营建议
- 明日优先延展「命理新闻」相关选题（当前占比 6/8）。

## 失败脚本
- generate_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年5月31日 22:49
- generate_daily_content.py | failed | [warn] DashScope model qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b failed; trying qwen3.6-flash-2026-04-16. Reason: HTTP 404: {"error":{"message":"The model `qwen3.5-flash,qwen3.6-flash-2026-04-16,qwen3.5-27b` does not exist or you do not have access to it.","type":"invalid_request_error","param":null,...
[ok] DashScope fallback model selected: qwen3.6-flash-2026-04-16
Gemini content generation failed: invalid Gemini response: missing zh_cn.social_posts
