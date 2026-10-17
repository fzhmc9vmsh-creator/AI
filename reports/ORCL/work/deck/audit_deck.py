# -*- coding: utf-8 -*-
"""
スライドの機械監査(L2)。bcg-slide-method の audit-loop.md が同期フォルダに無いため、
invest-consulting-deck/references/design-spec.md の規定から作った代替。
検査: 範囲・余白 / 配色 / フォント名・サイズ / 文字の収まり(推定) / 文字枠の重なり / 出所・ページ番号 / タイトルの形
使い方: python3 audit_deck.py deck.pptx [--json out.json]
例外指定: shape の name が 'bg_'(全面背景・パネル)で始まるものは余白・重なり検査から除外。
         'ovl_' で始まるものは意図した重ね(チャート上のラベル等)として重なり検査から除外。
"""
import sys, json, re
from pptx import Presentation
from pptx.util import Emu

EMU_IN = 914400
W_IN, H_IN = 13.333, 7.5
MARGIN = 0.45            # 0.5in 規定に丸め誤差を許す
PALETTE = {'197A56', '0E4D33', '86C99B', '1BA1A6', 'C0392B', 'D68910', '333333', '767676', 'D9D9D9', 'FFFFFF',
           'E67E22', '7B241C', 'EAF4EE', 'F2F2F2'}   # 末尾2色: 薄緑・薄灰の背景(テイクアウェイ・表の縞)
FONTS = {'Meiryo UI', 'Arial'}
MIN_PT = 8.0
TITLE_PT = (18.0, 20.0)


def inch(v):
    return (v or 0) / EMU_IN


def text_width_em(s):
    w = 0.0
    for ch in s:
        o = ord(ch)
        if o < 0x80:
            w += 0.56 if ch not in ' .,:;|!il1' else 0.3
        elif 0xFF61 <= o <= 0xFF9F:
            w += 0.5
        else:
            w += 1.0
    return w


def iter_shapes(shapes, dx=0, dy=0):
    for sh in shapes:
        if sh.shape_type == 6:  # group
            yield from iter_shapes(sh.shapes, dx, dy)
        else:
            yield sh


def colors_in(xml):
    return set(re.findall(r'srgbClr val="([0-9A-Fa-f]{6})"', xml))


def audit(path):
    prs = Presentation(path)
    issues = []
    n = len(prs.slides)
    for i, slide in enumerate(prs.slides, 1):
        kind = 'content'
        names = [s.name for s in slide.shapes]
        if any(nm.startswith('bg_cover') or nm.startswith('bg_divider') or nm.startswith('bg_agenda') for nm in names):
            kind = 'dark'
        boxes = []
        has_src = has_pg = False
        title = None
        for sh in iter_shapes(slide.shapes):
            x, y, w, h = inch(sh.left), inch(sh.top), inch(sh.width), inch(sh.height)
            nm = sh.name or ''
            # 1. 範囲と余白
            if x < -0.01 or y < -0.01 or x + w > W_IN + 0.01 or y + h > H_IN + 0.01:
                issues.append((i, 'Blocker', 'bounds', nm, f'範囲外 x={x:.2f} y={y:.2f} w={w:.2f} h={h:.2f}'))
            elif not nm.startswith('bg_') and (x < MARGIN - 0.2 or x + w > W_IN - MARGIN + 0.2 or y < 0.25 or y + h > H_IN - 0.2):
                issues.append((i, 'Major', 'margin', nm, f'余白不足 x={x:.2f} y={y:.2f} 右端={x + w:.2f} 下端={y + h:.2f}'))
            # 2. 配色
            xml = sh._element.xml
            bad = {c.upper() for c in colors_in(xml)} - PALETTE
            if bad:
                issues.append((i, 'Major', 'palette', nm, f'規定外の色 {sorted(bad)}'))
            if not sh.has_text_frame:
                continue
            tf = sh.text_frame
            text = tf.text.strip()
            if not text:
                continue
            if nm.startswith('src') or text.startswith('出所'):
                has_src = True
            if nm.startswith('pg') or re.fullmatch(r'\d{1,3}', text):
                has_pg = True
            if nm == 'title':
                title = text
            # 3. フォント
            sizes = []
            for p in tf.paragraphs:
                for r in p.runs:
                    f = r.font
                    if f.size is not None:
                        sizes.append(f.size.pt)
                        if f.size.pt < MIN_PT:
                            issues.append((i, 'Major', 'font-size', nm, f'{f.size.pt}pt < {MIN_PT}pt'))
                    fn = f.name
                    if fn and fn not in FONTS:
                        issues.append((i, 'Minor', 'font-name', nm, f'規定外フォント {fn}'))
            if nm == 'title' and sizes and not (TITLE_PT[0] <= max(sizes) <= TITLE_PT[1]):
                issues.append((i, 'Major', 'title-size', nm, f'タイトル {max(sizes)}pt(規定 18〜20pt)'))
            # 4. 文字の収まり(推定): 各段落の幅 ÷ 枠の内寸 → 行数 × 行高 ≤ 枠の高さ
            pt = max(sizes) if sizes else 12.0
            ml = inch(tf.margin_left) if tf.margin_left is not None else 0.1
            mr = inch(tf.margin_right) if tf.margin_right is not None else 0.1
            mt = inch(tf.margin_top) if tf.margin_top is not None else 0.05
            mb = inch(tf.margin_bottom) if tf.margin_bottom is not None else 0.05
            inner_w = max(0.05, w - ml - mr) * 0.92          # LibreOffice の置換フォント幅に 8% の余裕
            lines = 0
            for p in tf.paragraphs:
                ptxt = ''.join(r.text for r in p.runs) or ' '
                psz = max([r.font.size.pt for r in p.runs if r.font.size is not None] or [pt])
                em_in = psz / 72.0
                lines_p = max(1, -(-text_width_em(ptxt) * em_in // inner_w))
                lines += lines_p * (psz / pt)
            need_h = lines * pt / 72.0 * 1.2 + mt + mb
            if tf.word_wrap is not False and need_h > h + 0.02:
                sev = 'Blocker' if need_h > h * 1.25 else 'Major'
                issues.append((i, sev, 'text-fit', nm, f'推定 {need_h:.2f}in > 枠 {h:.2f}in(「{text[:24]}…」)'))
            if not nm.startswith('ovl_') and not nm.startswith('bg_'):
                boxes.append((nm, x, y, w, h, text[:16]))
        # 5. 文字枠の重なり
        for a in range(len(boxes)):
            for b in range(a + 1, len(boxes)):
                na, xa, ya, wa, ha, ta = boxes[a]
                nb, xb, yb, wb, hb, tb = boxes[b]
                ox = min(xa + wa, xb + wb) - max(xa, xb)
                oy = min(ya + ha, yb + hb) - max(ya, yb)
                if ox > 0.03 and oy > 0.03:
                    issues.append((i, 'Major', 'overlap', f'{na} × {nb}', f'重なり {ox:.2f}×{oy:.2f}in(「{ta}」「{tb}」)'))
        # 6. 出所・ページ番号(内容スライド)
        if kind == 'content' and i > 1:
            if not has_pg:
                issues.append((i, 'Major', 'footer', '-', 'ページ番号なし'))
        # 7. タイトルの形(メッセージ型: 体言止めを避ける)
        if kind == 'content' and title:
            if len(title) < 18:
                issues.append((i, 'Major', 'title-form', 'title', f'短すぎる(メッセージ型でない可能性)「{title}」'))
            if title.endswith('。'):
                issues.append((i, 'Minor', 'title-form', 'title', '句点で終わっている'))
    return n, issues


if __name__ == '__main__':
    path = sys.argv[1]
    n, issues = audit(path)
    order = {'Blocker': 0, 'Major': 1, 'Minor': 2}
    issues.sort(key=lambda r: (order[r[1]], r[0]))
    for r in issues:
        print('slide %2d [%s] %-10s %s: %s' % r)
    cnt = {k: sum(1 for r in issues if r[1] == k) for k in order}
    print(f'\n{n} slides | Blocker {cnt["Blocker"]} / Major {cnt["Major"]} / Minor {cnt["Minor"]}')
    print('RESULT:', 'PASS' if cnt['Blocker'] == 0 and cnt['Major'] == 0 else 'FAIL')
    if '--json' in sys.argv:
        json.dump([dict(slide=a, sev=b, kind=c, shape=d, msg=e) for a, b, c, d, e in issues],
                  open(sys.argv[sys.argv.index('--json') + 1], 'w'), ensure_ascii=False, indent=1)
