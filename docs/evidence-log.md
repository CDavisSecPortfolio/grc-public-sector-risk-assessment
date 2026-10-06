# Simulated evidence log

All observations below are authored inputs, not collected audit evidence. In a real assessment, record source system, collector, collection date, covered period, secure evidence location, and reviewer. Protect exports containing personal data.

| ID | Simulated input | Observation | Limitations |
| --- | --- | --- | --- |
| E-01 | Full account enrollment export | 102 of 120 staff accounts enrolled in MFA | Enrollment alone does not establish enforcement; policy and sign-in tests also needed |
| E-02 | Endpoint inventory and patch report | 26 of 120 devices beyond project 30-day patch target | Missing devices and exception legitimacy would need review |
| E-03 | Backup job reports and access list | Jobs report success; common admin access; no restore-test record | Job success does not show recoverability |
| E-04 | HR roster and identity export | Seven departed staff accounts active; four privileged grants lack need | Service accounts must be classified separately |
| E-05 | Vendor procurement packet | No current assurance review or incident notification terms in packet | Evidence might exist elsewhere; request before final conclusion |
| E-06 | Log source inventory | Endpoint alerts present; cloud admin events absent centrally | Requires live test to confirm pipeline and triage effectiveness |
| E-07 | Draft response procedure | Old contacts; no tabletop record | Interview participants and inspect operating evidence in a real review |
| E-08 | Export-folder permission listing | Broad staff access; no approved disposal schedule | File contents and actual use not observed |

## Example workpaper: R-04

**Objective:** Access remains appropriate after departure or role changes.

**Simulated method:** Compare the assumed full terminated-staff roster to the identity export, then inspect privileged-role assignments. This is a full-population simulation, not a sampled production test.

**Result:** Seven active departed-user accounts and four unjustified grants. Status: Partial. Current score: 4 × 4 = 16 (High).

**Recommendation:** Disable stale identities, confirm session/token revocation where supported, remove or approve excess privileges, then reconcile HR changes through an owned workflow.

**Closure evidence:** Account-disable timestamps, reconciliation with no unexplained differences, documented grant approvals, and tested revocation. A planned task or policy draft alone is insufficient.

**Target:** 2 × 4 = 8 (Moderate), conditional on effective operation and retesting. No actual residual score has been verified.
