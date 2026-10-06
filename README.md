# Public-Sector Cyber Risk Assessment

**A GRC portfolio case study prepared for Cornel Davis.**

A fictional municipal services agency needs to protect resident records while maintaining an online service portal. This project turns simulated assessment evidence into a scored risk register, NIST CSF 2.0 category mappings, and a practical 90-day remediation plan.

> Portfolio simulation: all organizations, assets, observations, evidence, and risk scores are synthetic. This is not an assessment of any actual employer or agency, an audit opinion, or proof of controls implemented by the portfolio owner. Prepared with AI assistance for review and learning.

## Start here

1. Read the [executive report](docs/executive-report.md) for the decisions and priorities.
2. Review the [scope and scoring method](docs/methodology.md).
3. Compare the [simulated evidence](docs/evidence-log.md) with the [risk register](data/risk-register.csv).
4. Inspect the [control assessment](data/control-assessment.csv) and [remediation plan](data/remediation-plan.csv).
5. Run the risk summarizer to validate scores and produce a dashboard.

## What this demonstrates

- Translate weaknesses into business risks affecting confidentiality, integrity, and availability.
- Distinguish current risk from a projected target after remediation.
- Map assessment findings to NIST CSF 2.0 categories.
- Assign accountable owners, deadlines, and objective closure evidence.
- Communicate priorities to management and record acceptance decisions.

## Scenario

Cedar Harbor Municipal Services is a fictional agency with 120 employees, a cloud resident portal, a Windows endpoint fleet, and a third-party hosting provider. The assessment assumes a 12-month risk horizon. See [methodology](docs/methodology.md) for exclusions and assumptions.

## Run locally

Requires Python 3.10+; no third-party packages or credentials.

```bash
python3 scripts/summarize_risks.py
```

The script validates unique risk IDs, score ranges, calculated scores, and rating labels. It then prints summary JSON and writes `docs/risk-dashboard.md`. Run it after editing the CSV.

## Project files

| File | Purpose |
| --- | --- |
| `docs/executive-report.md` | Leadership decisions and priority rationale |
| `docs/methodology.md` | Scope, evidence rules, scoring, and limitations |
| `docs/evidence-log.md` | Traceable synthetic observations |
| `docs/risk-dashboard.md` | Generated risk summary |
| `docs/risk-acceptance-template.md` | Time-limited exception workflow |
| `data/risk-register.csv` | Eight scored risks with target estimates |
| `data/control-assessment.csv` | Control gaps and evidence-based testing criteria |
| `data/remediation-plan.csv` | Sequenced work and closure criteria |
| `scripts/summarize_risks.py` | Reproducible validation and reporting |

## Framework source

[NIST Cybersecurity Framework 2.0, NIST CSWP 29](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf). Category mappings are an educational interpretation, not a comprehensive CSF assessment or certification. CSF outcomes inform this project; the scoring model, deadlines, and evidence examples are project-specific assumptions.

## Interview discussion

Be ready to explain why ransomware and identity risks are prioritized, why target scores are not verified residual scores, what evidence would close a finding, and why an average risk score can hide a critical exposure. Review the material before describing this as your completed hands-on work.
