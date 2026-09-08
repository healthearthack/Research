# Component C05: Geothermal Binary Organic Rankine Cycle (ORC) Energy Balance

**Dissertation Chapter 6 / Standalone Research Article Module**  
**Lead Scholar:** Andrew C. Kieckhefer  
*Health Earth Hack Research Laboratory • UW–Madison AOS Alum*  

---

## 🧩 Interface Contract (The Puzzle Connections)

```
[Component C01: Thermal Enthalpy (140°C Brine)]
                     │
                     ▼
   ┌─────────────────────────────────────────────────────────┐
   │ COMPONENT C05: Geothermal Energy Balance                │
   │                                                         │
   │ INPUTS:                                                 │
   │ • brine_enthalpy_kj_kg: 560 kJ/kg (from C01)            │
   │ • mass_flow_kg_s: 26.2 kg/s (14,200 bpd)                │
   │ • ambient_temperature_c: 25°C                           │
   │                                                         │
   │ OUTPUTS (Handoff to other puzzle pieces):               │
   │ ➔ net_clean_power_kw: 850 kW electricity ──▶ Local Skid│
   │ ➔ cooled_brine_temp_c: 65°C ──────────────▶ Sorption C01│
   │ ➔ parasitic_load_pct: 12.4% ──────────────▶ C06 Technoecon
   └─────────────────────────────────────────────────────────┘
```

---

## 🔬 Core Scientific Scope
1. **Low-Enthalpy Geothermal Thermodynamic Cycles:** Subcritical Organic Rankine Cycles using eco-friendly working fluids (R1233zd(E)).
2. **Thermal Coupling with DLE Adsorption:** Using the ORC evaporator as a primary brine cooler to protect temperature-sensitive aluminum hydroxide adsorbents.
3. **Net-Zero Skid Power Generation:** Providing 100% of the electrical demand of high-pressure reinjection pumps using co-produced geothermal heat.

---

## 📄 Standalone Article Reference
* **Article Draft:** [`article.md`](article.md)
* **Linked Working Paper:** [**WP-01**](../../publications/drafts/WP01_DLE_Wellbore_Repurposing_Review.md)
* **Target Journal:** *Geothermics* (Elsevier)
