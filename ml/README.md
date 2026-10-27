# CardioPulmo-HMS Machine Learning & Computer Vision

**Role:** Model Training, Feature Engineering, Evaluation & Inference  
**Lead Owner:** Member 5 (ML & Computer Vision Lead)  
**Technologies:** PyTorch, Torchvision, Scikit-learn, XGBoost, SHAP, DenseNet-121

---

## 1. Directory Structure

* `ml/notebooks/`: Exploratory Data Analysis (EDA), baseline prototyping, and visualization notebooks.
* `ml/src/`: Production-grade modular Python code for data loading, preprocessing pipelines, model architectures, and training loops.
* `ml/models/`: Trained model checkpoints, serialized pipeline transformers, and weights (`.pth`, `.joblib`). Ignored by Git.
* `ml/evaluation/`: Metric logs, ROC-AUC / PR-AUC curves, confusion matrices, and calibration evaluation reports.

---

## 2. Core Workstreams

1. **Computer Vision (NIH ChestX-ray14):** Multi-label classification across 14 thoracic pathologies using DenseNet-121 / CheXNet and Grad-CAM spatial localization.
2. **Tabular Machine Learning:** Calibrated 30-day decompensated heart failure risk estimation using XGBoost pipelines with SHAP explainability.
