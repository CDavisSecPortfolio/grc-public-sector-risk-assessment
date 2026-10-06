# Scope and methodology

## Assessment boundary

Fictional agency: Cedar Harbor Municipal Services. Systems: resident portal, cloud identity, 120 Windows endpoints, backup service, security monitoring, and the portal hosting vendor. Data: resident contact details, service requests, staff accounts, and operational records. Assumed horizon: 12 months. Day 0 is the hypothetical project kickoff, not a calendar commitment.

Excluded: payment-card processing, criminal justice systems, medical records, industrial controls, penetration testing, and formal legal compliance determinations. No production systems were accessed. No real personal information is included.

## Evidence and assessment approach

The evidence log contains authored simulation inputs. Control statuses reflect those inputs only. An implemented control would require both design evidence and evidence of operation. Missing evidence is an assessment gap, not proof that a real organization has no control.

For each risk: identify the asset, threat event, weakness, business consequence, current safeguards, owner, and control category. Rate likelihood and impact, then propose treatment and measurable acceptance criteria. Obtain actual evidence and owner approval before closing a real finding.

## Project-specific rating scales

Likelihood: 1 Rare (exceptional conditions); 2 Unlikely (limited exposure); 3 Possible (credible path); 4 Likely (recurring exposure or weak defenses); 5 Almost certain (frequent exposure and readily exploitable weakness). These are ordinal judgments, not numeric probability estimates.

Impact: 1 Negligible (minor disruption, no sensitive data loss); 2 Minor (short localized disruption); 3 Moderate (material departmental disruption or limited sensitive exposure); 4 Major (multi-day critical service disruption or substantial sensitive exposure); 5 Severe (prolonged agency-wide disruption or widespread sensitive disclosure). Use the highest credible confidentiality, integrity, or availability consequence.

Score = likelihood × impact. Bands: Low 1–4; Moderate 5–9; High 10–16; Critical 17–25. This is an internal model, not a NIST-prescribed scoring system. Equal scores require judgment about dependency, consequence, and exposure; multiplication does not produce a monetary loss estimate.

## Current and target risk

Current scores consider simulated existing controls. They are not uncontrolled inherent-risk scores. Target scores assume proposed controls operate effectively; they are forecasts, not verified residual risk. Retest implementation and operating effectiveness before assigning actual residual scores. Impact remains high when controls reduce likelihood but do not change the consequence of a successful event.

## Governance assumptions

Critical risks: escalate at kickoff; seek interim protection within 7 days and treatment within 30 days. High risks: assign an owner and target treatment within 60 days. Moderate risks: address within 90 days or request documented acceptance. Low risks: monitor quarterly. All dates are hypothetical planning assumptions.

Business owners approve risk acceptance with security review; the fictional agency director approves Critical exceptions. Each exception needs scope, rationale, interim controls, expiry within 90 days, review date, and escalation trigger. No risk is accepted in this simulation.

## Mapping limitations

CSF 2.0 mappings use category identifiers from the official NIST publication. They show relevant outcomes, not one-to-one equivalence to technical controls. This selected-scope exercise does not evaluate every category, a CSF Tier, compliance certification, or applicable legal obligations.
