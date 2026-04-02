# 问星AI 内容自动化运行报告 2026年4月2日 18:12

- 总体状态：partial_failure
- 本轮是否强制刷新：否
- 热点是否变化：是
- 变更签名：3d128f74372d8918f2af25e0ae91a3b45ec39b57
- Gemini 是否执行：是
- Gemini 审校是否执行：是
- 规则质检是否执行：是
- Gemini 内容包是否匹配本轮热点：是
- Buffer 是否执行：是

## 本轮热点标题
- 【暗戀專場】他發現你喜歡他嗎？以及他喜歡你嗎？愚人節拆盲盒了！|曖昧|暗戀|戀愛|桃花|塔羅占卜
- [ 易經６４卦算流年 初班0310 ] #天水訟 訟有孚窒惕中吉終凶 #易卦大成卦六十四卦 #坎卦命 #2026丙午馬年 #算流年唔駛用八字 #算流年唔駛用紫斗 #自己運程自己推算 #玄學課程 #風水課程 #擇日課程 #算命課程 #奇門 #易經 #風水命理 #風水布局 #算命算流年 #流年
- [新聞] 下葬61年祖母未腐反成蔭屍 命理師：
- ATM也能補財庫！命理師教1招清明「開運存錢法」…財庫補好補滿
- 4/6觀音生！命理師曝3大禁忌習俗與開運時辰，加碼3生肖財運爆棚，屬羊正財運旺

## 新增标题
- 【暗戀專場】他發現你喜歡他嗎？以及他喜歡你嗎？愚人節拆盲盒了！|曖昧|暗戀|戀愛|桃花|塔羅占卜
- ATM也能補財庫！命理師教1招清明「開運存錢法」…財庫補好補滿

## 失败脚本
- distribute_daily_content.py

## 脚本结果
- update_hot_news.py | ok | [warn] failed to fetch Reddit Search: HTTP Error 403: Blocked
updated 8 hot news items at 2026年4月2日 18:12
- generate_daily_content.py | ok | generated Gemini content bundle at 2026年4月2日 18:12 using gemini-2.5-pro
- review_daily_content.py | ok | reviewed Gemini content bundle using gemini-2.5-pro
- audit_daily_content.py | ok | content audit passed with 0 warnings
- distribute_daily_content.py | failed | Traceback (most recent call last):
  File "/home/runner/work/wenxingai/wenxingai/scripts/distribute_daily_content.py", line 81, in fetch_json
    with urllib.request.urlopen(request, timeout=45) as response:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/urllib/request.py", line 216, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/urllib/request.py", line 525, in open
    response = meth(req, response)
               ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/urllib/request.py", line 634, in http_response
    response = self.parent.error(
               ^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/urllib/request.py", line 563, in error
    return self._call_chain(*args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/urllib/request.py", line 496, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.11.15/x64/lib/python3.11/urllib/request.py", line 643, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 401: Unauthorized

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/wenxingai/wenxingai/scripts/distribute_daily_content.py", line 541, in <module>
    main()
  File "/home/runner/work/wenxingai/wenxingai/scripts/distribute_daily_content.py", line 516, in main
    results, failed_count = publish_jobs_to_buffer(jobs, state)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/wenxingai/wenxingai/scripts/distribute_daily_content.py", line 412, in publish_jobs_to_buffer
    profiles = get_buffer_profiles(api_key)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/wenxingai/wenxingai/scripts/distribute_daily_content.py", line 334, in get_buffer_profiles
    data = fetch_json(url)
           ^^^^^^^^^^^^^^^
  File "/home/runner/work/wenxingai/wenxingai/scripts/distribute_daily_content.py", line 89, in fetch_json
    raise RuntimeError(f"HTTP {exc.code} from {url}: {body}") from exc
RuntimeError: HTTP 401 from https://api.bufferapp.com/1/profiles.json?access_token=zXgwmR8Dg6WNvILjN99vMQbf3UfmsZPrmG5M9b7abh7: {"error":"OIDC tokens are not accepted for direct API access","code":401}
