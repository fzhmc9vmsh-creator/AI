# 共通部品。他のスクリプトから読み込まれます。
$ErrorActionPreference = 'Stop'
$script:Root = Split-Path -Parent $PSScriptRoot
$script:Config = Get-Content (Join-Path $Root 'config.json') -Raw -Encoding UTF8 | ConvertFrom-Json

function Write-Log([string]$Message) {
    $dir = Join-Path $Root 'logs'
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    "$(Get-Date -Format 's') $Message" | Add-Content -Path (Join-Path $dir 'dual-agent.log') -Encoding UTF8
}

function Find-Cli([string]$Name) {
    $c = Get-Command $Name -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($c) { return $c.Source }
    return $null
}

function Get-GoogleBackend {
    $pref = $Config.google_backend
    if ($pref -ne 'gemini' -and (Find-Cli 'agy')) { return 'agy' }
    if ($pref -ne 'agy' -and (Find-Cli 'gemini')) { return 'gemini' }
    return $null
}

# CLIを時間制限つきで実行する。戻り値: ExitCode, Output
function Invoke-Cli([string]$Exe, [string[]]$CliArgs, [int]$TimeoutSec) {
    $job = Start-Job -ScriptBlock {
        param($e, $a, $wd)
        Set-Location $wd
        $out = & $e @a 2>&1 | Out-String
        [pscustomobject]@{ Code = $LASTEXITCODE; Out = $out }
    } -ArgumentList $Exe, $CliArgs, $Root
    if (-not (Wait-Job $job -Timeout $TimeoutSec)) {
        Stop-Job $job; Remove-Job $job -Force
        return [pscustomobject]@{ ExitCode = 124; Output = 'TIMEOUT' }
    }
    $r = Receive-Job $job; Remove-Job $job -Force
    return [pscustomobject]@{ ExitCode = [int]$r.Code; Output = [string]$r.Out }
}

function Test-AuthError([string]$Text) {
    return ($Text -match '(?i)(not logged in|please log ?in|login required|unauthori[sz]ed|authenticate|sign in|/login|401)')
}
