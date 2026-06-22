# 24-data-localization-requirements.md

## Source URL
- https://www.legislation.gov.au/Details/C2017C00313/Html/Text#_Toc493614544 (My Health Records Act 2012, s 77)
- https://www.apra.gov.au/standards-and-guidance (APRA CPS 230 - Operational Risk)

## Last Verified
2026-05-19

## Authority Tier
Statute / Regulator Standard

## Currency Warning
APRA CPS 230 becomes effective **1 July 2025**.

## Key Facts
1. **Health Data (s 77):** Explicit prohibition on holding, taking, or processing My Health Record data outside Australia.
2. **Financial Services (CPS 230):** APRA-regulated entities (Banks/Insurers) must ensure their "critical operations" (including those outsourced to law firms) have robust data resilience; often practically necessitates Australian data residency.
3. **APP 8 (Privacy):** While not a "hard" localization requirement, the "deemed liability" of the Australian entity for overseas breaches makes Australian storage the "low risk" default.
4. **Government Contracts:** Many state and federal government legal panels mandate that all data (including backups) must remain in Australia.
5. **Cloud Regions:** Solos must specifically select "Australia" (e.g., Sydney/Melbourne) as their data region in AWS/Azure/Google Cloud.

## Verbatim Quote (if applicable)
"The System Operator... and a person who provides services to the System Operator... must not hold, take or have a My Health Record... outside Australia." — Section 77(1), My Health Records Act.

## Practical Implication for Solo Advocate
- Solos must verify the "Data Residency" of their Practice Management Software (PMS).
- Using "Standard" US-based cloud tiers is a breach for any solo handling health data or government panel work.
- Solos should obtain "Data Residency Certificates" from their vendors for compliance audits.
