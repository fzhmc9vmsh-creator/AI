# 環境確認。終了コード: 0=成功 10=ログイン必要 20=未インストール 1=その他
. (Join-Path $PSScriptRoot 'common.ps1')
$stateDir = Join-Path $Root 'state'
New-Item -ItemType Directory -Force -Path $stateDir | Out-Null

$claude = Find-Cli 'claude'
if (-not $claude) {
    "Claude Code (claude) が見つかりません。`nインストール: https://claude.com/product/claude-code" |
        Set-Content (Join-Path $Root 'NEEDS_INSTALL.md') -Encoding UTF8
    Write-Host 'NG: claude が未インストール'; exit 20
}
$backend = Get-GoogleBackend
if (-not $backend) {
    "Antigravity (agy) も Gemini CLI (gemini) も見つかりません。`nどちらか一方を公式手順で入れてください。" |
        Set-Content (Join-Path $Root 'NEEDS_INSTALL.md') -Encoding UTF8
    Write-Host 'NG: agy / gemini が未インストール'; exit 20
}
Write-Host "OK: claude = $claude"
Write-Host "OK: Google側 = $backend"

# 副作用のない短い問い合わせで認証を確認
$needLogin = @()
$r = Invoke-Cli $claude @('-p', '「OK」とだけ答えてください。', '--output-format', 'text') 120
if ($r.ExitCode -ne 0 -or (Test-AuthError $r.Output)) { $needLogin += 'claude' }
$gexe = Find-Cli $backend
$r2 = Invoke-Cli $gexe @('-p', '「OK」とだけ答えてください。', '--output-format', 'json') 120
if ($r2.ExitCode -ne 0 -or (Test-AuthError $r2.Output)) { $needLogin += $backend }

if ($needLogin.Count -gt 0) {
    $body = "# ログインが必要です`n`n次を順番に、ふつうのPowerShellで1つずつ実行し、ブラウザの公式画面でログインしてください。`n`n"
    foreach ($n in $needLogin) { $body += "``````n$n`n```````n`n" }
    $body | Set-Content (Join-Path $Root 'NEEDS_LOGIN.md') -Encoding UTF8
    Write-Host "NG: ログインが必要 -> $($needLogin -join ', ')  (NEEDS_LOGIN.md を見てください)"; exit 10
}
Remove-Item (Join-Path $Root 'NEEDS_LOGIN.md'), (Join-Path $Root 'NEEDS_INSTALL.md') -ErrorAction SilentlyContinue
@{ backend = $backend; checked = (Get-Date -Format 's') } | ConvertTo-Json |
    Set-Content (Join-Path $stateDir 'environment.json') -Encoding UTF8
Write-Host '環境確認: すべてOK'; exit 0
