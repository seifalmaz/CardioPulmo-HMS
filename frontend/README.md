# CardioPulmo-HMS Frontend

**Role:** Presentation Layer & Multi-Role Clinical Workspaces  
**Lead Owner:** Member 1 (Frontend Lead)  
**Technologies:** React 18/19, TypeScript, Tailwind CSS, Lucide Icons, Recharts / Plotly.js

---

## 1. Overview & Architecture

The frontend application provides unified clinical access across four primary roles via a persistent global Role Switcher:
1. **Patient Portal:** Scoped dashboard, medication & allergy alerts, released laboratory range bars, and cited AI assistant.
2. **Clinician Workspace:** 4-tab encounter studio (SOAP notes, Thoracic CV Grad-CAM viewer, Tabular ML SHAP risk panel, longitudinal labs) and the Cross-Specialty AI Handoff drawer.
3. **Laboratory Workspace:** Priority specimen work queue, LOINC result verification, and amendment auditing.
4. **Administrator & Governance Console:** User & specialty directory, LOINC catalogue management, operational BI analytics, and security audit log explorer.

---

## 2. Directory Structure (Planned)

```
frontend/
├── public/                     # Static assets, DICOM test samples, icons
├── src/
│   ├── assets/                 # SVGs and static brand graphics
│   ├── components/             # Reusable and role-specific UI components
│   │   ├── admin/              # Administrator & Governance console
│   │   ├── common/             # Badges, banners, role switchers, modals
│   │   ├── doctor/             # Clinician workspace, Grad-CAM viewer, SHAP panel
│   │   ├── lab/                # LIS work queue, result verification console
│   │   └── patient/            # Patient dashboard, range bars, cited chat
│   ├── data/                   # Clinical models, mock datasets, LOINC catalogue
│   ├── types/                  # TypeScript interface definitions (clinical.ts)
│   ├── App.tsx                 # Root application with role switching
│   ├── main.tsx                # Application entry point
│   └── index.css               # Tailwind CSS & design tokens
├── package.json                # Dependencies and scripts
├── tailwind.config.js          # Tailwind design theme
├── tsconfig.json               # TypeScript compiler options
└── vite.config.ts              # Vite build configuration
```

---

## 3. Initial Prototype Reference

An interactive, high-fidelity UI prototype validating all 4 roles, the NIH ChestX-ray14 Grad-CAM dual-pane viewer, and the AI handoff drawer was created during Milestone 1 in the local workspace directory `D:\Graduation Project`. When ready for formal repository integration, its components will be placed directly in this `frontend/` directory.
