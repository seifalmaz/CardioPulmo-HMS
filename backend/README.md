# CardioPulmo-HMS Backend

**Role:** Application Core, Business Workflows & Scoped REST APIs  
**Lead Owner:** Member 2 (Backend Lead)  
**Technologies:** Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic, PostgreSQL 16

---

## 1. Overview & Architecture

The backend implements the core clinical workflows, authentication, state machines, and API endpoints for CardioPulmo-HMS:
* **Authentication:** Argon2id password hashing and short-lived JWT access tokens with revocable refresh tokens.
* **RBAC & Data Scoping:** Middleware enforcing patient-specific resource ownership, clinician assignments, and zero clinical access for administrators.
* **Laboratory Lifecyle:** Automated state machine managing specimen transitions (`Ordered` &rarr; `Collected` &rarr; `Processing` &rarr; `Completed` &rarr; `Amended`).
* **Referral Management:** Storage and routing of cryptographically sealed cross-specialty AI handoffs.

---

## 2. Directory Structure (Planned)

```
backend/
├── app/
│   ├── api/                    # Versioned REST routers (v1)
│   │   ├── auth.py             # Login, token refresh, password management
│   │   ├── patients.py         # Patient profile and summary endpoints
│   │   ├── encounters.py       # SOAP notes and clinical encounters
│   │   ├── labs.py             # LIS order queue, verification, and amendments
│   │   ├── referrals.py        # Cross-specialty AI handoffs
│   │   └── ai.py               # Proxies to ML & CV inference services
│   ├── core/                   # Application settings, security, and dependencies
│   │   ├── config.py           # Pydantic Settings reading .env
│   │   ├── security.py         # Password hashing & JWT token generators
│   │   └── rbac.py             # Role & resource ownership guard dependencies
│   ├── db/                     # Database engine & session management
│   │   ├── session.py          # SQLAlchemy async engine & sessionmaker
│   │   └── base.py             # Declarative base model
│   ├── models/                 # SQLAlchemy 2.0 ORM database models
│   ├── schemas/                # Pydantic v2 request & response schemas
│   ├── services/               # Clinical business logic & state machines
│   └── main.py                 # FastAPI application factory & CORS setup
├── requirements.txt            # Python backend dependencies
└── tests/                      # Pytest unit & integration test suites
```
