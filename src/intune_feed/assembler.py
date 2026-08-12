"""
assembler.py — Phase 2: IT SecOps News Content Assembly

Reads the raw JSON output from scraper.py (_data/intune_feed_raw.json)
and generates a polished Jekyll-compatible Markdown blog post.

Output: _posts/YYYY-MM-DD-it-secops-news-MONTH-DD-YYYY.md
Triggered by GitHub Actions at 12:00 PM PT every weekday.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Template & Link helpers
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Convert a title string to a URL-safe slug."""
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug or "it-secops-news"


def escape_yaml(value: str) -> str:
    """Escape a string for YAML front matter."""
    return value.replace('"', '\\"')


def format_date_display(iso_str: str) -> str:
    """Format an ISO date string for human display."""
    try:
        dt = datetime.fromisoformat(iso_str)
        return dt.strftime("%B %-d, %Y at %I:%M %p UTC")
    except (ValueError, TypeError):
        try:
            # Windows fallback
            dt = datetime.fromisoformat(iso_str)
            day = dt.day
            return dt.strftime(f"%B {day}, %Y at %I:%M %p UTC")
        except Exception:
            return iso_str


def truncate(text: str, length: int = 250) -> str:
    """Truncate text to a max length."""
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


def linkify_cves_and_kbs(text: str) -> str:
    """Auto-linkify unlinked CVE numbers and KB numbers in body text."""
    if not text:
        return ""

    # Linkify CVE-YYYY-NNNN if not already inside a Markdown link to CVE.org
    def replace_cve(match):
        cve_id = match.group(0).upper()
        url = f"https://www.cve.org/CVERecord?id={cve_id}"
        return f"[{cve_id}]({url})"

    text = re.sub(r"(?<!\[)(?<!\()(CVE-\d{4}-\d{4,})", replace_cve, text, flags=re.IGNORECASE)

    # Linkify KBXXXXXXX if not already inside a Markdown link
    def replace_kb(match):
        kb_id = match.group(0).upper()
        digits_match = re.search(r"\d+", kb_id)
        if not digits_match:
            return kb_id
        digits = digits_match.group(0)
        url = f"https://support.microsoft.com/help/{digits}"
        return f"[{kb_id}]({url})"

    text = re.sub(r"(?<!\[)(?<!\()(KB\d{6,7})", replace_kb, text, flags=re.IGNORECASE)
    return text


def extract_cve_kb_links(text: str) -> list:
    """Extract list of Markdown links for any detected CVEs and KBs in title or summary."""
    if not text:
        return []

    cves = re.findall(r"CVE-\d{4}-\d{4,}", text, flags=re.IGNORECASE)
    kbs = re.findall(r"KB\d{6,7}", text, flags=re.IGNORECASE)

    links = []
    seen = set()

    for cve in cves:
        cve_upper = cve.upper()
        if cve_upper not in seen:
            seen.add(cve_upper)
            cve_org_url = f"https://www.cve.org/CVERecord?id={cve_upper}"
            nvd_url = f"https://nvd.nist.gov/vuln/detail/{cve_upper}"
            links.append(f"🛡️ **CVE:** [{cve_upper} (CVE.org)]({cve_org_url}) · [(NVD)]({nvd_url})")

    for kb in kbs:
        kb_upper = kb.upper()
        if kb_upper not in seen:
            seen.add(kb_upper)
            digits = re.search(r"\d+", kb_upper).group(0)
            links.append(f"🔧 **KB:** [{kb_upper} (Microsoft Support)](https://support.microsoft.com/help/{digits})")

    return links


def is_active_exploit(title: str, summary: str) -> bool:
    """Check if item mentions zero-day, active exploitation in the wild, or CISA KEV."""
    combined = f"{title} {summary}"
    pattern = re.compile(
        r"(?i)\b(zero[- ]?day|0-day|actively\s*exploit|exploited\s*in\s*the\s*wild|cisa\s*kev|known\s*exploit|wild\s*exploit)\b"
    )
    return bool(pattern.search(combined))


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------


def build_front_matter(date_str: str, now: datetime) -> str:
    """Build Jekyll YAML front matter."""
    dt_display = now.strftime("%B %d, %Y")
    dt_display = re.sub(r" 0(\d),", r" \1,", dt_display)
    title = f"IT SecOps News — {dt_display}"

    lines = [
        "---",
        "layout: post",
        f'title: "{escape_yaml(title)}"',
        f"date: {now.strftime('%Y-%m-%d %H:%M:%S +00:00')}",
        "categories: [intune-daily]",
        "tags: [secops, security-news, cve, patch-tuesday, active-exploits, intune, endpoint-management]",
        "author: Arnold",
        "---",
        "",
    ]
    return "\n".join(lines)


def build_header(date_str: str, source_count: int) -> str:
    """Build the report header section."""
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        display_date = dt.strftime("%B %d, %Y")
        display_date = re.sub(r" 0(\d),", r" \1,", display_date)
    except ValueError:
        display_date = date_str

    lines = [
        f"# 📡 IT SecOps News — {display_date}",
        "",
        "> Daily IT SecOps, vulnerability, patch, and security news briefing.",
        f"> Sources monitored: {source_count} feeds across Microsoft, CISA, security news, and IT communities",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def build_high_alerts(items: list) -> str:
    """Build the High Alerts section."""
    lines = [
        "## 🚨 High Alerts & Active Exploits",
        "",
        "Critical vulnerabilities, zero-days, active exploits in the wild, and emergency advisories requiring immediate IT SecOps attention.",
        "",
    ]

    if not items:
        lines.append("*No high-priority alerts or active exploits detected in the last 24 hours. All clear.* ✅")
        lines.append("")
        return "\n".join(lines)

    # Table summary format for high alerts
    lines.append("| Priority | Title | Source | Advisory / Link |")
    lines.append("|----------|-------|--------|-----------------|")

    for item in items[:10]:
        title = truncate(item.get("title", "Untitled"), 75)
        link = item.get("link", "#")
        source = item.get("source", "Unknown")
        summary = item.get("summary", "")
        
        priority_icon = "🔥 ACTIVELY EXPLOITED" if is_active_exploit(title, summary) else "🔴 HIGH"
        lines.append(f"| {priority_icon} | [{title}]({link}) | {source} | [Read News Article →]({link}) |")

    lines.append("")

    # Detail breakdown for top high alert items
    for item in items[:5]:
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        summary = item.get("summary", "")
        source = item.get("source", "Unknown")
        published = item.get("published", "")

        active_badge = "🔥 **[ACTIVELY EXPLOITED / ZERO-DAY]** " if is_active_exploit(title, summary) else ""
        cve_kb_refs = extract_cve_kb_links(f"{title} {summary}")

        lines.append(f"### {active_badge}[{title}]({link})")
        lines.append(f"**Source:** {source} · **Published:** {format_date_display(published)} · 🔗 **[Direct Link to Article / Advisory]({link})**")
        
        if cve_kb_refs:
            lines.append(f"> " + " · ".join(cve_kb_refs))

        if summary:
            linked_summary = linkify_cves_and_kbs(truncate(summary, 350))
            lines.append(f"> {linked_summary}")
            
        lines.append("")

    return "\n".join(lines)


def build_bad_updates(items: list) -> str:
    """Build the Bad Updates section — broken patches, KBs, and regressions."""
    lines = [
        "## ⚠️ Bad Updates & Known Issues",
        "",
        "Reports of problematic updates, broken KBs, OS regressions, and patches causing issues.",
        "",
    ]

    if not items:
        lines.append("*No problematic update reports detected today.*")
        lines.append("")
        return "\n".join(lines)

    for item in items[:12]:
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        summary = item.get("summary", "")
        source = item.get("source", "Unknown")
        score = item.get("reddit_score")
        comments = item.get("reddit_comments")

        meta_parts = [f"*{source}*"]
        if score is not None and score > 0:
            meta_parts.append(f"{score} upvotes")
        if comments is not None and comments > 0:
            meta_parts.append(f"{comments} comments")
        meta = " · ".join(meta_parts)

        cve_kb_refs = extract_cve_kb_links(f"{title} {summary}")
        ref_text = f" — {' · '.join(cve_kb_refs)}" if cve_kb_refs else ""

        lines.append(f"- 🟠 **[{title}]({link})** — {meta} · [Article Link →]({link}){ref_text}")
        if summary:
            linked_summary = linkify_cves_and_kbs(truncate(summary, 280))
            lines.append(f"  > {linked_summary}")
        lines.append("")

    return "\n".join(lines)


def build_upcoming_changes(items: list) -> str:
    """Build the Upcoming Changes section — Microsoft/Vendor changes within 14 days."""
    lines = [
        "## 📅 Upcoming Changes & Deprecations (14-Day Horizon)",
        "",
        "Upcoming security changes, feature retirements, and deadlines on the horizon.",
        "",
    ]

    if not items:
        lines.append("*No upcoming changes detected in the monitored feeds.*")
        lines.append("")
        return "\n".join(lines)

    for item in items[:15]:
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        summary = item.get("summary", "")
        source = item.get("source", "Unknown")

        lines.append(f"- 📆 **[{title}]({link})** — *{source}* · [Read Announcement →]({link})")
        if summary:
            linked_summary = linkify_cves_and_kbs(truncate(summary, 280))
            lines.append(f"  {linked_summary}")
        lines.append("")

    return "\n".join(lines)


def build_official_news(items: list) -> str:
    """Build the Official Microsoft & Security Advisories section."""
    lines = [
        "## ✅ Official Updates & Security Advisories",
        "",
        "Feature announcements, security blogs, and official releases.",
        "",
    ]

    if not items:
        lines.append("*No new official announcements detected today.*")
        lines.append("")
        return "\n".join(lines)

    for item in items[:12]:
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        summary = item.get("summary", "")
        source = item.get("source", "Unknown")

        cve_kb_refs = extract_cve_kb_links(f"{title} {summary}")
        ref_text = f" — {' · '.join(cve_kb_refs)}" if cve_kb_refs else ""

        lines.append(f"- **[{title}]({link})** — *{source}* · [Read Article →]({link}){ref_text}")
        if summary:
            linked_summary = linkify_cves_and_kbs(truncate(summary, 280))
            lines.append(f"  {linked_summary}")
        lines.append("")

    return "\n".join(lines)


def build_community_buzz(items: list) -> str:
    """Build the Community Buzz section."""
    lines = [
        "## 🐛 IT SecOps Community Buzz",
        "",
        "What IT SecOps teams and sysadmins are discussing today.",
        "",
    ]

    if not items:
        lines.append("*No notable community discussions detected today.*")
        lines.append("")
        return "\n".join(lines)

    for item in items[:15]:
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        summary = item.get("summary", "")
        source = item.get("source", "Unknown")
        score = item.get("reddit_score")
        comments = item.get("reddit_comments")

        meta_parts = [f"*{source}*"]
        if score is not None and score > 0:
            meta_parts.append(f"{score} upvotes")
        if comments is not None and comments > 0:
            meta_parts.append(f"{comments} comments")

        meta = " · ".join(meta_parts)
        cve_kb_refs = extract_cve_kb_links(f"{title} {summary}")
        ref_text = f" — {' · '.join(cve_kb_refs)}" if cve_kb_refs else ""

        lines.append(f"- **[{title}]({link})** — {meta} · [View Thread →]({link}){ref_text}")
        if summary:
            linked_summary = linkify_cves_and_kbs(truncate(summary, 220))
            lines.append(f"  > {linked_summary}")
        lines.append("")

    return "\n".join(lines)


def build_footer(generated_utc: str) -> str:
    """Build the report footer."""
    lines = [
        "---",
        "",
        f"*Generated automatically at {format_date_display(generated_utc)} · "
        "[View all IT SecOps news →](/blog/)*",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main assembly pipeline
# ---------------------------------------------------------------------------


def assemble_post(data: dict) -> str:
    """Take raw scraper JSON and produce a complete Jekyll Markdown post."""
    now = datetime.now(timezone.utc)
    date_str = data.get("date", now.strftime("%Y-%m-%d"))
    generated_utc = data.get("generated_utc", now.isoformat())
    source_status = data.get("source_status", [])
    items = data.get("items", {})

    high_alerts = items.get("high_alert", [])
    bad_updates = items.get("bad_updates", [])
    upcoming_changes = items.get("upcoming_changes", [])
    official_news = items.get("official_news", [])
    community_buzz = items.get("community_buzz", [])

    source_count = len(source_status)

    sections = [
        build_front_matter(date_str, now),
        build_header(date_str, source_count),
        build_high_alerts(high_alerts),
        "---\n",
        build_bad_updates(bad_updates),
        "---\n",
        build_upcoming_changes(upcoming_changes),
        "---\n",
        build_official_news(official_news),
        "---\n",
        build_community_buzz(community_buzz),
        build_footer(generated_utc),
    ]

    return "\n".join(sections)


def main():
    """Entry point: read raw JSON, assemble post, write to _posts/."""
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    input_path = repo_root / "_data" / "intune_feed_raw.json"
    posts_dir = repo_root / "_posts"

    posts_dir.mkdir(parents=True, exist_ok=True)

    if not input_path.exists():
        print(f"[assembler] ERROR: Input file not found: {input_path}")
        print("[assembler] Run scraper.py first (Phase 1) to generate the data file.")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"[assembler] Read raw data from: {input_path}")
    print(f"[assembler] Data date: {data.get('date', 'unknown')}")

    now = datetime.now(timezone.utc)
    post_content = assemble_post(data)

    date_str = data.get("date", now.strftime("%Y-%m-%d"))
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        display_date = dt.strftime("%B-%d-%Y").lower()
        display_date = re.sub(r"-0(\d)-", r"-\1-", display_date)
    except ValueError:
        display_date = date_str

    slug = f"it-secops-news-{display_date}"
    filename = f"{date_str}-{slug}.md"
    post_path = posts_dir / filename

    # Remove any existing same-day post (both old name and new name)
    patterns = [f"{date_str}-it-secops-news-*", f"{date_str}-microsoft-situational-awareness-*"]
    for pattern in patterns:
        for existing in posts_dir.glob(pattern):
            if existing != post_path:
                print(f"[assembler] Removing previous same-day post: {existing.name}")
                existing.unlink()

    with open(post_path, "w", encoding="utf-8") as f:
        f.write(post_content)

    print(f"\n[assembler] Post written to: {post_path}")
    print(f"[assembler] File size: {post_path.stat().st_size:,} bytes")
    print(f"[assembler] Post will appear at: /blog/{date_str}/{slug}/")


if __name__ == "__main__":
    main()
