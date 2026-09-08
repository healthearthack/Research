import os
import sys
import json
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CATALOG_FILE = os.path.join(BASE_DIR, "catalog.json")
LOG_FILE = os.path.join(BASE_DIR, "telemetry_stream.json")

def load_catalog():
    if not os.path.exists(CATALOG_FILE):
        print(f"[ERR] Catalog file not found at: {CATALOG_FILE}")
        sys.exit(1)
    with open(CATALOG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def audit_components(catalog):
    print("=" * 75)
    print("  [FRAME ENGINE] HEALTH EARTH HACK RESEARCH - DOCTORAL COMPONENT AUDIT")
    print(f"  Target Degree: {catalog.get('degree_target')}")
    print(f"  Institution:   {catalog.get('institution')}")
    print(f"  Lead Scholar:  {catalog.get('lead_researcher')}")
    print("=" * 75)

    components = catalog.get("components", [])
    total_score = 0.0
    audit_results = []

    for comp in components:
        comp_id = comp["id"]
        slug = comp["slug"]
        comp_dir = os.path.join(BASE_DIR, slug)
        readme_path = os.path.join(comp_dir, "README.md")
        article_path = os.path.join(comp_dir, "article.md")

        readme_exists = os.path.exists(readme_path)
        article_exists = os.path.exists(article_path)

        # Calculate live readiness
        readiness = comp["readiness_pct"]
        if not readme_exists:
            readiness = max(0.0, readiness - 15.0)
        if not article_exists:
            readiness = max(0.0, readiness - 20.0)

        total_score += readiness

        status_icon = "[ONLINE]" if readiness >= 50.0 else ("[ACTIVE]" if readiness >= 30.0 else "[DEV]")
        print(f"\n{status_icon} [{comp_id}] {comp['title']}")
        print(f"    Slug:         final/components/{slug}/")
        print(f"    Status:       {comp['status']} | Readiness: {readiness:.1f}%")
        print(f"    Anchor:       {comp['statutory_anchor']}")
        print(f"    Standalone:   {comp['linked_working_paper']} -> Target: {comp['target_journal']}")
        print(f"    Files:        README: {'[OK]' if readme_exists else '[MISSING]'} | Article: {'[OK]' if article_exists else '[MISSING]'}")

        audit_results.append({
            "id": comp_id,
            "title": comp["title"],
            "readiness_pct": readiness,
            "readme_present": readme_exists,
            "article_present": article_exists
        })

    avg_score = total_score / len(components) if components else 0.0
    print("\n" + "=" * 75)
    print(f"  📊 GLOBAL DISSERTATION COMPLETION STATUS: {avg_score:.1f}%")
    print(f"  Pillars Indexed: {len(components)} of 7 Interlocking Components Verified")
    print("=" * 75)

    return avg_score, audit_results

def emit_telemetry_event(event_type="AUDIT_CYCLE_COMPLETED", comp_id=None, note="Automated component bus sync"):
    catalog = load_catalog()
    avg_score, _ = audit_components(catalog)
    
    timestamp = datetime.now().isoformat() + "Z"
    event = {
        "timestamp": timestamp,
        "event_type": event_type,
        "target_component": comp_id or "ALL_SYSTEMS",
        "global_dissertation_readiness_pct": round(avg_score, 1),
        "note": note,
        "lead_researcher": catalog.get("lead_researcher"),
        "institutional_anchor": catalog.get("institution")
    }

    events = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                events = json.load(f)
        except Exception:
            events = []

    events.insert(0, event)
    events = events[:50]  # Keep last 50 events

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=2)

    print(f"[OK] Telemetry event emitted to: {LOG_FILE}")
    return event

if __name__ == "__main__":
    if "--audit" in sys.argv or len(sys.argv) == 1:
        emit_telemetry_event("ROUTINE_TELEMETRY_AUDIT", note="Full doctoral component bus scan")
    elif "--emit" in sys.argv:
        comp = sys.argv[2] if len(sys.argv) > 2 else "ALL"
        emit_telemetry_event("MANUAL_COMPONENT_UPDATE", comp_id=comp, note="Component updated by scholar")
