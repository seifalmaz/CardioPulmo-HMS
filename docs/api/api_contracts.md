# CardioPulmo-HMS: API Contracts & Architecture

## 1. Overview & Conventions

* **Framework:** Python 3.11+ / FastAPI
* **Base URL:** `/api/v1`
* **Authentication:** HTTP Bearer token (JWT)
* **Response Format:** JSON (strict Pydantic schemas)
* **Error Format:** RFC 7807 Problem Details:
  ```json
  {
    "detail": "Error description message",
    "status_code": 403,
    "error_code": "BOLA_VIOLATION",
    "correlation_id": "corr-uuid"
  }
  ```

---

## 2. Core Endpoint Summary

### Authentication & Users
* `POST /api/v1/auth/login`: Authenticate email/password with Argon2id; returns access & refresh tokens.
* `POST /api/v1/auth/refresh`: Issue new short-lived access token.
* `GET /api/v1/users/me`: Return authenticated session context and scoped permissions.

### Patients & Encounters
* `GET /api/v1/patients/{patient_id}`: Retrieve scoped patient summary (patient or assigned clinician only).
* `GET /api/v1/patients/{patient_id}/encounters`: Retrieve visit history.
* `POST /api/v1/encounters`: Create clinical encounter with structured SOAP notes.

### Laboratory Information System (LIS)
* `GET /api/v1/labs/orders`: Retrieve lab order queue filterable by priority (`STAT`, `Urgent`, `Routine`).
* `POST /api/v1/labs/orders`: Clinician submits test orders (LOINC mapped).
* `PATCH /api/v1/labs/specimens/{specimen_id}/status`: Advance specimen state (`Collected`, `Processing`, `Completed`).
* `POST /api/v1/labs/results/{order_id}/verify`: Record test result, verify flags, and apply digital sign-off.
* `POST /api/v1/labs/results/{result_id}/amend`: Record amended result with mandatory legal audit reason.

### Clinical AI & Computer Vision
* `POST /api/v1/ai/cxr-screening`: Submit radiograph image; returns calibrated probabilities across 14 pathologies and Grad-CAM heatmap URI.
* `POST /api/v1/ai/tabular-risk`: Submit clinical features; returns calibrated 30-day heart failure risk and local SHAP feature attributions.

### Cross-Specialty AI Handoff
* `POST /api/v1/referrals/handoff`: Generate and dispatch a provenance-sealed cross-specialty referral.
* `GET /api/v1/referrals/handoff/{correlation_id}`: Retrieve referral contract for review.
* `PATCH /api/v1/referrals/handoff/{correlation_id}/status`: Update referral state (`ACCEPTED`, `INFO_REQUESTED`, `REJECTED`).
