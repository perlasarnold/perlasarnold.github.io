import feedparser
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pytz
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

FEEDS = {
    "The Hacker News": "https://feeds.feedburner.com/TheHackersNews",
    "BleepingComputer": "https://www.bleepingcomputer.com/feed/",
    "Krebs on Security": "https://krebsonsecurity.com/feed/",
    "CISA Cyber Alerts": "https://www.cisa.gov/cybersecurity-advisories/all.xml"
}

def clean_html(raw_html):
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text(separator=' ', strip=True)
    if len(text) > 300:
        text = text[:297] + "..."
    return text

def run_digest():
    now = datetime.now(pytz.utc)
    cutoff = now - timedelta(hours=25)
    
    print("Welcome to your automated daily security digest. Here are the top security updates published in the last 24 hours across the industry.\n")
    
    found_articles = False
    
    for site_name, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
        except Exception:
            continue
            
        valid_entries = []
        for entry in feed.entries:
            try:
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    dt = datetime(*entry.published_parsed[:6], tzinfo=pytz.utc)
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    dt = datetime(*entry.updated_parsed[:6], tzinfo=pytz.utc)
                else:
                    continue 
                
                if dt >= cutoff:
                    valid_entries.append((entry, dt))
            except Exception:
                continue
                
        if valid_entries:
            found_articles = True
            print(f"## {site_name}")
            for entry, dt in sorted(valid_entries, key=lambda x: x[1], reverse=True):
                title = entry.get('title', 'No Title')
                link = entry.get('link', '#')
                summary = clean_html(entry.get('summary', ''))
                pub_date = dt.strftime("%Y-%m-%d %H:%M UTC")
                
                print(f"### [{title}]({link})")
                print(f"**Published:** {pub_date}\n")
                if summary:
                    print(f"> {summary}\n")
            print("---\n")
            
    if not found_articles:
        print("## All Quiet")
        print("No new security updates were found in the monitored feeds within the past 24 hours.")

if __name__ == "__main__":
    run_digest()
