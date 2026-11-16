# -*- coding: utf-8 -*-
"""pptx の全スライドの文字を、スライドごとに書き出す(検証用)。使い方: py -3 dump_deck_text.py deck.pptx out.md"""
import sys, zipfile, re, io
src, out = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(src)
names = sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)], key=lambda n: int(re.findall(r'\d+', n)[0]))
lines = []
for n in names:
    xml = z.read(n).decode('utf-8')
    paras = re.findall(r'<a:p>(.*?)</a:p>', xml, flags=re.S)
    texts = []
    for p in paras:
        t = ''.join(re.findall(r'<a:t>(.*?)</a:t>', p, flags=re.S))
        t = t.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').strip()
        if t:
            texts.append(t)
    no = int(re.findall(r'\d+', n)[0])
    lines.append(f'## p.{no}')
    lines.extend(texts)
    lines.append('')
io.open(out, 'w', encoding='utf-8').write('\n'.join(lines))
print(len(names), 'slides', sum(len(l) for l in lines), 'chars')
