#!/usr/bin/env python3
"""
Dual-Domain Local Server: Launches .oil (Port 8001) and .h2o (Port 8002) Sites.
Includes Gateway Mission Control on Port 8000.
"""

import json
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path

# Load live telemetry data
DATA_FILE = Path(__file__).resolve().parent / "data" / "sample_wellhead_stream.json"

def get_telemetry():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# ---------------------------------------------------------------------------
# HTML Templates (Self-Contained, High-Impact Cyber SCADA & Aquatic Themes)
# ---------------------------------------------------------------------------

OIL_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>.oil Subsurface Wellhead Barrier | Digital Twin</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', -apple-system, sans-serif; }
        body { background-color: #0b0f19; color: #f3f4f6; padding: 24px; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #d97706; padding-bottom: 16px; margin-bottom: 24px; }
        .badge { background: #b45309; color: #fff; padding: 6px 12px; border-radius: 4px; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 24px; }
        .card { background: #111827; border: 1px solid #374151; border-radius: 8px; padding: 20px; position: relative; overflow: hidden; }
        .card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #f59e0b; }
        .label { font-size: 12px; color: #9ca3af; text-transform: uppercase; font-weight: 600; margin-bottom: 8px; }
        .value { font-size: 32px; font-weight: 800; color: #fbbf24; font-family: monospace; }
        .sub { font-size: 13px; color: #6b7280; margin-top: 6px; }
        .status-ok { color: #10b981; font-weight: 700; }
        .nav-bar { background: #1f2937; padding: 16px 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; }
        .btn { background: #0284c7; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: 600; display: inline-block; transition: background 0.2s; }
        .btn:hover { background: #0369a1; }
        .console { background: #030712; border: 1px solid #1f2937; border-radius: 8px; padding: 16px; font-family: monospace; font-size: 13px; color: #10b981; margin-top: 20px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1 style="font-size: 26px; color: #f59e0b;">🛢️ .OIL DIGITAL TWIN: SUBSURFACE BARRIER TELEMETRY</h1>
            <p style="color: #9ca3af; margin-top: 4px;">Host: <strong>wellbore-01.smackover.oil:8001</strong> | Facility: HWU-SMACKOVER-ALPHA-01</p>
        </div>
        <div class="badge">TLD: .OIL ACTIVE</div>
    </div>

    <div class="grid">
        <div class="card">
            <div class="label">Annular Casing Pressure</div>
            <div class="value">842.1 <span style="font-size: 18px;">psi</span></div>
            <div class="sub">Threshold: &lt; 1,200 psi | <span class="status-ok">NOMINAL INTEGRITY</span></div>
        </div>
        <div class="card">
            <div class="label">Fiber DAS Acoustic Strain</div>
            <div class="value">1.45 <span style="font-size: 18px;">kHz</span></div>
            <div class="sub">SPE-21820 Downhole Resonance | <span class="status-ok">NO CASING SHEAR</span></div>
        </div>
        <div class="card">
            <div class="label">Reservoir Depth & Temp</div>
            <div class="value">128.4 <span style="font-size: 18px;">°C</span></div>
            <div class="sub">10,450 ft MD / 9,820 ft TVD (Smackover Fm)</div>
        </div>
        <div class="card">
            <div class="label">Surface Fugitive Methane</div>
            <div class="value">0.020 <span style="font-size: 18px;">kg/hr</span></div>
            <div class="sub">IRA 45X Zero-Leakage: <span class="status-ok">CERTIFIED COMPLIANT</span></div>
        </div>
        <div class="card">
            <div class="label">SCADA Field Bus Protocol</div>
            <div class="value" style="font-size: 24px;">Modbus/DNP3</div>
            <div class="sub">NIST SP 800-82r3 Isolated | 0 Exceptions</div>
        </div>
        <div class="card">
            <div class="label">PLC Firmware Integrity</div>
            <div class="value" style="font-size: 20px; color: #10b981;">VERIFIED_SHA256</div>
            <div class="sub">Cryptographic Attestation Active</div>
        </div>
    </div>

    <div class="nav-bar">
        <div>
            <strong>Cross-Domain Linkage:</strong> Pressurized formation brine flows from this .oil wellhead into the .h2o extraction circuit.
        </div>
        <div>
            <a href="http://localhost:8002" class="btn" target="_blank">💧 Switch to .h2o Smart Water Portal (Port 8002) →</a>
            <a href="http://localhost:8000" class="btn" style="background: #4b5563; margin-left: 8px;">Gateway Control</a>
        </div>
    </div>

    <div class="console">
[+] .OIL SCADA LOG: Connected to physical barrier at API-03-017-21948-REPURPOSED<br>
[+] DOWNHOLE TELEMETRY: Hydrostatic balance steady. Bottom-hole pressure: 4820.5 psi.<br>
[+] SATELLITE CORRELATION: Orbital overpass Sentinel-5P (TROPOMI) confirms zero atmospheric methane plume.<br>
[+] READY: Stream exported to Heriot-Watt University IGE Subsurface Laboratory.
    </div>
</body>
</html>
"""

H2O_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>.h2o Hydrothermal Brine & Smart Water | Digital Twin</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', -apple-system, sans-serif; }
        body { background-color: #030d1a; color: #f0fdfa; padding: 24px; }
        .header { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #0284c7; padding-bottom: 16px; margin-bottom: 24px; }
        .badge { background: #0369a1; color: #fff; padding: 6px 12px; border-radius: 4px; font-weight: 700; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 24px; }
        .card { background: #082f49; border: 1px solid #075985; border-radius: 8px; padding: 20px; position: relative; overflow: hidden; }
        .card::before { content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #38bdf8; }
        .label { font-size: 12px; color: #7dd3fc; text-transform: uppercase; font-weight: 600; margin-bottom: 8px; }
        .value { font-size: 32px; font-weight: 800; color: #38bdf8; font-family: monospace; }
        .sub { font-size: 13px; color: #94a3b8; margin-top: 6px; }
        .status-ok { color: #34d399; font-weight: 700; }
        .nav-bar { background: #0c4a6e; padding: 16px 20px; border-radius: 8px; display: flex; justify-content: space-between; align-items: center; }
        .btn { background: #d97706; color: white; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-weight: 600; display: inline-block; transition: background 0.2s; }
        .btn:hover { background: #b45309; }
        .console { background: #021827; border: 1px solid #0c4a6e; border-radius: 8px; padding: 16px; font-family: monospace; font-size: 13px; color: #38bdf8; margin-top: 20px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="header">
        <div>
            <h1 style="font-size: 26px; color: #38bdf8;">💧 .H2O SMART WATER: DIRECT LITHIUM & GEOTHERMAL RECOVERY</h1>
            <p style="color: #94a3b8; margin-top: 4px;">Host: <strong>dle-circuit.arkansas.h2o:8002</strong> | Ingestion Node: <strong>telemetry.smartwater.h2o</strong></p>
        </div>
        <div class="badge">TLD: .H2O ACTIVE</div>
    </div>

    <div class="grid">
        <div class="card">
            <div class="label">Brine Flow Rate</div>
            <div class="value">14,200 <span style="font-size: 18px;">bpd</span></div>
            <div class="sub">Continuous Hydrothermal Feed (GWPC 2024 Framework)</div>
        </div>
        <div class="card">
            <div class="label">Lithium Concentration</div>
            <div class="value">385.0 <span style="font-size: 18px;">ppm</span></div>
            <div class="sub">Smackover Brine (USGS 2024 Assessment)</div>
        </div>
        <div class="card">
            <div class="label">Daily Pure Lithium Yield</div>
            <div class="value" style="color: #34d399;">803.1 <span style="font-size: 18px;">kg/day</span></div>
            <div class="sub">Equivalent to <strong>4,275.0 kg/day LCE</strong> battery material</div>
        </div>
        <div class="card">
            <div class="label">DLE Sorption Efficiency</div>
            <div class="value">92.4 <span style="font-size: 18px;">%</span></div>
            <div class="sub">Kumar et al. (2024) Selective Adsorption Kinetics</div>
        </div>
        <div class="card">
            <div class="label">Geothermal ORC Output</div>
            <div class="value">850 <span style="font-size: 18px;">kW</span></div>
            <div class="sub">Net Clean Power: <strong>20.4 MWh/day</strong> (Inlet 112.8°C / Outlet 64.1°C)</div>
        </div>
        <div class="card">
            <div class="label">Resin Bed Differential P</div>
            <div class="value">18.4 <span style="font-size: 18px;">psi</span></div>
            <div class="sub">Column ΔP Nominal | No Scaling Detected</div>
        </div>
    </div>

    <div class="nav-bar">
        <div>
            <strong>Supervisory Alignment:</strong> Dr. Christos Chrysoulas — Smart Water Management Systems & Smart Grids (Heriot-Watt University).
        </div>
        <div>
            <a href="http://localhost:8001" class="btn" target="_blank">🛢️ Switch to .oil Barrier Portal (Port 8001) →</a>
            <a href="http://localhost:8000" class="btn" style="background: #334155; margin-left: 8px;">Gateway Control</a>
        </div>
    </div>

    <div class="console">
[+] .H2O SMART WATER LOG: Circuit online. Sorption column differential pressure optimal (18.4 psi).<br>
[+] HYDROCHEMICAL MASS BALANCE: 14,200 bpd brine yielding 803.1 kg Li/day with 92.4% recovery efficiency.<br>
[+] GEOTHERMAL TELEMETRY: Closed-loop ORC generator feeding 850 kW baseline power to local grid.<br>
[+] REINJECTION: Spent mineral-extracted water reinjected at 2,100 psi into deep disposal horizon.
    </div>
</body>
</html>
"""

GATEWAY_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dual-Domain Mission Control: .oil & .h2o</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', -apple-system, sans-serif; }
        body { background-color: #020617; color: #f8fafc; padding: 30px; }
        .hero { text-align: center; margin-bottom: 30px; }
        .hero h1 { font-size: 32px; letter-spacing: 1px; color: #38bdf8; margin-bottom: 8px; }
        .hero p { color: #94a3b8; font-size: 16px; max-width: 800px; margin: 0 auto; }
        .domains-container { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; max-width: 1200px; margin: 0 auto 30px auto; }
        .domain-box { border-radius: 12px; padding: 28px; border: 2px solid; position: relative; }
        .oil-box { background: #111827; border-color: #f59e0b; }
        .h2o-box { background: #082f49; border-color: #0284c7; }
        .domain-title { font-size: 22px; font-weight: 800; margin-bottom: 12px; display: flex; align-items: center; justify-content: space-between; }
        .tag { font-size: 12px; padding: 4px 8px; border-radius: 4px; font-weight: 700; }
        .oil-tag { background: #b45309; color: #fff; }
        .h2o-tag { background: #0369a1; color: #fff; }
        .feature-list { list-style: none; margin: 16px 0 24px 0; }
        .feature-list li { padding: 6px 0; color: #cbd5e1; font-size: 14px; border-bottom: 1px solid rgba(255,255,255,0.06); }
        .btn-launch { display: block; text-align: center; padding: 14px; border-radius: 8px; font-weight: 700; text-decoration: none; font-size: 15px; transition: transform 0.15s; }
        .btn-launch:hover { transform: translateY(-2px); }
        .btn-oil { background: #f59e0b; color: #000; }
        .btn-h2o { background: #38bdf8; color: #000; }
        .footer-note { text-align: center; color: #64748b; font-size: 14px; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="hero">
        <h1>⚡ DUAL-DOMAIN MISSION CONTROL: .OIL & .H2O</h1>
        <p>Decoupled Operational Technology Digital Twin Architecture for Mature Wellbore Repurposing, Direct Lithium Extraction (DLE), and Smart Water Telemetry.</p>
    </div>

    <div class="domains-container">
        <!-- .oil Domain Portal -->
        <div class="domain-box oil-box">
            <div class="domain-title" style="color: #fbbf24;">
                <span>🛢️ .OIL DOMAIN</span>
                <span class="tag oil-tag">PORT 8001</span>
            </div>
            <p style="color: #9ca3af; font-size: 14px;"><strong>Target:</strong> Subsurface Wellhead Barrier & Mechanical Casing Integrity</p>
            <ul class="feature-list">
                <li>• <strong>Endpoint:</strong> <code>wellbore-01.smackover.oil:8001</code></li>
                <li>• <strong>Depth / TVD:</strong> 10,450 ft MD (Smackover Limestone)</li>
                <li>• <strong>Annular Pressure:</strong> 842.1 psi (Casing Barrier Secure)</li>
                <li>• <strong>DAS Acoustic Strain:</strong> 1.45 kHz (SPE-21820 Inflow)</li>
                <li>• <strong>SCADA Security:</strong> NIST SP 800-82r3 Modbus Isolation</li>
                <li>• <strong>Emissions:</strong> 0.02 kg/hr (IRA 45X Certified Compliant)</li>
            </ul>
            <a href="http://localhost:8001" target="_blank" class="btn-launch btn-oil">🚀 Launch .oil Portal (localhost:8001) →</a>
        </div>

        <!-- .h2o Domain Portal -->
        <div class="domain-box h2o-box">
            <div class="domain-title" style="color: #38bdf8;">
                <span>💧 .H2O DOMAIN</span>
                <span class="tag h2o-tag">PORT 8002</span>
            </div>
            <p style="color: #94a3b8; font-size: 14px;"><strong>Target:</strong> Hydrothermal Brine Extraction & Smart Water Grid</p>
            <ul class="feature-list">
                <li>• <strong>Endpoint:</strong> <code>dle-circuit.arkansas.h2o:8002</code></li>
                <li>• <strong>Smart Water Node:</strong> <code>telemetry.smartwater.h2o</code></li>
                <li>• <strong>Brine Throughput:</strong> 14,200 bpd Produced Formation Water</li>
                <li>• <strong>Lithium Yield:</strong> 803.1 kg/day Li (4,275 kg/day LCE)</li>
                <li>• <strong>Clean Power:</strong> 850 kW Binary Geothermal ORC (20.4 MWh)</li>
                <li>• <strong>Faculty Match:</strong> Dr. Christos Chrysoulas (Smart Water)</li>
            </ul>
            <a href="http://localhost:8002" target="_blank" class="btn-launch btn-h2o">🚀 Launch .h2o Portal (localhost:8002) →</a>
        </div>
    </div>

    <div class="footer-note">
        Doctoral Research Candidate: <strong>Andrew C. Kieckhefer</strong> | Institute of GeoEnergy Engineering (IGE), Heriot-Watt University<br>
        Application ID: <code>9535a9e2-53ab-f111-8a75-06f0a7fb396f</code> | GitHub: <a href="https://github.com/healthearthack/Research" style="color: #38bdf8;" target="_blank">healthearthack/Research</a>
    </div>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# HTTP Request Handlers
# ---------------------------------------------------------------------------

class OilHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/telemetry":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = get_telemetry()
            self.wfile.write(json.dumps(data.get("reservoir_telemetry", {}), indent=2).encode())
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(OIL_HTML.encode("utf-8"))

    def log_message(self, format, *args):
        pass  # Suppress console clutter


class H2OHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/telemetry":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = get_telemetry()
            self.wfile.write(json.dumps(data.get("surface_processing_telemetry", {}), indent=2).encode())
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(H2O_HTML.encode("utf-8"))

    def log_message(self, format, *args):
        pass


class GatewayHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(GATEWAY_HTML.encode("utf-8"))

    def log_message(self, format, *args):
        pass


def run_server(handler_class, port, name):
    server = HTTPServer(("0.0.0.0", port), handler_class)
    print(f"[+] [{name}] ONLINE -> http://localhost:{port}")
    server.serve_forever()


def main():
    print("=" * 70)
    print("[*] LAUNCHING LOCAL DUAL-DOMAIN SITES: .OIL (8001) & .H2O (8002)")
    print("=" * 70)

    # Thread 1: Gateway Control on Port 8000
    t_gw = threading.Thread(target=run_server, args=(GatewayHandler, 8000, "MISSION CONTROL GATEWAY"), daemon=True)
    t_gw.start()

    # Thread 2: .oil Site on Port 8001
    t_oil = threading.Thread(target=run_server, args=(OilHandler, 8001, ".OIL WELLHEAD SITE"), daemon=True)
    t_oil.start()

    # Thread 3: .h2o Site on Port 8002
    t_h2o = threading.Thread(target=run_server, args=(H2OHandler, 8002, ".H2O SMART WATER SITE"), daemon=True)
    t_h2o.start()

    print("=" * 70)
    print("[+] ALL 3 LOCAL SITES ARE RUNNING LIVE:")
    print("   [+] Gateway Mission Control: http://localhost:8000")
    print("   [+] .oil Wellbore Barrier:   http://localhost:8001")
    print("   [+] .h2o Smart Water Brine:  http://localhost:8002")
    print("=" * 70)
    print("Press Ctrl+C to stop.")

    try:
        # Keep main thread alive
        threading.Event().wait()
    except KeyboardInterrupt:
        print("\n[*] Shutting down servers.")


if __name__ == "__main__":
    main()
