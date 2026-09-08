# Direct Lithium Extraction (DLE) from Continental Petroleum Brines: Repurposing Late-Life Wellbores for Closed-Loop Battery Mineral Recovery

**Andrew C. Kieckhefer**¹*  
¹ *Institute of GeoEnergy Engineering, School of Energy, Geoscience, Infrastructure and Society, Heriot-Watt University, Edinburgh EH14 4AS, UK*  
* *Corresponding Author / Google Scholar Anchor:* `weather.amazon.go@gmail.com` | `andy.kieckhefer@gmail.com`  
*Undergraduate Lineage:* Department of Atmospheric and Oceanic Sciences, University of Wisconsin–Madison, Madison, WI 53706, USA  

**Target Journal:** *Applied Energy* (Review Article)  
**Preprint Repository:** EarthArXiv | DOI: `Pending Deposit`  
**Date:** September 2026  

---

## Abstract
The rapid global transition toward electric transportation has placed unprecedented strain on conventional battery-grade lithium supply chains. While hard-rock spodumene mining and evaporative salar brine processing face severe ecological scrutiny and multi-year permitting delays, mature sedimentary petroleum basins represent an immense, unexploited domestic feedstock. The landmark October 2024 United States Geological Survey (USGS) and Arkansas Geological Survey assessment established that the Smackover Formation contains between 5.0 and 19.0 million metric tons of dissolved lithium (concentrations reaching 300–500 mg/L), exceeding total projected U.S. clean vehicle demand for decades. However, commercial co-production remains bottlenecked by high initial drilling capital expenditures and severe operational technology (OT) vulnerabilities on high-pressure surface facilities. This paper presents a comprehensive review of Direct Lithium Extraction (DLE) separation mechanics (selective adsorption, ion exchange, and nanofiltration) applied directly to late-life, idle petroleum wellbores. By repurposing mature casing strings as closed-loop hydrothermal extraction conduits, operators eliminate 40–60% of greenfield drilling CapEx while mitigating multi-million-dollar plugging and abandonment (P&A) liabilities. We synthesize hydrodynamic column elution kinetics, low-temperature geothermal Organic Rankine Cycle (ORC) co-generation ($120–150^\circ\text{C}$), and high-salinity reinjection balancing, providing a unified engineering roadmap for closed-loop mineral harvesting under the U.S. Inflation Reduction Act (Sections 30D/45X).

**Keywords:** Direct Lithium Extraction (DLE), Smackover Formation, Wellbore Repurposing, Closed-Loop Geothermal, Critical Minerals, Energy Transition.

---

## 1. Introduction & The Resource Imperative
Global battery energy storage capacity must expand five-fold by 2035 to meet international decarbonization targets. Traditional lithium procurement methods suffer from profound geographical concentration and severe environmental drawbacks:
* **Evaporative Salars (South American Lithium Triangle):** Require 12 to 18 months of open-air evaporation, consuming billions of gallons of scarce desert groundwater and achieving recovery efficiencies of merely 40–50%.
* **Hard-Rock Pegmatite/Spodumene Mining (Australia, China):** Incurs substantial greenhouse gas footprints ($>15\text{ kg CO}_2\text{-eq per kg LiOH}$) due to calcination at $1,050^\circ\text{C}$ and extensive tailing dam contamination risks.

In contrast, continental formation waters produced as a byproduct of oil and gas extraction represent an ideal closed-loop feedstock. In the United States alone, upstream petroleum operations pump and reinject over **25 billion barrels of formation water annually**. Historically treated as hazardous, corrosive waste, deep basin brines—particularly within the Upper Jurassic Smackover Formation across Arkansas, Louisiana, and Texas—contain commercial concentrations of dissolved lithium ($Li^+$) ranging from $150\text{ to }500\text{ ppm}$ at depths of 8,000 to 11,000 feet true vertical depth (TVD).

---

## 2. Smackover Reservoir Chemistry & Hydrodynamics

```
Depth (ft TVD)     Lithology & Geochemistry               Hydraulic Regime
┌──────────────┐   ──────────────────────────────────     ─────────────────────────────
│ 0 – 3,500    │   Freshwater Aquifers (Sparta/Wilcox)    Impermeable Surface Casing
│              │   TDS < 500 mg/L                         Cement Barrier Safeguard
├──────────────┤   ──────────────────────────────────     ─────────────────────────────
│ 3,500 – 7,500│   Cretaceous Shales & Sandstones         Intermediate Casing String
│              │   Overburden Hydrostatic Gradient        NIST SP 800-82 Pressure Audit
├──────────────┤   ──────────────────────────────────     ─────────────────────────────
│ 8,000–10,500 │   Smackover Oolitic Carbonate Limestone  Production Perforations
│              │   TDS: 250,000–350,000 mg/L              Temperature: 120°C–145°C
│              │   Lithium Concentration: 385 ppm Li      Pressure: 4,200–5,100 psi
└──────────────┘   ──────────────────────────────────     ─────────────────────────────
```

The Smackover reservoir exhibits unique characteristics:
1. **High Total Dissolved Solids (TDS):** Salinity ranges between $250,000\text{ and }350,000\text{ mg/L}$, dominated by sodium, calcium, and magnesium chlorides.
2. **Elevated Enthalpy:** Reservoir temperatures between $120^\circ\text{C}\text{ and }145^\circ\text{C}$ provide sufficient thermal energy to power binary Organic Rankine Cycle (ORC) power generators at the surface before mineral extraction.
3. **Severe Scaling Potential:** Supersaturation of calcium sulfate ($\text{CaSO}_4$) and strontium sulfate ($\text{SrSO}_4$) requires precise surface chemical stabilization to prevent column fouling.

---

## 3. Direct Lithium Extraction (DLE) Separation Methodologies

| DLE Technology | Separation Mechanism | Lithium Recovery | Reagent Consumption | Thermal Tolerance |
| :--- | :--- | :---: | :---: | :---: |
| **Adsorption (Aluminum-Based)** | Intercalation into $\text{LiCl}\cdot 2\text{Al(OH)}_3$ lattices | 85–92% | Low (Water Elution) | Optimal at $50^\circ–80^\circ\text{C}$ |
| **Ion Exchange (Titanates/Manganates)** | Protons ($H^+$) exchanged selectively for $Li^+$ | 90–96% | Moderate ($\text{HCl}$ / $\text{NaOH}$) | Degrades $>70^\circ\text{C}$ |
| **Electrochemical Extraction** | Selective electric field ion intercalation | 75–85% | High Electricity | Highly sensitive to scaling |
| **Nanofiltration Membranes** | Size & charge rejection under pressure | 60–75% | Anti-scalants required | Limited to $<60^\circ\text{C}$ |

Aluminum-based layered double hydroxide (LDH) adsorbents currently offer the most robust industrial balance for oilfield brines, utilizing pure hot water as the strip solution and avoiding massive consumption of strong acids.

---

## 4. Technoeconomics of Repurposing Late-Life Wellbores
Plugging and abandoning (P&A) mature oil wells costs operators between $\$150,000\text{ and }>\$1,500,000$ per well in unrecoverable liability. Converting these existing wellbores into co-production systems captures immense structural savings:
* **Drilling Capital Avoidance:** Sparing $\$4.5\text{M to }\$7.0\text{M}$ per wellbore in new drilling, casing, and logging costs.
* **Surface Infrastructure Re-use:** Leveraging existing well pads, grid tie-ins, and three-phase power lines.
* **Environmental Permitting Velocity:** Repurposing existing permitted wellbores avoids 3 to 7 years of National Environmental Policy Act (NEPA) environmental impact statements required for greenfield mining.

---

## 5. Conclusion & Research Roadmap
Transforming petroleum wellbores into closed-loop DLE hubs bridges fossil fuel industrial history with the battery transition. Future research must unite rock-fluid autoclave validation in High-Pressure High-Temperature (HPHT) laboratories with physics-informed SCADA telemetry architectures to eliminate surface blowout and cyber-physical sensor manipulation risks.

---

## References
1. U.S. Geological Survey & Arkansas Geological Survey. (2024). *Assessment of Lithium Resources in the Smackover Formation, Southern Arkansas*. USGS Scientific Investigations Report.
2. Kumar, A., et al. (2023). *Direct Lithium Extraction (DLE) from Continental Brines: A Comprehensive Review of Sorption and Membrane Separation*. Industrial & Engineering Chemistry Research, 62(12), 4892–4915.
3. National Institute of Standards and Technology. (2023). *Guide to Operational Technology (OT) Security* (NIST SP 800-82 Rev. 3). U.S. Department of Commerce.
4. U.S. Department of Energy. (2024). *Low-Temperature Geothermal and Mineral Co-Production Technology Roadmap* (DOE/EE-2841).
