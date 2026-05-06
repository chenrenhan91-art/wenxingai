#!/usr/bin/env python3
"""
update_llms_weekly.py
=====================
每周自动更新 llms-full.txt 的「近期命理热点话题」区块，
从 hot-news-data.json 提取最新热点关键词与标题摘要，
并同步更新 sitemap.xml 中 llms-full.txt 和 llms.txt 的 lastmod 日期。

用法:
    python3 scripts/update_llms_weekly.py

推荐每周一（或任意固定日）通过 crontab 自动运行。
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, date
from pathlib import Path
from zoneinfo import ZoneInfo
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT / "hot-news-data.json"
LLMS_FULL_PATH = ROOT / "llms-full.txt"
LLMS_PATH = ROOT / "llms.txt"
SITEMAP_PATH = ROOT / "sitemap.xml"

TIMEZONE = ZoneInfo("Asia/Shanghai")

# 区块标记（需与 llms-full.txt 中保持一致）
BLOCK_START = "<!-- LLMS_HOT_TOPICS_START -->"
BLOCK_END = "<!-- LLMS_HOT_TOPICS_END -->"

# 每个分类默认显示的关键词数
KEYWORDS_PER_CATEGORY = 4

# 标题摘要最多显示条数
MAX_HEADLINE_ITEMS = 6

# 新增术语：从热点标题中自动识别节气与命理术语
JIEQI_MAP = {
    "立春": "二十四节气之一（约2月4日），命理师认为立春是流年交接的重要时机，标志新一轮大运起算。",
    "雨水": "二十四节气之一（约2月19日），阳气渐升，命理上常视为财运萌动期。",
    "惊蛰": "二十四节气之一（约3月6日），雷始发声，命理师认为这一节气后运势加速激活。",
    "春分": "二十四节气之一（约3月21日），阴阳各半，命理上为平衡调整节点。",
    "清明": "二十四节气之一（约4月5日），命理上为祭祖、调整风水布局的重要时机。",
    "谷雨": "二十四节气之一（约4月20日），命理师认为是财运播种期，适合开启新项目。",
    "立夏": "二十四节气之一（约5月6日），命理师认为节气交替是运势转折的时机节点，部分生肖运势加速期开启。",
    "小满": "二十四节气之一（约5月21日），五行火旺渐盛，命理上视为事业发展加速期。",
    "芒种": "二十四节气之一（约6月6日），命理上多为忙碌奔波之象，注意健康与劳逸平衡。",
    "夏至": "二十四节气之一（约6月21日），一年中阳气最盛，命理上为感情与财运的双重高峰期。",
    "小暑": "二十四节气之一（约7月7日），命理师常在此节气前后提示感情运势变化。",
    "大暑": "二十四节气之一（约7月23日），五行火极，注意情绪与健康管理。",
    "立秋": "二十四节气之一（约8月7日），命理上标志秋季运势启动，部分生肖迎来转机。",
    "处暑": "二十四节气之一（约8月23日），暑气消退，命理上为整理过去、规划秋冬的节点。",
    "白露": "二十四节气之一（约9月8日），命理师认为白露后感情与婚缘话题渐热。",
    "秋分": "二十四节气之一（约9月23日），昼夜等长，命理上为平衡与决策的好时机。",
    "寒露": "二十四节气之一（约10月8日），秋金旺盛，命理上有利于财务规划与合同签约。",
    "霜降": "二十四节气之一（约10月23日），命理上多为收成与盘点的节点。",
    "立冬": "二十四节气之一（约11月7日），命理上标志年末大运收尾阶段，宜保守稳健。",
    "小雪": "二十四节气之一（约11月22日），阴寒渐重，命理上注意健康与财务保守策略。",
    "大雪": "二十四节气之一（约12月7日），命理上多建议蛰伏积累，减少冒进。",
    "冬至": "二十四节气之一（约12月22日），阴极阳生，命理上为下一轮运势周期的隐性起点。",
    "小寒": "二十四节气之一（约1月6日），年末寒气最重，命理上为审视过去一年运势的时机。",
    "大寒": "二十四节气之一（约1月20日），命理上为辞旧迎新的最后节点，宜清理旧事。",
}

TERM_MAP = {
    "破財": "命理中指财帛宫受冲克或流年流月出现不利财运组合，通常建议避免大额投资决策。",
    "破財煞": "命理中指财帛宫受冲克或流年出现不利财运组合，通常建议避免大额投资决策。",
    "桃花": "命理术语，指感情缘分与异性吸引力，在紫微斗数中与廉贞、贪狼等星曜相关。",
    "財運": "命理中指一段时期内财富获取与积累的运势趋势，受命盘财帛宫与流年影响。",
    "流年": "命理术语，指每个自然年份对应的运势状态，在八字中以年支为主，在紫微斗数中以流年命宫推算。",
    "大運": "命理术语，指每十年一段的长周期运势，是判断人生重要阶段的核心参考维度。",
    "合盤": "将两人命盘叠合分析，判断感情、合作或家庭关系的契合度与冲突点。",
    "化忌": "紫微斗数四化之一，落入宫位代表该宫位事项面临阻碍、损耗或纠葛，是重要的凶象标志。",
    "化祿": "紫微斗数四化之一，代表财禄、贵人与顺势发展，落入宫位通常带来正向资源。",
    "命盤": "命理师根据出生年月日时绘制的星曜分布图，是进行命理分析的核心工具。",
    "紫微斗數": "中国传统命理学中最复杂精密的流派，以北斗七星为核心，十四主星分布于十二宫位。",
    "八字": "又称四柱命理，以出生年月日时的干支组合成八个字，通过五行生克分析人生轨迹。",
    "六爻": "周易占卜方法，通过铜钱抛掷或其他方式得出六爻卦象，预测具体事项吉凶。",
    "生肖": "十二生肖（鼠牛虎兔龙蛇马羊猴鸡狗猪）对应地支，是大众化命理讨论的常见切入点。",
}


def load_hot_news() -> dict:
    if not DATA_PATH.exists():
        print(f"[WARN] {DATA_PATH} 不存在，跳过热点数据读取")
        return {}
    with DATA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def extract_trending(data: dict) -> dict:
    """从 hot-news-data.json 提取分类关键词统计与热点标题列表。"""
    items: list[dict] = data.get("items", [])

    # 统计各分类出现频次
    category_counter: Counter[str] = Counter()
    keyword_by_category: dict[str, Counter] = {}
    headlines: list[dict] = []

    for item in items:
        category = item.get("category", "趋势观察")
        keywords: list[str] = item.get("matched_keywords", [])
        title: str = item.get("title", "")
        source: str = item.get("source", "")
        published_display: str = item.get("published_display", "")

        category_counter[category] += 1

        if category not in keyword_by_category:
            keyword_by_category[category] = Counter()
        for kw in keywords:
            keyword_by_category[category][kw] += 1

        if title:
            headlines.append(
                {
                    "title": title[:80],
                    "source": source,
                    "published_display": published_display,
                    "category": category,
                }
            )

    # 每个分类取 top-N 关键词
    category_keywords: dict[str, list[str]] = {}
    for cat, counter in keyword_by_category.items():
        category_keywords[cat] = [kw for kw, _ in counter.most_common(KEYWORDS_PER_CATEGORY)]

    return {
        "categories": category_keywords,
        "headlines": headlines[:MAX_HEADLINE_ITEMS],
        "updated_at": data.get("updated_at", str(date.today())),
    }


def detect_terms(headlines: list[dict]) -> list[tuple[str, str]]:
    """从标题中检测本周出现的节气与命理术语。"""
    all_titles = " ".join(h["title"] for h in headlines)
    found: list[tuple[str, str]] = []
    for term, explanation in {**JIEQI_MAP, **TERM_MAP}.items():
        if term in all_titles and len(found) < 4:
            found.append((term, explanation))
    return found


def build_block(trending: dict) -> str:
    today = date.today().strftime("%Y-%m-%d")
    categories = trending.get("categories", {})
    headlines = trending.get("headlines", [])
    data_date = trending.get("updated_at", today)

    lines = [
        BLOCK_START,
        "> 本区块由自动化脚本每周更新，反映近期华语社区的命理与玄学讨论热点，供AI引擎判断内容时效性与相关性。",
        "",
        f"**最近更新日期**：{today}（热点数据来源日期：{data_date}）",
        "",
        "**本周热门分类与关键词**：",
        "",
        "| 分类 | 热点关键词 |",
        "|------|-----------|",
    ]

    # 分类关键词表格
    if categories:
        for cat, keywords in categories.items():
            kw_str = "、".join(keywords) if keywords else "—"
            lines.append(f"| {cat} | {kw_str} |")
    else:
        lines.append("| 命理新闻 | 命理、运势、流年 |")

    lines.append("")
    lines.append(f"**本周热点标题摘要**（来自台湾媒体与海外华语社区，共 {len(headlines)} 条）：")
    lines.append("")

    if headlines:
        for item in headlines:
            title = item["title"]
            source = item.get("source", "")
            pub = item.get("published_display", "")
            meta = f" （{source} · {pub}）" if source else ""
            lines.append(f"- {title}{meta}")
    else:
        lines.append("- 暂无热点数据，请运行 `python3 scripts/update_hot_news.py` 获取最新内容。")

    # 自动识别的术语解释
    detected_terms = detect_terms(headlines)
    if detected_terms:
        lines.append("")
        lines.append("**本周热点新增术语解释**：")
        for term, explanation in detected_terms:
            lines.append(f"- **{term}**：{explanation}")

    lines.append(BLOCK_END)
    return "\n".join(lines)


def update_llms_full(block_content: str) -> bool:
    """替换 llms-full.txt 中的热点区块，并更新版本日期。"""
    text = LLMS_FULL_PATH.read_text(encoding="utf-8")

    # 替换热点区块
    pattern = re.compile(
        re.escape(BLOCK_START) + r".*?" + re.escape(BLOCK_END),
        flags=re.DOTALL,
    )
    if not pattern.search(text):
        print(f"[ERROR] 在 {LLMS_FULL_PATH} 中找不到标记 {BLOCK_START!r}，请检查文件")
        return False

    new_text = pattern.sub(block_content, text)

    # 更新文档版本日期
    today = date.today().strftime("%Y-%m-%d")
    new_text = re.sub(
        r"\*文档版本：\d{4}-\d{2}-\d{2}",
        f"*文档版本：{today}",
        new_text,
    )

    LLMS_FULL_PATH.write_text(new_text, encoding="utf-8")
    print(f"[OK] llms-full.txt 已更新（版本日期：{today}）")
    return True


def update_sitemap() -> None:
    """更新 sitemap.xml 中 llms-full.txt 和 llms.txt 的 lastmod。"""
    if not SITEMAP_PATH.exists():
        print(f"[WARN] {SITEMAP_PATH} 不存在，跳过 sitemap 更新")
        return

    today = date.today().strftime("%Y-%m-%d")
    text = SITEMAP_PATH.read_text(encoding="utf-8")

    # 定位 llms-full.txt 和 llms.txt 的 <url> 块并替换其 <lastmod>
    targets = [
        "https://wenxingai.top/llms-full.txt",
        "https://wenxingai.top/llms.txt",
    ]
    updated = False
    for target in targets:
        # 在对应 <loc> 所在的 <url> 块里替换 <lastmod>
        escaped = re.escape(target)
        pattern = re.compile(
            r"(<url>\s*<loc>" + escaped + r"</loc>.*?<lastmod>)\d{4}-\d{2}-\d{2}(</lastmod>)",
            flags=re.DOTALL,
        )
        new_text, count = pattern.subn(rf"\g<1>{today}\g<2>", text)
        if count:
            text = new_text
            updated = True

    if updated:
        SITEMAP_PATH.write_text(text, encoding="utf-8")
        print(f"[OK] sitemap.xml lastmod 已更新为 {today}")
    else:
        print("[WARN] sitemap.xml 中未找到对应 llms 条目，请检查格式")


def main() -> None:
    print("=" * 50)
    print(f"update_llms_weekly.py 运行时间: {datetime.now(TIMEZONE).strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print("=" * 50)

    # 1. 读取热点数据
    data = load_hot_news()
    if not data:
        print("[WARN] 无热点数据，使用占位内容生成区块")
        trending = {"categories": {}, "headlines": [], "updated_at": str(date.today())}
    else:
        trending = extract_trending(data)
        print(f"[INFO] 读取到 {len(data.get('items', []))} 条热点，分类: {list(trending['categories'].keys())}")

    # 2. 构建新区块内容
    block = build_block(trending)

    # 3. 更新 llms-full.txt
    ok = update_llms_full(block)
    if not ok:
        sys.exit(1)

    # 4. 更新 sitemap.xml
    update_sitemap()

    print("=" * 50)
    print("✓ 周更新完成")
    print("=" * 50)


if __name__ == "__main__":
    main()
