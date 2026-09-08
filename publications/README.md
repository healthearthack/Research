# 📚 Academic Publications & Google Scholar Research Engine

**Master Publication Pipeline, Working Paper Series & Citation Engine**  
**Repository Anchor:** [`healthearthack/Research`](https://github.com/healthearthack/Research)  
**Lead Author & Doctoral Researcher:** Andrew C. Kieckhefer  
* **Primary Contact:** `andy.kieckhefer@gmail.com`  
* **Google Scholar Profile Anchor:** `weather.amazon.go@gmail.com`  
* **Institutional Lineage:** Heriot-Watt University (Dubai & Edinburgh) | University of Wisconsin–Madison (AOS Alum)  
* **Degree Track:** `Energy, EngD` — Institute of GeoEnergy Engineering (IGE) & School of Mathematical and Computer Sciences (MACS)  

---

## 🧭 Executive Mission: Rapid Google Scholar Activity & Academic Impact

Following the publishing models of prolific research directors like **Dr. Tracey Holloway (NASA HAQAST / ESWN)**, this directory operationalizes an automated pipeline to draft, peer-review, and preprint high-impact scientific manuscripts.

By coupling markdown-based academic authoring with automated PDF compilation and open-access preprint distribution (**EarthArXiv, arXiv, TechRxiv**), this research generates **citable Digital Object Identifiers (DOIs)** and active Google Scholar citations immediately—well before formal print journal publication.

```
publications/
├── README.md                                  # 📚 Master Publication Pipeline (This File)
├── target_journals_and_metrics.md             # 📊 Target Journal Directory (Applied Energy, IEEE, SPE, ERL)
├── drafts/                                    # ✍️ Active Markdown Working Papers
│   ├── WP01_DLE_Wellbore_Repurposing_Review.md
│   ├── WP02_OT_Cybersecurity_SCADA_Telemetry.md
│   └── WP03_Satellite_Subsurface_Emissions_Coupling.md
└── dist/                                      # 📄 Rendered Academic PDFs (Camera-Ready)
    ├── WP01_DLE_Wellbore_Repurposing_Review.pdf
    ├── WP02_OT_Cybersecurity_SCADA_Telemetry.pdf
    └── WP03_Satellite_Subsurface_Emissions_Coupling.pdf
```

---

## 📑 The Working Paper Series (In-Flight Manuscripts)

| Paper # | Working Title | Core Focus | Target Preprint | Target Journal | Status |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **WP-01** | [**Direct Lithium Extraction (DLE) from Continental Petroleum Brines**](drafts/WP01_DLE_Wellbore_Repurposing_Review.md) | Repurposing late-life petroleum wellbores into closed-loop DLE and geothermal co-production systems; Smackover brine fluid kinetics. | **EarthArXiv** | *Applied Energy*<br>*(IF: 11.2)* | 🟢 **DRAFT READY**<br>[PDF](dist/WP01_DLE_Wellbore_Repurposing_Review.pdf) |
| **WP-02** | [**Physics-Informed Anomaly Detection in Upstream SCADA Networks**](drafts/WP02_OT_Cybersecurity_SCADA_Telemetry.md) | Hardening Modbus/DNP3 wellhead RTUs against sensor spoofing using hydrodynamic mass-balance laws under NIST SP 800-82. | **TechRxiv** | *IEEE Trans. Industrial Informatics*<br>*(IF: 12.3)* | 🟢 **DRAFT READY**<br>[PDF](dist/WP02_OT_Cybersecurity_SCADA_Telemetry.pdf) |
| **WP-03** | [**Coupling Spaceborne Trace Gas Spectrometry with Wellhead DAS**](drafts/WP03_Satellite_Subsurface_Emissions_Coupling.md) | Ground-truthing Sentinel-5P TROPOMI trace gas columns with downhole Distributed Acoustic Sensing for IRA 45X tax credit certification. | **ESS Open Archive** | *Environmental Research Letters*<br>*(IF: 6.7)* | 🟢 **DRAFT READY**<br>[PDF](dist/WP03_Satellite_Subsurface_Emissions_Coupling.pdf) |

---

## ⚙️ Automated PDF Compilation Pipeline

This repository includes an automated Python compiler (`scripts/build_publications.py`) that converts markdown manuscripts into publication-formatted, camera-ready PDFs styled with academic typography:

```bash
# Compile all working papers to PDF & HTML
python scripts/build_publications.py
```

### Build Features:
* **Typography:** Classic academic serif (Times New Roman / Garamond), formal two-column or unified single-column layouts, running headers, and footers.
* **Metadata Block:** Formally styled author affiliations, email anchors, date stamps, and abstract callout boxes.
* **Math & Tables:** Full support for LaTeX math equations (`$...$`, `$$...$$`) and Markdown data tables.
* **Preprint Headers:** Pre-formatted with preprint banners and open citation blocks for rapid indexing on Google Scholar.

---

## 📈 Google Scholar Integration Playbook (Anchor: `weather.amazon.go@gmail.com`)

To activate and scale your public Google Scholar profile:

1. **Profile Ownership:**
   * Primary Connected Email: **`weather.amazon.go@gmail.com`** (verified for Google Scholar authorship management).
   * Secondary Institutional Email: `andy.kieckhefer@gmail.com` / Heriot-Watt University student ID.
2. **Instant Preprint Ingestion (Zero-Wait Indexing):**
   * Deposit the rendered PDFs (`publications/dist/*.pdf`) to **EarthArXiv** or **TechRxiv**.
   * EarthArXiv assigns an instant DOI via the Center for Open Science (COS).
   * Google Scholar automated crawlers index EarthArXiv / arXiv DOIs within **48–72 hours**.
3. **Citation Multiplier Effect:**
   * By drafting review and synthesis articles (WP-01 and WP-02), early citations will accumulate rapidly from global researchers citing your comprehensive Smackover basin review and OT security framework.
