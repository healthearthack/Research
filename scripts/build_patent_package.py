import os
import subprocess
import shutil
import markdown

PATENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "legal", "patents", "provisional_01")
DESKTOP_DIR = r"C:\Users\Owner\Desktop"
OUTPUT_HTML = os.path.join(PATENT_DIR, "USPTO_PROVISIONAL_PATENT_APPLICATION_PRINT_READY.html")
OUTPUT_PDF = os.path.join(PATENT_DIR, "USPTO_PROVISIONAL_PATENT_APPLICATION_PRINT_READY.pdf")
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

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

FORM_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        @page {{
            size: letter portrait;
            margin: 15mm 15mm 15mm 15mm;
            @top-right {{
                content: "{header_tag}";
                font-family: 'Courier New', Courier, monospace;
                font-size: 8pt;
                color: #555;
            }}
            @bottom-center {{
                content: "Page 1 of 1";
                font-family: 'Courier New', Courier, monospace;
                font-size: 8pt;
            }}
        }}
        * {{ box-sizing: border-box; }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            font-size: 9.5pt;
            line-height: 1.3;
            color: #000;
            background: #fff;
            margin: 0;
            padding: 0;
        }}
        h1 {{
            font-size: 12pt;
            font-weight: bold;
            text-align: center;
            text-transform: uppercase;
            margin: 0 0 4px 0;
            line-height: 1.2;
        }}
        h2 {{
            font-size: 10pt;
            font-weight: bold;
            text-transform: uppercase;
            margin: 8px 0 3px 0;
            border-bottom: 1px solid #000;
            padding-bottom: 2px;
        }}
        h3 {{
            font-size: 9.5pt;
            font-weight: bold;
            margin: 6px 0 2px 0;
        }}
        p {{
            margin: 0 0 5px 0;
            text-align: justify;
        }}
        em {{
            display: block;
            text-align: center;
            font-size: 8.5pt;
            color: #333;
            margin-bottom: 5px;
        }}
        pre, code {{
            font-family: 'Courier New', Courier, monospace;
            font-size: 8pt;
            background: #f8f8f8;
        }}
        pre {{
            border: 1px solid #bbb;
            padding: 3px 6px;
            margin: 3px 0;
            white-space: pre-wrap;
        }}
        hr {{
            border: none;
            border-top: 1px solid #888;
            margin: 5px 0;
        }}
        ul, ol {{
            margin: 2px 0 5px 18px;
            padding: 0;
        }}
        li {{
            margin-bottom: 2px;
        }}
    </style>
</head>
<body>
{content}
</body>
</html>
"""

def build():
    # 1. Build Merged Complete Application
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

    if os.path.exists(CHROME_PATH):
        cmd = [
            CHROME_PATH,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={OUTPUT_PDF}",
            OUTPUT_HTML
        ]
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if os.path.exists(OUTPUT_PDF):
                shutil.copy2(OUTPUT_PDF, os.path.join(DESKTOP_DIR, "USPTO_PROVISIONAL_PATENT_APPLICATION_PRINT_READY.pdf"))
                size = os.path.getsize(OUTPUT_PDF)
                print(f"[OK] Generated Print-Ready Full Patent PDF: {OUTPUT_PDF} ({size:,} bytes)")
        except Exception as e:
            print(f"[ERR] Failed to compile full PDF: {e}")

    # 2. Build Individual Standalone Forms
    forms = [
        {
            "md": "FORM_PTO_SB_16_COVER_SHEET.md",
            "title": "USPTO Form PTO/SB/16 - Provisional Application Cover Sheet",
            "tag": "USPTO FORM PTO/SB/16 (COVER SHEET)",
            "pdf_name": "FORM_PTO_SB_16_COVER_SHEET.pdf"
        },
        {
            "md": "FORM_PTO_SB_15A_MICRO_ENTITY.md",
            "title": "USPTO Form PTO/SB/15A - Certification of Micro Entity Status",
            "tag": "USPTO FORM PTO/SB/15A (MICRO ENTITY)",
            "pdf_name": "FORM_PTO_SB_15A_MICRO_ENTITY.pdf"
        }
    ]

    for item in forms:
        fpath = os.path.join(PATENT_DIR, item["md"])
        if os.path.exists(fpath):
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            body = markdown.markdown(content, extensions=["tables", "fenced_code"])
            html = FORM_TEMPLATE.format(title=item["title"], header_tag=item["tag"], content=body)
            temp_html = os.path.join(PATENT_DIR, item["pdf_name"].replace(".pdf", ".html"))
            with open(temp_html, "w", encoding="utf-8") as f:
                f.write(html)
            
            target_pdf = os.path.join(PATENT_DIR, item["pdf_name"])
            cmd = [
                CHROME_PATH,
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                f"--print-to-pdf={target_pdf}",
                temp_html
            ]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            desktop_pdf = os.path.join(DESKTOP_DIR, item["pdf_name"])
            shutil.copy2(target_pdf, desktop_pdf)
            size = os.path.getsize(desktop_pdf)
            print(f"[OK] Generated Standalone Form: {item['pdf_name']} ({size:,} bytes) -> Desktop & Repo")

if __name__ == "__main__":
    build()
