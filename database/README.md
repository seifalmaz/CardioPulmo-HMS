# CardioPulmo-HMS Database & Migrations

**Role:** Relational Schema, Alembic Versioning, and Seeding  
**Lead Owner:** Member 3 (DB & Security Lead)  
**Technologies:** PostgreSQL 16, SQLAlchemy 2.0, Alembic

---

## 1. Directory Structure

* `database/migrations/`: Alembic database schema migration scripts.
* `database/seeds/`: Initial deterministic seed data (LOINC test catalogues, standard reference intervals, demo clinician accounts).

---

## 2. Migration Commands

```bash
# Generate new migration
alembic revision --autogenerate -m "describe_migration"

# Apply pending migrations
alembic upgrade head
```
