# 🛠️ The Research Toolchain & Experimental Workbench: "The Tools to Make the Engine"

**Repository Pillar:** Tooling, Testbeds & Scaffolding for Doctoral Candidature  
**Doctoral Track:** `Energy, EngD` — Heriot-Watt University (Dubai & Edinburgh Campuses)  
**Author:** Andrew C. Kieckhefer (`andy.kieckhefer@gmail.com`)  
**Supervisory Alignment:** Dr. Christos Chrysoulas (Smart Grids & Smart Water Management Systems)  

---

## 🧭 The Philosophy: "The Tools to Make the Engine, Not the Engine Itself Yet"

In engineering and computational physical science, a high-impact doctorate does not begin with an unverified, full-scale commercial engine. **It begins with the precision instrumentation, virtual testbeds, and diagnostic toolchain required to build, test, and calibrate that engine over 3.5 years of rigorous research.**

```
┌───────────────────────────────────────────────────────────────────────────────────┐
│                      DOCTORAL DESTINATION (Years 3–4)                             │
│ The 360-Degree Cyber-Physical GeoEnergy Co-Production Engine                      │
│ (Validated in Heriot-Watt HPHT Core Flood Labs & Regional Field Pilots)           │
└────────────────────────────────────────▲──────────────────────────────────────────┘
                                         │ Built, calibrated, and proven by:
┌────────────────────────────────────────┴──────────────────────────────────────────┐
│                      THE CURRENT WORKBENCH & TOOLCHAIN                            │
│ 1. Dual-Domain Digital Twin Portals (website.oil:8000 & website.h2o:8001)         │
│ 2. SCADA Telemetry & Anomaly Evaluator (agent/)                                   │
│ 3. Autonomous Policy & Threat Radar (scripts/junior_researcher.py)                │
│ 4. Space-to-Subsurface Satellite Downscaling Bridge (NASA HAQAST / TROPOMI)       │
│ 5. Contributor Requisition Scaffolding ("Help Wanted" Boards)                     │
└───────────────────────────────────────────────────────────────────────────────────┘
```

Rather than claiming a completed commercial system on Day 1, this repository houses the **working developer toolchain, diagnostic simulators, and data pipelines** that enable Andrew Kieckhefer, faculty mentors (Dr. Christos Chrysoulas), and research collaborators to systematically engineer the thesis.

---

## 🧰 The 5 Core Workbench Tools

### 1. 🛢️ Subsurface Barrier Telemetry Simulator (`website.oil:8000`)
* **Tool Objective:** Provide an air-gapped, virtual testbed simulating physical wellbore casing dynamics without risking live high-pressure field assets.
* **Capabilities:**
  * Emulates annular casing pressure states ($842.1\text{ psi}$ vs. $< 1,200\text{ psi}$ critical threshold).
  * Simulates high-temperature Distributed Acoustic Sensing (DAS) fiber strain resonance ($1.45\text{ kHz}$).
  * Audits Modbus/TCP and DNP3 register traffic against **NIST SP 800-82 Rev. 3** OT security baselines.
* **Local Endpoint:** `http://website.oil:8000` (or `http://akbar.oil` / `http://localhost:8000`)

---

### 2. 💧 Hydrothermal Brine & Smart Water Circuit Simulator (`website.h2o:8001`)
* **Tool Objective:** Model surface Direct Lithium Extraction (DLE) kinetics and geothermal heat dissipation before physical HPHT core flood validation.
* **Capabilities:**
  * Computes selective $\text{Li}^+$ adsorption mass balances ($14,200\text{ bpd}$ brine at $385\text{ ppm Li} \rightarrow 803.1\text{ kg/day Li}$).
  * Simulates resin column differential pressure drop ($\Delta P = 18.4\text{ psi}$) to detect channeling or compaction.
  * Models Organic Rankine Cycle (ORC) binary power generation ($850\text{ kW}$ net clean output).
* **Local Endpoint:** `http://website.h2o:8001` (or `http://ma.h2o` / `http://localhost:8001`)

---

### 3. 🤖 Telemetry Diagnostic & Multi-LLM Reasoning Engine (`agent/`)
* **Tool Objective:** Serve as an intelligent analytical layer testing how AI reasoning engines (Claude, Gemini, or deterministic rule sets) evaluate physical sensor anomalies and cyber tampering.
* **Capabilities:**
  * Pydantic-enforced schema validation for wellbore and SCADA streams ([`agent/models.py`](../agent/models.py)).
  * Deterministic rule-based evaluation detecting tubing leaks, resin fouling, and unauthorized Modbus scans ([`agent/telemetry_monitor.py`](../agent/telemetry_monitor.py)).
  * Automated executive briefing generator supporting Anthropic Claude, Google Gemini, and an autonomous offline zero-key mode ([`agent/llm_analyst.py`](../agent/llm_analyst.py)).
* **Execution:** `python run_agent.py`

---

### 4. 📡 Autonomous Policy & ICS Threat Radar (`scripts/junior_researcher.py`)
* **Tool Objective:** Keep the research engine continuously aligned with rapidly evolving federal energy regulations and critical infrastructure threat advisories.
* **Capabilities:**
  * Scheduled CI/CD workflow running weekly via GitHub Actions.
  * Ingests U.S. Federal Register (DOE/BLM Geothermal Permitting, IRS Section 45X critical mineral rules) and CISA Energy Advisories.
  * Autonomously compiles intelligence digests into [`radar/`](../radar/).

---

### 5. 👥 Contributor & Requisition Scaffolding ("Help Wanted" Boards)
* **Tool Objective:** Modularize the doctoral research program into discrete work packages so domain specialists, master's students, and open-source contributors can plug into the toolchain.
* **Active Boards:**
  * 🛢️ **[.oil Requisitions](../sites/oil_8001/HELP_WANTED.md):** OT SCADA telemetry lead, wellbore geomechanics engineer, satellite methane analyst.
  * 💧 **[.h2o Requisitions](../sites/h2o_8002/HELP_WANTED.md):** DLE chemical process engineer, smart water SCADA lead, geothermal ORC engineer.

---

## 🚀 How to Launch the Full Workbench Locally
Run the unified multi-port server to spin up the `.oil` and `.h2o` testbeds:
```bash
python serve_domains.py
```
* Access `.oil` Barrier Testbed: **`http://localhost:8000`** (or `http://akbar.oil` / `http://website.oil:8000`)
* Access `.h2o` Smart Water Testbed: **`http://localhost:8001`** (or `http://ma.h2o` / `http://website.h2o:8001`)
