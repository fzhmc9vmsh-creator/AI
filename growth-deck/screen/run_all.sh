#!/usr/bin/env bash
# 1: universe.py -> 2: fetch.py -> 3: screen.py を順に実行し、進捗と所要時間を表示する。
# 使い方: ./run_all.sh            (実データ。Yahoo/JPX/楽天へ接続できる環境が必要)
#         ./run_all.sh --offline  (モックデータ。ネットワーク不要)
# 1 と 2 には引数をそのまま渡す。3 は data/ を読むだけなので引数なし。
set -euo pipefail
cd "$(dirname "$0")"
PY="${PYTHON:-python3}"

run_step() {
  local name="$1"; shift
  echo "==== [$name] 開始 $(date '+%H:%M:%S') ===="
  local t0
  t0=$(date +%s)
  "$@"
  echo "==== [$name] 完了 ($(( $(date +%s) - t0 ))s)"
  echo
}

total0=$(date +%s)
run_step universe "$PY" universe.py "$@"
run_step fetch "$PY" fetch.py "$@"
run_step screen "$PY" screen.py
echo "全体所要時間: $(( $(date +%s) - total0 ))s"
