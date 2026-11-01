# 使い方: delegate-google.ps1 <task-file> <output-name>
param([Parameter(Mandatory)][string]$TaskFile, [Parameter(Mandatory)][string]$OutputName)
. (Join-Path $PSScriptRoot 'common.ps1')

if ($OutputName -notmatch '^[A-Za-z0-9_-]+$') { Write-Host '出力名は英数字・_・- のみ'; exit 1 }
if (-not (Test-Path $TaskFile)) { Write-Host "依頼ファイルがありません: $TaskFile"; exit 1 }
$full = (Resolve-Path $TaskFile).Path
if (-not $full.StartsWith($Root, [StringComparison]::OrdinalIgnoreCase)) { Write-Host 'ワークスペース外のファイルは使えません'; exit 1 }

# 呼び出し回数の上限
$cf = Join-Path $Root 'state\google_calls.txt'
New-Item -ItemType Directory -Force -Path (Split-Path $cf) | Out-Null
$n = 0; if (Test-Path $cf) { $n = [int](Get-Content $cf -Raw) }
if ($n -ge [int]$Config.max_google_calls) { Write-Host "委任回数の上限($($Config.max_google_calls)回)に達しました"; exit 2 }

$backend = Get-GoogleBackend
if (-not $backend) { Write-Host 'agy / gemini がありません'; exit 20 }
$exe = Find-Cli $backend

$suffix = @"

---
【必ず守ること】
- 事実と推測を分けて書く。
- 事実にはURLと確認日を付ける。
- 確認できなかった事項を別に一覧する。
- 情報同士の矛盾候補があれば挙げる。
- 外部操作(送信・投稿・購入・公開・ログイン)は一切しない。
- パソコン内のファイルを変更・削除しない。調査と回答のみ。
"@
$prompt = (Get-Content $full -Raw -Encoding UTF8) + $suffix

$cliArgs = @('-p', $prompt, '--output-format', 'json')
if ($Config.google_model -ne 'auto') { $cliArgs += @('--model', [string]$Config.google_model) }

Set-Content $cf ($n + 1) -Encoding ASCII
Write-Log "delegate-google backend=$backend output=$OutputName call=$($n+1)"
$r = Invoke-Cli $exe $cliArgs ([int]$Config.max_runtime_minutes * 60 / 3)

$outDir = Join-Path $Root 'results\google'
New-Item -ItemType Directory -Force -Path $outDir | Out-Null
$jsonPath = Join-Path $outDir "$OutputName.json"
$mdPath = Join-Path $outDir "$OutputName.md"
Set-Content $jsonPath $r.Output -Encoding UTF8

if ($r.ExitCode -eq 124) { Write-Host 'タイムアウト'; exit 124 }
if (Test-AuthError $r.Output) { Write-Host 'Google側のログインが必要です (NEEDS_LOGIN.md)'; exit 10 }
if ($r.ExitCode -ne 0) { Write-Host "Google側がエラー終了 ($($r.ExitCode))"; exit 1 }

# JSONの形の違いを吸収して本文を取り出す
$text = $null
try {
    $obj = $r.Output | ConvertFrom-Json
    foreach ($k in 'response', 'result', 'text', 'output', 'content') {
        if ($obj.PSObject.Properties.Name -contains $k -and $obj.$k) { $text = [string]$obj.$k; break }
    }
} catch { $text = $r.Output }
if ([string]::IsNullOrWhiteSpace($text)) { Write-Host '空の回答でした'; exit 1 }
Set-Content $mdPath $text -Encoding UTF8
Write-Host "保存しました: $mdPath"; exit 0
