# CardioPulmo-HMS: System Specification & Requirements

## 1. Executive Summary & Guiding Charter

* **Project Goal:** Design and build an integrated, secure, web-based hospital management and clinical intelligence platform specialized for Cardiology and Pulmonology.
* **Core Pillars:**
  1. Multi-role clinical workflows (Patient, Doctor, Laboratory, Administrator).
  2. Reproducible healthcare data engineering platform (Medallion architecture).
  3. Operational, clinical, and epidemiological analytics.
  4. Two core machine learning workstreams:
     * Tabular Clinical Risk/Diagnosis ML with SHAP explanations.
     * Deep Learning Computer Vision on NIH ChestX-ray14 with PyTorch Grad-CAM localization.
  5. Source-grounded Patient RAG Assistant with verified citations.
  6. Structured, auditable AI-Agent Handoff protocol with cryptographic integrity and injection defense.
* **Effort Allocation:** 60% Software Engineering, 20% AI & Data Science, 20% Applied AI & Security.

---

## 2. The 7 Core Project Objectives

| ID | Domain | Objective Description & Concrete Deliverables |
| :--- | :--- | :--- |
| **OBJ-1** | **Hospital Workflows** | Role-specific web portals for Patients, Doctors (Cardiology & Pulmonology), Lab Technicians, and Administrators covering encounters, appointments, lab orders, thoracic imaging, and referrals. |
| **OBJ-2** | **Data Platform** | Repeatable batch ETL pipelines (Bronze Raw &rarr; Silver Validated &rarr; Gold Curated Star Schema) with automated schema validation, unit standardization, and lineage tracking. |
| **OBJ-3** | **BI & Analytics** | Operational, clinical, AI-evaluation, and WHO population-health dashboards whose KPIs have documented mathematical definitions and traceable table sources. |
| **OBJ-4** | **Tabular ML** | Train, calibrate, evaluate, and serve a leakage-free tabular clinical classification model with local SHAP explanations via a schema-validated FastAPI inference endpoint. |
| **OBJ-5** | **Computer Vision** | Multi-label thoracic pathology screening & localization pipeline using NIH ChestX-ray14 (PyTorch + Grad-CAM visual heatmaps) inside the clinician workspace. |
| **OBJ-6** | **Grounded Patient RAG** | Citation-backed patient education and navigation assistant, empirically benchmarking baseline Vector RAG against Graph-Enhanced Retrieval (GraphRAG). |
| **OBJ-7** | **Secure Agent Handoff** | Authenticated, schema-validated, auditable AI-assisted clinical handoff protocol between Cardiology and Pulmonology workflows with prompt-injection defenses. |

---

## 3. Explicit Clinical Non-Goal Boundary

**CardioPulmo-HMS is an educational, research, and clinical decision-support system.**
* It **does not** replace licensed medical judgment.
* It **does not** perform autonomous medical diagnosis or autonomously change prescription orders.
* All AI predictions, risk scores, and Grad-CAM heatmaps are presented as advisory visual aids requiring explicit clinician review and digital sign-off.
* In the event of system error or missing diagnostic tests, the system explicitly communicates uncertainty rather than hallucinating clinical recommendations.
