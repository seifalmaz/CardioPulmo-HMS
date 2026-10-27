# CardioPulmo-HMS: Deployment & Environment Guide

## 1. System Requirements

* **Operating System:** Linux (Ubuntu 22.04 LTS recommended) or Windows 10/11 with WSL2.
* **CPU:** 4+ cores recommended.
* **RAM:** 16 GB minimum (32 GB recommended for NIH ChestX-ray14 batch processing).
* **GPU (Optional for inference, recommended for training):** NVIDIA CUDA-compatible GPU with 8+ GB VRAM.

---

## 2. Local Development Setup

### Backend (FastAPI)
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend (React + Vite)
```bash
cd frontend
npm install
npm run dev
```

---

## 3. Containerized Deployment (Planned)

A `docker-compose.yml` will orchestrate:
1. `cardiopulmo-frontend`: Nginx reverse proxy serving static React build.
2. `cardiopulmo-backend`: Uvicorn workers running FastAPI application.
3. `cardiopulmo-db`: PostgreSQL 16 container with persistent volumes.
4. `cardiopulmo-ml`: TorchServe or dedicated FastAPI ML worker for CV Grad-CAM and SHAP calculations.
