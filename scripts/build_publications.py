import os
import glob
import subprocess
import markdown

DRAFTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "publications", "drafts")
DIST_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "publications", "dist")
os.makedirs(DIST_DIR, exist_ok=True)

METADATA = {
    "WP01_DLE_Wellbore_Repurposing_Review": {
        "title": "Direct Lithium Extraction (DLE) from Continental Petroleum Brines: Repurposing Late-Life Wellbores for Closed-Loop Battery Mineral Recovery",
        "authors": "Andrew C. Kieckhefer",
        "affiliations": "Institute of GeoEnergy Engineering, Heriot-Watt University, Edinburgh EH14 4AS, UK<br>Department of Atmospheric and Oceanic Sciences, University of Wisconsin–Madison, Madison, WI 53706, USA",
        "email": "weather.amazon.go@gmail.com | andy.kieckhefer@gmail.com",
        "server": "EarthArXiv",
        "journal": "Applied Energy",
        "date": "September 2026",
    },
    "WP02_OT_Cybersecurity_SCADA_Telemetry": {
        "title": "Physics-Informed Anomaly Detection in Upstream SCADA Networks: Mitigating Sensor Spoofing in High-Pressure Hydrothermal Wellheads",
        "authors": "Andrew C. Kieckhefer",
        "affiliations": "Institute of GeoEnergy Engineering, Heriot-Watt University, Edinburgh EH14 4AS, UK<br>Department of Atmospheric and Oceanic Sciences, University of Wisconsin–Madison, Madison, WI 53706, USA",
        "email": "weather.amazon.go@gmail.com | andy.kieckhefer@gmail.com",
        "server": "EarthArXiv",
        "journal": "IEEE Transactions on Industrial Informatics",
        "date": "September 2026",
    },
    "WP03_Satellite_Subsurface_Emissions_Coupling": {
        "title": "Coupling Spaceborne Trace Gas Spectrometry with Wellhead Distributed Acoustic Sensing for IRA 45X Zero-Emissions Verification",
        "authors": "Andrew C. Kieckhefer",
        "affiliations": "Institute of GeoEnergy Engineering, Heriot-Watt University, Edinburgh EH14 4AS, UK<br>Department of Atmospheric and Oceanic Sciences, University of Wisconsin–Madison, Madison, WI 53706, USA",
        "email": "weather.amazon.go@gmail.com | andy.kieckhefer@gmail.com",
        "server": "EarthArXiv / ESS Open Archive",
        "journal": "Environmental Research Letters",
        "date": "September 2026",
    },
    "WP04_Edge_To_Wellhead_Cyber_Physical_Synthesis": {
        "title": "From Edge to Wellhead: Translating Software-Defined Telemetry and Industrial IoT into Resilient Subsurface GeoEnergy Systems",
        "authors": "Andrew C. Kieckhefer",
        "affiliations": "Institute of GeoEnergy Engineering, Heriot-Watt University, Edinburgh EH14 4AS, UK<br>Department of Atmospheric and Oceanic Sciences, University of Wisconsin–Madison, Madison, WI 53706, USA",
        "email": "weather.amazon.go@gmail.com | andy.kieckhefer@gmail.com",
        "server": "EarthArXiv",
        "journal": "IEEE Internet of Things Magazine / Applied Energy",
        "date": "September 2026",
    }
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        @page {{
            size: letter;
            margin: 20mm 18mm 22mm 18mm;
            @top-right {{
                content: "PREPRINT / WORKING PAPER SERIES";
                font-family: 'Times New Roman', serif;
                font-size: 8pt;
                color: #555;
            }}
            @bottom-center {{
                content: "Page " counter(page);
                font-family: 'Times New Roman', serif;
                font-size: 9pt;
            }}
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Times New Roman', Times, 'Georgia', serif;
            font-size: 10.5pt;
            line-height: 1.45;
            color: #111;
            margin: 0;
            padding: 24px;
            background: #fff;
        }}
        .coversheet {{
            page-break-after: always;
            padding: 20px 10px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }}
        .coversheet-header {{
            font-size: 11pt;
            font-weight: 700;
            color: #0284c7;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            margin-bottom: 8px;
        }}
        .coversheet-rule {{
            border-top: 3px solid #0284c7;
            margin-bottom: 28px;
        }}
        .coversheet-title {{
            font-size: 19pt;
            font-weight: 800;
            line-height: 1.3;
            color: #0f172a;
            margin-bottom: 24px;
            text-align: left;
        }}
        .coversheet-meta {{
            font-size: 10.5pt;
            line-height: 1.65;
            color: #1e293b;
            margin-bottom: 24px;
        }}
        .coversheet-box {{
            background: #f8fafc;
            border: 1px solid #cbd5e1;
            border-left: 6px solid #0284c7;
            padding: 16px 20px;
            margin: 24px 0;
            border-radius: 4px;
        }}
        .coversheet-box h3 {{
            margin-top: 0;
            margin-bottom: 8px;
            color: #0f172a;
            font-size: 12pt;
        }}
        .coversheet-box p {{
            margin: 6px 0;
            font-size: 10pt;
            line-height: 1.5;
            color: #1e293b;
        }}
        .coversheet-footer {{
            margin-top: 36px;
            font-size: 9pt;
            line-height: 1.6;
            color: #64748b;
            border-top: 1px solid #e2e8f0;
            padding-top: 16px;
        }}
        .banner {{
            background: #f1f5f9;
            border-left: 4px solid #0284c7;
            padding: 8px 14px;
            font-size: 9pt;
            color: #334155;
            margin-bottom: 24px;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        }}
        h1 {{
            font-size: 18pt;
            font-weight: bold;
            line-height: 1.25;
            margin-bottom: 12px;
            color: #0f172a;
            text-align: center;
        }}
        h2 {{
            font-size: 13pt;
            font-weight: bold;
            margin-top: 22px;
            margin-bottom: 8px;
            color: #1e293b;
            border-bottom: 1px solid #cbd5e1;
            padding-bottom: 3px;
        }}
        h3 {{
            font-size: 11pt;
            font-weight: bold;
            margin-top: 14px;
            margin-bottom: 6px;
            color: #334155;
        }}
        p {{
            margin-bottom: 10px;
            text-align: justify;
            text-justify: inter-word;
        }}
        blockquote {{
            background: #f8fafc;
            border-left: 3px solid #64748b;
            margin: 14px 0;
            padding: 10px 16px;
            font-style: italic;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 16px 0;
            font-size: 9pt;
        }}
        th, td {{
            border: 1px solid #cbd5e1;
            padding: 6px 10px;
            text-align: left;
        }}
        th {{
            background: #f1f5f9;
            font-weight: bold;
            color: #0f172a;
        }}
        pre, code {{
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 8.5pt;
            background: #f8fafc;
        }}
        pre {{
            border: 1px solid #e2e8f0;
            border-radius: 4px;
            padding: 10px 14px;
            overflow-x: auto;
            line-height: 1.35;
        }}
        hr {{
            border: none;
            border-top: 1px solid #e2e8f0;
            margin: 18px 0;
        }}
        ul, ol {{
            margin: 8px 0 12px 20px;
            padding: 0;
        }}
        li {{
            margin-bottom: 4px;
        }}
    </style>
</head>
<body>
    {coversheet}
    <div class="banner">
        <strong>ACADEMIC PREPRINT SERIES</strong> | Author: Andrew C. Kieckhefer | Google Scholar Anchor: <code>weather.amazon.go@gmail.com</code> | Heriot-Watt University & UW–Madison
    </div>
    {content}
</body>
</html>
"""

def find_browser():
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    return None

def build():
    md_files = glob.glob(os.path.join(DRAFTS_DIR, "*.md"))
    if not md_files:
        print("No markdown drafts found in:", DRAFTS_DIR)
        return

    browser = find_browser()
    print(f"[*] Found {len(md_files)} manuscript(s) to compile...")
    if browser:
        print(f"[*] Using browser for PDF rendering: {browser}")
    else:
        print("[!] No headless browser found. Compiling HTML only.")

    for path in md_files:
        basename = os.path.splitext(os.path.basename(path))[0]
        html_out = os.path.join(DIST_DIR, f"{basename}.html")
        pdf_out = os.path.join(DIST_DIR, f"{basename}.pdf")

        meta = METADATA.get(basename, {
            "title": basename.replace("_", " "),
            "authors": "Andrew C. Kieckhefer",
            "affiliations": "Heriot-Watt University & UW–Madison AOS",
            "email": "weather.amazon.go@gmail.com",
            "server": "EarthArXiv",
            "journal": "Applied Energy",
            "date": "September 2026",
        })

        coversheet_html = f"""
        <div class="coversheet">
            <div class="coversheet-header">{meta['server']} PREPRINT SERIES &bull; COVERSHEET</div>
            <div class="coversheet-rule"></div>
            <div class="coversheet-title">{meta['title']}</div>
            
            <div class="coversheet-meta">
                <p><strong>Authors:</strong> {meta['authors']}</p>
                <p><strong>Affiliations:</strong><br>{meta['affiliations']}</p>
                <p><strong>Corresponding Author Email:</strong> <code>{meta['email']}</code></p>
            </div>

            <div class="coversheet-box">
                <h3>Preprint Status & Peer Review Statement</h3>
                <p><strong>Preprint Status:</strong> This is a non-peer reviewed preprint submitted to <strong>{meta['server']}</strong>.</p>
                <p><strong>Peer Review Status:</strong> This manuscript has been submitted to <em>{meta['journal']}</em> for peer review.</p>
            </div>

            <div class="coversheet-footer">
                <p><strong>License:</strong> Distributed under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International (CC BY 4.0) License</a>.</p>
                <p><strong>Repository Code & Data:</strong> <a href="https://github.com/healthearthack/Research">https://github.com/healthearthack/Research</a></p>
                <p><strong>Publication Date:</strong> {meta['date']}</p>
            </div>
        </div>
        """

        with open(path, "r", encoding="utf-8") as f:
            md_text = f.read()

        html_body = markdown.markdown(
            md_text,
            extensions=["tables", "fenced_code", "attr_list", "def_list"]
        )

        title = meta["title"]
        full_html = HTML_TEMPLATE.format(title=title, coversheet=coversheet_html, content=html_body)

        with open(html_out, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[OK] Generated HTML with Page 1 Coversheet: {html_out}")

        if browser:
            cmd = [
                browser,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_out}",
                html_out
            ]
            try:
                subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if os.path.exists(pdf_out):
                    size = os.path.getsize(pdf_out)
                    print(f"[OK] Generated Compliant PDF: {pdf_out} ({size:,} bytes)")
                else:
                    print(f"[!] PDF file not generated: {pdf_out}")
            except Exception as e:
                print(f"[ERR] Failed to render PDF for {basename}: {e}")

    generate_index_portal()
    print("[*] Compilation process complete.")

def generate_index_portal():
    index_file = os.path.join(DIST_DIR, "index.html")
    cards = []
    
    for key, meta in METADATA.items():
        pdf_name = f"{key}.pdf"
        html_name = f"{key}.html"
        cards.append(f"""
        <div class="pub-card">
            <div class="pub-badge">{meta['server']} &bull; {meta['date']}</div>
            <h2 class="pub-title">{meta['title']}</h2>
            <div class="pub-authors"><strong>Author:</strong> {meta['authors']}</div>
            <div class="pub-affil"><em>{meta['affiliations'].replace('<br>', ' &bull; ')}</em></div>
            <div class="pub-target">Target Journal: <strong>{meta['journal']}</strong></div>
            <div class="pub-actions">
                <a class="btn btn-pdf" href="{pdf_name}" target="_blank">📄 Download PDF</a>
                <a class="btn btn-html" href="{html_name}" target="_blank">🌐 Read HTML</a>
                <a class="btn btn-code" href="https://github.com/healthearthack/Research" target="_blank">💻 View Code</a>
            </div>
        </div>
        """)

    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Earth Hack Research Laboratory &bull; Public Publications Portal</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: #0f172a;
            color: #f8fafc;
            line-height: 1.6;
            padding: 40px 20px;
        }}
        .container {{
            max-width: 960px;
            margin: 0 auto;
        }}
        header {{
            border-bottom: 1px solid #334155;
            padding-bottom: 24px;
            margin-bottom: 32px;
        }}
        h1 {{
            font-size: 26pt;
            font-weight: 800;
            color: #38bdf8;
            letter-spacing: -0.5px;
            margin-bottom: 8px;
        }}
        .lead {{
            font-size: 11pt;
            color: #94a3b8;
        }}
        .nav-links {{
            margin-top: 14px;
            display: flex;
            gap: 16px;
            flex-wrap: wrap;
        }}
        .nav-links a {{
            color: #38bdf8;
            text-decoration: none;
            font-size: 9.5pt;
            font-weight: 600;
        }}
        .nav-links a:hover {{ text-decoration: underline; }}
        .pub-card {{
            background: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 24px;
            margin-bottom: 24px;
            transition: transform 0.15s ease, border-color 0.15s ease;
        }}
        .pub-card:hover {{
            transform: translateY(-2px);
            border-color: #38bdf8;
        }}
        .pub-badge {{
            font-size: 8.5pt;
            font-weight: 700;
            color: #38bdf8;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            margin-bottom: 8px;
        }}
        .pub-title {{
            font-size: 15pt;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 10px;
            line-height: 1.35;
        }}
        .pub-authors {{
            font-size: 10pt;
            color: #e2e8f0;
            margin-bottom: 4px;
        }}
        .pub-affil {{
            font-size: 9pt;
            color: #94a3b8;
            margin-bottom: 10px;
        }}
        .pub-target {{
            font-size: 9pt;
            color: #cbd5e1;
            margin-bottom: 18px;
        }}
        .pub-actions {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .btn {{
            display: inline-block;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 9.5pt;
            font-weight: 600;
            text-decoration: none;
            transition: opacity 0.2s ease;
        }}
        .btn:hover {{ opacity: 0.85; }}
        .btn-pdf {{ background: #0284c7; color: #ffffff; }}
        .btn-html {{ background: #334155; color: #f8fafc; }}
        .btn-code {{ background: #10b981; color: #ffffff; }}
        footer {{
            text-align: center;
            margin-top: 48px;
            padding-top: 24px;
            border-top: 1px solid #334155;
            font-size: 9pt;
            color: #64748b;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Health Earth Hack Research Laboratory</h1>
            <p class="lead">Open-Access Working Papers, Preprints & Cyber-Physical GeoEnergy Systems</p>
            <div class="nav-links">
                <a href="https://scholar.google.com/citations" target="_blank">🎓 Google Scholar Profile</a>
                <a href="https://github.com/healthearthack/Research" target="_blank">💻 GitHub Repository</a>
                <a href="https://thepolka.cloud/forecast" target="_blank">🌐 Real-Time Forecast Portal</a>
                <a href="http://website.oil:8000" target="_blank">🛢️ Wellbore SCADA Gateway (8000)</a>
            </div>
        </header>

        <main>
            {"".join(cards)}
        </main>

        <footer>
            <p>Authored by Andrew C. Kieckhefer &bull; Department of Atmospheric and Oceanic Sciences (Alum), UW–Madison</p>
            <p>Distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License.</p>
        </footer>
    </div>
</body>
</html>
"""
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"[OK] Generated Public Portal: {index_file}")

if __name__ == "__main__":
    build()


