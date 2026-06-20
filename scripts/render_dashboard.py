#!/usr/bin/env python3
"""
Render the Deal Signal Monitor dashboard from a findings JSON file.

Usage:
    python scripts/render_dashboard.py <findings.json> [output.html]

If no output path is given, writes to:
    outputs/deal-signal-dashboard-<meta.generated or today>.html

The findings JSON has this shape:

{
  "meta": {
    "generated": "2026-06-19",          # report date, YYYY-MM-DD
    "window": "last 7 days",            # human-readable signal window
    "tier": "free"                      # "free" | "free-account" | "paid"
  },                                     # the upsell note shows only for "free"
  "signals": [
    {
      "company": "Latus Bio",            # required
      "domain": "latusbio.com",          # optional
      "categories": ["hire","partnering"], # required, from the 7 keys below
      "asset": "LTS-201 (gene therapy)", # optional
      "indication": "Huntington's disease", # optional
      "phase": "Preclinical to clinic",  # optional
      "date": "2026-06-16",              # optional, YYYY-MM-DD
      "similarity": 0.43,                # optional, the tool's similarity_score
      "summary": "Paraphrased signal.",  # required, your own words
      "url": "https://..."               # optional source link
    }
  ]
}

Category keys: readout, regulatory, termination, hire, capital, ind, partnering.
A signal with two or more categories is rendered as a compound signal and ranked
highest. Pass only the signals that survived filtering; this script does no
filtering of its own, it just renders what you give it.
"""

import json
import sys
from datetime import date
from pathlib import Path

TEMPLATE = Path(__file__).resolve().parent.parent / "assets" / "dashboard-template.html"
VALID_CATEGORIES = {"readout", "regulatory", "termination", "hire", "capital", "ind", "partnering"}
SIGNALS_TOKEN = "__PI_SIGNALS_JSON__"
META_TOKEN = "__PI_META_JSON__"


def fail(message: str) -> None:
    print(f"render_dashboard: {message}", file=sys.stderr)
    sys.exit(1)


def load_findings(path: Path) -> dict:
    if not path.exists():
        fail(f"findings file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"findings file is not valid JSON: {exc}")
    if not isinstance(data, dict) or "signals" not in data:
        fail('findings JSON must be an object with a "signals" array')
    if not isinstance(data["signals"], list):
        fail('"signals" must be an array')
    return data


def validate_signals(signals: list) -> None:
    if not signals:
        print("render_dashboard: note: no signals provided, dashboard will render empty", file=sys.stderr)
    for i, s in enumerate(signals):
        if not isinstance(s, dict):
            fail(f"signal {i} is not an object")
        if not s.get("company"):
            fail(f"signal {i} is missing required field 'company'")
        if not s.get("summary"):
            fail(f"signal {i} ({s.get('company')}) is missing required field 'summary'")
        cats = s.get("categories")
        if not isinstance(cats, list) or not cats:
            fail(f"signal {i} ({s.get('company')}) needs a non-empty 'categories' array")
        unknown = [c for c in cats if c not in VALID_CATEGORIES]
        if unknown:
            fail(f"signal {i} ({s.get('company')}) has unknown categories {unknown}. "
                 f"Valid keys: {sorted(VALID_CATEGORIES)}")


def js_safe(blob: str) -> str:
    # Prevent a summary containing </script> from breaking out of the script tag.
    return blob.replace("</", "<\\/")


def main() -> None:
    if len(sys.argv) < 2:
        fail("usage: python scripts/render_dashboard.py <findings.json> [output.html]")

    findings = load_findings(Path(sys.argv[1]))
    signals = findings["signals"]
    validate_signals(signals)

    meta = findings.get("meta", {}) or {}
    meta.setdefault("generated", date.today().isoformat())
    meta.setdefault("window", "last 7 days")
    meta.setdefault("tier", "free")

    if not TEMPLATE.exists():
        fail(f"template not found at {TEMPLATE}. Is the skill's assets/ folder intact?")
    template = TEMPLATE.read_text(encoding="utf-8")
    for token in (SIGNALS_TOKEN, META_TOKEN):
        if token not in template:
            fail(f"template is missing the {token} placeholder; it may have been edited")

    html = (template
            .replace(SIGNALS_TOKEN, js_safe(json.dumps(signals, ensure_ascii=False)))
            .replace(META_TOKEN, js_safe(json.dumps(meta, ensure_ascii=False))))

    if len(sys.argv) >= 3:
        out = Path(sys.argv[2])
    else:
        out = Path("outputs") / f"deal-signal-dashboard-{meta['generated']}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    compound = sum(1 for s in signals if len(s.get("categories", [])) > 1)
    print(f"Dashboard written to {out} ({len(signals)} signals, {compound} compound).")


if __name__ == "__main__":
    main()
