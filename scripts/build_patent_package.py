import os
import subprocess
import markdown

PATENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "legal", "patents", "provisional_01")
OUTPUT_HTML = os.path.join(PATENT_DIR, "USPTO_PROVISIONAL_PATENT_APPLICATION_PRINT_READY.html")
OUTPUT_PDF = os.path.join(PATENT_DIR, "USPTO_PROVISIONAL_PATENT_APPLICATION_PRINT_READY.pdf")

FILES_TO_MERGE = [
    "FORM_PTO_SB_16_COVER_SHEET.md",
    "FORM_PTO_SB_15A_MICRO_ENTITY.md",
    "PROVISIONAL_SPECIFICATION.md",
    "PATENT_DRAWINGS.md"
]

HTML_WRAPPER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>USPTO Provisional Patent Application — Andrew Charles Kieckhefer</title>
    <style>
        @page {{
            size: letter;
            margin: 25mm 20mm 25mm 20mm;
            @top-right {{
                content: "USPTO PROVISIONAL PATENT APPLICATION";
                font-family: 'Courier New', Courier, monospace;
                font-size: 8pt;
                color: #444;
            }}
            @bottom-center {{
                content: "Page " counter(page);
                font-family: 'Courier New', Courier, monospace;
                font-size: 9pt;
            }}
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 11pt;
            line-height: 1.5;
            color: #000;
            background: #fff;
            padding: 20px;
        }}
        .page-break {{
            page-break-after: always;
        }}
        h1 {{
            font-size: 16pt;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            margin-bottom: 20px;
            line-height: 1.3;
        }}
        h2 {{
            font-size: 13pt;
            font-weight: bold;
            text-transform: uppercase;
            margin-top: 24px;
            margin-bottom: 12px;
            border-bottom: 1px solid #000;
            padding-bottom: 4px;
        }}
        h3 {{
            font-size: 11.5pt;
            font-weight: bold;
            margin-top: 18px;
            margin-bottom: 8px;
        }}
        p {{
            margin-bottom: 12px;
            text-align: justify;
            text-justify: inter-word;
        }}
        pre, code {{
            font-family: 'Courier New', Courier, monospace;
            font-size: 8.5pt;
            background: #fdfdfd;
        }}
        pre {{
            border: 1px solid #999;
            padding: 12px;
            line-height: 1.25;
            overflow-x: hidden;
            white-space: pre-wrap;
            margin: 16px 0;
        }}
        hr {{
            border: none;
            border-top: 1px solid #ccc;
            margin: 20px 0;
        }}
        ul, ol {{
            margin: 10px 0 14px 24px;
        }}
        li {{
            margin-bottom: 6px;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>
"""

def build():
    merged_md = []
    for fname in FILES_TO_MERGE:
        fpath = os.path.join(PATENT_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                merged_md.append(f.read())
            merged_md.append("\n\n<div class='page-break'></div>\n\n")

    full_text = "\n".join(merged_md)
    html_body = markdown.markdown(full_text, extensions=["tables", "fenced_code"])
    full_html = HTML_WRAPPER.format(content=html_body)

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[OK] Generated Patent Package HTML: {OUTPUT_HTML}")

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if os.path.exists(chrome_path):
        cmd = [
            chrome_path,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={OUTPUT_PDF}",
            OUTPUT_HTML
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if os.path.exists(OUTPUT_PDF):
                size = os.path.getsize(OUTPUT_PDF)
                print(f"[OK] Generated Print-Ready Patent PDF: {OUTPUT_PDF} ({size:,} bytes)")
        except Exception as e:
            print(f"[ERR] Failed to compile PDF: {e}")

if __name__ == "__main__":
    build()
