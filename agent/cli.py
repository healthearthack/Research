"""
Command-Line Interface for the Cyber-Physical GeoEnergy Telemetry Agent.
"""

import sys
import json
import argparse
from pathlib import Path

from agent.models import WellboreStream
from agent.telemetry_monitor import TelemetryMonitor
from agent.llm_analyst import TelemetryAnalyst


def analyze_command(data_path: str, provider: str, out_path: str = None) -> None:
    file_path = Path(data_path)
    if not file_path.exists():
        print(f"[-] Error: Telemetry file not found at '{data_path}'")
        sys.exit(1)

    print(f"[*] Ingesting wellhead stream from: {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    stream = WellboreStream(**raw_data)
    monitor = TelemetryMonitor()
    eval_result = monitor.evaluate(stream)

    print(f"[+] Physical Evaluation Complete. System Status: {eval_result.overall_health}")
    print(f"[+] Estimated Daily Lithium: {eval_result.estimated_daily_lithium_kg:,.1f} kg")
    print(f"[+] Estimated Daily Geothermal: {eval_result.estimated_daily_geothermal_mwh:.1f} MWh")

    analyst = TelemetryAnalyst(provider=provider)
    print(f"[*] Generating diagnostic brief using provider: '{provider}'...")
    brief = analyst.generate_brief(stream, eval_result)

    if out_path:
        out_file = Path(out_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(brief)
        print(f"[+] Diagnostic brief saved to: {out_file}")
    else:
        print("\n" + brief)


def main():
    parser = argparse.ArgumentParser(
        description="Cyber-Physical GeoEnergy Telemetry & Research Agent"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # analyze command
    analyze_parser = subparsers.add_parser(
        "analyze", help="Evaluate wellbore telemetry and generate AI diagnostic brief"
    )
    analyze_parser.add_argument(
        "--data",
        "-d",
        default="data/sample_wellhead_stream.json",
        help="Path to wellhead telemetry JSON file",
    )
    analyze_parser.add_argument(
        "--provider",
        "-p",
        default="auto",
        choices=["auto", "claude", "gemini", "offline"],
        help="Reasoning provider to use",
    )
    analyze_parser.add_argument(
        "--out",
        "-o",
        default=None,
        help="Optional path to output markdown brief",
    )

    args = parser.parse_args()

    if args.command == "analyze" or args.command is None:
        data = getattr(args, "data", "data/sample_wellhead_stream.json")
        provider = getattr(args, "provider", "auto")
        out = getattr(args, "out", None)
        analyze_command(data, provider, out)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
