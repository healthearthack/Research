import os
import glob
import subprocess
import markdown

DRAFTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "publications", "drafts")
DIST_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "publications", "dist")
os.makedirs(DIST_DIR, exist_ok=True)

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

        with open(path, "r", encoding="utf-8") as f:
            md_text = f.read()

        html_body = markdown.markdown(
            md_text,
            extensions=["tables", "fenced_code", "attr_list", "def_list"]
        )

        title = basename.replace("_", " ")
        full_html = HTML_TEMPLATE.format(title=title, content=html_body)

        with open(html_out, "w", encoding="utf-8") as f:
            f.write(full_html)
        print(f"[OK] Generated HTML: {html_out}")

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
                    print(f"[OK] Generated PDF: {pdf_out} ({size:,} bytes)")
                else:
                    print(f"[!] PDF file not generated: {pdf_out}")
            except Exception as e:
                print(f"[ERR] Failed to render PDF for {basename}: {e}")

    print("[*] Compilation process complete.")

if __name__ == "__main__":
    build()
