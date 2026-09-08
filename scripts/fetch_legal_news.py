import os
import feedparser
from datetime import datetime

FEEDS = {
    "Federal Register (Energy & Environment)": "https://www.federalregister.gov/api/v1/documents.rss?conditions[topics][]=environment",
    "FERC Updates": "https://www.ferc.gov/news-rss.xml",
    "DOE Geothermal Technologies": "https://www.energy.gov/eere/geothermal/listings/geothermal-news.rss"
}

def update_radar():
    os.makedirs("radar", exist_ok=True)
    output_file = "radar/regulatory_feed.md"
    today = datetime.utcnow().strftime("%Y-%m-%d")
    
    entries = [f"## Automated Policy & Telemetry Ingest — {today}\n"]
    
    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)
            entries.append(f"### {source}")
            for entry in feed.entries[:3]:
                entries.append(f"* **[{entry.title}]({entry.link})** — {entry.get('published', 'Recent')}")
            entries.append("")
        except Exception as e:
            entries.append(f"*Could not fetch {source}: {e}*\n")
            
    with open(output_file, "a") as f:
        f.write("\n".join(entries) + "\n\n")

if __name__ == "__main__":
    update_radar()
