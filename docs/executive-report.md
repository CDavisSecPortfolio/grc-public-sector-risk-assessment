# Executive report

## Decision requested

Authorize a hypothetical 90-day treatment program for the fictional Cedar Harbor Municipal Services agency. Prioritize identity protection, patch remediation, and tested recovery. Assign business accountability for remaining risk and require evidence before closure.

## Findings

Eight simulated risks were evaluated: two Critical, five High, and one Moderate. Critical exposures concern uncovered staff identities and overdue endpoint patches. Backups warrant parallel work because reported job success does not establish the ability to restore critical services.

| Priority | Risk | Current score | Why act now |
| --- | --- | --- | --- |
| 1 | R-01: Credential theft | 20 Critical | Staff access can expose or alter resident records |
| 2 | R-02: Ransomware | 20 Critical | Widespread weaknesses can interrupt agency operations |
| 3 | R-04: Inappropriate access | 16 High | Departed-user accounts and unnecessary privileges remain active |
| 4 | R-03: Failed recovery | 15 High | Restoration is untested and backup access shares failure paths |

These are qualitative scenario judgments, not measured attack probabilities. No dollar loss, breach occurrence, or compliance status is asserted.

## Treatment sequence

Days 0–30: review MFA exclusions and restrict interim access; remediate or isolate overdue endpoints; remove stale access; separate backup administration and conduct an isolated restore. The service owner must approve recovery objectives before testing.

Days 31–60: complete hosting-vendor review, connect and test cloud administrative monitoring, and exercise incident escalation. Vendor management should document notification expectations appropriate to the service and contract.

Days 61–90: restrict data exports, approve retention rules after recordkeeping review, retest completed actions, and refresh scores. A policy or ticket marked complete is insufficient closure evidence.

## Forecast and ongoing decisions

Proposed target ratings are three High and five Moderate. R-01, R-02, and R-03 remain High because a successful event could still have severe consequences even after likelihood decreases. These forecast scores do not prove risk reduction. Owners must validate operation before assigning actual residual ratings, and leadership must decide whether further mitigation or time-limited acceptance is appropriate.

Track MFA enforcement coverage, overdue patches, departed-user account exceptions, restore-test outcomes, log-feed health, and action completion with evidence. Averages should not replace attention to individual Critical risks.

## Limitations

This report is based solely on synthetic inputs and a selected scope. It is not a comprehensive NIST CSF implementation, audit, legal assessment, or real agency engagement. NIST category mappings support organizing the analysis; the project defines its own scales and planning targets.
