param(
    [int]$LookbackDays = 7,
    [int]$MaxItemsPerSource = 20,
    [string]$PostsRoot,
    [string]$DigestArchiveRoot
)

$ErrorActionPreference = 'Stop'

function Ensure-Directory {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        New-Item -ItemType Directory -Path $Path -Force | Out-Null
    }
}

function truncate {
    param(
        [string]$text,
        [int]$length
    )
    if ($null -eq $text) { return "" }
    if ($text.Length -le $length) { return $text }
    return $text.Substring(0, $length).Trim() + "..."
}

function Write-Utf8File {
    param(
        [string]$Path,
        [string]$Content
    )

    Ensure-Directory -Path (Split-Path -Parent $Path)
    Set-Content -LiteralPath $Path -Value $Content -Encoding utf8
}

function Get-WebContent {
    param([string]$Url)

    $headers = @{
        'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

    return Invoke-WebRequest -Uri $Url -Headers $headers -UseBasicParsing -TimeoutSec 45
}

function Get-DateValue {
    param($Value)

    if ($null -eq $Value -or [string]::IsNullOrWhiteSpace([string]$Value)) {
        return $null
    }

    try {
        return [datetimeoffset]$Value
    }
    catch {
        return $null
    }
}

function ConvertTo-Text {
    param([string]$Value)

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return ''
    }

    $text = $Value -replace '<[^>]+>', ' '
    $text = $text -replace '&nbsp;', ' '
    $text = $text -replace '&amp;', '&'
    $text = $text -replace '\s+', ' '
    return $text.Trim()
}

function ConvertTo-Slug {
    param([string]$Value)

    $slug = $Value.ToLowerInvariant()
    $slug = $slug -replace '[^a-z0-9]+', '-'
    $slug = $slug.Trim('-')

    if ([string]::IsNullOrWhiteSpace($slug)) {
        return 'weekly-security-digest'
    }

    return $slug
}

function Escape-FrontMatterValue {
    param([string]$Value)

    if ($null -eq $Value) {
        return ''
    }

    return ($Value -replace '"', '\"')
}

function Get-FeedDefinitions {
    return @(
        [pscustomobject]@{ Name = 'BleepingComputer'; Url = 'https://www.bleepingcomputer.com/feed/'; Format = 'rss' },
        [pscustomobject]@{ Name = 'CybersecurityNews'; Url = 'https://cybersecuritynews.com/feed/'; Format = 'rss' },
        [pscustomobject]@{ Name = 'Neowin'; Url = 'https://www.neowin.net/news/rss/'; Format = 'rss' },
        [pscustomobject]@{ Name = 'The Old New Thing'; Url = 'https://devblogs.microsoft.com/oldnewthing/feed/'; Format = 'rss' },
        [pscustomobject]@{ Name = 'Reddit r/cybersecurity'; Url = 'https://www.reddit.com/r/cybersecurity/new/.rss'; Format = 'atom' },
        [pscustomobject]@{ Name = 'Reddit r/sysadmin'; Url = 'https://www.reddit.com/r/sysadmin/new/.rss'; Format = 'atom' },
        [pscustomobject]@{ Name = 'Reddit r/Windows11'; Url = 'https://www.reddit.com/r/Windows11/new/.rss'; Format = 'atom' },
        [pscustomobject]@{ Name = 'NVD'; Url = 'https://nvd.nist.gov/vuln'; Format = 'nvd-api' },
        [pscustomobject]@{ Name = 'CVE.org'; Url = 'https://cve.org/'; Format = 'cve-derived' }
    )
}

function Get-RssItems {
    param(
        [xml]$Xml,
        [string]$SourceName
    )

    $items = [System.Collections.Generic.List[object]]::new()
    foreach ($node in @($Xml.rss.channel.item)) {
        if ($null -eq $node) {
            continue
        }

        $items.Add([pscustomobject]@{
            Source    = $SourceName
            Title     = [string]$node.title
            Link      = [string]$node.link
            Published = Get-DateValue -Value $node.pubDate
            Summary   = ConvertTo-Text -Value ([string]$node.description)
        })
    }

    return $items
}

function Get-AtomItems {
    param(
        [xml]$Xml,
        [string]$SourceName
    )

    $ns = New-Object System.Xml.XmlNamespaceManager($Xml.NameTable)
    $ns.AddNamespace('a', 'http://www.w3.org/2005/Atom')
    $entries = $Xml.SelectNodes('//a:entry', $ns)
    $items = [System.Collections.Generic.List[object]]::new()

    foreach ($entry in @($entries)) {
        $linkNode = $entry.SelectSingleNode("a:link[@rel='alternate']", $ns)
        if ($null -eq $linkNode) {
            $linkNode = $entry.SelectSingleNode('a:link', $ns)
        }

        $summaryNode = $entry.SelectSingleNode('a:summary', $ns)
        if ($null -eq $summaryNode) {
            $summaryNode = $entry.SelectSingleNode('a:content', $ns)
        }

        $items.Add([pscustomobject]@{
            Source    = $SourceName
            Title     = [string]$entry.SelectSingleNode('a:title', $ns).InnerText
            Link      = [string]$linkNode.Attributes['href'].Value
            Published = Get-DateValue -Value ($entry.SelectSingleNode('a:updated', $ns).InnerText)
            Summary   = ConvertTo-Text -Value ([string]$summaryNode.InnerText)
        })
    }

    return $items
}

function Get-NvdApiItems {
    param(
        [datetimeoffset]$Since,
        [int]$MaxItems
    )

    $start = $Since.ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ss.fffK")
    $end = [datetimeoffset]::UtcNow.ToString("yyyy-MM-ddTHH:mm:ss.fffK")
    $uri = "https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate=$([uri]::EscapeDataString($start))&pubEndDate=$([uri]::EscapeDataString($end))&resultsPerPage=$MaxItems&noRejected"

    $response = Get-WebContent -Url $uri
    $payload = $response.Content | ConvertFrom-Json
    $items = [System.Collections.Generic.List[object]]::new()

    foreach ($entry in @($payload.vulnerabilities)) {
        $cve = $entry.cve
        if ($null -eq $cve) {
            continue
        }

        $description = ''
        foreach ($desc in @($cve.descriptions)) {
            if ($desc.lang -eq 'en' -and -not [string]::IsNullOrWhiteSpace($desc.value)) {
                $description = $desc.value
                break
            }
        }

        $published = Get-DateValue -Value $cve.published
        $cveId = [string]$cve.id
        $items.Add([pscustomobject]@{
            Source    = 'NVD'
            Title     = $cveId
            Link      = "https://nvd.nist.gov/vuln/detail/$cveId"
            Published = $published
            Summary   = ConvertTo-Text -Value $description
            CveId     = $cveId
        })
    }

    return @($items | Sort-Object Published -Descending | Select-Object -First $MaxItems)
}

function ConvertTo-CveOrgItems {
    param(
        [object[]]$Items,
        [int]$MaxItems
    )

    $derived = [System.Collections.Generic.List[object]]::new()
    foreach ($item in @($Items | Select-Object -First $MaxItems)) {
        if ([string]::IsNullOrWhiteSpace($item.CveId)) {
            continue
        }

        $derived.Add([pscustomobject]@{
            Source    = 'CVE.org'
            Title     = $item.CveId
            Link      = "https://www.cve.org/CVERecord?id=$($item.CveId)"
            Published = $item.Published
            Summary   = $item.Summary
            CveId     = $item.CveId
        })
    }

    return @($derived)
}

function Get-FeedData {
    param(
        [pscustomobject]$Definition,
        [datetimeoffset]$Since,
        [int]$MaxItems
    )

    try {
        if ($Definition.Format -eq 'nvd-api') {
            $items = Get-NvdApiItems -Since $Since -MaxItems $MaxItems
        }
        elseif ($Definition.Format -eq 'cve-derived') {
            $nvdItems = Get-NvdApiItems -Since $Since -MaxItems $MaxItems
            $items = ConvertTo-CveOrgItems -Items $nvdItems -MaxItems $MaxItems
        }
        else {
            $response = Get-WebContent -Url $Definition.Url
            [xml]$xml = $response.Content

            if ($Definition.Format -eq 'atom') {
                $items = Get-AtomItems -Xml $xml -SourceName $Definition.Name
            }
            else {
                $items = Get-RssItems -Xml $xml -SourceName $Definition.Name
            }
        }

        $recentItems = @(
            $items |
            Where-Object { $null -ne $_.Published -and $_.Published -ge $Since } |
            Sort-Object Published -Descending |
            Select-Object -First $MaxItems
        )

        return [pscustomobject]@{
            Name    = $Definition.Name
            Status  = 'OK'
            Message = "Collected $($recentItems.Count) recent items"
            Items   = $recentItems
        }
    }
    catch {
        return [pscustomobject]@{
            Name    = $Definition.Name
            Status  = 'Error'
            Message = $_.Exception.Message
            Items   = @()
        }
    }
}

function Get-WatchRules {
    return @(
        [pscustomobject]@{ Name = 'Google Chrome'; Pattern = '(?i)\bchrome\b|\bchromium\b'; Category = 'Tanium'; Action = 'Validate Chrome coverage; update managed package if needed.' },
        [pscustomobject]@{ Name = 'Microsoft Edge'; Pattern = '(?i)\bedge\b|\bwebview2\b'; Category = 'Tanium'; Action = 'Validate Edge/WebView2 coverage; refresh managed package.' },
        [pscustomobject]@{ Name = 'Adobe Acrobat/Reader'; Pattern = '(?i)\badobe\b|\bacrobat\b|\breader\b'; Category = 'Tanium'; Action = 'Confirm Adobe exposure; push updated deployment.' },
        [pscustomobject]@{ Name = 'Microsoft Office / M365'; Pattern = '(?i)\boffice\s*365\b|\bm365\b|\boutlook\b|\bword\b|\bexcel\b|\bpowerpoint\b'; Category = 'Intune'; Action = 'Review Office update channel health and security baseline compliance.' },
        [pscustomobject]@{ Name = 'Windows Server / AD'; Pattern = '(?i)\bwindows\s*server\b|\bactive\s*directory\b|\bhyper-v\b|\bdns\s*server\b'; Category = 'Infrastructure'; Action = 'Review server hardening and AD security posture.' },
        [pscustomobject]@{ Name = 'Windows Workstation'; Pattern = '(?i)\bwindows\s*10\b|\bwindows\s*11\b|\bworkstation\b'; Category = 'Intune'; Action = 'Validate workstation security baseline and update compliance.' },
        [pscustomobject]@{ Name = 'Developer Apps (VSCode, Docker)'; Pattern = '(?i)\bvscode\b|\bvisual\s*studio\b|\bdocker\b|\bkubernetes\b|\bk8s\b|\bgit\b'; Category = 'AppSec'; Action = 'Monitor developer tool vulnerabilities and supply chain risks.' },
        [pscustomobject]@{ Name = '.NET Framework / Core'; Pattern = '(?i)\b\.net\b|\bdotnet\b|\basp\.net\b'; Category = 'AppSec'; Action = 'Review .NET runtime vulnerabilities and apply patches.' },
        [pscustomobject]@{ Name = 'Palo Alto GlobalProtect'; Pattern = '(?i)\bglobalprotect\b|\bpalo alto\b|\bprisma\b'; Category = 'Infrastructure'; Action = 'Review VPN client version and deployment.' },
        [pscustomobject]@{ Name = 'CrowdStrike'; Pattern = '(?i)\bcrowdstrike\b|\bfalcon\b'; Category = 'Security Ops'; Action = 'Review sensor guidance and deployment posture.' },
        [pscustomobject]@{ Name = 'Qualys'; Pattern = '(?i)\bqualys\b'; Category = 'Security Ops'; Action = 'Validate Cloud Agent release and health.' },
        [pscustomobject]@{ Name = 'BitLocker'; Pattern = '(?i)\bbitlocker\b'; Category = 'Intune'; Action = 'Review encryption policy and remediation gaps.' },
        [pscustomobject]@{ Name = 'LAPS'; Pattern = '(?i)\blaps\b|\blocal\s*admin\s*password\b'; Category = 'Intune'; Action = 'Validate LAPS scope and rotation posture.' },
        [pscustomobject]@{ Name = 'Conditional Access / MFA'; Pattern = '(?i)\bconditional\s*access\b|\bmfa\b|\bauthentication\s*strength\b'; Category = 'Security Ops'; Action = 'Review CA/MFA settings for tightening opportunities.' },
        [pscustomobject]@{ Name = 'Defender / Security Baselines'; Pattern = '(?i)\bdefender\b|\bantivirus\b|\bfirewall\b|\basr\b|\battack\s*surface\s*reduction\b'; Category = 'Intune'; Action = 'Review security controls and policy updates.' },
        [pscustomobject]@{ Name = 'Windows Update / Autopatch'; Pattern = '(?i)\bpatch\s*tuesday\b|\bwindows\s*update\b|\bautopatch\b|\bcumulative\s*update\b|\bout-of-band\b'; Category = 'Intune'; Action = 'Evaluate update rings and expedite actions if needed.' }
    )
}

function Get-MatchedRules {
    param(
        [string]$Text,
        [object[]]$Rules
    )

    $matchedRules = New-Object System.Collections.ArrayList
    foreach ($rule in $Rules) {
        if ($Text -match $rule.Pattern) {
            [void]$matchedRules.Add($rule)
        }
    }
    return @($matchedRules)
}

function Format-DateLine {
    param([datetimeoffset]$Value)

    if ($null -eq $Value) {
        return 'Unknown publish time'
    }

    return $Value.ToString('yyyy-MM-dd HH:mm:ss zzz')
}

function Get-PatchTuesdayExperienceItems {
    param(
        [object[]]$Items,
        [int]$MaxItems = 10
    )

    $patchTuesdayPattern = '(?i)\bpatch tuesday\b|\bwindows update\b|\bcumulative update\b|\bout-of-band\b|\bkb\d{6,7}\b'
    $experiencePattern = '(?i)\bissue\b|\bproblem\b|\bbroken\b|\bbug\b|\bbsod\b|\bblue screen\b|\bcrash\b|\breboot\b|\bslow\b|\bperformance\b|\bbitlocker\b|\brecovery\b|\bremote desktop\b|\bsign-in\b|\bprinting\b|\binstall fails\b|\bfailed\b'

    $candidates = @(
        $Items |
        Where-Object {
            $text = "$($_.Title) $($_.Summary)"
            ($text -match $patchTuesdayPattern) -and ($text -match $experiencePattern)
        } |
        Sort-Object Published -Descending
    )

    $ranked = foreach ($item in $candidates) {
        $text = "$($item.Title) $($item.Summary)"
        $score = 1
        if ($text -match '(?i)\bbitlocker\b|\brecovery\b') { $score += 3 }
        if ($text -match '(?i)\bbsod\b|\bblue screen\b|\bcrash\b') { $score += 2 }
        if ($text -match '(?i)\bremote desktop\b|\bsign-in\b|\bprinting\b') { $score += 2 }
        if ($item.Source -match 'Reddit r/sysadmin|Reddit r/Windows11|Neowin|BleepingComputer') { $score += 1 }

        [pscustomobject]@{
            Title     = $item.Title
            Link      = $item.Link
            Source    = $item.Source
            Published = $item.Published
            Summary   = $item.Summary
            Score     = $score
        }
    }

    return @(
        $ranked |
        Sort-Object -Property @{ Expression = 'Score'; Descending = $true }, @{ Expression = 'Published'; Descending = $true } |
        Group-Object Title |
        ForEach-Object { $_.Group | Select-Object -First 1 } |
        Select-Object -First $MaxItems
    )
}

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
if (-not $PostsRoot) {
    $PostsRoot = Join-Path $repoRoot '_posts'
}
if (-not $DigestArchiveRoot) {
    $DigestArchiveRoot = Join-Path $repoRoot 'blog-digest'
}

$nowUtc = [datetimeoffset]::UtcNow
$runDate = $nowUtc.ToString('yyyy-MM-dd')
$timestamp = $nowUtc.ToString('yyyy-MM-dd_HH-mm-ssZ')
$title = "Security Digest - $($nowUtc.ToString('MMMM d, yyyy'))"
$slug = ConvertTo-Slug -Value $title
$postFileName = "$runDate-$slug.md"
$postPath = Join-Path $PostsRoot $postFileName
$historicalFileName = "weekly-digest-$timestamp.md"
$historicalPath = Join-Path $DigestArchiveRoot $historicalFileName
$latestPath = Join-Path $DigestArchiveRoot 'latest-weekly-digest.md'
$indexPath = Join-Path $DigestArchiveRoot 'index.md'
$since = $nowUtc.AddDays(-1 * $LookbackDays)

Ensure-Directory -Path $PostsRoot
Ensure-Directory -Path $DigestArchiveRoot

$feedResults = foreach ($definition in (Get-FeedDefinitions)) {
    Get-FeedData -Definition $definition -Since $since -MaxItems $MaxItemsPerSource
}

$allItems = @($feedResults | ForEach-Object { $_.Items } | Where-Object { $null -ne $_ })
$watchRules = Get-WatchRules

$matchedItems = foreach ($item in ($allItems | Sort-Object Published -Descending)) {
    $text = "$($item.Title) $($item.Summary)"
    $ruleMatches = @(Get-MatchedRules -Text $text -Rules $watchRules)
    if ($ruleMatches.Count -eq 0) {
        continue
    }

    $categories = @($ruleMatches | ForEach-Object { $_.Category } | Sort-Object -Unique)
    $names = @($ruleMatches | ForEach-Object { $_.Name } | Sort-Object -Unique)
    $actions = @($ruleMatches | ForEach-Object { $_.Action } | Sort-Object -Unique)

    $score = 1
    if ($text -match '(?i)\bcritical\b|\bactively exploited\b|\bzero[- ]day\b|\brce\b|\bremote code execution\b') { $score += 3 }
    if ($text -match '(?i)\bmicrosoft\b|\bwindows\b|\bentra\b|\bintune\b|\bdefender\b') { $score += 1 }
    if ($categories.Count -gt 0) { $score += 1 }

    [pscustomobject]@{
        Title       = $item.Title
        Link        = $item.Link
        Source      = $item.Source
        Published   = $item.Published
        Summary     = $item.Summary
        Categories  = $categories
        Matched     = $names
        Actions     = $actions
        Score       = $score
    }
}

$dedupedItems = @(
    $matchedItems |
    Sort-Object -Property @{ Expression = 'Score'; Descending = $true }, @{ Expression = 'Published'; Descending = $true } |
    Group-Object Title |
    ForEach-Object { $_.Group | Select-Object -First 1 }
)

$highPriority = @($dedupedItems | Where-Object { $_.Score -ge 4 } | Select-Object -First 12)
$taniumItems = @($dedupedItems | Where-Object { $_.Categories -contains 'Tanium' } | Select-Object -First 12)
$intuneItems = @($dedupedItems | Where-Object { $_.Categories -contains 'Intune' } | Select-Object -First 12)
$watchItems = @(
    $allItems |
    Sort-Object Published -Descending |
    Where-Object {
        $text = "$($_.Title) $($_.Summary)"
        $text -match '(?i)\bcve\b|\bsecurity\b|\bpatch\b|\bvulnerability\b|\bexploit\b'
    } |
    Select-Object -First 15
)
$patchTuesdayExperienceItems = @(Get-PatchTuesdayExperienceItems -Items $allItems -MaxItems 8)

$digestLines = [System.Collections.Generic.List[string]]::new()
$digestLines.Add("# $title")
$digestLines.Add('')
$digestLines.Add("Daily security intelligence briefing for infrastructure and endpoint management teams. Consolidated from authoritative research, vendor advisories, and community discussions.")
$digestLines.Add('')
$digestLines.Add("- **Generated (UTC):** $($nowUtc.ToString('yyyy-MM-dd HH:mm:ss zzz'))")
$digestLines.Add("- **Lookback window:** $LookbackDays days")
$digestLines.Add('')

    $rocket = [char]::ConvertFromUtf32(0x1F680)
    $digestLines.Add('## ' + $rocket + ' Top Research & Advisories')
    if ($highPriority.Count -eq 0) {
        $digestLines.Add('- *No high-priority security research detected in this window.*')
    }
    else {
        foreach ($item in $highPriority) {
            $truncatedSummary = truncate -text $item.Summary -length 250
            $actionsJoined = $item.Actions -join ' '
            $digestLines.Add('- **[' + $item.Title + '](' + $item.Link + ')** - *(' + $item.Source + ')*')
            if (-not [string]::IsNullOrWhiteSpace($truncatedSummary)) {
                $digestLines.Add('  ' + $truncatedSummary)
            }
            if (-not [string]::IsNullOrWhiteSpace($actionsJoined)) {
                $digestLines.Add('  > **Action:** ' + $actionsJoined)
            }
            $digestLines.Add('')
        }
    }

    $allCategories = @($dedupedItems | ForEach-Object { $_.Categories } | Sort-Object -Unique)
    foreach ($cat in $allCategories) {
        if ($cat -eq 'Tanium' -or $cat -eq 'Intune') { continue }
        
        $catItems = @($dedupedItems | Where-Object { $_.Categories -contains $cat } | Where-Object { $highPriority.Title -notcontains $_.Title })
        if ($catItems.Count -eq 0) { continue }

        $emoji = [char]::ConvertFromUtf32(0x1F4E6) # Package
        if ($cat -eq 'AppSec') { $emoji = [char]::ConvertFromUtf32(0x1F4BB) } # Computer
        elseif ($cat -eq 'Infrastructure') { $emoji = [char]::ConvertFromUtf32(0x1F3D7) } # Construction
        elseif ($cat -eq 'Security Ops') { $emoji = [char]::ConvertFromUtf32(0x1F6E1) } # Shield

        $digestLines.Add('## ' + $emoji + ' ' + $cat)
        foreach ($item in $catItems) {
            $actionsJoined = $item.Actions -join ' '
            $digestLines.Add('- **[' + $item.Title + '](' + $item.Link + ')** - *(' + $item.Source + ')*')
            if (-not [string]::IsNullOrWhiteSpace($actionsJoined)) {
                $digestLines.Add('  ' + $actionsJoined)
            }
            $digestLines.Add('')
        }
    }

    $taniumIntuneItems = @($dedupedItems | Where-Object { $_.Categories -contains 'Tanium' -or $_.Categories -contains 'Intune' } | Where-Object { $highPriority.Title -notcontains $_.Title })
    if ($taniumIntuneItems.Count -gt 0) {
        $toolsEmoji = [char]::ConvertFromUtf32(0x1F6E0)
        $digestLines.Add('## ' + $toolsEmoji + ' Infrastructure & Endpoint Control')
        foreach ($item in $taniumIntuneItems) {
            $actionsJoined = $item.Actions -join ' '
            $digestLines.Add('- **[' + $item.Title + '](' + $item.Link + ')** - *(' + $item.Source + ')*')
            if (-not [string]::IsNullOrWhiteSpace($actionsJoined)) {
                $digestLines.Add('  ' + $actionsJoined)
            }
            $digestLines.Add('')
        }
    }

    if ($patchTuesdayExperienceItems.Count -gt 0) {
        $bandageEmoji = [char]::ConvertFromUtf32(0x1FA79)
        $digestLines.Add('## ' + $bandageEmoji + ' Patch Tuesday & Update Experience')
        foreach ($item in $patchTuesdayExperienceItems) {
            $truncatedSummary = truncate -text $item.Summary -length 200
            $digestLines.Add('- **[' + $item.Title + '](' + $item.Link + ')** - *(' + $item.Source + ')*')
            if (-not [string]::IsNullOrWhiteSpace($truncatedSummary)) {
                $digestLines.Add('  ' + $truncatedSummary)
            }
            $digestLines.Add('')
        }
    }

    $searchEmoji = [char]::ConvertFromUtf32(0x1F50D)
    $digestLines.Add('## ' + $searchEmoji + ' Quick Links (Watch Items)')
    foreach ($item in $watchItems | Select-Object -First 10) {
        $digestLines.Add('- [' + $item.Title + '](' + $item.Link + ') - *(' + $item.Source + ')*')
    }
    $digestLines.Add('')



$digestBody = $digestLines -join [Environment]::NewLine

$frontMatter = @(
    '---'
    'layout: post'
    "title: ""$(Escape-FrontMatterValue -Value $title)"""
    "date: $($nowUtc.ToString('yyyy-MM-dd HH:mm:ss zzz'))"
    'categories: [security-digest]'
    'tags: [security, tldr, situational-awareness, endpoint-management]'
    'author: Arnold'
    '---'
    ''
) -join [Environment]::NewLine

$postContent = $frontMatter + $digestBody + [Environment]::NewLine
Write-Utf8File -Path $postPath -Content $postContent
Write-Utf8File -Path $historicalPath -Content $digestBody
Write-Utf8File -Path $latestPath -Content $digestBody

$historicalFiles = @(
    Get-ChildItem -LiteralPath $DigestArchiveRoot -Filter 'weekly-digest-*.md' -File |
    Sort-Object Name -Descending
)

$indexLines = [System.Collections.Generic.List[string]]::new()
$indexLines.Add('---')
$indexLines.Add('layout: default')
$indexLines.Add('title: Digest Archive')
$indexLines.Add('permalink: /blog/digest-archive/')
$indexLines.Add('---')
$indexLines.Add('')
$indexLines.Add('# Security Digest Archive')
$indexLines.Add('')
$indexLines.Add('This archive stores the raw markdown generated for each weekly digest run.')
$indexLines.Add('')
$indexLines.Add('- [Latest generated digest](./latest-weekly-digest.md)')
$indexLines.Add('- Historical files are append-only and keep the timestamp in the filename.')
$indexLines.Add('')
$indexLines.Add('## Runs')
foreach ($file in $historicalFiles) {
    $indexLines.Add("- [$($file.Name)](./$($file.Name))")
}

Write-Utf8File -Path $indexPath -Content ($indexLines -join [Environment]::NewLine)

Write-Host "Jekyll post: $postPath"
Write-Host "Historical digest: $historicalPath"
Write-Host "Latest digest: $latestPath"
Write-Host "Archive index: $indexPath"
