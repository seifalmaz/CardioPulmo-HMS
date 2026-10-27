# CardioPulmo-HMS: Multi-Modal Dataset Strategy & Governance

## 1. Strict Dataset Separation Rule

> [!CAUTION]
> **Never merge Synthea, WHO, UCI/CDC, or NIH ChestX-ray14 records as though they belong to the same real individual.**
> In system demonstrations, synthetic patient encounters trigger the trained Tabular ML and NIH ChestX-ray14 Computer Vision models via explicitly labeled clinical simulation workflows.

---

## 2. Inventory of Multi-Modal Datasets

| Dataset & Source | Status | Modality & Scale | Intended Project Role & Split Governance |
| :--- | :--- | :--- | :--- |
| **A. Synthea EHR** | **CORE** | Synthetic CSV & HL7 FHIR R4 JSON | Seed fictional patients, encounters, vitals, conditions, and lab workflows. Strictly separated from ML training cohorts. |
| **B. NIH ChestX-ray14** | **CORE (CV)** | 112,120 Frontal CXR PNGs (30,805 Patients) | Primary Computer Vision Dataset: Multi-label classification & Grad-CAM localization across 14 thoracic pathologies. **Strict Patient-Level Split (70/15/15)**. |
| **C. UCI Heart Disease / CDC Indicators** | **CORE (ML)** | Structured Clinical Tabular CSV | Primary Tabular ML Dataset: Supervised classification of cardiovascular disease / cardio-metabolic risk indicators with zero-leakage pipelines. |
| **D. WHO NCD / GHO Microdata** | **CORE (BI)** | Population Survey & Macro Indicators | Macro population-level risk-factor comparisons (hypertension, smoking, mortality). Document survey weights and cross-country caveats. |
| **E. MIMIC-IV / PTB-XL ECG** | **OPTIONAL** | De-identified EHR / 12-Lead ECG Waveforms | Optional research extensions only if credentialing and all core hospital, Tabular ML, and NIH CV milestones are completed early. |

---

## 3. Storage & Privacy Controls

* **Raw Data Isolation:** Raw archives (`.zip`, `.tar.gz`, `.dcm`) reside in `data/raw/` and are excluded from version control via `.gitignore`.
* **Access Control:** De-identified images are served via temporary, signed URLs rather than publicly accessible endpoints.
* **Audit Lineage:** Every batch ingestion script records batch ID, input SHA-256 checksums, and record counts into the Medallion audit mart.
