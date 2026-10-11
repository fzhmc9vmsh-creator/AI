#!/usr/bin/env python3
"""検証用: docx を LibreOffice で開き、目次などのフィールドを更新してから PDF に書き出す。
使い方: python3 render_check.py in.docx out.pdf
(Yu Gothic / Calibri が無い環境でも確認できるよう、fontconfig の別名で IPAGothic / Carlito に置き換える。
 docx 自体のフォント指定は変えない。)"""
import os, subprocess, sys, time, tempfile, shutil

src, dst = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
work = tempfile.mkdtemp(prefix='rc_')
conf = os.path.join(work, 'fonts.conf')
open(conf, 'w').write('''<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig><include ignore_missing="yes">/etc/fonts/fonts.conf</include>
<match target="pattern"><test name="family" qual="any"><string>Yu Gothic</string></test><edit name="family" mode="assign" binding="strong"><string>IPAGothic</string></edit></match>
<match target="pattern"><test name="family" qual="any"><string>Calibri</string></test><edit name="family" mode="assign" binding="strong"><string>Carlito</string></edit></match>
</fontconfig>''')
env = dict(os.environ, FONTCONFIG_FILE=conf)
port = 2002
proc = subprocess.Popen(['soffice', '--headless', '--invisible', '--norestore', '--nologo',
    '-env:UserInstallation=file://' + os.path.join(work, 'profile'),
    '--accept=socket,host=localhost,port=%d;urp;' % port], env=env,
    stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    import uno
    from com.sun.star.beans import PropertyValue
    def pv(n, v):
        p = PropertyValue(); p.Name = n; p.Value = v; return p
    local = uno.getComponentContext()
    resolver = local.ServiceManager.createInstanceWithContext('com.sun.star.bridge.UnoUrlResolver', local)
    ctx = None
    for _ in range(60):
        try:
            ctx = resolver.resolve('uno:socket,host=localhost,port=%d;urp;StarOffice.ComponentContext' % port); break
        except Exception:
            time.sleep(1)
    if ctx is None: raise SystemExit('soffice に接続できません')
    desktop = ctx.ServiceManager.createInstanceWithContext('com.sun.star.frame.Desktop', ctx)
    doc = desktop.loadComponentFromURL(uno.systemPathToFileUrl(src), '_blank', 0, (pv('Hidden', True),))
    idx = doc.getDocumentIndexes()
    for i in range(idx.getCount()):
        idx.getByIndex(i).update()
    print('indexes updated:', idx.getCount())
    doc.getTextFields().refresh()
    doc.storeToURL(uno.systemPathToFileUrl(dst), (pv('FilterName', 'writer_pdf_Export'),))
    doc.close(True)
    try: desktop.terminate()
    except Exception: pass
finally:
    time.sleep(1)
    proc.terminate()
    shutil.rmtree(work, ignore_errors=True)
print('wrote', dst)
