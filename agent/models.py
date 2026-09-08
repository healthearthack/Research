"""
Pydantic Data Models for Subsurface Wellbore Telemetry and OT Security.
Includes .oil and .h2o Digital Twin Domain Addressing schemas.
"""

from datetime import datetime
from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class DomainAddressing(BaseModel):
    oil_domain: str = Field(
        ...,
        description="Digital twin endpoint for legacy hydrocarbon wellbore integrity (.oil TLD)",
        example="wellbore-01.smackover.oil",
    )
    h2o_domain: str = Field(
        ...,
        description="Digital twin endpoint for hydrothermal brine extraction & DLE (.h2o TLD)",
        example="dle-circuit.arkansas.h2o",
    )
    smart_water_endpoint: str = Field(
        "telemetry.smartwater.h2o",
        description="Industrial IoT SCADA endpoint for smart water & produced brine telemetry",
    )
    tld_classification: Optional[Dict[str, str]] = Field(
        default=None,
        description="Semantic definition of .oil and .h2o operational zones",
    )


class ReservoirTelemetry(BaseModel):
    measured_depth_ft: float = Field(..., description="Measured depth of the well in feet")
    true_vertical_depth_ft: float = Field(..., description="True vertical depth in feet")
    bottom_hole_temperature_c: float = Field(..., description="Bottom-hole temperature in Celsius")
    wellhead_temperature_c: float = Field(..., description="Surface wellhead fluid temperature in Celsius")
    bottom_hole_pressure_psi: float = Field(..., description="Reservoir bottom-hole pressure in psi")
    wellhead_casing_pressure_psi: float = Field(..., description="Annular casing pressure at the wellhead in psi")
    brine_flow_rate_bpd: float = Field(..., description="Brine volumetric production rate in barrels per day")
    lithium_concentration_ppm: float = Field(..., description="Dissolved lithium concentration in mg/L (ppm)")


class SurfaceProcessingTelemetry(BaseModel):
    dle_sorption_bed_pressure_drop_psi: float = Field(..., description="Differential pressure across DLE resin columns")
    dle_lithium_recovery_efficiency_pct: float = Field(..., description="Direct Lithium Extraction recovery rate (%)")
    geothermal_orc_heat_exchanger_inlet_c: float = Field(..., description="ORC primary heat exchanger inlet temp in Celsius")
    geothermal_orc_heat_exchanger_outlet_c: float = Field(..., description="ORC heat exchanger outlet temp in Celsius")
    net_geothermal_power_kw: float = Field(..., description="Net electrical output from binary geothermal cycle in kW")
    reinjection_pressure_psi: float = Field(..., description="Pressure required for reservoir brine reinjection in psi")


class OTSecurityTelemetry(BaseModel):
    scada_protocol: str = Field(..., description="Active industrial SCADA communication protocol")
    plc_firmware_integrity: str = Field(..., description="Cryptographic state of field PLC firmware")
    modbus_exception_count_last_10m: int = Field(0, description="Count of illegal function/register exceptions")
    distributed_acoustic_sensing_strain_khz: float = Field(..., description="Dominant fiber-optic acoustic frequency in kHz")
    cisa_threat_level: str = Field("LOW_NOMINAL", description="Applicable CISA ICS threat level")
    surface_methane_flux_kg_hr: float = Field(0.0, description="Surface fugitive methane emission rate in kg/hr")


class WellboreStream(BaseModel):
    facility_id: str
    basin: str
    well_id: str
    timestamp_utc: datetime
    operational_mode: str
    domain_addressing: DomainAddressing
    reservoir_telemetry: ReservoirTelemetry
    surface_processing_telemetry: SurfaceProcessingTelemetry
    cyber_physical_ot_security: OTSecurityTelemetry


class AnomalyItem(BaseModel):
    parameter: str
    value: float
    threshold: str
    severity: str  # "CRITICAL", "WARNING", "INFO"
    message: str


class EvaluationResult(BaseModel):
    facility_id: str
    well_id: str
    timestamp_utc: datetime
    oil_domain: str
    h2o_domain: str
    smart_water_endpoint: str
    overall_health: str  # "NOMINAL", "DEGRADED", "CRITICAL"
    anomalies: List[AnomalyItem] = []
    ira_45x_compliance: bool = True
    estimated_daily_lithium_kg: float
    estimated_daily_geothermal_mwh: float
