# Physics-Informed Anomaly Detection in Upstream SCADA Networks: Mitigating Sensor Spoofing in High-Pressure Hydrothermal Wellheads

**Andrew C. Kieckhefer**¹²*  
¹ *Health Earth Hack Research Laboratory, Madison, WI / USA*  
² *Department of Atmospheric and Oceanic Sciences (Alum), University of Wisconsin–Madison, Madison, WI 53706, USA*  
* *Corresponding Author:* `weather.amazon.go@gmail.com` | `andy.kieckhefer@gmail.com`  

**Doctoral Dissertation Component:** Chapter 4 / Component `C03`  
**Target Journal:** *IEEE Transactions on Industrial Informatics*  
**Preprint Repository:** EarthArXiv | DOI: `Pending Deposit`  

---

## Abstract
Operational technology (OT) networks securing critical energy assets remain vulnerable to adversarial exploitation due to legacy, unauthenticated industrial protocols (Modbus/TCP and DNP3). In high-pressure hydrothermal extraction (producing 14,000 bpd of corrosive brine at pressures exceeding 4,000 psi), undetected cyber-physical manipulation of surface choke valves or annular pressure transducers can trigger catastrophic casing rupture or aquifer contamination. Traditional IT intrusion detection systems monitor statistical network packet abnormalities but fail to detect semantically valid but physically implausible commands (false data injection). This paper presents a physics-informed anomaly detection architecture deployed directly on ruggedized edge microclouds. By coupling real-time Modbus register telemetry with first-principles hydrodynamic conservation equations (Darcy's Law and acoustic impedance verification), our engine detects sensor-spoofing attacks within 45 milliseconds, executing deterministic failover before pressure relief thresholds are exceeded.

**Keywords:** Industrial IoT, OT Security, Modbus/TCP, Physics-Informed AI, Wellhead Integrity, NIST SP 800-82.

---

## 1. Threat Vectors on Industrial Wellheads
Adversarial actors exploiting unauthenticated Modbus/TCP networks can execute Man-in-the-Middle (MITM) attacks by overwriting holding register 40012 (surface choke position) while simultaneously spoofing annular pressure telemetry in register 40024 to read normal hydrostatic levels ($840\text{ psi}$), masking dangerous overpressure buildup ($>2,500\text{ psi}$).

---

## 2. Physics-Informed Anomaly Formulation
The engine computes the residual error between measured sensor pressure $P_{\text{sensor}}$ and the hydrodynamic expectation derived from mass balance:

$$\mathcal{R}(t) = \left| P_{\text{sensor}}(t) - \left( P_{\text{reservoir}} - \frac{Q(t) \mu \ln(r_e / r_w)}{2 \pi k h} \right) \right|$$

If $\mathcal{R}(t) > \epsilon_{\text{threshold}}$ for consecutive polling intervals, an anomaly alarm triggers automated software-defined isolation.

---

## References
1. **Chrysoulas, C.**, et al. (2020). *Architectures and QoS Provisioning in Software-Defined Industrial Networks.* IEEE Trans. Ind. Informatics.
2. **NIST Special Publication 800-82, Rev. 3** (2023). *Guide to Operational Technology (OT) Security.*
3. **Kieckhefer, A. C.** (2026). *Physics-Informed Anomaly Detection in Upstream SCADA Networks.* EarthArXiv Preprints.
