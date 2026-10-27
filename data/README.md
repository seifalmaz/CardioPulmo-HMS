# CardioPulmo-HMS Data Management & Governance

**Role:** Data Engineering, Ingestion, and Medallion Storage  
**Lead Owner:** Member 4 (Data Engineering Lead)

---

## 1. Directory Structure

* `data/raw/`: Immutable, read-only landing zone for downloaded raw datasets (Bronze tier). Excluded from Git tracking.
* `data/processed/`: Schema-validated, unit-normalized Silver tier datasets. Excluded from Git tracking.
* `data/synthetic/`: Synthea-generated synthetic EHR records used for functional and unit testing.

---

## 2. Governance Rules

> [!IMPORTANT]
> 1. Never commit patient PII, un-anonymized datasets, or large raw archives into Git.
> 2. All files in `data/raw/` must have corresponding SHA-256 integrity checksums logged in the audit mart.
> 3. Synthetic EHR data must always be clearly demarcated with the `synthetic` prefix in MRNs and patient IDs (`pat-syn-XXXX`).
