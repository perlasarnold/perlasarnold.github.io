"""
scraper.py — Phase 1: Intune Daily Intelligence Data Collection

Fetches data from three distinct source types:
  1. RSS Feeds   — Microsoft 365 Roadmap, Intune Blog, Windows IT Pro Blog,
                   Microsoft Security Blog, BleepingComputer, Neowin, etc.
  2. Reddit JSON — r/Intune, r/sysadmin, r/SCCM, r/AzureAD, r/microsoft365,
                   r/Windows11 (public .json endpoints, no API key needed)
  3. News RSS    — The Hacker News, BleepingComputer (Intune-relevant items)

Applies keyword-based severity classification:
  🚨 HIGH ALERT     — zero-days, critical CVEs, actively exploited vulns
  ✅ OFFICIAL NEWS   — Microsoft roadmap, GA, deprecations, what's new
  🐛 COMMUNITY BUZZ — Admin discussions, troubleshooting, tips

Output: _data/intune_feed_raw.json
Triggered by GitHub Actions at 6:00 AM PT every weekday.
"""

import json
import io
import os
import re
import sys
import hashlib
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup

# Ensure UTF-8 output on Windows consoles
if sys.stdout and hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

LOOKBACK_HOURS = int(os.environ.get("LOOKBACK_HOURS", "25"))
MAX_ITEMS_PER_SOURCE = int(os.environ.get("MAX_ITEMS_PER_SOURCE", "25"))

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/135.0.0.0 Safari/537.36"
)

REQUESTS_TIMEOUT = 30  # seconds

# RSS feed definitions — Microsoft official + security news
RSS_FEEDS = [
    {
        "name": "Microsoft 365 Roadmap",
        "url": "https://www.microsoft.com/en-us/microsoft-365/RoadmapFeatureRSS",
        "type": "rss",
    },
    {
        "name": "Microsoft Intune What's New",
        "url": "https://learn.microsoft.com/api/search/rss?search=intune+whats+new&locale=en-us&%24top=20",
        "type": "rss",
    },
    {
        "name": "Windows IT Pro Blog",
        "url": "https://techcommunity.microsoft.com/t5/windows-it-pro-blog/bg-p/Windows10Blog/rss",
        "type": "rss",
    },
    {
        "name": "Microsoft Security Blog",
        "url": "https://www.microsoft.com/en-us/security/blog/feed/",
        "type": "rss",
    },
    {
        "name": "Microsoft Entra Blog",
        "url": "https://techcommunity.microsoft.com/t5/microsoft-entra-blog/bg-p/Identity/rss",
        "type": "rss",
    },
    {
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/",
        "type": "rss",
    },
    {
        "name": "Neowin",
        "url": "https://www.neowin.net/news/rss/",
        "type": "rss",
    },
    {
        "name": "The Hacker News",
        "url": "https://feeds.feedburner.com/TheHackersNews",
        "type": "rss",
    },
    {
        "name": "Krebs on Security",
        "url": "https://krebsonsecurity.com/feed/",
        "type": "rss",
    },
    {
        "name": "The Old New Thing",
        "url": "https://devblogs.microsoft.com/oldnewthing/feed/",
        "type": "rss",
    },
]

# Reddit sources (public JSON endpoints — no API key needed)
REDDIT_SOURCES = [
    {
        "name": "Reddit r/Intune",
        "url": "https://www.reddit.com/r/Intune/new/.json?limit=25",
        "type": "reddit",
    },
    {
        "name": "Reddit r/MicrosoftIntune",
        "url": "https://www.reddit.com/r/MicrosoftIntune/new/.json?limit=25",
        "type": "reddit",
    },
    {
        "name": "Reddit r/sysadmin",
        "url": "https://www.reddit.com/r/sysadmin/new/.json?limit=25",
        "type": "reddit",
    },
    {
        "name": "Reddit r/SCCM",
        "url": "https://www.reddit.com/r/SCCM/new/.json?limit=25",
        "type": "reddit",
    },
    {
        "name": "Reddit r/microsoft365",
        "url": "https://www.reddit.com/r/microsoft365/new/.json?limit=25",
        "type": "reddit",
    },
    {
        "name": "Reddit r/AzureAD",
        "url": "https://www.reddit.com/r/AzureAD/new/.json?limit=25",
        "type": "reddit",
    },
    {
        "name": "Reddit r/Windows11",
        "url": "https://www.reddit.com/r/Windows11/new/.json?limit=25",
        "type": "reddit",
    },
]

# ---------------------------------------------------------------------------
# Keyword classification rules
# ---------------------------------------------------------------------------

# Intune relevance filter — items must match at least one of these to be kept
INTUNE_KEYWORDS = re.compile(
    r"(?i)\b("
    r"intune|endpoint\s*manager|autopilot|autopatch|"
    r"mdm|mobile\s*device\s*management|"
    r"conditional\s*access|compliance\s*polic|configuration\s*profile|"
    r"device\s*enrollment|windows\s*autopilot|"
    r"microsoft\s*defender\s*for\s*endpoint|"
    r"entra|azure\s*ad|bitlocker|laps|"
    r"windows\s*update\s*for\s*business|"
    r"app\s*protection\s*polic|managed\s*app|"
    r"co-?management|tenant\s*attach|"
    r"endpoint\s*security|endpoint\s*privilege|"
    r"remote\s*help|windows\s*365|cloud\s*pc|"
    r"win32\s*app|lob\s*app|company\s*portal|"
    r"graph\s*api.*device|device\s*management"
    r")\b"
)

# 🚨 HIGH ALERT — critical security issues
HIGH_ALERT_KEYWORDS = re.compile(
    r"(?i)\b("
    r"zero[- ]?day|actively\s*exploit|critical\s*vuln|"
    r"remote\s*code\s*execution|rce|privilege\s*escalation|"
    r"out[- ]of[- ]band|emergency\s*patch|"
    r"cve-\d{4}-\d{4,}|"
    r"critical\s*security|security\s*breach|"
    r"ransomware.*intune|intune.*ransomware|"
    r"authentication\s*bypass|credential\s*leak|"
    r"cisa\s*kev|known\s*exploit"
    r")\b"
)

# ✅ OFFICIAL NEWS — Microsoft announcements
OFFICIAL_NEWS_KEYWORDS = re.compile(
    r"(?i)\b("
    r"what'?s\s*new|generally\s*available|ga\s*release|"
    r"public\s*preview|private\s*preview|"
    r"deprecat|retir(e|ing|ement)|end[- ]of[- ](?:support|life)|"
    r"roadmap|feature\s*update|service\s*update|"
    r"announcement|rolling\s*out|now\s*available|"
    r"microsoft\s*learn|tech\s*community\s*blog|"
    r"changelog|release\s*notes"
    r")\b"
)

OFFICIAL_SOURCES = {
    "Microsoft 365 Roadmap",
    "Microsoft Intune What's New",
    "Windows IT Pro Blog",
    "Microsoft Security Blog",
    "Microsoft Entra Blog",
}

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def clean_html(raw: str, max_length: int = 400) -> str:
    """Strip HTML tags and truncate.

    Reddit's selftext_html is HTML-entity-encoded, so we unescape first.
    """
    if not raw:
        return ""
    import html
    # Unescape HTML entities (handles Reddit's &lt;div&gt; encoding)
    unescaped = html.unescape(raw)
    soup = BeautifulSoup(unescaped, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > max_length:
        text = text[: max_length - 3] + "..."
    return text


def item_fingerprint(title: str, link: str) -> str:
    """Generate a dedup fingerprint from title + link."""
    normalized = re.sub(r"\s+", " ", (title + link).lower().strip())
    return hashlib.md5(normalized.encode("utf-8")).hexdigest()[:12]


def classify_item(title: str, summary: str, source_name: str) -> str:
    """Classify an item into HIGH_ALERT, OFFICIAL_NEWS, or COMMUNITY_BUZZ."""
    text = f"{title} {summary}"

    # High alert takes priority
    if HIGH_ALERT_KEYWORDS.search(text):
        return "high_alert"

    # Official news from Microsoft sources, or matching official keywords
    if source_name in OFFICIAL_SOURCES or OFFICIAL_NEWS_KEYWORDS.search(text):
        return "official_news"

    # Everything else is community buzz
    return "community_buzz"


def is_intune_relevant(title: str, summary: str, source_name: str) -> bool:
    """Check if an item is relevant to Intune/endpoint management."""
    # Microsoft official sources are always relevant
    if source_name in OFFICIAL_SOURCES:
        return True
    text = f"{title} {summary}"
    return bool(INTUNE_KEYWORDS.search(text))


def parse_date_struct(date_struct) -> datetime | None:
    """Convert feedparser's time_struct to a timezone-aware datetime."""
    if date_struct is None:
        return None
    try:
        return datetime(*date_struct[:6], tzinfo=timezone.utc)
    except Exception:
        return None


# ---------------------------------------------------------------------------
# Source fetchers
# ---------------------------------------------------------------------------


def fetch_rss_feed(feed_def: dict, cutoff: datetime) -> dict:
    """Fetch and parse an RSS/Atom feed."""
    name = feed_def["name"]
    url = feed_def["url"]
    items = []

    try:
        response = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUESTS_TIMEOUT,
        )
        response.raise_for_status()
        feed = feedparser.parse(response.text)

        for entry in feed.entries[:MAX_ITEMS_PER_SOURCE]:
            published = parse_date_struct(
                getattr(entry, "published_parsed", None)
                or getattr(entry, "updated_parsed", None)
            )

            if published is None or published < cutoff:
                continue

            title = entry.get("title", "").strip()
            link = entry.get("link", "").strip()
            summary = clean_html(entry.get("summary", ""))

            if not title:
                continue

            if not is_intune_relevant(title, summary, name):
                continue

            category = classify_item(title, summary, name)
            fp = item_fingerprint(title, link)

            items.append(
                {
                    "fingerprint": fp,
                    "title": title,
                    "link": link,
                    "source": name,
                    "published": published.isoformat(),
                    "summary": summary,
                    "category": category,
                }
            )

        return {
            "name": name,
            "status": "OK",
            "count": len(items),
            "items": items,
        }

    except Exception as exc:
        return {
            "name": name,
            "status": "Error",
            "count": 0,
            "message": str(exc),
            "items": [],
        }


def fetch_reddit_source(source_def: dict, cutoff: datetime) -> dict:
    """Fetch posts from a Reddit subreddit using the public JSON API."""
    name = source_def["name"]
    url = source_def["url"]
    items = []

    try:
        response = requests.get(
            url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUESTS_TIMEOUT,
        )
        response.raise_for_status()
        data = response.json()

        children = data.get("data", {}).get("children", [])

        for child in children[:MAX_ITEMS_PER_SOURCE]:
            post = child.get("data", {})
            created_utc = post.get("created_utc")
            if created_utc is None:
                continue

            published = datetime.fromtimestamp(created_utc, tz=timezone.utc)
            if published < cutoff:
                continue

            title = post.get("title", "").strip()
            selftext = clean_html(post.get("selftext_html", "") or post.get("selftext", ""))
            link = f"https://www.reddit.com{post.get('permalink', '')}"
            score = post.get("score", 0)
            num_comments = post.get("num_comments", 0)

            if not title:
                continue

            if not is_intune_relevant(title, selftext, name):
                continue

            category = classify_item(title, selftext, name)
            fp = item_fingerprint(title, link)

            items.append(
                {
                    "fingerprint": fp,
                    "title": title,
                    "link": link,
                    "source": name,
                    "published": published.isoformat(),
                    "summary": selftext,
                    "category": category,
                    "reddit_score": score,
                    "reddit_comments": num_comments,
                }
            )

        return {
            "name": name,
            "status": "OK",
            "count": len(items),
            "items": items,
        }

    except Exception as exc:
        return {
            "name": name,
            "status": "Error",
            "count": 0,
            "message": str(exc),
            "items": [],
        }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------


def run_scraper() -> dict:
    """Execute the full scraping pipeline and return structured data."""
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(hours=LOOKBACK_HOURS)

    print(f"[scraper] Starting data collection at {now.isoformat()}")
    print(f"[scraper] Lookback window: {LOOKBACK_HOURS}h (cutoff: {cutoff.isoformat()})")

    source_results = []

    # 1. RSS feeds
    for feed_def in RSS_FEEDS:
        print(f"[scraper] Fetching RSS: {feed_def['name']}...")
        result = fetch_rss_feed(feed_def, cutoff)
        print(f"[scraper]   -> {result['status']}: {result['count']} items")
        source_results.append(result)

    # 2. Reddit sources
    for source_def in REDDIT_SOURCES:
        print(f"[scraper] Fetching Reddit: {source_def['name']}...")
        result = fetch_reddit_source(source_def, cutoff)
        print(f"[scraper]   -> {result['status']}: {result['count']} items")
        source_results.append(result)

    # 3. Collect and deduplicate all items
    seen_fingerprints = set()
    all_items = {"high_alert": [], "official_news": [], "community_buzz": []}

    for result in source_results:
        for item in result.get("items", []):
            fp = item["fingerprint"]
            if fp in seen_fingerprints:
                continue
            seen_fingerprints.add(fp)
            category = item["category"]
            all_items[category].append(item)

    # Sort each category by published date (newest first)
    for category in all_items:
        all_items[category].sort(key=lambda x: x.get("published", ""), reverse=True)

    # Build source status summary
    source_status = []
    for result in source_results:
        entry = {
            "name": result["name"],
            "status": result["status"],
            "count": result["count"],
        }
        if "message" in result:
            entry["message"] = result["message"]
        source_status.append(entry)

    total_items = sum(len(v) for v in all_items.values())
    print(f"\n[scraper] Collection complete:")
    print(f"  HIGH ALERTS:    {len(all_items['high_alert'])}")
    print(f"  OFFICIAL NEWS:  {len(all_items['official_news'])}")
    print(f"  COMMUNITY BUZZ: {len(all_items['community_buzz'])}")
    print(f"  TOTAL UNIQUE:   {total_items}")

    output = {
        "generated_utc": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "lookback_hours": LOOKBACK_HOURS,
        "source_status": source_status,
        "items": all_items,
    }

    return output


def main():
    """Entry point: run scraper and write output to _data/intune_feed_raw.json."""
    # Determine repo root (works both locally and in GitHub Actions)
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent  # src/intune_feed/../../ = repo root
    output_path = repo_root / "_data" / "intune_feed_raw.json"

    # Ensure _data directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Run the scraper
    data = run_scraper()

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n[scraper] Output written to: {output_path}")
    print(f"[scraper] File size: {output_path.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
