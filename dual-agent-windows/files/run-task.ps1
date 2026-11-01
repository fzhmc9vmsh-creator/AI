# 使い方: run-task.ps1 "依頼内容"
param([Parameter(Mandatory, ValueFromRemainingArguments)][string[]]$Request)
. (Join-Path $PSScriptRoot 'bin\common.ps1')
$text = $Request -join ' '
$stateDir = Join-Path $Root 'state'
foreach ($d in 'tasks', 'workspace', 'final', 'results\google', 'logs', 'state') {
    New-Item -ItemType Directory -Force -Path (Join-Path $Root $d) | Out-Null
}

& (Join-Path $Root 'bin\check-environment.ps1')
if ($LASTEXITCODE -ne 0) { Write-Host "環境確認でNG(コード $LASTEXITCODE)。NEEDS_*.md を見てください。"; exit $LASTEXITCODE }

Set-Content (Join-Path $Root 'tasks\current.md') $text -Encoding UTF8
Set-Content (Join-Path $stateDir 'google_calls.txt') 0 -Encoding ASCII
$start = Get-Date
@{ status = 'running'; started = $start.ToString('s'); request = $text } | ConvertTo-Json |
    Set-Content (Join-Path $stateDir 'status.json') -Encoding UTF8

$prompt = @"
あなたは主任です。CLAUDE.md の指示に従い、tasks/current.md の依頼を実行してください。
1. 計画を workspace/plan.md に保存する。
2. 大量調査・長文処理・反論レビューは、Google側に最大$($Config.max_google_calls)回まで委任する。
   委任の方法: tasks/ に依頼ファイルを書き、次を実行する。
   powershell -NoProfile -ExecutionPolicy Bypass -File ./bin/delegate-google.ps1 tasks/<依頼ファイル>.md <出力名>
   結果は results/google/<出力名>.md に入る。
3. 結果を自分で検証し、最終成果物を final/ に保存する。
4. workspace/completion-report.md に、成果物・検証内容・委任回数・未確認事項を書く。
"@

$allowed = @(
    'Read', 'Write', 'Edit', 'Glob', 'Grep',
    'Bash(powershell -NoProfile -ExecutionPolicy Bypass -File ./bin/delegate-google.ps1 *)',
    'Bash(powershell -NoProfile -ExecutionPolicy Bypass -File ./bin/verify-output.ps1 *)',
    'Bash(dir *)', 'Bash(type *)'
)
$denied = @('WebFetch', 'Bash(rm *)', 'Bash(del *)', 'Bash(rmdir *)', 'Bash(Remove-Item *)', 'Bash(git push *)', 'Bash(curl *)', 'Bash(Invoke-WebRequest *)')

$claude = Find-Cli 'claude'
$cliArgs = @('-p', $prompt, '--model', [string]$Config.claude_model, '--permission-mode', 'default',
    '--allowedTools', ($allowed -join ','), '--disallowedTools', ($denied -join ','))
$r = Invoke-Cli $claude $cliArgs ([int]$Config.max_runtime_minutes * 60)
Set-Content (Join-Path $Root 'logs\last-claude-output.txt') $r.Output -Encoding UTF8

$calls = 0; $cf = Join-Path $stateDir 'google_calls.txt'; if (Test-Path $cf) { $calls = [int](Get-Content $cf -Raw) }
$ok = ($r.ExitCode -eq 0) -and (Get-ChildItem (Join-Path $Root 'final') -File -ErrorAction SilentlyContinue | Where-Object Length -gt 0)
@{ status = $(if ($ok) { 'done' } else { 'failed' }); finished = (Get-Date).ToString('s'); google_calls = $calls; exit_code = $r.ExitCode } |
    ConvertTo-Json | Set-Content (Join-Path $stateDir 'status.json') -Encoding UTF8

Write-Host ''
Write-Host $(if ($ok) { "完了。成果物: $(Join-Path $Root 'final')" } else { '失敗または成果物なし。logs\last-claude-output.txt を見てください。' })
if ($ok) { exit 0 } else { exit 1 }
