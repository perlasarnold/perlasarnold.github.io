[CmdletBinding()]
param(
    [string]$InstallRoot = 'C:\llama-cpp',
    [int]$Port = 8123,
    [switch]$SkipScheduledTask
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$script:ProgressSteps = @(
    'Bootstrap checks',
    'Install Claude Code',
    'Detect hardware',
    'Choose model',
    'Download and install llama.cpp',
    'Create launch script',
    'Update Claude settings',
    'Validate Claude settings',
    'Register scheduled task',
    'Finish'
)
$script:CurrentProgressStep = 0

function Write-Section {
    param([string]$Message)
    Write-Host ''
    Write-Host "== $Message ==" -ForegroundColor Cyan
}

function Start-Step {
    param(
        [string]$Message,
        [string]$Status = 'In progress'
    )

    $stepIndex = [Array]::IndexOf($script:ProgressSteps, $Message)
    if ($stepIndex -ge 0) {
        $script:CurrentProgressStep = $stepIndex + 1
    }
    else {
        $script:CurrentProgressStep++
    }

    $percent = [math]::Min([math]::Round(($script:CurrentProgressStep / $script:ProgressSteps.Count) * 100), 99)
    Write-Progress -Id 1 -Activity 'Setup Llama.cpp + Claude Code' -Status $Status -CurrentOperation $Message -PercentComplete $percent
    Write-Section $Message
}

function Update-StepStatus {
    param([string]$Status)

    $current = if ($script:CurrentProgressStep -gt 0 -and $script:CurrentProgressStep -le $script:ProgressSteps.Count) {
        $script:ProgressSteps[$script:CurrentProgressStep - 1]
    }
    else {
        'Working'
    }

    $percent = [math]::Min([math]::Round(($script:CurrentProgressStep / $script:ProgressSteps.Count) * 100), 99)
    Write-Progress -Id 1 -Activity 'Setup Llama.cpp + Claude Code' -Status $Status -CurrentOperation $current -PercentComplete $percent
}

function Complete-Progress {
    Write-Progress -Id 1 -Activity 'Setup Llama.cpp + Claude Code' -Status 'Completed' -CurrentOperation 'Done' -PercentComplete 100 -Completed
}

function Test-IsAdministrator {
    $identity = [Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object Security.Principal.WindowsPrincipal($identity)
    return $principal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function ConvertTo-Hashtable {
    param([Parameter(ValueFromPipeline = $true)]$InputObject)

    if ($null -eq $InputObject) {
        return $null
    }

    if ($InputObject -is [System.Collections.IDictionary]) {
        $result = @{}
        foreach ($key in $InputObject.Keys) {
            $result[$key] = ConvertTo-Hashtable $InputObject[$key]
        }
        return $result
    }

    if ($InputObject -is [System.Collections.IEnumerable] -and -not ($InputObject -is [string])) {
        $list = @()
        foreach ($item in $InputObject) {
            $list += ConvertTo-Hashtable $item
        }
        return $list
    }

    if ($InputObject.PSObject.Properties.Count -gt 0) {
        $result = @{}
        foreach ($prop in $InputObject.PSObject.Properties) {
            $result[$prop.Name] = ConvertTo-Hashtable $prop.Value
        }
        return $result
    }

    return $InputObject
}

function Get-TotalMemoryGiB {
    try {
        return [math]::Round(([Microsoft.VisualBasic.Devices.ComputerInfo]::new().TotalPhysicalMemory / 1GB), 1)
    }
    catch {
        try {
            $computerInfo = Get-ComputerInfo
            if ($computerInfo.CsTotalPhysicalMemory) {
                return [math]::Round(($computerInfo.CsTotalPhysicalMemory / 1GB), 1)
            }
        }
        catch {
        }
    }

    throw 'Unable to detect total system memory.'
}

function Get-NvidiaGpuInfo {
    $nvidiaSmi = Get-Command 'nvidia-smi.exe' -ErrorAction SilentlyContinue
    if (-not $nvidiaSmi) {
        return $null
    }

    try {
        $raw = & $nvidiaSmi.Source --query-gpu=name,memory.total --format=csv,noheader,nounits 2>$null
        if (-not $raw) {
            return $null
        }

        $first = ($raw | Select-Object -First 1).Trim()
        $parts = $first -split ','
        if ($parts.Count -lt 2) {
            return $null
        }

        return [pscustomobject]@{
            Name     = $parts[0].Trim()
            MemoryGiB = [math]::Round(([double]$parts[1].Trim() / 1024), 1)
        }
    }
    catch {
        return $null
    }
}

function Get-HardwareProfile {
    $memoryGiB = Get-TotalMemoryGiB
    $logicalProcessors = [Environment]::ProcessorCount
    $gpu = Get-NvidiaGpuInfo

    [pscustomobject]@{
        MemoryGiB          = $memoryGiB
        LogicalProcessors  = $logicalProcessors
        NvidiaGpu          = $gpu
        RecommendedThreads = [math]::Max([math]::Min($logicalProcessors - 2, 12), 2)
    }
}

function Get-ContextSizeForMemory {
    param([double]$MemoryGiB)

    if ($MemoryGiB -ge 24) { return 32768 }
    if ($MemoryGiB -ge 12) { return 24576 }
    if ($MemoryGiB -ge 8) { return 16384 }
    return 8192
}

function Get-ModelCatalog {
    @(
        [pscustomobject]@{
            Rank             = 1
            Name             = 'Qwen2.5-Coder 14B Instruct'
            HuggingFaceRef   = 'bartowski/Qwen2.5-Coder-14B-Instruct-GGUF:Q4_K_M'
            HuggingFaceRepo  = 'bartowski/Qwen2.5-Coder-14B-Instruct-GGUF'
            HuggingFaceFile  = 'Qwen2.5-Coder-14B-Instruct-Q4_K_M.gguf'
            EstimatedRamGiB  = 24
            QualityNote      = 'Best code quality in this list if your box has the RAM for it.'
        }
        [pscustomobject]@{
            Rank             = 2
            Name             = 'Qwen2.5-Coder 7B Instruct'
            HuggingFaceRef   = 'bartowski/Qwen2.5-Coder-7B-Instruct-GGUF:Q4_K_M'
            HuggingFaceRepo  = 'bartowski/Qwen2.5-Coder-7B-Instruct-GGUF'
            HuggingFaceFile  = 'Qwen2.5-Coder-7B-Instruct-Q4_K_M.gguf'
            EstimatedRamGiB  = 12
            QualityNote      = 'Strong default balance of quality, latency, and memory use.'
        }
        [pscustomobject]@{
            Rank             = 3
            Name             = 'Qwen2.5-Coder 3B Instruct'
            HuggingFaceRef   = 'bartowski/Qwen2.5-Coder-3B-Instruct-GGUF:Q4_K_M'
            HuggingFaceRepo  = 'bartowski/Qwen2.5-Coder-3B-Instruct-GGUF'
            HuggingFaceFile  = 'Qwen2.5-Coder-3B-Instruct-Q4_K_M.gguf'
            EstimatedRamGiB  = 6
            QualityNote      = 'Safer choice for smaller systems or background use.'
        }
        [pscustomobject]@{
            Rank             = 4
            Name             = 'Qwen2.5-Coder 1.5B Instruct'
            HuggingFaceRef   = 'bartowski/Qwen2.5-Coder-1.5B-Instruct-GGUF:Q4_K_M'
            HuggingFaceRepo  = 'bartowski/Qwen2.5-Coder-1.5B-Instruct-GGUF'
            HuggingFaceFile  = 'Qwen2.5-Coder-1.5B-Instruct-Q4_K_M.gguf'
            EstimatedRamGiB  = 3
            QualityNote      = 'Fastest option, but the weakest for harder coding tasks.'
        }
    )
}

function Get-RankedModelOptions {
    param([double]$MemoryGiB)

    $catalog = Get-ModelCatalog
    $viable = $catalog | Where-Object { $_.EstimatedRamGiB -le ($MemoryGiB * 0.8) }
    if (-not $viable) {
        $viable = $catalog | Select-Object -Last 1
    }

    return $viable
}

function Select-Model {
    param(
        [double]$MemoryGiB,
        [int]$LogicalProcessors,
        $NvidiaGpu
    )

    $options = Get-RankedModelOptions -MemoryGiB $MemoryGiB

    Write-Section 'Detected hardware'
    Write-Host ("RAM: {0} GiB" -f $MemoryGiB)
    Write-Host ("Logical processors: {0}" -f $LogicalProcessors)
    if ($NvidiaGpu) {
        Write-Host ("NVIDIA GPU: {0} ({1} GiB VRAM)" -f $NvidiaGpu.Name, $NvidiaGpu.MemoryGiB)
    }
    else {
        Write-Host 'NVIDIA GPU: not detected'
    }

    Write-Section 'Ranked model options for this system'
    for ($i = 0; $i -lt $options.Count; $i++) {
        $option = $options[$i]
        $label = if ($i -eq 0) { 'Recommended' } else { 'Supported' }
        Write-Host ("[{0}] {1} - est. {2} GiB RAM - {3} - {4}" -f ($i + 1), $option.Name, $option.EstimatedRamGiB, $label, $option.QualityNote)
    }

    $defaultSelection = 1
    $selection = Read-Host ("Choose a model [default {0}]" -f $defaultSelection)
    if ([string]::IsNullOrWhiteSpace($selection)) {
        $selection = $defaultSelection
    }

    $index = 0
    if (-not [int]::TryParse($selection, [ref]$index)) {
        throw 'Model selection must be a number.'
    }

    if ($index -lt 1 -or $index -gt $options.Count) {
        throw 'Model selection is out of range.'
    }

    return $options[$index - 1]
}

function Get-GitHubHeaders {
    @{
        'User-Agent' = 'homelab-llama-cpp-bootstrap'
        'Accept'     = 'application/vnd.github+json'
    }
}

function Refresh-ProcessPath {
    $machinePath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
    $userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
    $env:Path = @($machinePath, $userPath) -join ';'
}

function Ensure-ClaudeCodeInstalled {
    $existing = Get-Command 'claude' -ErrorAction SilentlyContinue
    if ($existing) {
        Update-StepStatus 'Claude Code already installed'
        Write-Host ("Claude Code already available at: {0}" -f $existing.Source)
        return $existing.Source
    }

    Update-StepStatus 'Running Anthropic installer'
    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

    try {
        & ([scriptblock]::Create((Invoke-RestMethod -Uri 'https://claude.ai/install.ps1')))
    }
    catch {
        throw "Claude Code install failed via Anthropic's official Windows installer: $($_.Exception.Message)"
    }

    Refresh-ProcessPath
    Update-StepStatus 'Verifying Claude Code command'
    $installed = Get-Command 'claude' -ErrorAction SilentlyContinue
    if (-not $installed) {
        throw 'Claude Code installation finished, but the `claude` command is still not on PATH in this session.'
    }

    Write-Host ("Claude Code installed at: {0}" -f $installed.Source)
    return $installed.Source
}

function Get-LlamaCppReleaseAsset {
    param($HardwareProfile)

    [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

    $release = Invoke-RestMethod -Uri 'https://api.github.com/repos/ggml-org/llama.cpp/releases/latest' -Headers (Get-GitHubHeaders)
    $assets = @($release.assets)
    if (-not $assets) {
        throw 'No downloadable assets were returned from the llama.cpp release API.'
    }

    $cpuAsset = $assets | Where-Object { $_.name -match 'win-cpu-x64\.zip$' } | Select-Object -First 1
    $cudaAsset = $assets | Where-Object { $_.name -match 'win-cuda-[0-9.]+-x64\.zip$' } | Sort-Object name -Descending | Select-Object -First 1

    if ($HardwareProfile.NvidiaGpu -and $cudaAsset) {
        return [pscustomobject]@{
            Flavor = 'cuda'
            Asset  = $cudaAsset
            Reason = 'NVIDIA GPU detected, so a CUDA build was selected.'
        }
    }

    if (-not $cpuAsset) {
        throw 'Could not find a Windows x64 CPU asset in the latest llama.cpp release.'
    }

    return [pscustomobject]@{
        Flavor = 'cpu'
        Asset  = $cpuAsset
        Reason = 'No NVIDIA GPU was detected, so a CPU build was selected.'
    }
}

function Install-LlamaCpp {
    param(
        [string]$Destination,
        $HardwareProfile
    )

    $assetInfo = Get-LlamaCppReleaseAsset -HardwareProfile $HardwareProfile

    Update-StepStatus 'Resolving latest llama.cpp release'
    Write-Host $assetInfo.Reason
    Write-Host ("Asset: {0}" -f $assetInfo.Asset.name)

    $tempRoot = Join-Path $env:TEMP ('llama-cpp-' + [guid]::NewGuid().ToString('n'))
    $zipPath = Join-Path $tempRoot $assetInfo.Asset.name
    $extractPath = Join-Path $tempRoot 'extract'

    New-Item -ItemType Directory -Path $tempRoot -Force | Out-Null
    Update-StepStatus 'Downloading llama.cpp archive'
    Invoke-WebRequest -Uri $assetInfo.Asset.browser_download_url -Headers (Get-GitHubHeaders) -OutFile $zipPath

    if (Test-Path $Destination) {
        Write-Host ("Clearing previous install at {0}" -f $Destination)
        Remove-Item -LiteralPath $Destination -Recurse -Force
    }

    New-Item -ItemType Directory -Path $Destination -Force | Out-Null
    Update-StepStatus 'Extracting llama.cpp files'
    Expand-Archive -Path $zipPath -DestinationPath $extractPath -Force

    $serverExe = Get-ChildItem -Path $extractPath -Filter 'llama-server.exe' -Recurse | Select-Object -First 1
    if (-not $serverExe) {
        throw 'llama-server.exe was not found in the downloaded archive.'
    }

    Copy-Item -Path (Join-Path $serverExe.Directory.FullName '*') -Destination $Destination -Recurse -Force
    Update-StepStatus 'Finalizing llama.cpp install'

    Remove-Item -LiteralPath $tempRoot -Recurse -Force
    return $assetInfo
}

function New-LaunchScriptContent {
    param(
        [string]$InstallRoot,
        [int]$Port,
        [string]$ModelRepo,
        [string]$ModelFile,
        [int]$Threads,
        [int]$ContextSize,
        [string]$Alias,
        [string]$BuildFlavor
    )

    $gpuLine = if ($BuildFlavor -eq 'cuda') { "  -ngl 99 ``" } else { $null }

    $lines = @(
        '$env:ANTHROPIC_BASE_URL = "http://127.0.0.1:' + $Port + '"'
        '$env:ANTHROPIC_API_KEY = "sk-local-key"'
        '$env:CLAUDE_CODE_MODEL = "' + $Alias + '"'
        '$env:CLAUDE_CODE_TIMEOUT = "300000"'
        ''
        '& "' + (Join-Path $InstallRoot 'llama-server.exe') + '" `'
        '  -hf ' + $ModelRepo + ' `'
        '  -hff ' + $ModelFile + ' `'
        '  -t ' + $Threads + ' -c ' + $ContextSize + ' --port ' + $Port + ' `'
    )

    if ($gpuLine) {
        $lines += $gpuLine
    }

    $lines += '  --alias ' + $Alias
    return ($lines -join [Environment]::NewLine) + [Environment]::NewLine
}

function Write-LaunchScript {
    param(
        [string]$InstallRoot,
        [int]$Port,
        $Model,
        $HardwareProfile,
        [string]$BuildFlavor
    )

    $launchPath = Join-Path $InstallRoot 'Launch-Llama.ps1'
    $contextSize = Get-ContextSizeForMemory -MemoryGiB $HardwareProfile.MemoryGiB
    $alias = 'claude-3-5-sonnet-20241022'
    $content = New-LaunchScriptContent `
        -InstallRoot $InstallRoot `
        -Port $Port `
        -ModelRepo $Model.HuggingFaceRepo `
        -ModelFile $Model.HuggingFaceFile `
        -Threads $HardwareProfile.RecommendedThreads `
        -ContextSize $contextSize `
        -Alias $alias `
        -BuildFlavor $BuildFlavor

    Set-Content -LiteralPath $launchPath -Value $content -Encoding UTF8
    return [pscustomobject]@{
        Path        = $launchPath
        Alias       = $alias
        ContextSize = $contextSize
    }
}

function Update-ClaudeSettings {
    param(
        [int]$Port,
        [string]$ModelAlias
    )

    $claudeDir = Join-Path $HOME '.claude'
    $settingsPath = Join-Path $claudeDir 'settings.json'
    New-Item -ItemType Directory -Path $claudeDir -Force | Out-Null

    $settings = @{}
    if (Test-Path $settingsPath) {
        $timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
        Copy-Item -LiteralPath $settingsPath -Destination ($settingsPath + '.' + $timestamp + '.bak') -Force

        $raw = Get-Content -LiteralPath $settingsPath -Raw
        if (-not [string]::IsNullOrWhiteSpace($raw)) {
            $settings = ConvertTo-Hashtable (ConvertFrom-Json -InputObject $raw)
        }
    }

    if (-not $settings.ContainsKey('env') -or -not ($settings.env -is [hashtable])) {
        $settings['env'] = @{}
    }

    $settings.env['ANTHROPIC_BASE_URL'] = "http://127.0.0.1:$Port"
    $settings.env['ANTHROPIC_API_KEY'] = 'sk-local-key'
    $settings.env['CLAUDE_CODE_MODEL'] = $ModelAlias
    $settings.env['CLAUDE_CODE_ATTRIBUTION_HEADER'] = '0'
    $settings.env['CLAUDE_CODE_TIMEOUT'] = '300000'

    $json = $settings | ConvertTo-Json -Depth 10
    Set-Content -LiteralPath $settingsPath -Value $json -Encoding UTF8
    return $settingsPath
}

function Assert-ClaudeSettings {
    param(
        [string]$SettingsPath,
        [int]$Port,
        [string]$ModelAlias
    )

    if (-not (Test-Path $SettingsPath)) {
        throw "Claude settings file was not created: $SettingsPath"
    }

    $settings = ConvertTo-Hashtable (Get-Content -LiteralPath $SettingsPath -Raw | ConvertFrom-Json)
    if (-not $settings.ContainsKey('env')) {
        throw 'Claude settings validation failed: missing env object.'
    }

    $expected = @{
        ANTHROPIC_BASE_URL = "http://127.0.0.1:$Port"
        ANTHROPIC_API_KEY = 'sk-local-key'
        CLAUDE_CODE_MODEL = $ModelAlias
        CLAUDE_CODE_ATTRIBUTION_HEADER = '0'
        CLAUDE_CODE_TIMEOUT = '300000'
    }

    foreach ($key in $expected.Keys) {
        if (-not $settings.env.ContainsKey($key)) {
            throw "Claude settings validation failed: missing env.$key"
        }

        if ([string]$settings.env[$key] -ne [string]$expected[$key]) {
            throw "Claude settings validation failed: env.$key expected '$($expected[$key])' but found '$($settings.env[$key])'"
        }
    }

    Write-Host ("Claude settings validated successfully in: {0}" -f $SettingsPath)
}

function Register-LlamaTask {
    param([string]$LaunchScriptPath)

    $taskName = 'LlamaCpp Claude Code'
    $currentUser = '{0}\{1}' -f $env:USERDOMAIN, $env:USERNAME
    $action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument ('-NoProfile -ExecutionPolicy Bypass -WindowStyle Minimized -File "{0}"' -f $LaunchScriptPath)
    $trigger = New-ScheduledTaskTrigger -AtLogOn -User $currentUser
    $settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
    $principal = New-ScheduledTaskPrincipal -UserId $currentUser -LogonType Interactive -RunLevel Highest

    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Force | Out-Null
    return $taskName
}

Start-Step 'Bootstrap checks' 'Preparing setup'
if (-not (Test-IsAdministrator)) {
    throw "Run this script from an elevated PowerShell session because it installs into $InstallRoot and registers a startup task."
}

Start-Step 'Install Claude Code' 'Checking Claude Code installation'
$claudePath = Ensure-ClaudeCodeInstalled

Start-Step 'Detect hardware' 'Inspecting system resources'
$hardwareProfile = Get-HardwareProfile

Start-Step 'Choose model' 'Waiting for model selection'
$selectedModel = Select-Model -MemoryGiB $hardwareProfile.MemoryGiB -LogicalProcessors $hardwareProfile.LogicalProcessors -NvidiaGpu $hardwareProfile.NvidiaGpu

Start-Step 'Download and install llama.cpp' 'Preparing llama.cpp install'
$installResult = Install-LlamaCpp -Destination $InstallRoot -HardwareProfile $hardwareProfile

Start-Step 'Create launch script' 'Writing Launch-Llama.ps1'
$launchScript = Write-LaunchScript -InstallRoot $InstallRoot -Port $Port -Model $selectedModel -HardwareProfile $hardwareProfile -BuildFlavor $installResult.Flavor

Start-Step 'Update Claude settings' 'Writing settings.json'
$settingsPath = Update-ClaudeSettings -Port $Port -ModelAlias $launchScript.Alias

Start-Step 'Validate Claude settings' 'Reading settings.json back'
Assert-ClaudeSettings -SettingsPath $settingsPath -Port $Port -ModelAlias $launchScript.Alias

$taskName = $null
if (-not $SkipScheduledTask) {
    Start-Step 'Register scheduled task' 'Creating Windows logon task'
    $taskName = Register-LlamaTask -LaunchScriptPath $launchScript.Path
}

Start-Step 'Finish' 'Wrapping up'
Write-Host ("Installed llama.cpp to: {0}" -f $InstallRoot)
Write-Host ("Launch script: {0}" -f $launchScript.Path)
Write-Host ("Claude settings updated: {0}" -f $settingsPath)
Write-Host ("Claude executable: {0}" -f $claudePath)
Write-Host ("Model: {0}" -f $selectedModel.Name)
Write-Host ("Model reference: {0}" -f $selectedModel.HuggingFaceRef)
Write-Host ("Context size: {0}" -f $launchScript.ContextSize)

if ($taskName) {
    Write-Host ("Scheduled task created: {0}" -f $taskName)
}

Write-Host ''
Write-Host 'Next run:'
Write-Host ("1. Start the server now with: {0}" -f $launchScript.Path)
Write-Host '2. Open a new terminal and run: claude'
Write-Host '3. Accept the environment API key prompt if shown.'
Write-Host '4. Inside Claude Code, run: /reset'
Complete-Progress
