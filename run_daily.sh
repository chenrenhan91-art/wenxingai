#!/usr/bin/env bash
# run_daily.sh
# ============
# 每日自动化流水线：
#   1. 抓取最新命理热点资讯，更新 hot-news-data.json、index.html 与 mingli-xuanxue-news.html
#   2. 每周一自动运行 update_llms_weekly.py，更新 llms-full.txt 热点区块
#   3. 生成 SEO/GEO 主题页并更新 GEO 新鲜度信号、健康报告、关键词运营 brief 与可选 IndexNow 提交
#
# 用法:
#   bash run_daily.sh          # 手动运行
#   (crontab 自动调用，详见文件末尾注释)
#
# 日志输出位置: logs/run_daily.log

set -euo pipefail

# ── 路径配置 ──────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$SCRIPT_DIR"
LOG_DIR="$ROOT_DIR/logs"
LOG_FILE="$LOG_DIR/run_daily.log"
PYTHON="python3"

# ── 初始化日志目录 ────────────────────────────────────────
mkdir -p "$LOG_DIR"

# 时间戳函数
ts() { date '+%Y-%m-%d %H:%M:%S'; }

log() { echo "[$(ts)] $*" | tee -a "$LOG_FILE"; }

# ── 开始 ──────────────────────────────────────────────────
log "=================================================="
log "开始每日自动化流水线"
log "工作目录: $ROOT_DIR"
log "=================================================="

cd "$ROOT_DIR"

# ── Step 1: 抓取热点新闻 ─────────────────────────────────
log "[Step 1] 运行 update_hot_news.py ..."
if $PYTHON scripts/update_hot_news.py >> "$LOG_FILE" 2>&1; then
    log "[Step 1] ✓ 热点资讯更新成功"
else
    EXIT_CODE=$?
    log "[Step 1] ✗ update_hot_news.py 失败 (exit $EXIT_CODE)，继续执行后续步骤"
fi

# ── Step 2: 每周一更新 llms-full.txt ─────────────────────
DAY_OF_WEEK=$(date '+%u')  # 1=周一 ... 7=周日

if [[ "$DAY_OF_WEEK" == "1" ]]; then
    log "[Step 2] 今天是周一，运行 update_llms_weekly.py ..."
    if $PYTHON scripts/update_llms_weekly.py >> "$LOG_FILE" 2>&1; then
        log "[Step 2] ✓ llms-full.txt 周更新成功"
    else
        EXIT_CODE=$?
        log "[Step 2] ✗ update_llms_weekly.py 失败 (exit $EXIT_CODE)"
    fi
else
    log "[Step 2] 今天是周${DAY_OF_WEEK}，跳过 llms 周更新（仅周一运行）"
fi

# ── Step 3: 生成 SEO/GEO 主题页 ───────────────────────────
log "[Step 3] 运行 generate_seo_geo_topic_pages.py ..."
if $PYTHON scripts/generate_seo_geo_topic_pages.py >> "$LOG_FILE" 2>&1; then
    log "[Step 3] ✓ SEO/GEO 主题页生成成功"
else
    EXIT_CODE=$?
    log "[Step 3] ✗ generate_seo_geo_topic_pages.py 失败 (exit $EXIT_CODE)"
fi

# ── Step 4: 更新 GEO 新鲜度信号 ───────────────────────────
log "[Step 4] 运行 update_geo_signals.py ..."
if $PYTHON scripts/update_geo_signals.py >> "$LOG_FILE" 2>&1; then
    log "[Step 4] ✓ GEO 新鲜度信号更新成功"
else
    EXIT_CODE=$?
    log "[Step 4] ✗ update_geo_signals.py 失败 (exit $EXIT_CODE)"
fi

# ── Step 5: 生成 SEO/GEO 自动化健康报告 ───────────────────
log "[Step 5] 运行 run_seo_geo_automation.py ..."
if $PYTHON scripts/run_seo_geo_automation.py >> "$LOG_FILE" 2>&1; then
    log "[Step 5] ✓ SEO/GEO 健康报告生成成功"
else
    EXIT_CODE=$?
    log "[Step 5] ✗ run_seo_geo_automation.py 失败 (exit $EXIT_CODE)"
fi

# ── Step 6: 生成 SEO/GEO 内容运营 brief ───────────────────
log "[Step 6] 运行 plan_seo_geo_content.py ..."
if $PYTHON scripts/plan_seo_geo_content.py >> "$LOG_FILE" 2>&1; then
    log "[Step 6] ✓ SEO/GEO 内容运营 brief 生成成功"
else
    EXIT_CODE=$?
    log "[Step 6] ✗ plan_seo_geo_content.py 失败 (exit $EXIT_CODE)"
fi

# ── Step 7: 可选提交 IndexNow ─────────────────────────────
log "[Step 7] 运行 submit_indexnow.py ..."
if $PYTHON scripts/submit_indexnow.py >> "$LOG_FILE" 2>&1; then
    log "[Step 7] ✓ IndexNow 提交流程完成（未配置 key 时会自动跳过）"
else
    EXIT_CODE=$?
    log "[Step 7] ✗ submit_indexnow.py 失败 (exit $EXIT_CODE)"
fi

# ── 完成 ──────────────────────────────────────────────────
log "=================================================="
log "每日流水线完成"
log "=================================================="

# ── Crontab 配置参考 ──────────────────────────────────────
# 运行以下命令添加定时任务:
#   crontab -e
#
# 然后添加以下两行（按需选择一种，推荐方式A）：
#
# 【方式A：每天早上 8:00 自动运行（包含周一 llms 更新、SEO/GEO 报告、内容 brief 与可选 IndexNow）】
#   0 8 * * * /bin/bash /Users/apple/Desktop/wenxingai-main/run_daily.sh >> /Users/apple/Desktop/wenxingai-main/logs/run_daily.log 2>&1
#
# 【方式B：分开调度——每天抓热点和 GEO 报告，每周一更新 llms】
#   0 8 * * *   cd /Users/apple/Desktop/wenxingai-main && python3 scripts/update_hot_news.py >> logs/run_daily.log 2>&1
#   0 9 * * 1   cd /Users/apple/Desktop/wenxingai-main && python3 scripts/update_llms_weekly.py >> logs/run_daily.log 2>&1
#   0 10 * * *  cd /Users/apple/Desktop/wenxingai-main && python3 scripts/generate_seo_geo_topic_pages.py && python3 scripts/update_geo_signals.py && python3 scripts/run_seo_geo_automation.py && python3 scripts/plan_seo_geo_content.py && python3 scripts/submit_indexnow.py >> logs/run_daily.log 2>&1
