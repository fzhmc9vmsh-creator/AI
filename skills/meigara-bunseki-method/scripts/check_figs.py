#!/usr/bin/env python3
"""資料の図の網羅検査: py -3 check_figs.py <deck フォルダ>
deck/figs.json に {"F1": "s08a", ...} と図番号 → スライド id の対応を書く。章立ての型だけ見て図の一覧と照合しない失敗を止める。
図カタログ F1〜F26 と deck-rules-v2 の必須スライドがすべて、meta.js の ORDER にあるスライドへ対応していなければ FAIL。
"""
import json
import os
import subprocess
import sys

REQUIRED = {f'F{i}': n for i, n in enumerate([
    '鳥の目事業構造マップ', '構造変化オーバーレイ', '強気派vs弱気派対照表', '判別KPI計器盤', '検証スケジュール', '目標株価計算フロー',
    'エントリー価格ゾーン', '時系列投資戦略', '移行現在地ロードマップ', '収益・費用フロー解剖', 'シナリオ採点表', 'シナリオ×PEG感応度',
    '年度別適正株価パス', 'リスクマトリクス', '事業エンジン図', '機構台帳サマリ', '市場との差分', '根幹KPI加速度表',
    '損益フロー図(サンキー)', '競合との品質×価格', 'FCF・レバレッジの経路', '戦略施策の事業価値', '会社のシナリオ・ストーリー図',
    '事業の積み木と用語', '事業間の関係図', '成長分野の注目度'], 1)}
REQUIRED.update({
    'R-G': '成長の尺度 G1〜G8', 'R-phase': 'フェーズと二層の構造', 'R-eps': 'EPSの要因分解', 'R-macro': 'マクロの両面',
    'R-capital': '資本モデルの業界比較', 'R-cond6': '条件6の市場比較', 'R-peg': '構造評価→許容PEGの導出', 'R-credit': '信用と資本の制約',
    'R-tree': 'シナリオの節点ツリー', 'R-ceo': '条件5 経歴の関係図', 'R-cross': '交差確認(平均しない)',
})
IMAGE = {'F19'}  # 画像で描く図


def main():
    deck = sys.argv[1]
    figs = json.load(open(os.path.join(deck, 'figs.json'), encoding='utf-8'))
    order = json.loads(subprocess.run(['node', '-e', "console.log(JSON.stringify(require('./meta.js').ORDER))"],
                                      cwd=deck, capture_output=True, text=True, check=True).stdout)
    errs = []
    for k, name in REQUIRED.items():
        ids = figs.get(k)
        if not ids:
            errs.append(f'{k} {name}: 対応するスライドがない')
            continue
        for i in ([ids] if isinstance(ids, str) else ids):
            f = os.path.join(deck, 'slides', i + '.js')
            if i not in order or not os.path.exists(f):
                errs.append(f'{k} {name}: {i} が ORDER かファイルにない')
            elif k in IMAGE and 'addImage' not in open(f, encoding='utf-8').read():
                errs.append(f'{k} {name}: {i} に画像がない')
    for e in errs:
        print('誤り:', e)
    print(f'{len(REQUIRED)} 項目 / 誤り {len(errs)} → {"FAIL" if errs else "PASS"}')
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
