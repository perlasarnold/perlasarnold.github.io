---
layout: post
title: "IT SecOps News — November 12, 2026"
date: 2026-11-12 18:40:47 +00:00
categories: [intune-daily]
tags: [secops, security-news, cve, patch-tuesday, active-exploits, intune, endpoint-management]
author: Arnold
---

# 📡 IT SecOps News — November 12, 2026

> Daily IT SecOps, vulnerability, patch, and security news briefing.
> Sources monitored: 17 feeds across Microsoft, CISA, security news, and IT communities

---

## 🚨 High Alerts & Active Exploits

Critical vulnerabilities, zero-days, active exploits in the wild, and emergency advisories requiring immediate IT SecOps attention.

| Priority | Title | Source | Advisory / Link |
|----------|-------|--------|-----------------|
| 🔥 ACTIVELY EXPLOITED | [New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into S...](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html) |
| 🔥 ACTIVELY EXPLOITED | [New Windows SignDrop zero-day gives hackers SYSTEM privileges](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/) |
| 🔴 HIGH | [Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Au...](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html) |
| 🔴 HIGH | [186 Fake AI Domains Redirect Users to ClickFix Lures, Browser Malware, a...](https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html) |
| 🔴 HIGH | [Police dismantle Gootloader, CastleRAT, StealC malware infrastructure](https://www.bleepingcomputer.com/news/security/police-dismantles-gootloader-castlerat-stealc-malware-infrastructure/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/police-dismantles-gootloader-castlerat-stealc-malware-infrastructure/) |
| 🔴 HIGH | [Your Endpoint Management Platform Could Be Your Biggest Security Risk](https://www.bleepingcomputer.com/news/security/your-endpoint-management-platform-could-be-your-biggest-security-risk/) | BleepingComputer | [Read News Article →](https://www.bleepingcomputer.com/news/security/your-endpoint-management-platform-could-be-your-biggest-security-risk/) |
| 🔴 HIGH | [SCKit Malware Turns ScreenConnect Support Sessions Into Potential MSP At...](https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/sckit-malware-targets-screenconnect.html) |
| 🔴 HIGH | [PTC Patches Critical Windchill and FlexPLM Flaw That Could Enable Remote...](https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/ptc-patches-critical-windchill-and.html) |
| 🔴 HIGH | [Critical Pre-Auth MongoDB Flaw (CVE-2026-118383) Can Crash Lagging Serve...](https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/critical-pre-auth-mongodb-flaw-cve-2026.html) |
| 🔴 HIGH | [Remus malware claims to retain Gmail account access even after a passwor...](https://www.neowin.net/news/remus-malware-claims-to-retain-gmail-account-access-even-after-a-password-change/?utm_source=rss) | Neowin | [Read News Article →](https://www.neowin.net/news/remus-malware-claims-to-retain-gmail-account-access-even-after-a-password-change/?utm_source=rss) |

### 🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** [New SignDrop Zero-Day Exploit Turns Windows CLFS Security Feature Into SYSTEM Access](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html)
**Source:** The Hacker News · **Published:** November 12, 2026 at 05:50 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/11/new-signdrop-zero-day-exploit-turns.html)**
> Public exploit code released earlier this week claims that a local Windows user can gain SYSTEM privileges through the Common Log File System driver. The proof of concept, called SignDrop, targets a log-authentication feature added to the driver last year. It abuses how clfs.sys creates companion files when a privileged process opens a prepared ...

### 🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** [New Windows SignDrop zero-day gives hackers SYSTEM privileges](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/)
**Source:** BleepingComputer · **Published:** November 12, 2026 at 04:04 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.bleepingcomputer.com/news/security/new-windows-signdrop-zero-day-gives-hackers-system-privileges/)**
> Security researcher Abdelhamid Naceri (also known as Nightmare Eclipse) has released a new Windows zero-day exploit that can let attackers gain SYSTEM privileges. [...]

### [Citrix Patches 12 NetScaler and Secure Access Client Flaws, Including Authentication Bypass](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html)
**Source:** The Hacker News · **Published:** November 12, 2026 at 03:38 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/11/citrix-patches-12-netscaler-and-secure.html)**
> 🛡️ **CVE:** [CVE-2026-120868 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-120868) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-120868)
> Citrix has released patches for multiple critical security flaws impacting NetScaler ADC, Citrix NetScaler Gateway, and NetScaler Console that could lead to denial-of-service (DoS) or an authentication bypass. The critical vulnerabilities that impact NetScaler ADC and NetScaler Gateway are listed below - [CVE-2026-120868](https://www.cve.org/CVERecord?id=CVE-2026-120868) (CVSS score: 9.3) - A mem...

### [186 Fake AI Domains Redirect Users to ClickFix Lures, Browser Malware, and Search Hijackers](https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html)
**Source:** The Hacker News · **Published:** November 12, 2026 at 03:15 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/11/186-fake-ai-domains-redirect-users-to.html)**
> Cybersecurity researchers have found that lookalike domains masquerading as artificial intelligence (AI) tools are being used to serve ClickFix-style lures, browser-hijacking malware, and a set of extensions that hijack user searches. This delivery pattern has been codenamed TypoPrompting by Island. "AI-app lookalikes that turn an attempt to rea...

### [Police dismantle Gootloader, CastleRAT, StealC malware infrastructure](https://www.bleepingcomputer.com/news/security/police-dismantles-gootloader-castlerat-stealc-malware-infrastructure/)
**Source:** BleepingComputer · **Published:** November 12, 2026 at 03:07 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.bleepingcomputer.com/news/security/police-dismantles-gootloader-castlerat-stealc-malware-infrastructure/)**
> Europol and law enforcement partners from nine countries have seized hundreds of servers and domains used by the Gootloader, CastleRAT, and StealC malware operations. [...]

---

## ⚠️ Bad Updates & Known Issues

Reports of problematic updates, broken KBs, OS regressions, and patches causing issues.

- 🟠 **[Microsoft: Recent Windows updates cause SQL Server performance issues](https://www.bleepingcomputer.com/news/microsoft/microsoft-recent-windows-updates-cause-sql-server-performance-issues/)** — *BleepingComputer* · [Article Link →](https://www.bleepingcomputer.com/news/microsoft/microsoft-recent-windows-updates-cause-sql-server-performance-issues/)
  > Microsoft has confirmed that Windows updates released since the October 2026 Patch Tuesday are causing SQL Server performance and stability issues. [...]

- 🟠 **[Microsoft explains how Windows 11 KB5132061 install fail bug is being fixed](https://www.neowin.net/news/microsoft-explains-how-windows-11-kb5132061-install-fail-bug-is-being-fixed/?utm_source=rss)** — *Neowin* · [Article Link →](https://www.neowin.net/news/microsoft-explains-how-windows-11-kb5132061-install-fail-bug-is-being-fixed/?utm_source=rss) — 🔧 **KB:** [KB5132061 (Microsoft Support)](https://support.microsoft.com/help/5132061)
  > Microsoft shares how it's tackling Windows 11 [KB5132061](https://support.microsoft.com/help/5132061) installation failures, though frustrated users may have to wait a while. Read more...

---

## 📅 Upcoming Changes & Deprecations (14-Day Horizon)

Upcoming security changes, feature retirements, and deadlines on the horizon.

- 📆 **[Microsoft shares how upcoming eMudhra patch for Windows 11/10 will be delivered](https://www.neowin.net/news/microsoft-shares-how-upcoming-emudhra-patch-for-windows-1110-will-be-delivered/?utm_source=rss)** — *Neowin* · [Read Announcement →](https://www.neowin.net/news/microsoft-shares-how-upcoming-emudhra-patch-for-windows-1110-will-be-delivered/?utm_source=rss)
  Microsoft is preparing the latest eMudhra patch following the recent certificate security concerns. New details are up for admins to consider. Read more...

- 📆 **[Dynamics 365 Customer Insights - Journeys: Create event experience that match your business structure by supporting leads, contacts, or both​](https://www.microsoft.com/microsoft-365/roadmap?id=579982)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579982)
  Align event registrations with the way your organization manages customer data. By supporting lead-based registration journeys and existing matching rules, you can avoid unnecessary Contact creation, improve data quality, and ensure event attendees follow the same lead managem...

- 📆 **[Power Automate: Direct triggers for desktop flows](https://www.microsoft.com/microsoft-365/roadmap?id=579975)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579975)
  Desktop flows will support direct triggers, enabling automations to start in response to supported events without requiring an intermediary cloud flow. This simplifies automation design and reduces the effort required to connect desktop flows to business processes. GA date: Ma...

- 📆 **[Power Automate: Credentials - Integration with Delinea secret server](https://www.microsoft.com/microsoft-365/roadmap?id=579974)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579974)
  Power Automate will support Delinea Secret Server as an external credential provider for desktop flows. Organizations can securely use credentials managed in Delinea for machine sign-in and credential retrieval during attended and unattended automation. GA date: March CY2027

- 📆 **[Dynamics 365 Customer Insights - Journeys: Send each message only once with deduplication for SMS and custom channels](https://www.microsoft.com/microsoft-365/roadmap?id=579903)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579903)
  Deduplicates recipients by contact point, so each phone number or custom channel address gets the message once per send. Eliminates manual post-send clean-up, wasted messaging spend and the customer annoyance of duplicate texts. Brings SMS and custom channels to parity with em...

- 📆 **[Outlook: Copilot Chat Sheet UX Update for Mobile](https://www.microsoft.com/microsoft-365/roadmap?id=579897)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579897)
  Copilot Chat in Outlook on iOS and Android is getting updated! You'll notice smoother animations, improved strings, and some small changes to the header, such as the new/temporary chat button being moved behind the ... button. GA date: December CY2026

- 📆 **[Microsoft Edge: Top sites in Edge search bar](https://www.microsoft.com/microsoft-365/roadmap?id=579193)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579193)
  Adding easy access to top sites in Edge search bar on desktop. Users can add, edit, remove, or hide top sites. Admins can control available to this feature using the NewTabPageManagedQuickLinks and NewTabPageQuickLinksEnabled policies. GA date: January CY2027

- 📆 **[Microsoft 365: [Education] Practice presentations with Speaker Coach in Learning Activities](https://www.microsoft.com/microsoft-365/roadmap?id=578880)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=578880)
  In learning activities, students can rehearse presentations, receive feedback on their delivery, and practice again with targeted suggestions to improve clarity and confidence. #education GA date: December CY2026

- 📆 **[Dynamics 365 Finance: Submit only validated records to Dynamics 365 Finance](https://www.microsoft.com/microsoft-365/roadmap?id=578877)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=578877)
  The write to business rules engine configuration experience introduces an option to submit only records that have successfully passed Account structure validation. When enabled, Business Performance Planning filters the writeback dataset and submits only records marked as vali...

- 📆 **[Dynamics 365 Customer Insights - Journeys: Build audiences faster with reusable segment templates](https://www.microsoft.com/microsoft-365/roadmap?id=578863)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=578863)
  Segment templates help you build audiences without recreating queries for each campaign. Choose a built-in template for common scenarios such as event attendance or email engagement, or save your own segment query as a reusable custom template. Add placeholders with hint text ...

- 📆 **[Microsoft 365: [Education] Microsoft Learning Zone - Minecraft connected lessons](https://www.microsoft.com/microsoft-365/roadmap?id=577545)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=577545)
  Bring Minecraft Education to every classroom with AI-powered tools that match curriculum goals to Build Challenges, blend lessons with project-based learning, launch directly from Learning Zone, and give you full visibility into participation, completion, and student understan...

- 📆 **[Microsoft 365 admin center: Cross-Tenant Orchestrated Migration](https://www.microsoft.com/microsoft-365/roadmap?id=576273)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=576273)
  Cross-Tenant Orchestrated Migration for User Data Migration (UDM) and Shared Data Migration (SDM) allows customers to move their Microsoft 365 data from one Microsoft tenant to another. UDM includes the ability to move user mailboxes, OneDrive accounts, Teams chats, and Teams ...

- 📆 **[Dynamics 365 Project Operations: Archive project cost actuals with long-term retention](https://www.microsoft.com/microsoft-365/roadmap?id=573238)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=573238)
  Organizations managing high volumes of project transactions need to retain historical cost data without allowing years of completed transactions to continually increase the volume of active operational data. This capability enables organizations to archive processed project st...

---

## ✅ Official Updates & Security Advisories

Feature announcements, security blogs, and official releases.

- **[Get the Intune Company Portal App - Microsoft Intune](https://learn.microsoft.com/en-us/intune/user-help/company-portal/)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/user-help/company-portal/)
  Get the Intune Company Portal app Summarize this article for me In this article Microsoft Intune helps organizations manage access to their internal apps, data, and resources. Intune Company Portal is the app that lets you, as an employee or student in your organization, secur...

- **[Device enrollment guide for Microsoft Intune - Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-enrollment/guide)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/device-enrollment/guide)
  Enrollment guide: Microsoft Intune enrollment Summarize this article for me In this article Microsoft Intune, together with Microsoft Entra ID, facilitates a secure, streamlined process for registering and enrolling devices that want access to your internal resources. Once use...

- **[Step 5 – Enroll devices in Microsoft Intune - Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-enrollment/enroll-devices)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/device-enrollment/enroll-devices)
  Step 5 – Enroll devices in Microsoft Intune Summarize this article for me In this article In the final phase of deployment, devices are registered or joined in Microsoft Entra ID, enrolled in Microsoft Intune, and checked for compliance. During enrollment, Microsoft Intune ins...

- **[Enroll devices using a device enrollment manager account - Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-enrollment/setup-enrollment-manager)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/device-enrollment/setup-enrollment-manager)
  Add device enrollment managers Summarize this article for me In this article A device enrollment manager (DEM) is a nonadministrator user who can enroll devices in Intune. Supported enrollment methods A device enrollment manager can use the following methods to enroll devices ...

- **[Get an Apple MDM Push certificate for Intune - Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-enrollment/apple/create-mdm-push-certificate)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/device-enrollment/apple/create-mdm-push-certificate)
  Get an Apple MDM push certificate Summarize this article for me In this article Upload and renew your Apple MDM push certificates in Microsoft Intune. An Apple MDM Push certificate is required to manage iOS/iPadOS and macOS devices in Microsoft Intune, and enables devices to e...

- **[Android device enrollment guide for Microsoft Intune - Microsoft Intune](https://learn.microsoft.com/en-us/intune/device-enrollment/android/guide)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/device-enrollment/android/guide)
  Enrollment guide: Enroll Android devices in Microsoft Intune Summarize this article for me In this article Personal and organization-owned devices can be enrolled in Intune. There's also a visual guide of the different enrollment options for each platform: Download PDF version...

- **[The global socket: how threat actors are weaponizing GSocket for stealthy C2](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)** — *Microsoft Security Blog* · [Read Article →](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)
  Threat actors are deploying GSocket on compromised Linux servers to keep encrypted remote access after the original vulnerability is patched. Learn how to detect, investigate, and remediate this activity. The post The global socket: how threat actors are weaponizing GSocket fo...

---

## 🐛 IT SecOps Community Buzz

What IT SecOps teams and sysadmins are discussing today.

- **[Critical Red Hat Quay Flaw Lets Attackers Read and Overwrite All Private Container Images in a Registry](https://thehackernews.com/2026/11/critical-red-hat-quay-flaw-lets.html)** — *The Hacker News* · [View Thread →](https://thehackernews.com/2026/11/critical-red-hat-quay-flaw-lets.html)
  > A critical flaw in Red Hat Quay allows an attacker who can access a Quay registry to read and overwrite private container images in every repository. Quay enables anonymous access by default, and while it is enabled, ...

- **[Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes in VMs](https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html)** — *The Hacker News* · [View Thread →](https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html)
  > Google Cloud VMs on AMD Turin chips need a guest OS patch and a stop-and-start to protect against three CPU side-channel flaws, Google said this week. The company has already applied mitigations against attacks betwee...

- **[Hackers plant GSocket on Linux servers for persistent access](https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/)** — *BleepingComputer* · [View Thread →](https://www.bleepingcomputer.com/news/security/hackers-plant-gsocket-on-linux-servers-for-persistent-access/)
  > Multiple threat actors are abusing GSocket, a legitimate open-source remote access tool, to maintain access to Linux servers even after patching the vulnerabilities exploited to gain initial access. [...]

- **[Microsoft introduces Entra security feature that even admins can't disable](https://www.neowin.net/news/microsoft-introduces-entra-security-feature-that-even-admins-cant-disable/?utm_source=rss)** — *Neowin* · [View Thread →](https://www.neowin.net/news/microsoft-introduces-entra-security-feature-that-even-admins-cant-disable/?utm_source=rss)
  > Microsoft's new Entra security feature gives admins seven days to recover important accounts. But once enabled, nobody can disable it. Read more...

- **[Latest Windows 11 update KB5132061 could break your PowerShell scripts](https://www.neowin.net/news/latest-windows-11-update-kb5132061-could-break-your-powershell-scripts/?utm_source=rss)** — *Neowin* · [View Thread →](https://www.neowin.net/news/latest-windows-11-update-kb5132061-could-break-your-powershell-scripts/?utm_source=rss) — 🔧 **KB:** [KB5132061 (Microsoft Support)](https://support.microsoft.com/help/5132061)
  > Microsoft's latest Windows update could cause trouble for PowerShell users. Some previously working scripts may now fail signature verification, but Microsoft has a fix. Read more...

---

*Generated automatically at November 12, 2026 at 06:40 PM UTC · [View all IT SecOps news →](/blog/)*
