# セットアップ: files\ の中身を %USERPROFILE%\dual-agent にコピーし、ショートカットを作る。
# 既存ファイルは上書き前に backups\<日時>\ へ退避します。
$ErrorActionPreference = 'Stop'
$src = Join-Path $PSScriptRoot 'files'
$dst = Join-Path $env:USERPROFILE 'dual-agent'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'

foreach ($d in '', 'bin', 'tasks', 'results\google', 'workspace', 'final', 'logs', 'state', 'backups') {
    New-Item -ItemType Directory -Force -Path (Join-Path $dst $d) | Out-Null
}
Get-ChildItem $src -Recurse -File | ForEach-Object {
    $rel = $_.FullName.Substring($src.Length + 1)
    $target = Join-Path $dst $rel
    if (Test-Path $target) {
        $bk = Join-Path $dst "backups\$stamp\$rel"
        New-Item -ItemType Directory -Force -Path (Split-Path $bk) | Out-Null
        Copy-Item $target $bk
    }
    New-Item -ItemType Directory -Force -Path (Split-Path $target) | Out-Null
    Copy-Item $_.FullName $target -Force
}

# デスクトップのショートカット
$desktop = [Environment]::GetFolderPath('Desktop')
$ws = New-Object -ComObject WScript.Shell
$lnk = $ws.CreateShortcut((Join-Path $desktop 'AI共同作業.lnk'))
$lnk.TargetPath = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\powershell.exe"
$lnk.Arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$dst\start.ps1`""
$lnk.WorkingDirectory = $dst
$lnk.Save()

Write-Host "配置先: $dst"
Write-Host "ショートカット: $desktop\AI共同作業.lnk"
& "$dst\bin\check-environment.ps1"
exit $LASTEXITCODE
