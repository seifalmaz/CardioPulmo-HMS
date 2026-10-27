# CardioPulmo-HMS Global Test Suites

**Role:** End-to-End, Integration, and Security Verification

---

## 1. Directory Structure

* `tests/integration/`: Cross-service API tests validating authentication, RBAC, laboratory state machines, and AI handoff endpoints using FastAPI `TestClient`.
* `tests/end-to-end/`: Complete browser-driven clinical workflow simulations (e.g., patient booking &rarr; clinician encounter &rarr; lab order &rarr; LIS verification &rarr; Pulmonology AI handoff) using Playwright.

---

## 2. Running Test Suites

```bash
# Run all unit and integration tests
pytest tests/ -v

# Run with test coverage report
pytest --cov=backend/app --cov-report=html
```
