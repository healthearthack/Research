# USPTO PROVISIONAL PATENT APPLICATION — DRAWING SHEETS (FIGS. 1–4)

**INVENTOR:** Andrew Charles Kieckhefer  
**APPLICATION TITLE:** System and Method for a Physics-Constrained Edge-Native Small Language Model for Autonomous Wellhead Telemetry Ingestion, Cyber-Physical Anomaly Neutralization, and Hydrothermal Fluid Balancing  

---

### SHEET 1 OF 4: FIG. 1 — OVERALL SYSTEM ARCHITECTURE & EDGE DEPLOYMENT

```
                                      FIG. 1
                        WELLHEAD EDGE INFRASTRUCTURE OVERVIEW

 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                      SURFACE INFRASTRUCTURE & SKID                          │
 │                                                                             │
 │                 ┌───────────────────────────────────────┐                   │
 │                 │  [112] Open-Path Methane Detector     │                   │
 │                 └──────────────────┬────────────────────┘                   │
 │                                    │                                        │
 │   ┌─────────────────────────────┐  │  ┌─────────────────────────────────┐   │
 │   │  [106] Annular Pressure     │  │  │  [108] Wellhead Temperature     │   │
 │   │        Transducer           │  │  │        Transducer               │   │
 │   └──────────────┬──────────────┘  │  └────────────────┬────────────────┘   │
 │                  │                 │                   │                    │
 │                  ▼                 ▼                   ▼                    │
 │      ┌──────────────────────────────────────────────────────────────┐       │
 │      │        [104] HIGH-PRESSURE SURFACE CHRISTMAS TREE            │       │
 │      │        • Mechanical Choke Manifold & ESD Wing Valve          │       │
 │      └──────────────────────────────┬───────────────────────────────┘       │
 │                                     │                                       │
 │              ┌──────────────────────┴──────────────────────┐                │
 │              │      Modbus RTU / DNP3 Industrial Loop      │                │
 │              └──────────────────────┬──────────────────────┘                │
 │                                     ▼                                       │
 │      ┌──────────────────────────────────────────────────────────────┐       │
 │      │       [120] EDGE-NATIVE INFERENCE UNIT (ENIU)                │       │
 │      │       • [122] Microprocessor (ARM Cortex-A78 / RISC-V)       │       │
 │      │       • [124] Hardware Cryptographic Enclave                 │       │
 │      │       • [126] Solid-State Local Storage Memory               │       │
 │      │       • [130] Quantized Small Language Model (<500 MB)       │       │
 │      └──────────────────────────────┬───────────────────────────────┘       │
 │                                     │                                       │
 └─────────────────────────────────────┼───────────────────────────────────────┘
                                       │
                      =================▼=================
                      GROUND SURFACE (CONTINENTAL BASIN)
                      =================┬=================
                                       │
 ┌─────────────────────────────────────┼───────────────────────────────────────┐
 │                     SUBSURFACE WELLBORE GEOMECHANICS                        │
 │                                                                             │
 │  ┌───────────────────────────────────────────────────────────────────────┐  │
 │  │ [102] 7-Inch Repurposed Production Casing String                      │  │
 │  │ • High-T Brine Conveyance (14,200 bpd at 120°C - 145°C)               │  │
 │  │ • Hydrostatic Annular Pressure Gradient (0.52 psi/ft)                 │  │
 │  │ • [110] Distributed Acoustic Sensing (DAS) Optical Fiber (1.45 kHz)   │  │
 │  └──────────────────────────────────┬────────────────────────────────────┘  │
 │                                     │                                       │
 │                                     ▼                                       │
 │  ┌───────────────────────────────────────────────────────────────────────┐  │
 │  │ [100] Deep Continental Brine Aquifer (Smackover Formation at 10,400ft)│  │
 │  └───────────────────────────────────────────────────────────────────────┘  │
 └─────────────────────────────────────────────────────────────────────────────┘
```

---

### SHEET 2 OF 4: FIG. 2 — MULTI-MODAL CYBER-PHYSICAL TOKENIZER

```
                                      FIG. 2
                     CYBER-PHYSICAL MULTI-MODAL TOKENIZATION

     [202] INGESTED HETEROGENEOUS WELLHEAD & SUBSURFACE DATA FRAME
     ┌──────────────────────────────────────────────────────────────┐
     │ • Modbus Holding Register 40001 (Raw Hex Bytes: 0x01A4)      │
     │ • Modbus Holding Register 40012 (Choke Position Setpoint)    │
     │ • Annular Casing Pressure Transducer (P_annular = 842.1 psi) │
     │ • Downhole Fiber DAS Acoustic Spectral Frequency (1.45 kHz)  │
     │ • Top-of-Atmosphere Satellite Column Retrieval (TROPOMI XCH4)│
     └──────────────────────────────┬───────────────────────────────┘
                                    │
                                    ▼
                 ┌───────────────────────────────────────┐
                 │ [200] MULTI-MODAL TOKENIZATION ENGINE │
                 └──────────────────┬────────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
 ┌─────────────────┐        ┌─────────────────┐        ┌─────────────────┐
 │ [204] PROTOCOL  │        │ [206] CONTINUOUS│        │ [208] ACOUSTIC  │
 │ SEMANTIC TOKENS │        │ HYDRODYNAMIC    │        │ WAVELET TOKENS  │
 │ • FC03_READ_REG │        │ QUANTILE TOKENS │        │ • CWT Spectral  │
 │ • FC16_WRITE_REG│        │ • ASME Phase Bin│        │   Decomposition │
 │ • CRC16_INTEG   │        │ • Enthalpy Band │        │ • Resonant Peak │
 └────────┬────────┘        └────────┬────────┘        └────────┬────────┘
          │                          │                          │
          └──────────────────────────┼──────────────────────────┘
                                     │
                                     ▼
      ┌──────────────────────────────────────────────────────────────┐
      │ [210] UNIFIED LATENT EMBEDDING SPACE (Dimension: d_model)    │
      │ • Encodes cyber syntax, fluid physics, and acoustic strain   │
      └──────────────────────────────────────────────────────────────┘
```

---

### SHEET 3 OF 4: FIG. 3 — PHYSICS-CONSTRAINED ATTENTION MECHANISM

```
                                      FIG. 3
                      NEURAL ATTENTION & OBJECTIVE FUNCTION

      ┌──────────────────────────────────────────────────────────────┐
      │ Latent Token Embedding Sequence: E = [e_1, e_2, ..., e_T]    │
      └──────────────────────────────┬───────────────────────────────┘
                                     │
                                     ▼
      ┌──────────────────────────────────────────────────────────────┐
      │ [300] N-Layer Multi-Head Self-Attention Transformer          │
      │ Attention(Q, K, V) = softmax( (Q K^T) / sqrt(d_k) ) V        │
      └──────────────────────────────┬───────────────────────────────┘
                                     │
                                     ▼
      ┌──────────────────────────────────────────────────────────────┐
      │ [302] PHYSICS-CONSTRAINED LOSS PENALTY EVALUATION ENGINE     │
      │ L_total = L_cross_entropy + L_physics                        │
      └──────────────────────────────┬───────────────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         │                           │                           │
         ▼                           ▼                           ▼
 ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐
 │ [304] DARCY     │         │ [306] MASS      │         │ [308] CASING    │
 │ FLOW PENALTY    │         │ BALANCE PENALTY │         │ STRESS PENALTY  │
 │ L_Darcy:        │         │ L_mass:         │         │ L_stress:       │
 │ Residual vs.    │         │ Inflow minus    │         │ von Mises burst │
 │ Porous Media    │         │ Outflow balance │         │ margin vs. yield│
 │ Governing Laws  │         │ conservation    │         │ strength limit  │
 └────────┬────────┘         └────────┬────────┘         └────────┬────────┘
          │                           │                           │
          └───────────────────────────┼───────────────────────────┘
                                      │
                                      ▼
      ┌──────────────────────────────────────────────────────────────┐
      │ [310] LOGIT PROBABILITY MODULATION                           │
      │ Non-physical state transitions mathematically driven to P=0  │
      └──────────────────────────────────────────────────────────────┘
```

---

### SHEET 4 OF 4: FIG. 4 — ANOMALY NEUTRALIZATION & CLOSED-LOOP ACTUATION

```
                                      FIG. 4
               ADVERSARIAL ATTACK INTERCEPTION & HARDWARE ACTUATION

    [402] Adversarial Ingress (Man-in-the-Middle Injection Attack)
    • Injects malicious Modbus command: Open Choke Register 40012 to 100%
    • Injects spoofed telemetry: Annular Pressure Register 40024 = 820 psi
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │ [404] Small Language Model Ingests Ingress Data Frame at Edge   │
    └───────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │ [406] Real-Time Physics-Informed Cross-Validation (<45 ms)      │
    │ • 100% Choke Opening must produce acoustic shift to f > 2.2 kHz │
    │ • Measured acoustic strain remains quiescent at f = 1.45 kHz    │
    │ • Darcy reservoir model indicates rapid casing pressurization   │
    └───────────────────────────┬─────────────────────────────────────┘
                                │
                                ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │ [408] DISCREPANCY DETECTED: Semantic False Data Injection Flag  │
    └───────────────────────────┬─────────────────────────────────────┘
                                │
        ┌───────────────────────┴───────────────────────┐
        │ Dual Concurrent Execution (<30 ms)            │
        ▼                                               ▼
┌───────────────────────────────┐       ┌───────────────────────────────┐
│ [410] HARDWARE-LEVEL OVERRIDE │       │ [412] CRYPTOGRAPHIC AUDIT     │
│ Direct 24V DC discrete trip   │       │ Generates SHA-256 immutable   │
│ signal to Emergency Shut-In   │       │ audit ledger token with       │
│ (ESD) solenoid valve; closes  │       │ telemetry timestamp for       │
│ surface wing valve physically │       │ regulatory EPA/IRA compliance │
└───────────────────────────────┘       └───────────────────────────────┘
```
