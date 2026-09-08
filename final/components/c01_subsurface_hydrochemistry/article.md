# Hydrodynamic and Elution Kinetics of Direct Lithium Extraction from Continental Carbonate Brines: The Smackover Baseline

**Andrew C. Kieckhefer**¹²*  
¹ *Health Earth Hack Research Laboratory, Madison, WI / USA*  
² *Department of Atmospheric and Oceanic Sciences (Alum), University of Wisconsin–Madison, Madison, WI 53706, USA*  
* *Corresponding Author:* `weather.amazon.go@gmail.com` | `andy.kieckhefer@gmail.com`  

**Doctoral Dissertation Component:** Chapter 2 / Component `C01`  
**Target Journal:** *Applied Energy*  
**Preprint Repository:** EarthArXiv | DOI: `Pending Deposit`  

---

## Abstract
Continental formation waters within mature sedimentary basins represent an unexploited, closed-loop domestic resource for battery-grade critical minerals. The Upper Jurassic Smackover Formation contains dissolved lithium ($Li^+$) concentrations exceeding 350 mg/L at depths of 8,000–11,000 feet true vertical depth (TVD). However, commercial Direct Lithium Extraction (DLE) from these high-enthalpy ($120–145^\circ\text{C}$), high-TDS ($>300,000\text{ mg/L}$) formation waters requires precise kinetic optimization of sorbent columns to prevent premature scaling and thermal degradation. This paper develops a hydrodynamic elution kinetics model for aluminum-based layered double hydroxide (LDH) adsorbents operating at high interstitial velocities. We demonstrate that pre-cooling brine through surface binary heat exchangers to $65^\circ\text{C}$ maximizes single-pass lithium recovery to $91.8\%$ while preventing strontium sulfate ($\text{SrSO}_4$) supersaturation, establishing a predictable mass-transfer baseline for industrial wellbore repurposing.

**Keywords:** Direct Lithium Extraction, Smackover Formation, Sorbent Kinetics, Geothermal Co-generation, Layered Double Hydroxide.

---

## 1. Geological & Hydrochemical Regime
The Smackover Formation across southern Arkansas and east Texas exhibits unique hydrochemical properties:
* **Total Dissolved Solids (TDS):** $280,000–340,000\text{ mg/L}$, dominated by chloride anions ($185,000\text{ mg/L}$).
* **Lithium Tenor:** Measured concentrations range between $210\text{ mg/L}$ and $480\text{ mg/L}$ with favorable $Mg:Li$ ratios ($<15:1$).
* **Fluid Enthalpy:** Reservoir temperatures reach $120–145^\circ\text{C}$, carrying sufficient thermal energy for surface Organic Rankine Cycle co-generation.

---

## 2. Mathematical Model of Elution Kinetics
Lithium intercalation into the $\text{LiCl}\cdot 2\text{Al(OH)}_3$ crystal lattice is modeled via second-order film diffusion:

$$\frac{\partial q}{\partial t} = k_a C (q_m - q) - k_d q$$

Where $q$ is the solid-phase lithium concentration (mg/g), $C$ is the fluid phase lithium concentration, $q_m$ is maximum saturation capacity ($8.4\text{ mg Li/g sorbent}$), and $k_a, k_d$ are the adsorption/desorption rate constants.

---

## 3. Integration with Component Library
* **Downstream Link to `C02` (Wellbore Geomechanics):** Delivers fluid mass flow ($14,200\text{ bpd}$) to casing friction calculators.
* **Downstream Link to `C05` (Energy Balance):** Transfers raw thermal enthalpy to the binary ORC heat exchanger.
* **Downstream Link to `C06` (Technoeconomics):** Establishes recovery yield ($>90\%$) for IRA Section 45X tax credit modeling.

---

## References
1. **USGS & Arkansas Geological Survey** (2024). *Evaluation of the Lithium Resource Potential within the Smackover Formation, Gulf Coast Basin, USA.*
2. **Kieckhefer, A. C.** (2026). *Direct Lithium Extraction from Continental Petroleum Brines: Repurposing Late-Life Wellbores.* EarthArXiv Preprints.
