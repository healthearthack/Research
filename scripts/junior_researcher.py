import os
import sys
import datetime
import urllib.request
import xml.etree.ElementTree as ET

# Key Energy, Geothermal, DLE & Cyber Feeds
FEEDS = {
    "Federal Register (Energy & Environment)": "https://www.federalregister.gov/api/v1/documents.rss?conditions[topics][]=energy",
    "DOE Geothermal Technologies Office": "https://www.energy.gov/eere/geothermal/listings/geothermal-news.rss",
    "FERC Regulatory Directives": "https://www.ferc.gov/news-rss.xml",
    "CISA Critical Infrastructure Alerts": "https://www.cisa.gov/cybersecurity-advisories.xml"
}

KEYWORDS = [
    "lithium", "brine", "geothermal", "wellbore", "critical minerals",
    "smackover", "operational technology", "scada", "modbus", "telemetry",
    "produced water", "inflow", "cybersecurity", "subsurface"
]

def fetch_feed(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Junior-Researcher-Agent/1.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            return response.read()
    except Exception as e:
        print(f"Warning: Could not reach {url}: {e}")
        return None

def parse_and_filter(xml_data, source_name):
    matches = []
    if not xml_data:
        return matches
    try:
        root = ET.fromstring(xml_data)
        # Handle standard RSS items
        for item in root.findall(".//item"):
            title = item.findtext("title") or "No Title"
            link = item.findtext("link") or "#"
            desc = item.findtext("description") or ""
            pub_date = item.findtext("pubDate") or "Recent"

            text_to_search = f"{title} {desc}".lower()
            found_keywords = [kw for kw in KEYWORDS if kw in text_to_search]

            if found_keywords:
                matches.append({
                    "source": source_name,
                    "title": title.strip(),
                    "link": link.strip(),
                    "date": pub_date.strip(),
                    "keywords": list(set(found_keywords))
                })
    except Exception as e:
        print(f"XML Parsing error for {source_name}: {e}")
    return matches

def main():
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    week_str = datetime.datetime.utcnow().strftime("%Y-W%W")
    
    all_findings = []
    for name, url in FEEDS.items():
        print(f"Scanning {name}...")
        data = fetch_feed(url)
        all_findings.extend(parse_and_filter(data, name))

    digest_file = f"radar/weekly_digests/digest_{today}.md"
    
    report = [
        f"# Junior Researcher Intelligence Briefing — {today}",
        f"*Autonomous Policy, Legal & Telemetry Radar for GeoEnergy Engineering*",
        "",
        "## Executive Summary",
        f"Automated scan completed on `{today}` across federal energy registers, geothermal bulletins, and cyber infrastructure directives.",
        f"Total high-signal intelligence items detected: **{len(all_findings)}**",
        "",
        "---",
        "",
        "## Key Regulatory & Technical Signals",
        ""
    ]

    if not all_findings:
        report.append("*No new critical threshold signals detected matching target keywords this cycle. Baselines remain stable.*")
    else:
        for item in all_findings:
            kw_tags = ", ".join([f"`{k}`" for k in item['keywords']])
            report.append(f"### [{item['title']}]({item['link']})")
            report.append(f"* **Source:** {item['source']} | **Date:** {item['date']}")
            report.append(f"* **Detected Triggers:** {kw_tags}")
            report.append(f"* **Doctoral Relevance:** Informs subsurface wellbore telemetry, DLE permitting, or OT security assumptions.")
            report.append("")

    report.append("---")
    report.append("## Proposed Thesis & Living Document Actions")
    report.append("1. **Verify Citations:** Cross-reference flagged policy changes with `references/annotated_bibliography.md`.")
    report.append("2. **Model Calibration:** Check if new FERC/CISA directives impact downhole telemetry assumptions.")
    report.append("")

    with open(digest_file, "w", encoding="utf-8") as f:
        f.write("\n".join(report))
        
    print(f"✔ Intelligence briefing written to {digest_file}")

if __name__ == "__main__":
    main()