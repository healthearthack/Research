import os
import sys
import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

DRAFTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "publications", "drafts")
os.makedirs(DRAFTS_DIR, exist_ok=True)

# High-priority RSS and JSON API endpoints for your exact research niche
FEEDS = {
    "Federal Register (Energy & Minerals)": "https://www.federalregister.gov/api/v1/articles.json?conditions%5Bterm%5D=lithium+OR+geothermal+OR+%22direct+lithium+extraction%22+OR+%22wellbore%22&order=newest",
    "Google News (Direct Lithium Extraction & Smackover)": "https://news.google.com/rss/search?q=%22Direct+Lithium+Extraction%22+OR+%22Smackover%22+lithium&hl=en-US&gl=US&ceid=US:en",
    "Google News (SCADA & Industrial OT Security)": "https://news.google.com/rss/search?q=%22SCADA%22+AND+(%22wellhead%22+OR+%22critical+infrastructure%22+OR+%22Modbus%22)&hl=en-US&gl=US&ceid=US:en",
    "Google News (Satellite Emissions & IRA 45X)": "https://news.google.com/rss/search?q=%22IRA+45X%22+OR+%22TROPOMI%22+methane+OR+%22TEMPO%22+satellite&hl=en-US&gl=US&ceid=US:en"
}

KEYWORDS_HIGH_IMPACT = [
    "smackover", "direct lithium extraction", "dle", "ira 45x", "section 45x",
    "geothermal", "wellbore", "class vi", "modbus", "scada", "tropomi", "methane",
    "usgs", "doe", "epa", "tax credit", "critical minerals"
]

def fetch_feed_items():
    items = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) HealthEarthHackResearchSentinel/1.0"}
    
    # 1. Fetch Federal Register API
    fed_url = FEEDS["Federal Register (Energy & Minerals)"]
    try:
        req = urllib.request.Request(fed_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            for art in data.get("results", [])[:5]:
                items.append({
                    "source": "Federal Register",
                    "title": art.get("title", ""),
                    "url": art.get("html_url", ""),
                    "date": art.get("publication_date", ""),
                    "summary": art.get("abstract", "") or art.get("snippet", "") or "Federal rulemaking/notice."
                })
    except Exception as e:
        print(f"[!] Error fetching Federal Register: {e}")

    # 2. Fetch Google News RSS Feeds
    for feed_name, url in FEEDS.items():
        if "Google News" not in feed_name:
            continue
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10) as resp:
                xml_data = resp.read()
                root = ET.fromstring(xml_data)
                for item in root.findall(".//item")[:5]:
                    title = item.find("title").text if item.find("title") is not None else ""
                    link = item.find("link").text if item.find("link") is not None else ""
                    pub_date = item.find("pubDate").text if item.find("pubDate") is not None else ""
                    desc = item.find("description").text if item.find("description") is not None else ""
                    items.append({
                        "source": feed_name,
                        "title": title,
                        "url": link,
                        "date": pub_date,
                        "summary": desc
                    })
        except Exception as e:
            print(f"[!] Error fetching {feed_name}: {e}")

    return items

def filter_significant_events(items):
    significant = []
    seen_titles = set()
    for item in items:
        title_lower = item["title"].lower()
        if title_lower in seen_titles:
            continue
        seen_titles.add(title_lower)
        
        matches = [kw for kw in KEYWORDS_HIGH_IMPACT if kw in title_lower or kw in item["summary"].lower()]
        if matches:
            item["matched_keywords"] = matches
            significant.append(item)
    return significant

def scaffold_rapid_response_paper(event):
    date_str = datetime.now().strftime("%Y_%m_%d")
    clean_title = "".join(c for c in event["title"] if c.isalnum() or c in (" ", "_", "-")).strip()
    words = clean_title.split()[:8]
    slug = "_".join(words)
    filename = f"RR_{date_str}_{slug}.md"
    target_file = os.path.join(DRAFTS_DIR, filename)

    content = f"""# Rapid Response: {event['title']}

**Andrew C. Kieckhefer**¹²*  
¹ *Health Earth Hack Research Laboratory, Madison, WI / USA*  
² *Department of Atmospheric and Oceanic Sciences (Alum), University of Wisconsin–Madison, Madison, WI 53706, USA*  
* *Corresponding Author / Google Scholar Anchor:* `weather.amazon.go@gmail.com` | `andy.kieckhefer@gmail.com`  

**Publication Category:** Rapid Response Policy & Technical Assessment  
**Target Repository:** EarthArXiv Preprints / Zenodo | DOI: `Pending Deposit`  
**Trigger Event Date:** {datetime.now().strftime('%B %d, %Y')}  
**Source Baseline:** [{event['source']}]({event['url']})  

---

## Executive Summary
On {datetime.now().strftime('%B %d, %Y')}, a critical development occurred regarding **{event['title']}**. This rapid response brief synthesizes the technical, hydrochemical, and operational implications for continental brine critical mineral extraction, idle wellbore repurposing, and industrial cyber-physical resilience. We contextualize how this event impacts active engineering workflows under the U.S. Inflation Reduction Act (IRA Section 45X) and modern operational technology (OT) security frameworks.

**Keywords:** Rapid Response, Policy Assessment, Direct Lithium Extraction, Smackover Formation, Energy Transition, Wellbore Integrity.

---

## 1. Regulatory & Technical Context
* **Official Event / Notice:** {event['title']}
* **Source & Origin:** {event['source']}
* **Primary Focus Areas:** {", ".join(event.get('matched_keywords', []))}

{event['summary']}

The introduction of this policy or technical development fundamentally reshapes the operational risk calculus for domestic energy operators. Rather than treating this development as an isolated legal announcement, it must be evaluated through the lens of coupled subsurface thermodynamics, high-pressure brine transport, and edge-level cyber-physical telemetry.

---

## 2. Hydrodynamic, Geochemical & Engineering Implications
1. **Subsurface Fluid Balancing:** Production of high-temperature ($120–145^\\circ\\text{{C}}$) Smackover formation water requires deterministic surface pressure balancing to mitigate casing shear and induced seismicity.
2. **Column Elution & Scaling Kinetics:** Shifts in regulatory standards mandate closed-loop chemical monitoring at the wellhead edge to maintain lithium recovery efficiencies above 90% without unmitigated scale deposition.
3. **Operational Technology (OT) Safeguards:** As facilities expand telemetry under this mandate, field field-level Modbus/TCP and DNP3 controllers must incorporate physics-informed anomaly detection under NIST SP 800-82 guidelines to prevent adversarial sensor spoofing.

---

## 3. Technoeconomic & IRA 45X Impact Matrix

| Dimension | Legacy Regulatory Baseline | New Rapid-Response Framework | Engineering Action Item |
| :--- | :--- | :--- | :--- |
| **Federal Subsidy Qualification** | Annual self-certification | Continuous empirical telemetry | Deploy edge-validated MRV ledgers |
| **Environmental Compliance** | Intermittent point-source OGI | Multiscale space-to-wellhead monitoring | Couple Sentinel-5P with fiber DAS |
| **Capital Expenditure (CapEx)** | High greenfield drilling costs | Repurposed late-life wellbore conduits | Save 40–60% via idle well conversion |

---

## 4. Strategic Recommendations for Industrial Operators
1. **Accelerate Wellbore Repurposing:** Prioritize late-life Class II and production wellbores meeting intermediate casing burst thresholds ($>4,500\\text{{ psi}}$).
2. **Deploy Distributed Edge Telemetry:** Avoid reliance on remote cloud latency by executing safety trip logic on ruggedized wellhead microclouds.
3. **Maintain Continuous MRV:** Link spaceborne trace gas retrievals with downhole acoustic sensors to satisfy zero-emissions audits for maximum tax credit yield.

---

## References & Official Gazettes

1. **{event['source']}** ({datetime.now().strftime('%Y')}). *Official Docket / Notice: {event['title']}.* Available at: {event['url']}
2. **Kieckhefer, A. C.** (2026). *Direct Lithium Extraction (DLE) from Continental Petroleum Brines: Repurposing Late-Life Wellbores for Closed-Loop Battery Mineral Recovery.* EarthArXiv Preprints.
3. **Kieckhefer, A. C.** (2026). *From Edge to Wellhead: Translating Software-Defined Telemetry and Industrial IoT into Resilient Subsurface GeoEnergy Systems.* EarthArXiv Preprints / Zenodo.
4. **NIST Special Publication 800-82, Rev. 3** (2023). *Guide to Operational Technology (OT) Security.*
"""
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"[OK] Generated Rapid Response Draft: {target_file}")
    return target_file

def main():
    print("[*] Health Earth Hack Research — Policy & News Sentinel running...")
    items = fetch_feed_items()
    print(f"[*] Retrieved {len(items)} latest news & policy item(s).")
    
    significant = filter_significant_events(items)
    print(f"[+] Found {len(significant)} high-impact event(s) matching your research niche:")
    
    for idx, event in enumerate(significant[:5], 1):
        print(f"  {idx}. [{event['source']}] {event['title'][:85]}...")
        print(f"     Keywords: {', '.join(event['matched_keywords'])}")
        print(f"     Link: {event['url'][:75]}...")

    if "--scaffold" in sys.argv and significant:
        top_event = significant[0]
        print(f"\n[*] Scaffolding publication for top event: {top_event['title']}")
        scaffold_rapid_response_paper(top_event)
        print("[*] Run 'python scripts/build_publications.py' to compile into PDF.")

if __name__ == "__main__":
    main()
