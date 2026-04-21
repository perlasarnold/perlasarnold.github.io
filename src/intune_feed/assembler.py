"""
assembler.py — Phase 2: Microsoft Situational Awareness Content Assembly

Reads the raw JSON output from scraper.py (_data/intune_feed_raw.json)
and generates a polished Jekyll-compatible Markdown blog post.

Output: _posts/YYYY-MM-DD-microsoft-situational-awareness-MONTH-DD-YYYY.md
Triggered by GitHub Actions at 12:00 PM PT every weekday.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# Template helpers
# ---------------------------------------------------------------------------


def slugify(text: str) -> str:
    """Convert a title string to a URL-safe slug."""
    slug = text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug or "microsoft-situational-awareness"


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
            # Windows doesn't support %-d
            dt = datetime.fromisoformat(iso_str)
            day = dt.day
            return dt.strftime(f"%B {day}, %Y at %I:%M %p UTC")
        except Exception:
            return iso_str


def truncate(text: str, length: int = 200) -> str:
    """Truncate text to a max length."""
    if len(text) <= length:
        return text
    return text[: length - 3] + "..."


# ---------------------------------------------------------------------------
# Section builders
# ---------------------------------------------------------------------------


def build_front_matter(date_str: str, now: datetime) -> str:
    """Build Jekyll YAML front matter."""
    dt_display = now.strftime("%B %d, %Y")
    # Remove leading zero from day
    dt_display = re.sub(r" 0(\d),", r" \1,", dt_display)
    title = f"Microsoft Situational Awareness — {dt_display}"

    lines = [
        "---",
        "layout: post",
        f'title: "{escape_yaml(title)}"',
        f"date: {now.strftime('%Y-%m-%d %H:%M:%S +00:00')}",
        "categories: [intune-daily]",
        "tags: [intune, endpoint-management, daily-intel, situational-awareness]",
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
        f"# 📡 Microsoft Situational Awareness — {display_date}",
        "",
        "> Daily intelligence briefing for Intune administrators.",
        f"> Sources monitored: {source_count} feeds across Microsoft, Reddit, and security news",
        "",
        "---",
        "",
    ]
    return "\n".join(lines)


def build_high_alerts(items: list) -> str:
    """Build the High Alerts section."""
    lines = [
        "## 🚨 High Alerts",
        "",
        "Items requiring immediate attention from endpoint management teams.",
        "",
    ]

    if not items:
        lines.append("*No high-priority alerts detected in the last 24 hours. All clear.* ✅")
        lines.append("")
        return "\n".join(lines)

    # Table format for high alerts
    lines.append("| Priority | Title | Source |")
    lines.append("|----------|-------|--------|")

    for item in items[:10]:
        title = truncate(item.get("title", "Untitled"), 80)
        link = item.get("link", "#")
        source = item.get("source", "Unknown")
        lines.append(f"| 🔴 | [{title}]({link}) | {source} |")

    lines.append("")

    # Add details for each alert
    for item in items[:5]:
        title = item.get("title", "Untitled")
        link = item.get("link", "#")
        summary = item.get("summary", "")
        source = item.get("source", "Unknown")
        published = item.get("published", "")

        lines.append(f"### [{title}]({link})")
        lines.append(f"**Source:** {source} · **Published:** {format_date_display(published)}")
        if summary:
            lines.append(f"> {truncate(summary, 300)}")
        lines.append("")

    return "\n".join(lines)


def build_bad_updates(items: list) -> str:
    """Build the Bad Updates section — broken patches and regressions."""
    lines = [
        "## ⚠️ Bad Updates & Known Issues",
        "",
        "Reports of problematic updates, regressions, and patches causing issues.",
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

        lines.append(f"- 🟠 **[{title}]({link})** — {meta}")
        if summary:
            lines.append(f"  > {truncate(summary, 250)}")
        lines.append("")

    return "\n".join(lines)


def build_upcoming_changes(items: list) -> str:
    """Build the Upcoming Changes section — Microsoft changes within 14 days."""
    lines = [
        "## 📅 Upcoming Changes (14-Day Horizon)",
        "",
        "Microsoft changes on the horizon. Plan and act before these take effect.",
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

        lines.append(f"- 📆 **[{title}]({link})** — *{source}*")
        if summary:
            lines.append(f"  {truncate(summary, 250)}")
        lines.append("")

    return "\n".join(lines)


def build_official_news(items: list) -> str:
    """Build the Official Microsoft Updates section."""
    lines = [
        "## ✅ Official Microsoft Updates",
        "",
        "Feature changes, deprecations, and roadmap items from Microsoft.",
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

        lines.append(f"- **[{title}]({link})** — *{source}*")
        if summary:
            lines.append(f"  {truncate(summary, 250)}")
        lines.append("")

    return "\n".join(lines)


def build_community_buzz(items: list) -> str:
    """Build the Community Buzz section."""
    lines = [
        "## 🐛 Community Buzz",
        "",
        "What Intune admins are discussing today.",
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

        # Build metadata line
        meta_parts = [f"*{source}*"]
        if score is not None and score > 0:
            meta_parts.append(f"{score} upvotes")
        if comments is not None and comments > 0:
            meta_parts.append(f"{comments} comments")

        meta = " · ".join(meta_parts)

        lines.append(f"- **[{title}]({link})** — {meta}")
        if summary:
            lines.append(f"  > {truncate(summary, 200)}")
        lines.append("")

    return "\n".join(lines)


def build_source_health(source_status: list) -> str:
    """Build the Source Health table."""
    lines = [
        "## 📊 Source Health",
        "",
        "| Source | Status | Items Collected |",
        "|--------|--------|-----------------|",
    ]

    for source in source_status:
        name = source.get("name", "Unknown")
        status = source.get("status", "Unknown")
        count = source.get("count", 0)
        message = source.get("message", "")

        if status == "OK":
            status_icon = "✅ OK"
        else:
            status_icon = f"⚠️ {status}"
            if message:
                status_icon += f" — {truncate(message, 60)}"

        lines.append(f"| {name} | {status_icon} | {count} |")

    lines.append("")
    return "\n".join(lines)


def build_footer(generated_utc: str) -> str:
    """Build the report footer."""
    lines = [
        "---",
        "",
        f"*Generated automatically at {format_date_display(generated_utc)} · "
        "[View all daily intel →](/blog/)*",
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

    # Assemble the full post — bad updates right after alerts, upcoming before official
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
        "---\n",
        build_source_health(source_status),
        build_footer(generated_utc),
    ]

    return "\n".join(sections)


def main():
    """Entry point: read raw JSON, assemble post, write to _posts/.

    If a post for the same date already exists (e.g. from a manual re-trigger),
    it is replaced rather than creating a duplicate.
    """
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent
    input_path = repo_root / "_data" / "intune_feed_raw.json"
    posts_dir = repo_root / "_posts"

    # Ensure directories exist
    posts_dir.mkdir(parents=True, exist_ok=True)

    # Read raw data
    if not input_path.exists():
        print(f"[assembler] ERROR: Input file not found: {input_path}")
        print("[assembler] Run scraper.py first (Phase 1) to generate the data file.")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"[assembler] Read raw data from: {input_path}")
    print(f"[assembler] Data date: {data.get('date', 'unknown')}")
    print(f"[assembler] Items: "
          f"{len(data.get('items', {}).get('high_alert', []))} alerts, "
          f"{len(data.get('items', {}).get('official_news', []))} official, "
          f"{len(data.get('items', {}).get('community_buzz', []))} community")

    # Assemble the post content
    now = datetime.now(timezone.utc)
    post_content = assemble_post(data)

    # Generate filename
    date_str = data.get("date", now.strftime("%Y-%m-%d"))
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        display_date = dt.strftime("%B-%d-%Y").lower()
        display_date = re.sub(r"-0(\d)-", r"-\1-", display_date)
    except ValueError:
        display_date = date_str

    slug = f"microsoft-situational-awareness-{display_date}"
    filename = f"{date_str}-{slug}.md"
    post_path = posts_dir / filename

    # Remove any existing microsoft-situational-awareness post for the same date.
    # This ensures manual re-triggers (workflow_dispatch) replace instead of duplicate.
    existing_pattern = f"{date_str}-microsoft-situational-awareness-*"
    for existing in posts_dir.glob(existing_pattern):
        if existing != post_path:
            print(f"[assembler] Removing previous same-day post: {existing.name}")
            existing.unlink()

    # Write the post (overwrites if same filename already exists)
    with open(post_path, "w", encoding="utf-8") as f:
        f.write(post_content)

    print(f"\n[assembler] Post written to: {post_path}")
    print(f"[assembler] File size: {post_path.stat().st_size:,} bytes")
    print(f"[assembler] Post will appear at: /blog/{date_str}/{slug}/")


if __name__ == "__main__":
    main()

