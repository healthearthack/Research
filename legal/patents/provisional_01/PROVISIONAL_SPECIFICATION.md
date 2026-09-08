# UNITED STATES PROVISIONAL PATENT APPLICATION SPECIFICATION

**TITLE OF THE INVENTION:**  
SYSTEM AND METHOD FOR A PHYSICS-CONSTRAINED EDGE-NATIVE SMALL LANGUAGE MODEL FOR AUTONOMOUS WELLHEAD TELEMETRY INGESTION, CYBER-PHYSICAL ANOMALY NEUTRALIZATION, AND HYDROTHERMAL FLUID BALANCING

**INVENTOR:**  
Andrew Charles Kieckhefer (Madison, WI, USA)

---

## CROSS-REFERENCE TO RELATED APPLICATIONS
This application claims priority and benefit under 35 U.S.C. 111(b) as a provisional patent application.

## STATEMENT REGARDING FEDERALLY SPONSORED RESEARCH OR DEVELOPMENT
Not Applicable.

---

## FIELD OF THE INVENTION
The present invention relates generally to industrial artificial intelligence, cyber-physical systems (CPS), and operational technology (OT) cybersecurity. More specifically, the invention relates to domain-specific, quantized Small Language Models (SLMs) configured for edge execution adjacent to high-pressure wellhead manifolds to autonomously parse industrial serial telemetry (Modbus/DNP3), validate sensor signals against first-principles governing fluid mechanics, and neutralize adversarial false data injection attacks in real time.

---

## BACKGROUND OF THE INVENTION
Critical energy infrastructure—including geothermal extraction wells, Direct Lithium Extraction (DLE) facilities, and repurposed petroleum wellbores—operates under extreme thermodynamic and mechanical conditions. Modern facilities co-produce deep formation brines at temperatures exceeding $120^\circ\text{C}$ to $145^\circ\text{C}$ and pressures exceeding $4,000\text{ psi}$. Historically, wellhead monitoring relied on air-gapped serial networks utilizing unauthenticated, plaintext industrial fieldbus protocols such as Modbus RTU and DNP3.

With the advent of autonomous operations and environmental reporting mandates (e.g., U.S. Inflation Reduction Act Section 45X and EPA Subpart W), operators have connected previously isolated wellhead controllers to wide-area networks (WANs) and centralized cloud analytics pipelines. This transition has introduced two critical technological vulnerabilities:

1. **Network Latency Bottlenecks:** Centralized hyperscale cloud computing architectures incur round-trip network latencies between 200 milliseconds and multiple seconds across remote cellular or satellite links. In high-pressure hydrothermal extraction, hydrodynamic pressure surges, acoustic cavitation, and casing shear events propagate across steel casing strings in under 50 milliseconds. Centralized cloud models cannot execute safety shut-in commands within the physical reaction window required to prevent catastrophic wellbore burst.

2. **Semantic False Data Injection Attacks:** Legacy field protocols (Modbus/TCP) lack cryptographic authentication, message integrity checks, or session state verification. An adversarial actor executing a Man-in-the-Middle (MITM) attack can overwrite holding registers (e.g., commanding a choke valve actuator to close while spoofing pressure sensor registers to indicate safe hydrostatic levels). Conventional Information Technology (IT) Intrusion Detection Systems (IDS) inspect network packet syntax or statistical traffic volume; they fail to detect semantically valid packets that command physically disastrous actuator states.

Prior art Large Language Models (LLMs) are computationally bloated (requiring clusters of high-power GPUs), nondeterministic, prone to hallucination, and incapable of low-power edge execution on un-air-conditioned wellhead skids. Accordingly, there is an urgent and unfulfilled need for an edge-native, quantized Small Language Model whose neural attention architecture is mathematically constrained by governing physical laws to autonomously detect and neutralize cyber-physical attacks at the machine interface.

---

## SUMMARY OF THE INVENTION
The present invention solves the aforementioned problems by providing a system, method, and non-transitory computer-readable medium embodying an **Edge-Native, Physics-Constrained Small Language Model (SLM)** specifically architected for autonomous wellhead monitoring and cyber-physical protection.

In a preferred embodiment, the system includes:
1. **A Cyber-Physical Multi-Modal Tokenizer:** A specialized tokenization engine that ingests heterogeneous industrial telemetry streams—including Modbus RTU holding registers, downhole Distributed Acoustic Sensing (DAS) strain frequencies ($1.45\text{ kHz}$), spaceborne satellite methane column retrievals (Sentinel-5P/TEMPO), and fluid thermodynamic parameters—and maps them into a unified, domain-specific semantic token vocabulary.
2. **A Physics-Constrained Neural Attention Architecture:** A compact transformer neural network (0.5B to 1.5B parameters) wherein the attention weight matrices and loss functions are mathematically bounded by deterministic physical equations, including Darcy's Law for subsurface porous media flow, hydrodynamic mass conservation, and acoustic impedance transit times. Any generated state transition that violates physical conservation of mass or energy is mathematically penalized to zero probability.
3. **An Edge-Deterministic Quantization Pipeline:** The neural network weights are quantized to 2-bit or 4-bit integer representations (INT2/INT4), allowing the model to execute completely offline within a memory footprint of less than 500 megabytes on a ruggedized edge microcontroller (e.g., ARM Cortex or RISC-V) with a guaranteed inference latency of less than 50 milliseconds.
4. **Autonomous Anomaly Neutralization & Actuator Control:** Upon identifying an adversarial false data injection attack or sensor failure, the model generates an explainable diagnostic ledger and simultaneously issues hardware-level trip commands to local emergency shut-in (ESD) solenoid valves, bypassing compromised network layers.

---

## BRIEF DESCRIPTION OF THE DRAWINGS
The accompanying drawings illustrate preferred embodiments of the present invention and are incorporated into and form a part of this specification:

* **FIG. 1** is a high-level system architectural diagram illustrating the cyber-physical edge deployment of the Small Language Model at a high-pressure wellhead skid.
* **FIG. 2** is a schematic flowchart of the Cyber-Physical Multi-Modal Tokenizer transforming raw industrial register bytes and acoustic frequencies into latent domain tokens.
* **FIG. 3** is a structural block diagram of the Physics-Constrained Attention Mechanism showing the integration of Darcy's Law and mass conservation penalty functions.
* **FIG. 4** is an operational control flowchart showing the autonomous detection, isolation, and actuation workflow under an adversarial false data injection attack.

---

## DETAILED DESCRIPTION OF THE PREFERRED EMBODIMENTS

Referring now to the drawings in detail:

### 1. System Architecture & Edge Deployment (FIG. 1)
As depicted in **FIG. 1**, a repurposed late-life petroleum wellbore [100] penetrates a deep continental brine aquifer (e.g., Smackover Formation at 10,400 ft TVD). A production tubing string [102] conveys geothermal brine at $140^\circ\text{C}$ and $4,500\text{ psi}$ to a surface Christmas tree manifold [104]. 

A plurality of sensors are disposed across the wellhead:
* Annular pressure transducer [106] monitoring casing-tubing annulus.
* Wellhead temperature sensor [108].
* Downhole fiber-optic Distributed Acoustic Sensing (DAS) cable [110] measuring acoustic strain at $1.45\text{ kHz}$.
* Surface laser open-path methane detector [112].

A local Programmable Logic Controller (PLC) or Remote Terminal Unit (RTU) [114] communicates with these sensors via Modbus RTU/TCP. Disposed adjacent to the wellhead manifold within a Class I, Division 2 explosion-proof enclosure is the **Edge-Native Inference Unit (ENIU)** [120]. The ENIU includes a low-power microprocessor [122] (e.g., ARM Cortex-A78 or RISC-V), a hardware cryptographic enclave [124], and local solid-state memory [126] hosting the quantized Small Language Model [130]. The ENIU operates completely severed from public internet dependencies.

### 2. Multi-Modal Cyber-Physical Tokenization (FIG. 2)
Conventional language models process textual characters. As shown in **FIG. 2**, the present tokenizer [200] ingests a heterogeneous data frame [202] comprising:
$$\mathbf{X} = \{ \text{Reg}_{40001}, \text{Reg}_{40012}, P_{\text{annular}}, T_{\text{brine}}, f_{\text{DAS}}, \text{XCH}_{4} \}$$

The tokenizer decomposes raw binary bytes into domain-specific structured tokens:
1. **Protocol Semantic Tokens [204]:** Maps Modbus function codes (e.g., `FC03: Read Holding Registers`, `FC16: Write Multiple Registers`) into categorical embeddings.
2. **Continuous Hydrodynamic Quantile Tokens [206]:** Discretizes continuous fluid pressure and temperature into non-linear, thermodynamic-phase quantile bins based on ASME steam tables.
3. **Acoustic Wavelet Tokens [208]:** Decomposes raw $1.45\text{ kHz}$ fiber-optic DAS waveforms using continuous wavelet transforms into discrete spectral frequency tokens.

The resulting composite vector is mapped into a unified latent embedding space [210] of dimension $d_{\text{model}} = 1024$.

### 3. Physics-Constrained Neural Attention & Objective Functions (FIG. 3)
As illustrated in **FIG. 3**, the transformer architecture comprises an $N$-layer multi-head self-attention backbone [300]. To prevent hallucination and guarantee physical plausibility, the loss function $\mathcal{L}_{\text{total}}$ incorporates hard mathematical penalty constraints:

$$\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{cross-entropy}} + \lambda_{\text{Darcy}} \mathcal{L}_{\text{Darcy}} + \lambda_{\text{mass}} \mathcal{L}_{\text{mass}} + \lambda_{\text{stress}} \mathcal{L}_{\text{stress}}$$

Where:
* **Darcy Penalty Function:**
  $$\mathcal{L}_{\text{Darcy}} = \left| \Delta P_{\text{predicted}} - \left( \frac{Q \cdot \mu \cdot \ln(r_e / r_w)}{2 \pi k h} \right) \right|^2$$
  Where $Q$ is volumetric flow rate, $\mu$ is fluid viscosity, $k$ is formation permeability, and $h$ is net pay thickness.
* **Mass Conservation Penalty:**
  $$\mathcal{L}_{\text{mass}} = \left| \dot{m}_{\text{in}} - (\dot{m}_{\text{out}} + \dot{m}_{\text{annular}}) \right|^2$$
* **Casing Triaxial Stress Penalty:**
  $$\mathcal{L}_{\text{stress}} = \max\left(0, \sigma_{\text{vonMises}} - 0.80 \cdot Y_{\text{steel}}\right)$$
  Where $Y_{\text{steel}}$ is the minimum yield strength of casing string [102].

If a proposed next-token state transition represents an impossible physical scenario (e.g., pressure dropping while flow velocity drops to zero and acoustic vibration increases), the penalty term drives the logit probability of that sequence to zero.

### 4. Deterministic Edge Quantization & Autonomous Actuation (FIG. 4)
The model is post-training quantized via Group-Wise Affine Quantization (INT4/INT2) to execute within a footprint of $420\text{ MB}$. When deployed, inference across the sequence occurs in $<45\text{ milliseconds}$.

Referring to **FIG. 4**, during an adversarial MITM attack:
* An adversary transmits malicious Modbus command [402] overwriting surface choke register 40012 to $100\%$ open while spoofing annular pressure register 40024 to read $820\text{ psi}$.
* The SLM [130] ingests the frame [404] and executes physics-informed cross-validation [406].
* The model determines that a $100\%$ choke position must physically yield a pressure drop across manifold [104] of $\Delta P > 650\text{ psi}$ and an acoustic DAS signature of $f > 2.2\text{ kHz}$.
* Because measured acoustic frequency remains at $1.45\text{ kHz}$ and annular pressure exceeds the Darcy balance expectation, the model flags a **Semantic False Data Injection Anomaly** [408].
* The model executes two concurrent actions:
  1. Issues an isolated, hardware-level 24V DC discrete trip signal to an Emergency Shut-In (ESD) solenoid actuator [410], mechanically closing the wing valve within 30 milliseconds.
  2. Generates a cryptographically signed SHA-256 diagnostic report token [412] routed to a local immutable audit ledger.

---

## EXEMPLARY CLAIMS (For Priority Preservation)
While provisional applications do not require formal claims, the following claims demonstrate the patentable scope of the invention:

1. An edge-native cyber-physical telemetry monitoring system for high-pressure wellhead infrastructure, comprising:
   an edge computing device disposed adjacent to a physical wellhead manifold, the edge device comprising a processor, memory, and a physical communication interface coupled to industrial fieldbus sensors;
   a multi-modal tokenizer stored in memory and executable by the processor, configured to convert binary industrial fieldbus register bytes and downhole acoustic waveforms into unified semantic tokens;
   a neural network model stored in memory, wherein attention weight matrices of the neural network are constrained by mathematical penalty functions derived from fluid mass conservation and Darcy's Law;
   wherein the neural network executes deterministic inference on the semantic tokens in less than 50 milliseconds to identify physical-semantic discrepancies indicative of an adversarial sensor-spoofing attack; and
   an actuation interface configured to generate a physical override signal commanding an automated wellhead shut-in valve upon identification of the discrepancy.

2. The system of claim 1, wherein the neural network is quantized to an integer precision of 4 bits or less and has a total memory footprint of less than 500 megabytes.

3. The system of claim 1, wherein the industrial fieldbus sensors comprise at least one of a Modbus RTU register, a Modbus/TCP packet, and a DNP3 protocol frame.

4. The system of claim 1, wherein the multi-modal tokenizer further ingests top-of-atmosphere spaceborne satellite trace gas column densities and downhole fiber-optic distributed acoustic sensing (DAS) strain frequencies to verify zero fugitive emissions.

5. A method for autonomous cyber-physical protection of a high-pressure wellhead, the method comprising:
   ingesting, via an edge microcontroller, a real-time data frame of industrial fieldbus registers;
   tokenizing the data frame into latent embedded vectors using a domain-specific cyber-physical tokenizer;
   evaluating the embedded vectors using an edge-quantized small language model whose loss function incorporates thermodynamic mass balance and casing burst safety constraints;
   detecting an adversarial false data injection attack when reported fieldbus values violate the thermodynamic constraints; and
   transmitting an electrical control signal directly to an emergency shut-in actuator to isolate the wellhead without cloud dependency.

---

## ABSTRACT OF THE DISCLOSURE
A system, method, and edge-native Small Language Model (SLM) for autonomous wellhead telemetry ingestion, cyber-physical anomaly neutralization, and hydrothermal fluid balancing. The system includes an edge computing device deployed adjacent to high-pressure wellhead infrastructure. A multi-modal tokenizer ingests industrial fieldbus registers (Modbus/DNP3), fiber-optic acoustic strain, and satellite trace gas columns into a unified domain vocabulary. A compact, quantized neural network (0.5B–1.5B parameters) executes sub-50ms inference, with its attention weights mathematically constrained by Darcy's Law and mass conservation. When an adversarial actor injects false sensor telemetry, the model identifies the physical-semantic violation and triggers an autonomous mechanical wellhead shut-in valve completely severed from cloud network dependencies.
