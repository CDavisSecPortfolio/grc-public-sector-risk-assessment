#!/usr/bin/env python3
"""Validate the simulation register and generate a concise dashboard."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def rating(score):
    if score <= 4: return "Low"
    if score <= 9: return "Moderate"
    if score <= 16: return "High"
    return "Critical"

def summarize():
    with (ROOT / "data/risk-register.csv").open(newline="", encoding="utf-8") as f:
        risks = list(csv.DictReader(f))
    if not risks:
        raise ValueError("Risk register is empty")
    ids = set()
    for r in risks:
        if not r["risk_id"] or r["risk_id"] in ids:
            raise ValueError("Missing or duplicate risk ID")
        ids.add(r["risk_id"])
        for prefix in ("current", "target"):
            likelihood = int(r[f"{prefix}_likelihood"])
            impact = int(r[f"{prefix}_impact"])
            if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
                raise ValueError(f"{r['risk_id']}: scale must be 1..5")
            score = likelihood * impact
            if int(r[f"{prefix}_score"]) != score:
                raise ValueError(f"{r['risk_id']}: incorrect {prefix} score")
            if r[f"{prefix}_rating"] != rating(score):
                raise ValueError(f"{r['risk_id']}: incorrect {prefix} rating")
    bands = ("Critical", "High", "Moderate", "Low")
    current = Counter(r["current_rating"] for r in risks)
    target = Counter(r["target_rating"] for r in risks)
    result = {"risk_count": len(risks),
              "current": {b: current[b] for b in bands},
              "projected_target": {b: target[b] for b in bands}}
    lines = ["# Risk dashboard", "", "Generated from `data/risk-register.csv`.", "",
             "Targets are forecasts; actual residual risk requires validation.", "",
             "| Rating | Current | Projected target |", "| --- | ---: | ---: |"]
    lines += [f"| {b} | {current[b]} | {target[b]} |" for b in bands]
    lines += ["", "## Current priorities", "", "| Risk | Score | Owner |", "| --- | ---: | --- |"]
    ranked = sorted(risks, key=lambda r: (-int(r["current_score"]), r["risk_id"]))
    lines += [f"| {r['risk_id']} | {r['current_score']} | {r['owner']} |" for r in ranked]
    (ROOT / "docs/risk-dashboard.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return result

if __name__ == "__main__":
    print(json.dumps(summarize(), indent=2))
