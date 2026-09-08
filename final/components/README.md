# 🧩 The Doctoral Frame Engine: Reverse-Engineered Dissertation Component Library

**Master Architectural Blueprint: Converting the Heriot-Watt Doctor of Engineering (`Energy, EngD`) Dissertation into an Interlocking Component Library (2027–2030)**  
**Repository Anchor:** [`healthearthack/Research/final/components`](https://github.com/healthearthack/Research/tree/main/final/components)  
**Lead Doctoral Researcher:** Andrew C. Kieckhefer  
*Department of Atmospheric and Oceanic Sciences (Alum), University of Wisconsin–Madison*  
*Health Earth Hack Research Laboratory*  

---

## 🏛️ The Paradigm: Reverse-Engineering the Final Doctoral Capstone

Traditional PhD and EngD dissertations suffer from **"monolithic latency"**: 300 pages of research remain locked in drafts until Year 4, invisible to the scientific community and industrial partners.

This repository **reverses that paradigm**. We reverse-engineer the final doctoral dissertation into **7 modular, interlocking puzzle pieces (Components `C01` through `C07`)**. 

```
                                      ┌──────────────────────────────────────────────────────────┐
                                      │             FINAL DISSERTATION CAPSTONE                  │
                                      │ "Closed-Loop Cyber-Physical GeoEnergy Systems:           │
                                      │  Repurposing Continental Wellbores for DLE & Geothermal" │
                                      └────────────────────────────┬─────────────────────────────┘
                                                                   │
                  ┌─────────────────┬─────────────────┬────────────┴────┬─────────────────┬─────────────────┐
                  ▼                 ▼                 ▼                 ▼                 ▼                 ▼
          ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
          │ COMPONENT C01 │ │ COMPONENT C02 │ │ COMPONENT C03 │ │ COMPONENT C04 │ │ COMPONENT C05 │ │ COMPONENT C06 │
          │ Subsurface    │ │ Wellbore      │ │ OT SCADA      │ │ Multiscale    │ │ Geothermal    │ │ Statutory     │
          │ Hydrochemistry│ │ Geomechanics  │ │ Cyber Defense │ │ Orbital MRV   │ │ Energy Balance│ │ Technoeconomics│
          │ (Smackover)   │ │ (Casing Burst)│ │ (Physics-AI)  │ │ (TROPOMI/DAS) │ │ (Binary ORC)  │ │ (IRA 45X/AOGC)│
          └───────┬───────┘ └───────┬───────┘ └───────┬───────┘ └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
                  │                 │                 │                 │                 │                 │
                  └─────────────────┴─────────────────┼─────────────────┴─────────────────┴─────────────────┘
                                                      │
                                                      ▼
                                      ┌───────────────────────────────┐
                                      │ COMPONENT C07:                │
                                      │ Transatlantic Clean Energy    │
                                      │ Diplomacy & Advocacy Charters │
                                      └───────────────┬───────────────┘
                                                      │
                                                      ▼
                                      ┌───────────────────────────────┐
                                      │  FRAME ENGINE TELEMETRY BUS   │
                                      │  (Continuous Event Streaming) │
                                      └───────────────────────────────┘
```

### The Three Golden Rules of the Component Library:
1. **Each Component is a Standalone Article:** Every component contains its own complete, publication-ready research article (`article.md`), with abstract, mathematical formulations, validation benchmarks, and bibliography.
2. **Deterministic Input/Output Contracts:** Component A's mathematical outputs feed directly as Component B's physical inputs. No component exists in isolation.
3. **Every Update Emits Marketable Telemetry:** Whenever a component's dataset, code, or equations are refined, the **Frame Engine (`engine.py`)** runs cross-component alignment tests and publishes a real-time event log to the public laboratory stream.

---

## 🧩 The 7 Component Puzzle Pieces & Interface Contracts

| Component ID | Title & Scientific Scope | Key Input Interfaces | Key Output Interfaces | Standalone Publication Anchor | Target Journal |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **`C01`** | **[Subsurface Hydrochemistry](c01_subsurface_hydrochemistry/)**<br>Smackover formation water geochemistry, lithium adsorption column kinetics, and silica scaling prevention. | Basin depth ($9,000–11,000\text{ ft}$), TDS ($300\text{k mg/L}$), $Li^+$ grade ($385\text{ ppm}$). | Fluid throughput ($14,200\text{ bpd}$), $Li$ recovery efficiency ($>90\%$), elution pH. | [**WP-01**](../../publications/drafts/WP01_DLE_Wellbore_Repurposing_Review.md) | *Applied Energy* |
| **`C02`** | **[Wellbore Geomechanics](c02_wellbore_geomechanics/)**<br>Thermal cyclic fatigue on late-life casing strings, cement sheath impedance, and P&A cost avoidance. | High-T fluid velocity from `C01`, reservoir pressure gradient ($0.52\text{ psi/ft}$). | Annular burst safety margin ($>4,500\text{ psi}$), micro-annular strain ($1.45\text{ kHz}$). | [**WP-01**](../../publications/drafts/WP01_DLE_Wellbore_Repurposing_Review.md) | *SPE Journal* |
| **`C03`** | **[OT Cyber-Physical SCADA](c03_cyberphysical_scada_ot/)**<br>Physics-informed anomaly detection auditing Modbus/DNP3 field registers against Darcy's Law. | Annular pressure from `C02`, surface choke valve setpoint commands. | Anomaly detection flag ($<50\text{ ms}$ latency), automated SDN telemetry reroute. | [**WP-02**](../../publications/drafts/WP02_OT_Cybersecurity_SCADA_Telemetry.md) & [**WP-04**](../../publications/drafts/WP04_Edge_To_Wellhead_Cyber_Physical_Synthesis.md) | *IEEE Trans. Ind. Informatics* |
| **`C04`** | **[Multiscale Orbital MRV](c04_orbital_multiscale_mrv/)**<br>Coupling top-down Sentinel-5P/TEMPO trace gas column inversions with bottom-up DAS fiber optics. | Downhole acoustic strain from `C02`, local surface laser detector readings. | Cryptographic zero-emissions proof ledger for EPA Subpart W & IRA Section 45X. | [**WP-03**](../../publications/drafts/WP03_Satellite_Subsurface_Emissions_Coupling.md) | *Environ. Res. Letters* |
| **`C05`** | **[Geothermal Energy Balance](c05_geothermal_energy_balance/)**<br>Binary Organic Rankine Cycle (ORC) co-generation harvesting enthalpy ($140^\circ\text{C}$) prior to chemical sorption. | Thermal enthalpy ($120–145^\circ\text{C}$) from `C01`, surface cooling ambient $T$. | Clean electricity generated ($850\text{ kW}$), cooled brine ($60^\circ\text{C}$) to `C01`. | [**WP-01**](../../publications/drafts/WP01_DLE_Wellbore_Repurposing_Review.md) | *Geothermics* |
| **`C06`** | **[Statutory Technoeconomics](c06_statutory_technoeconomics/)**<br>The Legal Compass engine: 26 U.S.C. § 45X tax subsidies, SDWA Class II/V permitting, AOGC royalties. | Recovery purity from `C01`, emissions certification from `C04`, CapEx from `C02`. | Levelized cost of lithium (LCOL), 10% production tax credit yield, internal rate of return (IRR). | [**legal/README.md**](../../legal/README.md) | *Energy Policy* |
| **`C07`** | **[Transatlantic Diplomacy & Advocacy](c07_transatlantic_diplomacy_advocacy/)**<br>Project GO DoD Arabic scholarship lineage, UAE ADEK/Masdar clean-tech exchange, Athena SWAN Carers Fund. | Heriot-Watt Dubai/Edinburgh campus mobility, Caregiver in Science support protocols. | Bilateral MENA-US critical mineral supply chains, academic equity compliance charter. | [**advocacy/README.md**](../../advocacy/README.md) | *Nature Energy (Perspectives)* |

---

## ⚡ The Frame Engine Orchestrator (`engine.py`)

The Frame Engine is an automated Python verification bus located at [`engine.py`](engine.py). It:
1. **Tests Interface Integrity:** Audits that all 7 components pass deterministic mathematical handoffs (e.g. Component `C01` enthalpy matches Component `C05` heat exchanger intake).
2. **Tracks Dissertation Readiness:** Calculates a machine-readable readiness score ($0–100\%$) across all 14 academic quarters.
3. **Emits Public Telemetry:** Writes component state updates directly to [`telemetry_stream.json`](telemetry_stream.json), which feeds live to your public portals ([`website.oil:8000`](http://localhost:8000), [`website.h2o:8001`](http://localhost:8001), and [`publications/dist/index.html`](../../publications/dist/index.html)).

### Running the Engine:
```bash
python final/components/engine.py --audit
```
