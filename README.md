# CardioPulmo-HMS

**Intelligent Hospital Management System Specialized for Cardiology & Pulmonology**  
*with a Secure AI Agent Handoff Mechanism*

---

## 1. Project Overview & Academic Identity

* **Project Name:** `CardioPulmo-HMS`
* **Academic Thesis Title:**  
  *Design and Development of an Intelligent Hospital Management System Using Artificial Intelligence and Data Analytics, with a Secure AI Agent Handoff Mechanism.*
* **Authors:** 6-Member Computer Science Graduation Project Team.
* **Specialization:** Cardiology & Pulmonology Clinical Co-Management.
* **Planning Effort Allocation:**
  * **60%** Software Engineering (Hospital Workflows, Role Portals, Security, Lab Lifecycle)
  * **20%** AI & Data Science (NIH ChestX-ray14 CV Screening, Tabular Risk ML, Medallion ETL)
  * **20%** Applied AI & Secure Agent Handoff (Cross-Specialty Protocol, Prompt Injection Defense, Cited Patient GraphRAG)

The primary objective of **CardioPulmo-HMS** is to build a functional, production-ready, and clinically governed hospital management system. It is designed not as a disconnected research prototype, but as an integrated clinical application addressing the diagnostic and care-coordination overlaps between cardiovascular and respiratory illnesses.

---

## 2. Clinical Domain & Overlapping Cardio-Pulmonary Care

Patients frequently present to hospital clinics with non-specific, overlapping symptoms such as **dyspnea (shortness of breath)**, **chest discomfort**, **hypoxemia**, and **fatigue**. In traditional hospital information systems, Cardiology and Pulmonology operate in administrative and informational silos:

* Fluid retention caused by **Heart Failure (HFrEF/HFpEF)** causes pulmonary congestion and bilateral **pleural effusion**.
* Chronic lung pathology (e.g., **COPD**, pulmonary fibrosis) drives elevated pulmonary vascular resistance leading to right heart strain (**Cor Pulmonale**).
* Diagnostic handoffs, imaging reviews, and biomarker trends (e.g., **NT-proBNP**, **hs-cTnI**, **PaO2/PaCO2**) require cross-departmental coordination that is historically prone to communication failure, lost context, or lack of provenance.

CardioPulmo-HMS bridges this gap by unifying multi-role hospital workflows with verified clinical AI decision-support and an auditable, cryptographically validated AI Agent Handoff mechanism.

---

## 3. Core Hospital Management Workflows

CardioPulmo-HMS provides four distinct, role-scoped web workspaces enforcing strict least-privilege access:

1. **Patient Portal (`Role: Patient`):**
   * Accessible patient dashboard with upcoming visit schedules, active medication summaries, and verified allergy alerts.
   * Released laboratory panels with visual reference range bars and longitudinal biomarker sparklines.
   * Clinician-approved visit instructions (sodium/fluid limits, daily weight tracking).
   * Cited Patient AI Health Assistant with verified clinical citations and non-diagnostic guardrails.

2. **Clinician Encounter Studio (`Role: Doctor — Cardiology & Pulmonology`):**
   * Clinical Command Center tracking daily patient queues, incoming/outgoing referrals, and STAT alerts.
   * **Tab A (Clinical SOAP & Vitals):** Encrypted encounter documentation, 12-lead ECG review, and arterial blood gas references.
   * **Tab B (Thoracic CV Studio):** Frontal radiograph viewer with PyTorch Grad-CAM localization across 14 thoracic pathologies and mandatory clinician sign-off.
   * **Tab C (Tabular ML Clinical Risk):** Calibrated 30-day decompensation risk gauge, SHAP feature waterfall attribution, and clinical what-if scenario simulations.
   * **Tab D (Longitudinal Labs & Trends):** Multi-encounter trend tracking and one-click LOINC test ordering.
   * **Cross-Specialty AI Handoff Drawer:** Provenance-sealed referral generation between Cardiology and Pulmonology.

3. **Laboratory Information System (`Role: Lab Staff`):**
   * Specimen and order queue filterable by priority (`STAT`, `Urgent`, `Routine`).
   * Specimen lifecycle transitions: `Ordered` &rarr; `Collected` &rarr; `Processing` &rarr; `Completed` &rarr; `Amended`.
   * Result entry console with automated demographic reference interval flagging and digital verification sign-off.
   * Immutable amendment audit logging requiring mandatory clinical justification.
   * Turnaround Time (TAT) analytics and specimen rejection tracking.

4. **Administrator & Security Governance Console (`Role: Administrator`):**
   * Enforced data isolation: **Administrators have zero access to raw clinical patient records**.
   * Role-Based Access Control (RBAC) directory and specialty credentialing.
   * LOINC test catalogue and reference range interval configuration.
   * Enterprise operational dashboards (bed occupancy, length of stay, laboratory throughput) and WHO NCD macro indicators.
   * Immutable tamper-evident audit trail capturing authentication, BOLA/IDOR interceptions, and AI handoff transactions.

---

## 4. Planned AI & Data Science Contributions

CardioPulmo-HMS integrates empirical data science directly into clinical workflows without compromising data integrity:

* **Deep Learning Computer Vision (NIH ChestX-ray14):**
  * Multi-label screening across 14 thoracic pathologies (Effusion, Cardiomegaly, Infiltration, Atelectasis, Pneumonia, Edema, etc.).
  * Fine-tuned DenseNet-121 / CheXNet backbone trained strictly on patient-level splits (`GroupShuffleSplit` 70/15/15) to prevent longitudinal data leakage.
  * Spatial visual interpretability via **Grad-CAM heatmaps** overlaid on frontal radiographs with PACS-style window/level contrast controls.
* **Primary Tabular Machine Learning (Cardio-Metabolic Risk):**
  * Calibrated clinical risk estimation (e.g., 30-day decompensated heart failure risk) using Scikit-Learn and XGBoost/LightGBM pipelines.
  * Rigorous probability calibration using Platt Scaling / Isotonic Regression with Brier score optimization.
  * Local model explainability via **SHAP (SHapley Additive exPlanations)** waterfall bar charts isolating exact biomarker risk drivers (e.g., NT-proBNP, SpO2 desaturation, systolic blood pressure).
* **Medallion Data Engineering Pipeline:**
  * Bronze (Raw immutable snapshots with SHA-256 checksums) &rarr; Silver (Validated, schema-checked, and unit-standardized records) &rarr; Gold (Curated Star Schema analytical marts: `fact_encounters`, `fact_lab_results`, `fact_referrals`, `fact_model_predictions`).

---

## 5. Secure AI Agent Handoff Protocol

When a Cardiologist requests Pulmonology consultation (e.g., finding bilateral pleural effusion during acute decompensated heart failure management) or vice versa, the system generates an auditable, minimal **AI Referral Handoff Packet**:

* **Minimum-Necessary Context Scoping:** Gathers only pertinent vitals, verified lab results, and CV screening probabilities.
* **Explicit Uncertainty & Missingness:** Flags pending tests (e.g., pending ABG or missing spirometry) to prevent diagnostic overconfidence.
* **Cryptographic Provenance:** Embeds an immutable **SHA-256 seal** over the clinical payload.
* **Adversarial Prompt-Injection Defense:** Uses strict Pydantic JSON schema boundaries and sanitizes untrusted free-text clinician notes.
* **Human-in-the-Loop Governance:** Referrals require receiving clinician acceptance (`Accept`, `Request Info`, `Reject`) before entering the medical record.

---

## 6. System Architecture & Verified Technology Stack

### System Layer & Confirmed Technologies

| System Layer | Confirmed Technology Choice | Status / Candidate Alternatives |
| :--- | :--- | :--- |
| **Frontend UI** | **React 18/19, TypeScript, Tailwind CSS, Lucide Icons** | Confirmed (Phase 1 prototype validated) |
| **Data Visualization** | **Recharts / Plotly.js** | Confirmed for EHR sparklines, SHAP waterfalls, & TAT charts |
| **Backend API** | **Python 3.11+, FastAPI, Pydantic v2** | Confirmed for async performance & strict schema validation |
| **ORM & Migrations** | **SQLAlchemy 2.0, Alembic** | Confirmed for relational mapping & database versioning |
| **Primary Database** | **PostgreSQL 16** | Confirmed for relational integrity, JSONB support, and RBAC |
| **Security & Auth** | **Argon2id, Short-lived JWT, Scoped RBAC** | Confirmed for zero-trust token auth and password security |
| **Tabular ML** | **Scikit-Learn, XGBoost, SHAP** | Confirmed for tabular classification & explainability |
| **Computer Vision** | **PyTorch, Torchvision, DenseNet-121, Grad-CAM** | Confirmed for ChestX-ray14 multi-label screening |
| **Patient Assistant** | **FastAPI, Vector Store (Chroma), NetworkX (GraphRAG)** | Confirmed candidate architecture for cited guidance |
| **Testing** | **Pytest, Pytest-Asyncio, Playwright** | Confirmed for unit, integration, and E2E validation |

---

## 7. Team Responsibilities & 6-Member Ownership

| Team Member | Domain & Role | Primary Integration Responsibilities |
| :--- | :--- | :--- |
| **Member 1** | **Frontend Lead** | 4 Role Portals, Dual-Pane CXR Viewer, Grad-CAM overlays, Accessibility, Playwright UI tests |
| **Member 2** | **Backend Lead** | FastAPI core, Encounters, Appointments, Lab & Referral state machines, REST contracts |
| **Member 3** | **DB & Security Lead** | PostgreSQL schema, Alembic migrations, Argon2id auth, BOLA/IDOR guards, Security audit logs |
| **Member 4** | **Data Engineering Lead** | Bronze/Silver/Gold ETL, Star Schema analytical marts, Synthea pipelines, Great Expectations reports |
| **Member 5** | **ML & Computer Vision Lead** | NIH ChestX-ray14 patient split & DenseNet-121 training, Grad-CAM service, Tabular ML & SHAP API |
| **Member 6** | **Applied AI & Agent Lead** | Cited Patient RAG assistant, Vector vs. GraphRAG benchmarking, Cardio-Pulmo handoff protocol |

---

## 8. Multi-Modal Dataset Strategy & Governance

Strict data governance is enforced across all project phases. **Datasets are never mixed or merged into fictional combined individual profiles:**

1. **Synthea EHR:** Synthetic HL7 FHIR / CSV patient cohort used to seed non-real patients, visits, vitals, conditions, and lab orders.
2. **NIH ChestX-ray14:** 112,120 frontal chest radiographs across 30,805 unique patients used exclusively for computer vision training, validation, and holdout testing under strict patient-level partition.
3. **UCI Heart Disease / CDC Indicators:** Structured tabular benchmarks used for tabular risk classifier training.
4. **WHO Non-Communicable Diseases (GHO):** Macro-level population health indicators used exclusively for administrative and epidemiological analytics.

---

## 9. Repository Directory Structure

```
CardioPulmo-HMS/
├── README.md                           # Master project documentation
├── .gitignore                          # Strict gitignore covering secrets, data, and models
├── .env.example                        # Safe environment variable configuration template
├── docs/                               # Architectural, clinical, and security specifications
│   ├── requirements/                   # Functional and non-functional requirements
│   ├── architecture/                   # System architecture and RBAC specifications
│   ├── database/                       # Star schema and relational data dictionary
│   ├── api/                            # FastAPI endpoint contracts and schemas
│   ├── datasets/                       # Multi-modal dataset strategy and governance
│   ├── machine-learning/               # Tabular ML and NIH ChestX-ray14 CV specifications
│   ├── agent-handoff/                  # Cross-Specialty AI handoff protocol specification
│   ├── testing/                        # Test strategy, security audits, and benchmarks
│   └── deployment/                     # Local and production deployment guides
├── frontend/                           # React + TypeScript + Tailwind CSS application
├── backend/                            # FastAPI application and business workflows
├── data/                               # Healthcare data storage (git-ignored)
│   ├── raw/                            # Bronze raw immutable datasets
│   ├── processed/                      # Silver validated datasets
│   └── synthetic/                      # Synthea generated patient records
├── ml/                                 # Machine learning code and pipelines
│   ├── notebooks/                      # Exploratory data analysis and model training
│   ├── src/                            # Training, preprocessing, and evaluation code
│   ├── models/                         # Model weights and artifacts (git-ignored)
│   └── evaluation/                     # Metric evaluation reports, ROC-AUC, and calibration
├── agent-handoff/                      # Cardio-Pulmonology AI Handoff Protocol
│   ├── schemas/                        # Pydantic models and JSON schemas
│   ├── tests/                          # Integrity, signature, and injection defense tests
│   └── examples/                       # Sample handoff referral payloads
├── database/                           # Relational database resources
│   ├── migrations/                     # Alembic migration scripts
│   └── seeds/                          # Initial database seed scripts (LOINC, accounts)
├── tests/                              # Global test suites
│   ├── integration/                    # Multi-component integration tests
│   └── end-to-end/                     # End-to-end workflow verification
└── scripts/                            # Operational, setup, and ETL batch scripts
```

---

## 10. Security, Privacy & Clinical Limitations

* **Clinical Non-Goal Boundary:** CardioPulmo-HMS is an educational, research, and clinical decision-support system. It **does not** provide autonomous medical diagnosis and cannot prescribe treatments without explicit licensed clinician verification.
* **Data Isolation & Least Privilege:** System Administrators have zero read permissions on clinical EHR tables or patient encounter notes.
* **BOLA / IDOR Protection:** All API endpoints validate resource ownership against authenticated user session context (verified with automated `403 Forbidden` security test suites).
* **Prompt Injection Guardrails:** Free-text clinical notes in referrals are strictly delimited and passed through schema-enforced parsers before AI processing.
* **Local Storage & Privacy:** Real patient data is strictly prohibited in this repository. All development and testing use synthetic Synthea data or public de-identified research benchmarks.

---

## 11. Implementation Roadmap & Acceptance Milestones

* [x] **Milestone 1 — Architecture & UI Mockups:** Complete DB schema, API contracts, threat model, and interactive 4-role prototype (Completed).
* [ ] **Milestone 2 — Secure Hospital MVP:** Argon2id authentication, RBAC middleware, Patient/Doctor portals, Appointments, and cross-patient isolation.
* [ ] **Milestone 3 — Laboratory Information Module:** LOINC test catalogue, specimen order-to-verification lifecycle, and immutable amendment auditing.
* [ ] **Milestone 4 — Medallion ETL & Analytical Marts:** Bronze/Silver/Gold batch pipelines, Star Schema analytical marts, and BI dashboards.
* [ ] **Milestone 5 — NIH ChestX-ray14 CV & Tabular ML:** PyTorch DenseNet-121 training on patient-level split, Grad-CAM visualization, and XGBoost SHAP integration.
* [ ] **Milestone 6 — Cited Patient RAG & GraphRAG:** Approved clinical education corpus indexing, strict citation enforcement, and GraphRAG benchmarking.
* [ ] **Milestone 7 — Secure AI Agent Handoff Protocol:** Pydantic schema enforcement, SHA-256 seal verification, context minimization, and prompt-injection defense.
* [ ] **Milestone 8 — End-to-End Verification & Delivery:** Comprehensive functional, security, data-pipeline, and AI evaluation test suites for thesis defense.

---

## 12. Setup & Getting Started

*(Detailed installation guides will expand as backend and frontend packages are initialized in their respective directories.)*

### Prerequisites
* **Python:** 3.11+
* **Node.js:** 18+ (LTS recommended)
* **Git:** 2.40+
* **PostgreSQL:** 16+

### Quick Start (Local Setup)
1. **Clone the repository:**
   ```bash
   git clone https://github.com/seifalmaz/CardioPulmo-HMS.git
   cd CardioPulmo-HMS
   ```
2. **Environment configuration:**
   ```bash
   cp .env.example .env
   # Edit .env with your local database and server parameters
   ```
3. **Follow component READMEs:**
   * Backend setup instructions: [`backend/README.md`](file:///D:/CardioPulmo-HMS/backend/README.md)
   * Frontend setup instructions: [`frontend/README.md`](file:///D:/CardioPulmo-HMS/frontend/README.md)
   * AI Handoff documentation: [`agent-handoff/README.md`](file:///D:/CardioPulmo-HMS/agent-handoff/README.md)
