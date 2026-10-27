# CardioPulmo-HMS Documentation Hub

Welcome to the comprehensive technical documentation for **CardioPulmo-HMS: Intelligent Cardio-Pulmonary Hospital Management System**.

## Documentation Sitemap

| Category | Document | Description |
| :--- | :--- | :--- |
| **Requirements** | [`requirements/system_specification.md`](file:///D:/CardioPulmo-HMS/docs/requirements/system_specification.md) | Full system specification, objectives OBJ-1 through OBJ-7, and clinical boundaries |
| **Architecture** | [`architecture/system_architecture.md`](file:///D:/CardioPulmo-HMS/docs/architecture/system_architecture.md) | Multi-role portal architecture, RBAC matrix, and Medallion ETL pipeline |
| **Database** | [`database/data_dictionary_and_star_schema.md`](file:///D:/CardioPulmo-HMS/docs/database/data_dictionary_and_star_schema.md) | OLTP schema, Star Schema analytical marts (`fact_encounters`, `dim_doctor`, etc.) |
| **API** | [`api/api_contracts.md`](file:///D:/CardioPulmo-HMS/docs/api/api_contracts.md) | FastAPI endpoint specifications, Pydantic schemas, and error handling |
| **Datasets** | [`datasets/dataset_strategy.md`](file:///D:/CardioPulmo-HMS/docs/datasets/dataset_strategy.md) | Multi-modal data strategy (Synthea, NIH ChestX-ray14, UCI, WHO GHO) |
| **Machine Learning** | [`machine-learning/ml_cv_specifications.md`](file:///D:/CardioPulmo-HMS/docs/machine-learning/ml_cv_specifications.md) | NIH ChestX-ray14 DenseNet-121 Grad-CAM, XGBoost SHAP waterfall models |
| **Agent Handoff** | [`agent-handoff/protocol_specification.md`](file:///D:/CardioPulmo-HMS/docs/agent-handoff/protocol_specification.md) | Cross-specialty handoff JSON contract, SHA-256 seal, and prompt-injection guardrails |
| **Testing** | [`testing/test_strategy.md`](file:///D:/CardioPulmo-HMS/docs/testing/test_strategy.md) | Unit, integration, security (BOLA/IDOR), and clinical simulation test plans |
| **Deployment** | [`deployment/deployment_guide.md`](file:///D:/CardioPulmo-HMS/docs/deployment/deployment_guide.md) | Local development, environment setup, containerization, and production considerations |
