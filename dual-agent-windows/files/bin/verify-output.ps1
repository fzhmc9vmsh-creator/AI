# 使い方: verify-output.ps1 <file>  ファイルが存在し空でないことを確認する(読み取りのみ)
param([Parameter(Mandatory)][string]$Path)
if (-not (Test-Path $Path)) { Write-Host "NG: ありません $Path"; exit 1 }
$len = (Get-Item $Path).Length
if ($len -le 0) { Write-Host "NG: 空です $Path"; exit 1 }
Write-Host "OK: $Path ($len バイト)"; exit 0
