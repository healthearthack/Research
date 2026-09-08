# Thermo-Mechanical Casing Integrity and Shear Resistance in Repurposed Continental Wellbores for Closed-Loop Brine Extraction

**Andrew C. Kieckhefer**¹²*  
¹ *Health Earth Hack Research Laboratory, Madison, WI / USA*  
² *Department of Atmospheric and Oceanic Sciences (Alum), University of Wisconsin–Madison, Madison, WI 53706, USA*  
* *Corresponding Author:* `weather.amazon.go@gmail.com` | `andy.kieckhefer@gmail.com`  

**Doctoral Dissertation Component:** Chapter 3 / Component `C02`  
**Target Journal:** *SPE Journal*  
**Preprint Repository:** EarthArXiv | DOI: `Pending Deposit`  

---

## Abstract
Converting mature, idle oil and gas wellbores into high-rate hydrothermal conduits for Direct Lithium Extraction (DLE) eliminates up to 60% of greenfield drilling expenditures while mitigating multi-million-dollar plugging and abandonment (P&A) liabilities. However, sustained circulation of corrosive, high-temperature ($120–145^\circ\text{C}$) brine at flow rates exceeding 14,000 barrels per day induces severe thermal stress, annular pressure buildup (APB), and cement sheath fatigue. This paper presents a coupled thermo-hydro-mechanical finite-difference simulation of repurposed 7-inch production casing strings in deep sedimentary basins. We evaluate triaxial casing burst safety factors, cement micro-annular gas migration, and acoustic impedance under cyclic thermal loading, establishing rigorous mechanical screening criteria for safe conversion under state Underground Injection Control (UIC) regulations.

**Keywords:** Wellbore Repurposing, Annular Pressure Buildup, Thermo-Mechanical Fatigue, Casing Integrity, DLE Brine Extraction.

---

## 1. Wellbore Architecture & Stress Regimes
Mature wells in the Smackover Formation feature typical casing architectures:
* **Surface Casing:** 9-5/8 inch steel set across freshwater aquifers ($0–3,500\text{ ft}$).
* **Production Casing:** 7-inch L-80 or P-110 ($26\text{ lb/ft}$) extending to $10,400\text{ ft}$ TVD.
* **Thermal Stress Formulation:**
  $$\sigma_T = \frac{E \alpha \Delta T}{1 - \nu}$$
  Where $E$ is Young's Modulus ($207\text{ GPa}$), $\alpha$ is the thermal expansion coefficient ($1.2 \times 10^{-5}\text{ K}^{-1}$), $\Delta T$ is temperature differential, and $\nu$ is Poisson's ratio ($0.30$).

---

## 2. Integration with Component Library
* **Input from `C01` (Hydrochemistry):** Ingests fluid volume, density, and operating temperature.
* **Output to `C03` (OT SCADA):** Provides safe baseline annular pressure envelope ($4,200–5,100\text{ psi}$) to the anomaly detection engine.
* **Output to `C04` (Multiscale MRV):** Feeds acoustic impedance frequencies for downhole fiber-optic strain cross-checks.

---

## References
1. **NIST & API** (2023). *Recommended Practice for Annular Casing Pressure Management for Onshore Wells.* API RP 90-2.
2. **Kieckhefer, A. C.** (2026). *Direct Lithium Extraction from Continental Petroleum Brines: Repurposing Late-Life Wellbores.* EarthArXiv Preprints.
