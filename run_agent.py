#!/usr/bin/env python3
"""
One-Click Root Runner for the Cyber-Physical GeoEnergy Telemetry Agent.
Executes telemetry analysis and produces an automated executive brief.
"""

from agent.cli import analyze_command

if __name__ == "__main__":
    analyze_command(
        data_path="data/sample_wellhead_stream.json",
        provider="auto",
        out_path="radar/latest_telemetry_diagnostic.md",
    )
