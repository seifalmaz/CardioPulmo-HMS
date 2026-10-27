# CardioPulmo-HMS Operational & Batch Scripts

**Role:** Automation, Data Ingestion, and Developer Utilities

---

## 1. Directory Contents (Planned)

* `setup_environment.sh` / `setup_environment.ps1`: Automated developer setup script for Python venv, dependencies, and git hooks.
* `download_datasets.py`: Script to download and verify Synthea, UCI, and WHO sample datasets.
* `run_medallion_etl.py`: Batch ETL runner executing Bronze &rarr; Silver &rarr; Gold data pipelines.
* `seed_demo_database.py`: CLI command to populate the local PostgreSQL database with demo cardio-pulmonary cases.
