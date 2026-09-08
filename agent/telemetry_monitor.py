"""
Subsurface Telemetry Monitor & OT Threat Evaluator.
Performs deterministic physics-based checks, SCADA protocol audits,
and maps telemetry streams across .oil and .h2o digital twin domains.
"""

from typing import List
from agent.models import WellboreStream, EvaluationResult, AnomalyItem


class TelemetryMonitor:
    """Evaluates wellhead physical metrics and OT cybersecurity parameters."""

    # Physical & Operational Thresholds
    MAX_CASING_PRESSURE_PSI = 1200.0
    MIN_LITHIUM_RECOVERY_PCT = 80.0
    MAX_RESIN_DELTA_P_PSI = 35.0
    MAX_METHANE_FLUX_KG_HR = 0.25  # EPA / IRA clean incentive limit
    MAX_MODBUS_EXCEPTIONS = 2

    def evaluate(self, stream: WellboreStream) -> EvaluationResult:
        anomalies: List[AnomalyItem] = []
        r = stream.reservoir_telemetry
        s = stream.surface_processing_telemetry
        o = stream.cyber_physical_ot_security
        d = stream.domain_addressing

        # 1. Check Annular Casing Pressure (.oil domain)
        if r.wellhead_casing_pressure_psi > self.MAX_CASING_PRESSURE_PSI:
            anomalies.append(
                AnomalyItem(
                    parameter=f"{d.oil_domain}::wellhead_casing_pressure_psi",
                    value=r.wellhead_casing_pressure_psi,
                    threshold=f"< {self.MAX_CASING_PRESSURE_PSI} psi",
                    severity="CRITICAL",
                    message="High annular casing pressure detected on .oil barrier. Potential downhole tubing leak or casing barrier compromise.",
                )
            )

        # 2. Check DLE Resin Sorption Bed Differential Pressure (.h2o domain)
        if s.dle_sorption_bed_pressure_drop_psi > self.MAX_RESIN_DELTA_P_PSI:
            anomalies.append(
                AnomalyItem(
                    parameter=f"{d.h2o_domain}::dle_sorption_bed_pressure_drop_psi",
                    value=s.dle_sorption_bed_pressure_drop_psi,
                    threshold=f"< {self.MAX_RESIN_DELTA_P_PSI} psi",
                    severity="WARNING",
                    message="Elevated DLE column differential pressure on .h2o circuit. Possible particulate fouling or resin bed compaction.",
                )
            )

        # 3. Check DLE Recovery Efficiency (.h2o domain)
        if s.dle_lithium_recovery_efficiency_pct < self.MIN_LITHIUM_RECOVERY_PCT:
            anomalies.append(
                AnomalyItem(
                    parameter=f"{d.h2o_domain}::dle_lithium_recovery_efficiency_pct",
                    value=s.dle_lithium_recovery_efficiency_pct,
                    threshold=f"> {self.MIN_LITHIUM_RECOVERY_PCT}%",
                    severity="WARNING",
                    message="Sub-optimal lithium extraction recovery rate. Inspect elution cycle kinetics and resin capacity.",
                )
            )

        # 4. Check Surface Methane Leakage (TROPOMI Satellite & IRA 45X Correlator)
        if o.surface_methane_flux_kg_hr > self.MAX_METHANE_FLUX_KG_HR:
            anomalies.append(
                AnomalyItem(
                    parameter=f"{d.oil_domain}::surface_methane_flux_kg_hr",
                    value=o.surface_methane_flux_kg_hr,
                    threshold=f"< {self.MAX_METHANE_FLUX_KG_HR} kg/hr",
                    severity="CRITICAL",
                    message="Fugitive methane emission detected above threshold. Disqualifies asset from IRA clean energy credits.",
                )
            )

        # 5. Check Industrial OT Protocol Integrity
        if o.modbus_exception_count_last_10m > self.MAX_MODBUS_EXCEPTIONS:
            anomalies.append(
                AnomalyItem(
                    parameter=f"{d.smart_water_endpoint}::modbus_exception_count_last_10m",
                    value=float(o.modbus_exception_count_last_10m),
                    threshold=f"<= {self.MAX_MODBUS_EXCEPTIONS}",
                    severity="CRITICAL",
                    message="Excessive Modbus/TCP exception packets detected. Potential unauthorized register scanning or MITM tampering.",
                )
            )

        # Compute Operational Yields
        daily_brine_liters = r.brine_flow_rate_bpd * 158.987
        daily_lithium_kg = (
            daily_brine_liters
            * r.lithium_concentration_ppm
            * (s.dle_lithium_recovery_efficiency_pct / 100.0)
        ) / 1_000_000.0

        daily_geothermal_mwh = (s.net_geothermal_power_kw * 24.0) / 1000.0

        critical_count = sum(1 for a in anomalies if a.severity == "CRITICAL")
        warning_count = sum(1 for a in anomalies if a.severity == "WARNING")

        if critical_count > 0:
            overall_health = "CRITICAL"
        elif warning_count > 0:
            overall_health = "DEGRADED"
        else:
            overall_health = "NOMINAL"

        ira_compliant = o.surface_methane_flux_kg_hr <= self.MAX_METHANE_FLUX_KG_HR

        return EvaluationResult(
            facility_id=stream.facility_id,
            well_id=stream.well_id,
            timestamp_utc=stream.timestamp_utc,
            oil_domain=d.oil_domain,
            h2o_domain=d.h2o_domain,
            smart_water_endpoint=d.smart_water_endpoint,
            overall_health=overall_health,
            anomalies=anomalies,
            ira_45x_compliance=ira_compliant,
            estimated_daily_lithium_kg=round(daily_lithium_kg, 2),
            estimated_daily_geothermal_mwh=round(daily_geothermal_mwh, 2),
        )
