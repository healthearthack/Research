# Component C03: OT Cyber-Physical SCADA Telemetry & Anomaly Engine

**Dissertation Chapter 4 / Standalone Research Article Module**  
**Lead Scholar:** Andrew C. Kieckhefer  
*Health Earth Hack Research Laboratory • UW–Madison AOS Alum*  

---

## 🧩 Interface Contract (The Puzzle Connections)

```
[Component C02: Annular Pressure & Strain]
                    │
                    ▼
   ┌─────────────────────────────────────────────────────────┐
   │ COMPONENT C03: OT Cyber-Physical SCADA Engine           │
   │                                                         │
   │ INPUTS:                                                 │
   │ • modbus_registers: Register 40001-40050 (Wellhead RTU) │
   │ • annular_burst_margin_psi: 4,850 psi (from C02)        │
   │ • elution_ph_target: 5.8 (from C01)                     │
   │                                                         │
   │ OUTPUTS (Handoff to other puzzle pieces):               │
   │ ➔ anomaly_flag (True/False, <50 ms latency) ─▶ Local ESD│
   │ ➔ sdn_reroute_event (Dynamic flow rule) ─────▶ MACS Bus │
   │ ➔ verified_telemetry_hash ───────────────────▶ C04 / C06│
   └─────────────────────────────────────────────────────────┘
```

---

## 🔬 Core Scientific Scope
1. **Legacy Protocol Vulnerabilities:** Security analysis of unauthenticated Modbus/TCP and DNP3 industrial serial loops on high-pressure wellheads.
2. **Physics-Informed Anomaly Detection (PIAD):** Cross-validating field telemetry against Darcy's Law and real-time hydrodynamic mass balance.
3. **Software-Defined Telemetry Failover:** Decoupling the control plane from the data plane (Chrysoulas et al., 2020) to maintain continuous zero-trust operation under adversarial MITM attacks.

---

## 📄 Standalone Article Reference
* **Article Draft:** [`article.md`](article.md)
* **Linked Working Papers:** [**WP-02**](../../publications/drafts/WP02_OT_Cybersecurity_SCADA_Telemetry.md) & [**WP-04**](../../publications/drafts/WP04_Edge_To_Wellhead_Cyber_Physical_Synthesis.md)
* **Target Journal:** *IEEE Transactions on Industrial Informatics*
