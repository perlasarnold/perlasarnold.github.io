---
layout: post
title: "IT SecOps News — September 17, 2026"
date: 2026-09-17 15:25:25 +00:00
categories: [intune-daily]
tags: [secops, security-news, cve, patch-tuesday, active-exploits, intune, endpoint-management]
author: Arnold
---

# 📡 IT SecOps News — September 17, 2026

> Daily IT SecOps, vulnerability, patch, and security news briefing.
> Sources monitored: 17 feeds across Microsoft, CISA, security news, and IT communities

---

## 🚨 High Alerts & Active Exploits

Critical vulnerabilities, zero-days, active exploits in the wild, and emergency advisories requiring immediate IT SecOps attention.

| Priority | Title | Source | Advisory / Link |
|----------|-------|--------|-----------------|
| 🔴 HIGH | [Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious D...](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html) |
| 🔴 HIGH | [Chinese hackers use SparroWocky malware in govt espionage attacks](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/) |
| 🔥 ACTIVELY EXPLOITED | [Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/) |
| 🔥 ACTIVELY EXPLOITED | [Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Act...](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html) |
| 🔴 HIGH | [Iranian hackers use CHOSEN BRICK Windows malware to spy on targets](https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/) |
| 🔴 HIGH | [Malware bypasses browser checks to force install Chrome, Edge extensions](https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/malware-bypasses-browser-checks-to-force-install-chrome-edge-extensions/) |
| 🔴 HIGH | [Attackers Exploit Issabel Framework Flaw Enabling Unauthenticated OS Com...](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/09/attackers-exploit-issabel-framework.html) |
| 🔴 HIGH | [Three Threat Groups Target Russian Enterprises With Backdoors, Ransomwar...](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html) |

### [Critical Unbound DNSSEC Validator Flaw Could Allow RCE via a Malicious DNS Zone](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)
**Source:** The Hacker News · **Published:** September 17, 2026 at 12:30 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/09/critical-unbound-dnssec-validator-flaw.html)**
> 🛡️ **CVE:** [CVE-2026-81642 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-81642) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-81642)
> Every release of the Unbound DNS resolver before 1.26.1 has a critical heap overflow in its DNSSEC validator, maintainer NLnet Labs said in an advisory on Wednesday. An attacker who controls a malicious zone and queries a vulnerable resolver can trigger it, enabling remote code execution. Unbound 1.26.1, released the same day, fixes the bug, tra...

### [Chinese hackers use SparroWocky malware in govt espionage attacks](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/)
**Source:** BleepingComputer · **Published:** September 17, 2026 at 09:00 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-sparrowocky-malware-in-govt-espionage-attacks/)**
> The China-linked espionage group FamousSparrow has been using a new backdoor named SparroWocky in attacks on government organizations in Latin America. [...]

### 🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** [Cisco warns of max severity ISE zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/)
**Source:** BleepingComputer · **Published:** September 17, 2026 at 07:20 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.bleepingcomputer.com/news/security/cisco-warns-of-identity-service-engine-zero-day-exploited-in-attacks/)**
> Cisco has released security updates to address a maximum-severity Identity Services Engine vulnerability that attackers are actively exploiting in the wild. [...]

### 🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** [Cisco Warns of New Zero-Day ISE Auth Bypass (CVSS 10.0) Exploited in Active Attacks](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)
**Source:** The Hacker News · **Published:** September 17, 2026 at 06:39 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/09/cisco-warns-of-new-zero-day-ise-auth.html)**
> 🛡️ **CVE:** [CVE-2026-76460 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-76460) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-76460)
> Cisco has warned of a fresh maximum-severity security flaw impacting Identity Services Engine (ISE) that has come under active exploitation. The vulnerability, tracked as [CVE-2026-76460](https://www.cve.org/CVERecord?id=CVE-2026-76460) (CVSS score: 10.0), could allow an unauthenticated, remote attacker to bypass authentication. "This vulnerability is due to insufficient authentication control o...

### [Iranian hackers use CHOSEN BRICK Windows malware to spy on targets](https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/)
**Source:** BleepingComputer · **Published:** September 16, 2026 at 08:24 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.bleepingcomputer.com/news/security/iranian-hackers-use-chosen-brick-windows-malware-to-spy-on-targets/)**
> Government agencies are warning that Iranian state-linked hackers are using a Windows malware strain named CHOSEN BRICK to target dissidents, activists, and journalists worldwide. [...]

---

## ⚠️ Bad Updates & Known Issues

Reports of problematic updates, broken KBs, OS regressions, and patches causing issues.

*No problematic update reports detected today.*

---

## 📅 Upcoming Changes & Deprecations (14-Day Horizon)

Upcoming security changes, feature retirements, and deadlines on the horizon.

- 📆 **[Microsoft to strip App Governance access from admin role](https://www.neowin.net/news/microsoft-to-strip-app-governance-access-from-admin-role/?utm_source=rss)** — *Neowin* · [Read Announcement →](https://www.neowin.net/news/microsoft-to-strip-app-governance-access-from-admin-role/?utm_source=rss)
  Audit tenant permissions ahead of the deadline to prevent access loss in Microsoft Defender for Cloud Apps and transition personnel to alternative roles like Security Administrator. Read more...

- 📆 **[Microsoft Teams: Schedule Teams Channel Meeting from Win32](https://www.microsoft.com/microsoft-365/roadmap?id=571389)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=571389)
  Users can now schedule Teams Channel Meetings from Win32 (Outlook classic client) GA date: October CY2026

- 📆 **[Microsoft Teams: Customize blocked file extensions for Weaponizable File Protection](https://www.microsoft.com/microsoft-365/roadmap?id=571298)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=571298)
  Microsoft Teams is expanding admin controls for Weaponizable File Protection. Administrators will be able to customize which file types are blocked in Teams to align with their organization's security requirements or continue using the Microsoft-recommended default list. This ...

- 📆 **[SharePoint: New Mobile Experience on iOS and Android](https://www.microsoft.com/microsoft-365/roadmap?id=571200)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=571200)
  The SharePoint mobile app for iOS and Android is redesigned around the personalized SharePoint Discover experience, bringing your most relevant files, sites, people, and news together in one place, with improved site browsing, in-app file previews, refreshed news and search, d...

- 📆 **[Dynamics 365 Field Service: Automatically complete Project Tasks when field work is finished](https://www.microsoft.com/microsoft-365/roadmap?id=570860)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=570860)
  Keep project plans aligned with field execution by automatically completing a linked Project Task when its Work Order is completed. When project work is carried out through Field Service, the Work Order often represents the execution of a specific Project Task. With this capab...

- 📆 **[Dynamics 365 Field Service: Bring project material plans into field execution](https://www.microsoft.com/microsoft-365/roadmap?id=570855)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=570855)
  When the Field Service and Project Operations integration is enabled, material estimates created in a project plan can now create connected Work Order Products on the related Field Service work order. This allows project-planned materials to flow into Field Service without req...

---

## ✅ Official Updates & Security Advisories

Feature announcements, security blogs, and official releases.

*No new official announcements detected today.*

---

## 🐛 IT SecOps Community Buzz

What IT SecOps teams and sysadmins are discussing today.

- **[CISO's Expert Guide to Agentic Pentesting for Websites](https://thehackernews.com/2026/09/cisos-expert-guide-to-agentic.html)** — *The Hacker News* · [View Thread →](https://thehackernews.com/2026/09/cisos-expert-guide-to-agentic.html)
  > Attackers now weaponize new vulnerabilities in about five days (Mandiant, part of Google Cloud). The median organization takes 43 days to patch one (Verizon DBIR 2026). A new free guide explains how autonomous AI agen...

- **[Microsoft explains why admins must act soon to adopt Windows 11 Autopilot device preparation](https://www.neowin.net/news/microsoft-explains-why-admins-must-act-soon-to-adopt-windows-11-autopilot-device-preparation/?utm_source=rss)** — *Neowin* · [View Thread →](https://www.neowin.net/news/microsoft-explains-why-admins-must-act-soon-to-adopt-windows-11-autopilot-device-preparation/?utm_source=rss)
  > Microsoft has explained how admins can transition from Windows Autopilot to Autopilot device preparation. The company has also explained why that's essential now. Read more...

- **[Microsoft wants organizations to ditch traditional VPNs for Entra Private Access](https://www.neowin.net/news/microsoft-wants-organizations-to-ditch-traditional-vpns-for-entra-private-access/?utm_source=rss)** — *Neowin* · [View Thread →](https://www.neowin.net/news/microsoft-wants-organizations-to-ditch-traditional-vpns-for-entra-private-access/?utm_source=rss)
  > Microsoft thinks your VPN may be putting your organization at risk, and it has a new plan to change how your workforce connects to private resources. Read more...

- **[Microsoft issues manual fix for Windows 11 KB5124008 domain bug](https://www.neowin.net/news/microsoft-issues-manual-fix-for-windows-11-kb5124008-domain-bug/?utm_source=rss)** — *Neowin* · [View Thread →](https://www.neowin.net/news/microsoft-issues-manual-fix-for-windows-11-kb5124008-domain-bug/?utm_source=rss) — 🔧 **KB:** [KB5124008 (Microsoft Support)](https://support.microsoft.com/help/5124008)
  > [KB5124008](https://support.microsoft.com/help/5124008) drops secure channels on Windows 11 24H2 and 25H2 systems. Find out how to disable Machine Identity Isolation and repair your domain trust. Read more...

- **[Windows 11 KB5124008 update breaks domain trust for some users](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5124008-update-breaks-domain-trust-for-some-users/)** — *BleepingComputer* · [View Thread →](https://www.bleepingcomputer.com/news/microsoft/windows-11-kb5124008-update-breaks-domain-trust-for-some-users/) — 🔧 **KB:** [KB5124008 (Microsoft Support)](https://support.microsoft.com/help/5124008)
  > Microsoft is investigating reports that the Windows 11 [KB5124008](https://support.microsoft.com/help/5124008) security update is breaking domain trust relationships on some enterprise systems, preventing users from logging in with valid domain credentials. [...]

---

*Generated automatically at September 17, 2026 at 03:25 PM UTC · [View all IT SecOps news →](/blog/)*
