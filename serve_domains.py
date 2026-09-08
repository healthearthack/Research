#!/usr/bin/env python3
"""
Dual-Domain Local Server:
  - website.oil:8000  -> Subsurface Wellhead Barrier SCADA & HELP WANTED Board
  - website.h2o:8001  -> Hydrothermal Brine / Smart Water & HELP WANTED Board
"""

import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "data" / "sample_wellhead_stream.json"

def get_telemetry():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# ---------------------------------------------------------------------------
# HTML: website.oil:8000 (Subsurface Barrier & Help Wanted)
# ---------------------------------------------------------------------------

WEBSITE_OIL_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>website.oil:8000 | Subsurface Barrier & Help Wanted</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif; }
        body { background-color: #0b0f19; color: #f3f4f6; padding: 28px; line-height: 1.5; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #f59e0b; padding-bottom: 18px; margin-bottom: 24px; }
        .host-badge { background: #d97706; color: #000; font-weight: 800; font-size: 16px; padding: 6px 14px; border-radius: 6px; font-family: monospace; letter-spacing: 0.5px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; margin-bottom: 28px; }
        .card { background: #111827; border: 1px solid #374151; border-radius: 8px; padding: 18px; position: relative; }
        .card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #f59e0b; }
        .label { font-size: 11px; color: #9ca3af; text-transform: uppercase; font-weight: 700; margin-bottom: 6px; }
        .value { font-size: 28px; font-weight: 800; color: #fbbf24; font-family: monospace; }
        .sub { font-size: 12px; color: #6b7280; margin-top: 4px; }
        .status-ok { color: #10b981; font-weight: 700; }
        
        /* Help Wanted Section */
        .section-title { font-size: 20px; font-weight: 800; color: #f59e0b; margin: 28px 0 16px 0; display: flex; align-items: center; gap: 10px; }
        .help-wanted-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px; margin-bottom: 28px; }
        .job-card { background: #182234; border: 1px solid #b45309; border-radius: 8px; padding: 20px; transition: transform 0.15s; }
        .job-card:hover { transform: translateY(-2px); border-color: #f59e0b; }
        .job-tag { background: #78350f; color: #fde68a; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; font-family: monospace; }
        .job-title { font-size: 16px; font-weight: 700; color: #fff; margin: 10px 0 6px 0; }
        .job-desc { font-size: 13px; color: #cbd5e1; margin-bottom: 12px; }
        .job-reqs { font-size: 12px; color: #94a3b8; background: #0f172a; padding: 8px 12px; border-radius: 6px; font-family: monospace; }
        
        .nav-bar { background: #1f2937; padding: 16px 22px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; }
        .btn { background: #0284c7; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: 700; font-size: 14px; }
        .btn:hover { background: #0369a1; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1 style="font-size: 26px; color: #f59e0b;">🛢️ WEBSITE.OIL:8000 — SUBSURFACE BARRIER DIGITAL TWIN</h1>
            <p style="color: #9ca3af; margin-top: 4px;">Host Address: <strong>http://website.oil:8000</strong> (or <code>http://localhost:8000</code>) | Facility: HWU-SMACKOVER-ALPHA-01</p>
        </div>
        <div class="host-badge">website.oil:8000</div>
    </div>

    <!-- Live Telemetry -->
    <div class="grid">
        <div class="card">
            <div class="label">Annular Casing Pressure</div>
            <div class="value">842.1 <span style="font-size: 16px;">psi</span></div>
            <div class="sub">Threshold: &lt; 1,200 psi | <span class="status-ok">BARRIER INTEGRITY SECURE</span></div>
        </div>
        <div class="card">
            <div class="label">Fiber DAS Acoustic Strain</div>
            <div class="value">1.45 <span style="font-size: 16px;">kHz</span></div>
            <div class="sub">SPE-21820 Downhole Inflow | <span class="status-ok">NOMINAL FREQUENCY</span></div>
        </div>
        <div class="card">
            <div class="label">Reservoir Depth & Temp</div>
            <div class="value">128.4 <span style="font-size: 16px;">°C</span></div>
            <div class="sub">10,450 ft MD / 9,820 ft TVD (Smackover Formation)</div>
        </div>
        <div class="card">
            <div class="label">Surface Fugitive Methane</div>
            <div class="value">0.020 <span style="font-size: 16px;">kg/hr</span></div>
            <div class="sub">IRA 45X Standard: <span class="status-ok">CERTIFIED ZERO-LEAKAGE</span></div>
        </div>
    </div>

    <!-- Help Wanted Board -->
    <div class="section-title">
        <span>🚨 OPEN RESEARCH REQUISITIONS ("HELP WANTED") — .OIL:8000 DOMAIN</span>
    </div>

    <div class="help-wanted-container">
        <!-- Role 1 -->
        <div class="job-card">
            <span class="job-tag">REQUISITION: OIL-01</span>
            <div class="job-title">Subsurface OT Threat & SCADA Telemetry Lead</div>
            <div class="job-desc">Lead deep packet inspection and network segmentation for Modbus/TCP and DNP3 industrial RTUs under NIST SP 800-82 Rev. 3 and CISA energy advisories.</div>
            <div class="job-reqs">Skills: Python / C++ / SCADA / Wireshark / OT Security</div>
        </div>

        <!-- Role 2 -->
        <div class="job-card">
            <span class="job-tag">REQUISITION: OIL-02</span>
            <div class="job-title">Wellbore Geomechanics & Casing Barrier Specialist</div>
            <div class="job-desc">Model cyclic thermal and pressure stress on legacy steel casing under continuous high-flow brine co-extraction (>120°C) to eliminate blowout and leakage risks.</div>
            <div class="job-reqs">Skills: Petroleum Engineering / Rock Mechanics / FEA Modeling</div>
        </div>

        <!-- Role 3 -->
        <div class="job-card">
            <span class="job-tag">REQUISITION: OIL-03</span>
            <div class="job-title">Orbital Satellite Remote Sensing Ground-Truther</div>
            <div class="job-desc">Couple orbital TROPOMI (Sentinel-5P) and NASA TEMPO trace gas columns with wellhead sensor arrays to verify zero fugitive emissions across repurposed wellheads.</div>
            <div class="job-reqs">Skills: Atmospheric Science / NetCDF / Python / NASA Earthdata</div>
        </div>
    </div>

    <div class="nav-bar">
        <div>
            <strong>Cross-Domain Flow:</strong> Hydrothermal brine flows from this .oil barrier into the .h2o recovery circuit.
        </div>
        <div>
            <a href="http://localhost:8001" class="btn">💧 Launch website.h2o:8001 (Smart Water Site) →</a>
        </div>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# HTML: website.h2o:8001 (Smart Water & Help Wanted)
# ---------------------------------------------------------------------------

WEBSITE_H2O_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>website.h2o:8001 | Smart Water & Help Wanted</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif; }
        body { background-color: #030d1a; color: #f0fdfa; padding: 28px; line-height: 1.5; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 3px solid #0284c7; padding-bottom: 18px; margin-bottom: 24px; }
        .host-badge { background: #0284c7; color: #fff; font-weight: 800; font-size: 16px; padding: 6px 14px; border-radius: 6px; font-family: monospace; letter-spacing: 0.5px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 18px; margin-bottom: 28px; }
        .card { background: #082f49; border: 1px solid #075985; border-radius: 8px; padding: 18px; position: relative; }
        .card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #38bdf8; }
        .label { font-size: 11px; color: #7dd3fc; text-transform: uppercase; font-weight: 700; margin-bottom: 6px; }
        .value { font-size: 28px; font-weight: 800; color: #38bdf8; font-family: monospace; }
        .sub { font-size: 12px; color: #94a3b8; margin-top: 4px; }
        .status-ok { color: #34d399; font-weight: 700; }
        
        /* Help Wanted Section */
        .section-title { font-size: 20px; font-weight: 800; color: #38bdf8; margin: 28px 0 16px 0; display: flex; align-items: center; gap: 10px; }
        .help-wanted-container { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 18px; margin-bottom: 28px; }
        .job-card { background: #0c4a6e; border: 1px solid #0284c7; border-radius: 8px; padding: 20px; transition: transform 0.15s; }
        .job-card:hover { transform: translateY(-2px); border-color: #38bdf8; }
        .job-tag { background: #0369a1; color: #e0f2fe; padding: 3px 8px; border-radius: 4px; font-size: 11px; font-weight: 700; font-family: monospace; }
        .job-title { font-size: 16px; font-weight: 700; color: #fff; margin: 10px 0 6px 0; }
        .job-desc { font-size: 13px; color: #cbd5e1; margin-bottom: 12px; }
        .job-reqs { font-size: 12px; color: #7dd3fc; background: #082f49; padding: 8px 12px; border-radius: 6px; font-family: monospace; }
        
        .nav-bar { background: #075985; padding: 16px 22px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; }
        .btn { background: #f59e0b; color: #000; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: 700; font-size: 14px; }
        .btn:hover { background: #d97706; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1 style="font-size: 26px; color: #38bdf8;">💧 WEBSITE.H2O:8001 — SMART WATER & DLE DIGITAL TWIN</h1>
            <p style="color: #94a3b8; margin-top: 4px;">Host Address: <strong>http://website.h2o:8001</strong> (or <code>http://localhost:8001</code>) | Faculty Alignment: Dr. Christos Chrysoulas</p>
        </div>
        <div class="host-badge">website.h2o:8001</div>
    </div>

    <!-- Live Telemetry -->
    <div class="grid">
        <div class="card">
            <div class="label">Brine Volumetric Throughput</div>
            <div class="value">14,200 <span style="font-size: 16px;">bpd</span></div>
            <div class="sub">Continuous Feed (GWPC 2024 Produced Water Census)</div>
        </div>
        <div class="card">
            <div class="label">Daily Pure Lithium Yield</div>
            <div class="value" style="color: #34d399;">803.1 <span style="font-size: 16px;">kg/day</span></div>
            <div class="sub">Equivalent to <strong>4,275.0 kg/day LCE</strong> battery grade</div>
        </div>
        <div class="card">
            <div class="label">Geothermal ORC Power</div>
            <div class="value">850 <span style="font-size: 16px;">kW</span></div>
            <div class="sub">20.4 MWh/day Baseload (Inlet 112.8°C / Outlet 64.1°C)</div>
        </div>
        <div class="card">
            <div class="label">Resin Bed Differential P</div>
            <div class="value">18.4 <span style="font-size: 16px;">psi</span></div>
            <div class="sub">Kumar et al. (2024) Kinetics | <span class="status-ok">OPTIMAL FLOW</span></div>
        </div>
    </div>

    <!-- Help Wanted Board -->
    <div class="section-title">
        <span>🚨 OPEN RESEARCH REQUISITIONS ("HELP WANTED") — .H2O:8001 DOMAIN</span>
    </div>

    <div class="help-wanted-container">
        <!-- Role 1 -->
        <div class="job-card">
            <span class="job-tag">REQUISITION: H2O-01</span>
            <div class="job-title">Direct Lithium Extraction (DLE) Process Engineer</div>
            <div class="job-desc">Synthesize selective ion-exchange and sorption kinetics for Smackover formation waters (385 ppm Li) to optimize elution purity and resin life cycles.</div>
            <div class="job-reqs">Skills: Chemical Engineering / Separation Science / PHREEQC</div>
        </div>

        <!-- Role 2 -->
        <div class="job-card">
            <span class="job-tag">REQUISITION: H2O-02</span>
            <div class="job-title">Smart Water SCADA & Reinjection Hydraulics Lead</div>
            <div class="job-desc">Design distributed IoT telemetry control loops managing high-pressure reinjection (2,100 psi) under Dr. Christos Chrysoulas's Smart Water Management paradigm.</div>
            <div class="job-reqs">Skills: Industrial IoT / Control Systems / Fluid Mechanics</div>
        </div>

        <!-- Role 3 -->
        <div class="job-card">
            <span class="job-tag">REQUISITION: H2O-03</span>
            <div class="job-title">Geothermal Binary ORC Thermodynamic Engineer</div>
            <div class="job-desc">Optimize binary Organic Rankine Cycle working fluid heat transfer to harvest 850 kW net electrical output from co-produced brine enthalpy.</div>
            <div class="job-reqs">Skills: Thermodynamics / Heat Exchangers / Python Energy Models</div>
        </div>
    </div>

    <div class="nav-bar">
        <div>
            <strong>Supervisory Nexus:</strong> Dr. Christos Chrysoulas — Smart Water Management Systems (Heriot-Watt University).
        </div>
        <div>
            <a href="http://localhost:8000" class="btn">🛢️ Launch website.oil:8000 (Subsurface Site) →</a>
        </div>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# Request Handlers
# ---------------------------------------------------------------------------

class OilHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(WEBSITE_OIL_HTML.encode("utf-8"))

    def log_message(self, format, *args):
        pass


class H2OHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(WEBSITE_H2O_HTML.encode("utf-8"))

    def log_message(self, format, *args):
        pass


def run_server(handler_class, port, name):
    server = HTTPServer(("0.0.0.0", port), handler_class)
    print(f"[+] [{name}] ONLINE -> http://localhost:{port}")
    server.serve_forever()


def main():
    print("=" * 70)
    print("[*] LAUNCHING DUAL-DOMAIN SITES: website.oil:8000 & website.h2o:8001")
    print("=" * 70)

    # Port 8000: website.oil:8000
    t_oil = threading.Thread(
        target=run_server,
        args=(OilHandler, 8000, "website.oil:8000 (Subsurface Barrier & Help Wanted)"),
        daemon=True,
    )
    t_oil.start()

    # Port 8001: website.h2o:8001
    t_h2o = threading.Thread(
        target=run_server,
        args=(H2OHandler, 8001, "website.h2o:8001 (Smart Water & Help Wanted)"),
        daemon=True,
    )
    t_h2o.start()

    print("=" * 70)
    print("[+] BOTH SITES ACTIVE & SERVING:")
    print("   [+] website.oil:8000 -> http://localhost:8000 (or http://website.oil:8000)")
    print("   [+] website.h2o:8001 -> http://localhost:8001 (or http://website.h2o:8001)")
    print("=" * 70)
    print("Press Ctrl+C to terminate.")

    try:
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\n[*] Shutting down servers.")


if __name__ == "__main__":
    main()
