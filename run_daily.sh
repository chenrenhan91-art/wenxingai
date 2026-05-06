#!/usr/bin/env bash
# run_daily.sh
# ============
# 每日自动化流水线：
#   1. 抓取最新命理热点资讯，更新 hot-news-data.json、index.html 与 mingli-xuanxue-news.html
#   2. 每周一自动运行 update_llms_weekly.py，更新 llms-full.txt 热点区块
#
# 用法:
#   bash run_daily.sh          # 手动运行
#   (crontab 自动调用，详见文件末尾注释)
#
# 日志输出位置: logs/run_daily.log

set -euo pipefail

# ── 路径配置 ──────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
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
# 【方式A：每天早上 8:00 自动运行（包含周一的 llms 更新）】
#   0 8 * * * /bin/bash /Users/apple/Desktop/wenxingai-main/run_daily.sh >> /Users/apple/Desktop/wenxingai-main/logs/run_daily.log 2>&1
#
# 【方式B：分开调度——每天 8:00 抓热点，每周一 9:00 更新 llms】
#   0 8 * * *   cd /Users/apple/Desktop/wenxingai-main && python3 scripts/update_hot_news.py >> logs/run_daily.log 2>&1
#   0 9 * * 1   cd /Users/apple/Desktop/wenxingai-main && python3 scripts/update_llms_weekly.py >> logs/run_daily.log 2>&1
