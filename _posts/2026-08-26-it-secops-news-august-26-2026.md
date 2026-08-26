---
layout: post
title: "IT SecOps News — August 26, 2026"
date: 2026-08-26 11:26:09 +00:00
categories: [intune-daily]
tags: [secops, security-news, cve, patch-tuesday, active-exploits, intune, endpoint-management]
author: Arnold
---

# 📡 IT SecOps News — August 26, 2026

> Daily IT SecOps, vulnerability, patch, and security news briefing.
> Sources monitored: 17 feeds across Microsoft, CISA, security news, and IT communities

---

## 🚨 High Alerts & Active Exploits

Critical vulnerabilities, zero-days, active exploits in the wild, and emergency advisories requiring immediate IT SecOps attention.

| Priority | Title | Source | Advisory / Link |
|----------|-------|--------|-----------------|
| 🔴 HIGH | [Newly SLEEPWALKER Backdoor Waits for One Crafted Packet, Then Runs Its O...](https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html) |
| 🔴 HIGH | [Critical Gitea RCE Actively Exploited as Reported Attack Drops Miner-Lik...](https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html) |
| 🔴 HIGH | [24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages](https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html) |
| 🔴 HIGH | [E4del and PINHOLE RATs Turn FTP Banners Into Dead Drops for Malware Comm...](https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html) | The Hacker News | [Read News Article →](https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html) |

### [Newly SLEEPWALKER Backdoor Waits for One Crafted Packet, Then Runs Its Own Bytecode](https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html)
**Source:** The Hacker News · **Published:** August 26, 2026 at 07:12 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/08/newly-sleepwalker-backdoor-waits-for.html)**
> An independent malware researcher has documented a previously unreported Windows backdoor, dubbed SLEEPWALKER, that stays inert in memory until a specifically crafted network packet reaches the machine and then runs commands written in a 23-instruction language of its own design. The sample is an unsigned 64-bit Windows dynamic-link library (DLL...

### [Critical Gitea RCE Actively Exploited as Reported Attack Drops Miner-Like Payload](https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html)
**Source:** The Hacker News · **Published:** August 26, 2026 at 06:27 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/08/critical-gitea-rce-actively-exploited.html)**
> 🛡️ **CVE:** [CVE-2026-60004 (CVE.org)](https://www.cve.org/CVERecord?id=CVE-2026-60004) · [(NVD)](https://nvd.nist.gov/vuln/detail/CVE-2026-60004)
> The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Tuesday warned of active exploitation efforts targeting a recently patched critical security flaw impacting Gitea. The vulnerability in question is [CVE-2026-60004](https://www.cve.org/CVERecord?id=CVE-2026-60004) (CVSS score: 9.8), a case of remote code execution that allows an attacker with ordinary write access to a repositor...

### [24 npm Packages Abuse unpkg Mirrors to Host Fake Cloudflare CAPTCHA Pages](https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html)
**Source:** The Hacker News · **Published:** August 25, 2026 at 11:52 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/08/24-npm-packages-abuse-unpkg-mirrors-to.html)**
> Cybersecurity researchers have disclosed details of a new campaign that uses a cluster of 24 npm packages as free phishing infrastructure for redirecting to ClickFix-style fake CAPTCHA pages. "While the malware is simply a single HTML page inside the npm package, and while downloading it wouldn't do harm, the threat actor’s use of npm isn't to i...

### [E4del and PINHOLE RATs Turn FTP Banners Into Dead Drops for Malware Commands](https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html)
**Source:** The Hacker News · **Published:** August 25, 2026 at 11:33 AM UTC · 🔗 **[Direct Link to Article / Advisory](https://thehackernews.com/2026/08/e4del-and-pinhole-rats-turn-ftp-banners.html)**
> Cybersecurity researchers are calling attention to a new campaign that employs FTP banners as dead drop resolvers (DDRs) to deliver two previously unreported remote access trojans (RATs) tracked as E4del and PINHOLE. While threat actors are known to abuse legitimate services to point to additional command-and-control (C2) infrastructure and blen...

---

## ⚠️ Bad Updates & Known Issues

Reports of problematic updates, broken KBs, OS regressions, and patches causing issues.

*No problematic update reports detected today.*

---

## 📅 Upcoming Changes & Deprecations (14-Day Horizon)

Upcoming security changes, feature retirements, and deadlines on the horizon.

- 📆 **[Planner: Connected Plans](https://www.microsoft.com/microsoft-365/roadmap?id=569929)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=569929)
  Connected Plans let teams link related plans together to organize work across projects and initiatives. Navigate between connected plans and make related work easier to find and manage. GA date: September CY2026

- 📆 **[Microsoft Copilot (Microsoft 365): Power BI reports as references in Copilot Notebooks](https://www.microsoft.com/microsoft-365/roadmap?id=569928)** — *Microsoft 365 Roadmap* · [Read Announcement →](https://www.microsoft.com/microsoft-365/roadmap?id=569928)
  Copilot Notebooks now lets users add Power BI reports as references, bringing report data directly into their notebooks alongside files. Copilot uses this information to help generate more relevant summaries, presentations, and briefs grounded in the organization's data. GA da...

- 📆 **[In development - Microsoft Intune](https://learn.microsoft.com/en-us/intune/whats-new/in-development)** — *Microsoft Intune What's New* · [Read Announcement →](https://learn.microsoft.com/en-us/intune/whats-new/in-development)
  In development for Microsoft Intune Summarize this article for me In this article To help in your readiness and planning, this article lists Intune UI updates and features that are in development but not yet released. When a feature enters production, whether it's in preview o...

---

## ✅ Official Updates & Security Advisories

Feature announcements, security blogs, and official releases.

- **[Hackers now exploit critical Gitea flaw in code injection attacks](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-gitea-flaw-in-code-injection-attacks/)** — *BleepingComputer* · [Read Article →](https://www.bleepingcomputer.com/news/security/hackers-now-exploit-critical-gitea-flaw-in-code-injection-attacks/)
  Attackers are now exploiting a critical-severity vulnerability in the Gitea self-hosted Git service, according to the U.S. Cybersecurity and Infrastructure Security Agency (CISA). [...]

- **[Deploy Remote Help with Microsoft Intune - Microsoft Intune](https://learn.microsoft.com/en-us/intune/remote-help/deploy)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/remote-help/deploy)
  Deploying Remote Help with Microsoft Intune Summarize this article for me In this article This article describes the steps to deploy Remote Help with Microsoft Intune. ⚙️Set up your tenant ⬇️Download Remote Help 🛠️Install Remote Help ⚙️Configure Remote Help 🔄️Update Remote Hel...

- **[Plan for Remote Help with Microsoft Intune - Microsoft Intune](https://learn.microsoft.com/en-us/intune/remote-help/plan)** — *Microsoft Intune What's New* · [Read Article →](https://learn.microsoft.com/en-us/intune/remote-help/plan)
  Planning for Remote Help with Microsoft Intune Summarize this article for me In this article In this article, users who provide help are referred to as helpers, and users that receive help are referred to as sharers, as they share their session with the helper. Keep the Remote...

---

## 🐛 IT SecOps Community Buzz

What IT SecOps teams and sysadmins are discussing today.

- **[Fake Apple Support AI Calls Target Stolen-Device Owners for Passcodes and 2FA Codes](https://thehackernews.com/2026/08/fake-apple-support-ai-calls-target.html)** — *The Hacker News* · [View Thread →](https://thehackernews.com/2026/08/fake-apple-support-ai-calls-target.html)
  > Cybersecurity researchers have disclosed details of a phishing-as-a-service (PhaaS) platform built to strip Apple's Activation Lock from stolen devices, using rented AI voice agents that call theft victims posing as A...

- **[Frontier AI: Vulnerability Management's Systemic Revolution](https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html)** — *The Hacker News* · [View Thread →](https://thehackernews.com/2026/08/frontier-ai-vulnerability-managements.html)
  > Vulnerability management has been a staple of security programs since the dawn of the cybersecurity discipline. The symbiotic relationship between vulnerability and patch management teams has also existed for that tim...

---

*Generated automatically at August 26, 2026 at 11:25 AM UTC · [View all IT SecOps news →](/blog/)*
