---
layout: post
title: "IT SecOps News — November 24, 2026"
date: 2026-11-24 20:58:51 +00:00
categories: [intune-daily]
tags: [secops, security-news, cve, patch-tuesday, active-exploits, intune, endpoint-management]
author: Arnold
---

# 📡 IT SecOps News — November 24, 2026

> Daily IT SecOps, vulnerability, patch, and security news briefing.
> Sources monitored: 17 feeds across Microsoft, CISA, security news, and IT communities

---

## 🚨 High Alerts & Active Exploits

Critical vulnerabilities, zero-days, active exploits in the wild, and emergency advisories requiring immediate IT SecOps attention.

| Priority | Title | Source | Advisory / Link |
|----------|-------|--------|-----------------|
| 🔴 HIGH | [VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After ...](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html) |
| 🔴 HIGH | [Google Researcher Shows How a Single Bit Change in .NET Files Bypassed W...](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html) |
| 🔴 HIGH | [Danfoss AK-SM 8xxA Series](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03) | CISA Cyber Advisories | [Read News Article →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03) |
| 🔴 HIGH | [AutomationDirect C-More EA9 Programming Software](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01) | CISA Cyber Advisories | [Read News Article →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01) |
| 🔴 HIGH | [Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Lab...](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html) |

### 🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** [VMware vCenter Hit by Another Critical 9.8-Rated Auth Bypass Flaw After Zero-Day Exploitation](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html)
**Source:** The Hacker News · **Published:** November 24, 2026 at 01:28 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/11/vmware-vcenter-hit-by-another-critical.html)**
> 🛡️ **CVE:** [CVE-2026-123903 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-123903) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-123903)
> Broadcom has shipped patches to address 23 vulnerabilities impacting VMware ESX, vCenter, Workstation, Fusion, and Avi Load Balancer, including one critical bug that could be abused to bypass authentication. The critical vulnerability, tracked as [CVE-2026-123903](https://www.cve.org/CVERecord?id=CVE-2026-123903), is rated 9.8 out of 10.0 on the CVSS scoring system. It resides in the VMware Direc...

### [Google Researcher Shows How a Single Bit Change in .NET Files Bypassed Windows Code Integrity](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html)
**Source:** The Hacker News · **Published:** November 24, 2026 at 12:02 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/11/google-researcher-shows-how-single-bit.html)**
> 🛡️ **CVE:** [CVE-2026-87268 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-87268) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-87268)
> A quirk in how the .NET Framework loads a program file let a local attacker run untrusted code past two separate protections on Windows built to block it, Google Project Zero researcher James Forshaw showed in a write-up published yesterday. The same loading behavior bypassed Oracle VirtualBox's process hardening on Windows hosts, tracked as CVE...

### [Danfoss AK-SM 8xxA Series](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03)
**Source:** CISA Cyber Advisories · **Published:** November 24, 2026 at 12:00 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03)**
> 🛡️ **CVE:** [CVE-2026-129713 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-129713) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-129713)
> View CSAF Summary Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code with webserver privileges. The following versions of Danfoss AK-SM 8xxA Series are affected: AK-SM8xxA <=5.4.0 (CVE-2026-129713) CVSS Vendor Equipment v3 9.8 Danfoss AK-SM8xxA 1 Vulnerability Stack-based Buffer Overflow Background Cr...

### [AutomationDirect C-More EA9 Programming Software](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01)
**Source:** CISA Cyber Advisories · **Published:** November 24, 2026 at 12:00 PM UTC · 🔗 **[Direct Link to Article / Advisory](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01)**
> 🛡️ **CVE:** [CVE-2026-127280 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-127280) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-127280)
> View CSAF Summary Successful exploitation of this vulnerability could allow attackers to corrupt application memory and cause instability or a crash, potentially leading to arbitrary code execution, if a user is convinced to open a malicious file. The following versions of AutomationDirect C-More EA9 Programming Software are affected: C-More EA9...

### 🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** [Hackers Exploit N-able MailAssure Flaw While AI Agents Exploit MONAI Label Zero-Day](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)
**Source:** The Hacker News · **Published:** November 24, 2026 at 06:02 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/11/hackers-exploit-n-able-mailassure-flaw.html)**
> 🛡️ **CVE:** [CVE-2026-134624 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-134624) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-134624)
> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday added two flaws impacting N-able MailAssure and MONAI Label to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation. The critical vulnerabilities are listed below - [CVE-2026-134624](https://www.cve.org/CVERecord?id=CVE-2026-134624) (CVSS score: 9.3) - A server-side request forgery (SSR...

---

## ⚠️ Bad Updates & Known Issues

Reports of problematic updates, broken KBs, OS regressions, and patches causing issues.

*No problematic update reports detected today.*

---

## 📅 Upcoming Changes & Deprecations (14-Day Horizon)

Upcoming security changes, feature retirements, and deadlines on the horizon.

- 📆 **[Dynamics 365 Customer Insights - Journeys: Stop tracking email opens without disabling other tracking](https://www.microsoft.com/microsoft-365/roadmap?id=581967)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581967)
  Choose whether to track email opens separately from other tracking in Dynamics 365 Customer Insights - Journeys. A dedicated consent purpose lets you omit tracking pixels from new emails while link clicks, website interactions, UTM parameters, and form prefill continue to foll...

- 📆 **[Microsoft Teams: Improved device settings experience on Teams Rooms on Android](https://www.microsoft.com/microsoft-365/roadmap?id=581965)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581965)
  We’re enhancing the on-device admin settings experience for Teams Rooms on Android by improving information structure, organization and navigation. These updates make it easier for admins to find, understand, and adjust device settings directly from the console, improving over...

- 📆 **[Dynamics 365 Contact Center: Set wait times as short as 5 seconds in orchestration playbooks](https://www.microsoft.com/microsoft-365/roadmap?id=581803)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581803)
  Orchestration playbooks can now re-evaluate the conditions every 5 seconds instead of every 30 seconds. With this shorter interval, you get finer control over priority escalation and Bullseye pool expansion. As a result, conversations reach the right queue or specialist sooner...

- 📆 **[Dynamics 365 Human Resources: Expand talent sourcing through employee referrals](https://www.microsoft.com/microsoft-365/roadmap?id=581791)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581791)
  Employee referrals provide organizations with an additional talent-sourcing channel by enabling employees to participate actively in the recruitment process. This capability helps organizations: Expand talent reach: Access potential candidates through employees' professional n...

- 📆 **[Dynamics 365 Sales: Customize how Recommended Actions are prioritized with custom instructions](https://www.microsoft.com/microsoft-365/roadmap?id=581790)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581790)
  Administrators can customize how the Recommended Actions agent prioritizes actions by configuring natural-language instructions for individual source agents. This gives organizations greater flexibility to align AI-generated recommendations with their sales strategies while re...

- 📆 **[Dynamics 365 Contact Center: Trace conversation journeys end to end across your contact center](https://www.microsoft.com/microsoft-365/roadmap?id=581759)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581759)
  Journey Visualization brings live conversation data onto the map of your contact center configuration, so admins can see how conversations actually flow, not just how they were designed to flow. Admins can spot patterns across many conversations, then select any single convers...

- 📆 **[Dynamics 365 Contact Center: Visualize and manage your contact center setup with visual designer](https://www.microsoft.com/microsoft-365/roadmap?id=581758)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581758)
  Visual Designer shows your entire contact center configuration as one interactive map: channels, workstreams, classification and routing rules, queues, and overflow handling, and how they connect. Admins can see how conversations will flow, spot gaps or misconfigurations, and ...

- 📆 **[Microsoft Edge: Choose a Profile at Startup](https://www.microsoft.com/microsoft-365/roadmap?id=581721)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581721)
  Microsoft Edge is introducing a profile picker at startup, making it easier to begin each browsing session with the right profile. Users can choose among their work, personal, or other available profiles, add a new profile, or browse as a guest before opening the browser. This...

- 📆 **[Microsoft Teams: Raise your hand to speak up at large events with up to 100,000 attendees](https://www.microsoft.com/microsoft-365/roadmap?id=581720)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581720)
  Ask your questions live and take part in the conversation, even at events with up to 100,000 attendees. In events this size, attendees can now raise their hand in Teams when they have a question. Organizers can then let people with a raised hand turn on their mic and camera to...

- 📆 **[Microsoft Teams: Share reactions at events with up to 100,000 attendees](https://www.microsoft.com/microsoft-365/roadmap?id=581719)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=581719)
  Stay more engaged and connected with the audience, even at events with up to 100,000 attendees. Teams now supports reactions in events at this scale. You can send reactions during the event and see the reactions others send, so everyone can share the moment together. GA date: ...

- 📆 **[Microsoft Copilot (Microsoft 365): The more you use Copilot in Office the better it gets](https://www.microsoft.com/microsoft-365/roadmap?id=580889)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=580889)
  Copilot in Word, Excel, PowerPoint, and Workspaces across Copilot App and OneNote will use memory to learn your work patterns and personalize responses. With memory, Copilot can offer more relevant suggestions, hold the pen in a way that represents you, and adapt to your prefe...

- 📆 **[Outlook: Add Custom Flag Descriptions for Clearer Follow-Ups](https://www.microsoft.com/microsoft-365/roadmap?id=580885)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=580885)
  You can add custom text to an email's follow-up flag to describe what you need to do. Use your own words to capture the next step for each flagged message. This gives you a clear reminder of why you flagged the email when you return to it. #newoutlookforwindows GA date: Februa...

- 📆 **[PowerPoint: Customize your Presenter view layout](https://www.microsoft.com/microsoft-365/roadmap?id=579892)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=579892)
  New controls in Presenter view will let you reposition and resize the speaker notes, set speaker notes to a specific text size, and customize the position of slides and notes into a view that works for you. The existing layout will remain the default unless you change it. GA d...

---

## ✅ Official Updates & Security Advisories

Feature announcements, security blogs, and official releases.

- **[Schneider Electric EcoStruxure Power Build Rapsody software](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02)** — *CISA Cyber Advisories* · [Read Article →](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02)
  View CSAF Summary Schneider Electric is aware of a vulnerability in its EcoStruxure™ Power Build Rapsody product. The EcoStruxure™ Power Build Rapsody is used to enter or import the single line diagram, to get the extensive bill of material of your switchboard, including all d...

- **[Microsoft is rolling out maintenance windows in Intune](https://www.neowin.net/news/microsoft-is-rolling-out-maintenance-windows-in-intune/?utm_source=rss)** — *Neowin* · [Read Article →](https://www.neowin.net/news/microsoft-is-rolling-out-maintenance-windows-in-intune/?utm_source=rss)
  Intune admins can now configure maintenance windows for managed Windows 11 devices, with support for several types of updates. Read more...

---

## 🐛 IT SecOps Community Buzz

What IT SecOps teams and sysadmins are discussing today.

- **[Radware discloses breach exposing customer cloud access keys](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)** — *BleepingComputer* · [View Thread →](https://www.bleepingcomputer.com/news/security/radware-discloses-breach-exposing-customer-cloud-access-keys/)
  > Cybersecurity company Radware says attackers gained access to some of its customers' account details and cloud access keys through an unsecured internal Cloud WAF (Web Application Firewall) management API that was lef...

- **[OpenAI and Cisco Unveil AI-Assisted Linux Security Tool to Block Exploits Before Patching](https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html)** — *The Hacker News* · [View Thread →](https://thehackernews.com/2026/11/openai-and-cisco-unveil-ai-assisted.html)
  > OpenAI and Cisco have teamed up to launch Shirudo (meaning "shield" in Japanese), an open-source Linux runtime that allows artificial intelligence (AI) agents to defend systems without downtime. "It lets agents write ...

---

*Generated automatically at November 24, 2026 at 08:58 PM UTC · [View all IT SecOps news →](/blog/)*
