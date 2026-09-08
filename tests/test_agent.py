"""
Comprehensive Unit Tests for the Cyber-Physical GeoEnergy Telemetry Agent.
Standard library unittest implementation for zero-dependency local & CI execution.
"""

import json
import unittest
from pathlib import Path
from datetime import datetime, timezone

from agent.models import (
    WellboreStream,
    DomainAddressing,
    ReservoirTelemetry,
    SurfaceProcessingTelemetry,
    OTSecurityTelemetry,
)
from agent.telemetry_monitor import TelemetryMonitor
from agent.llm_analyst import TelemetryAnalyst


class TestTelemetryAgent(unittest.TestCase):

    def setUp(self):
        self.stream = WellboreStream(
            facility_id="HWU-SMACKOVER-ALPHA-01",
            basin="Smackover Formation",
            well_id="API-03-017-21948-REPURPOSED",
            timestamp_utc=datetime.now(timezone.utc),
            operational_mode="CO_PRODUCTION_DLE_GEOTHERMAL",
            domain_addressing=DomainAddressing(
                oil_domain="wellbore-01.smackover.oil",
                h2o_domain="dle-circuit.arkansas.h2o",
                smart_water_endpoint="telemetry.smartwater.h2o",
            ),
            reservoir_telemetry=ReservoirTelemetry(
                measured_depth_ft=10450.0,
                true_vertical_depth_ft=9820.0,
                bottom_hole_temperature_c=128.4,
                wellhead_temperature_c=114.2,
                bottom_hole_pressure_psi=4820.5,
                wellhead_casing_pressure_psi=842.1,
                brine_flow_rate_bpd=14200.0,
                lithium_concentration_ppm=385.0,
            ),
            surface_processing_telemetry=SurfaceProcessingTelemetry(
                dle_sorption_bed_pressure_drop_psi=18.4,
                dle_lithium_recovery_efficiency_pct=92.4,
                geothermal_orc_heat_exchanger_inlet_c=112.8,
                geothermal_orc_heat_exchanger_outlet_c=64.1,
                net_geothermal_power_kw=850.0,
                reinjection_pressure_psi=2100.0,
            ),
            cyber_physical_ot_security=OTSecurityTelemetry(
                scada_protocol="Modbus/TCP + DNP3",
                plc_firmware_integrity="VERIFIED_SHA256",
                modbus_exception_count_last_10m=0,
                distributed_acoustic_sensing_strain_khz=1.45,
                cisa_threat_level="LOW_NOMINAL",
                surface_methane_flux_kg_hr=0.02,
            ),
        )
        self.monitor = TelemetryMonitor()

    def test_nominal_evaluation(self):
        result = self.monitor.evaluate(self.stream)
        self.assertEqual(result.overall_health, "NOMINAL")
        self.assertEqual(len(result.anomalies), 0)
        self.assertTrue(result.ira_45x_compliance)
        self.assertEqual(result.oil_domain, "wellbore-01.smackover.oil")
        self.assertEqual(result.h2o_domain, "dle-circuit.arkansas.h2o")
        self.assertGreater(result.estimated_daily_lithium_kg, 0)
        self.assertGreater(result.estimated_daily_geothermal_mwh, 0)

    def test_casing_pressure_critical_anomaly(self):
        self.stream.reservoir_telemetry.wellhead_casing_pressure_psi = 1450.0  # Above 1200 threshold
        result = self.monitor.evaluate(self.stream)

        self.assertEqual(result.overall_health, "CRITICAL")
        self.assertGreaterEqual(len(result.anomalies), 1)
        self.assertIn("wellhead_casing_pressure_psi", result.anomalies[0].parameter)
        self.assertIn(".oil", result.anomalies[0].parameter)

    def test_dle_resin_delta_p_warning(self):
        self.stream.surface_processing_telemetry.dle_sorption_bed_pressure_drop_psi = 42.0  # Above 35 psi
        result = self.monitor.evaluate(self.stream)

        self.assertEqual(result.overall_health, "DEGRADED")
        self.assertTrue(any("dle_sorption_bed_pressure_drop_psi" in a.parameter for a in result.anomalies))
        self.assertTrue(any(".h2o" in a.parameter for a in result.anomalies))

    def test_methane_leakage_ira_disqualification(self):
        self.stream.cyber_physical_ot_security.surface_methane_flux_kg_hr = 0.85  # Above 0.25 limit
        result = self.monitor.evaluate(self.stream)

        self.assertFalse(result.ira_45x_compliance)
        self.assertEqual(result.overall_health, "CRITICAL")

    def test_modbus_exception_ot_threat(self):
        self.stream.cyber_physical_ot_security.modbus_exception_count_last_10m = 5
        result = self.monitor.evaluate(self.stream)

        self.assertEqual(result.overall_health, "CRITICAL")
        self.assertTrue(any("modbus_exception_count_last_10m" in a.parameter for a in result.anomalies))

    def test_analyst_deterministic_offline_generation(self):
        result = self.monitor.evaluate(self.stream)
        analyst = TelemetryAnalyst(provider="offline")
        brief = analyst.generate_brief(self.stream, result)

        self.assertIn("# 🛡️ Autonomous GeoEnergy & OT Diagnostic Brief", brief)
        self.assertIn("wellbore-01.smackover.oil", brief)
        self.assertIn("dle-circuit.arkansas.h2o", brief)
        self.assertIn("telemetry.smartwater.h2o", brief)
        self.assertIn("850 kW", brief)

    def test_sample_json_loading(self):
        json_path = Path("data/sample_wellhead_stream.json")
        self.assertTrue(json_path.exists())
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        stream = WellboreStream(**data)
        self.assertEqual(stream.domain_addressing.oil_domain, "wellbore-01.smackover.oil")
        self.assertEqual(stream.domain_addressing.h2o_domain, "dle-circuit.arkansas.h2o")


if __name__ == "__main__":
    unittest.main()
