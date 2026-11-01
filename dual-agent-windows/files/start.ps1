# デスクトップの「AI共同作業」から起動されます。
$Host.UI.RawUI.WindowTitle = 'AI共同作業'
Set-Location $PSScriptRoot
Write-Host '=== AI共同作業 (Claudeが責任者、Google AIが調査担当) ==='
Write-Host '依頼内容を入力して Enter を押してください。何も入れずに Enter で終了します。'
$req = Read-Host '依頼'
if ([string]::IsNullOrWhiteSpace($req)) { exit 0 }
& "$PSScriptRoot\run-task.ps1" $req
Write-Host ''
if (Test-Path "$PSScriptRoot\final") { Start-Process explorer.exe "$PSScriptRoot\final" }
Read-Host '終了するには Enter を押してください'
