# CardioPulmo-HMS: Machine Learning & Computer Vision Specifications

## 1. Workstream 1: Computer Vision on NIH ChestX-ray14

### Objective
Provide thoracic radiograph screening assistance within the Pulmonology and Cardiology Clinician Workspace, detecting and localizing 14 thoracic pathologies.

### The 14 Target Pathologies
1. **Effusion** (Cardio-pulmonary link)
2. **Cardiomegaly** (Cardiology link)
3. **Pneumonia**
4. **Edema**
5. **Atelectasis**
6. **Pneumothorax**
7. **Infiltration**
8. **Consolidation**
9. **Emphysema**
10. **Fibrosis**
11. **Mass**
12. **Nodule**
13. **Pleural Thickening**
14. **Hernia**

### Split Governance & Leakage Prevention
* Partition images strictly by **Patient ID** (70% Train, 15% Validation, 15% Holdout Test) using `GroupShuffleSplit`.
* Scans of the same patient across longitudinal follow-ups must never appear across both training and test splits.

### Architecture & Loss
* **Backbone:** DenseNet-121 (CheXNet weights) or EfficientNet-B2 with a 14-output sigmoid classification head.
* **Loss Function:** Positive-class weighted binary cross-entropy (`BCEWithLogitsLoss`) or Asymmetric Focal Loss to handle extreme class imbalance.
* **Explainability:** Grad-CAM spatial gradients computed from the final convolutional block (`denseblock4`), rendered as side-by-side heatmaps with PACS windowing controls.

---

## 2. Workstream 2: Primary Tabular Machine Learning

### Objective
Calibrated 30-day clinical decompensation risk prediction for acute heart failure patients with local feature explainability.

### Model Pipeline
* **Preprocessing:** `ColumnTransformer` with median imputation for continuous biomarkers (NT-proBNP, Creatinine, SpO2) and one-hot encoding for categorical factors, strictly fit inside a `Pipeline` on the training split only.
* **Classifiers:** Regularized Logistic Regression baseline vs. Random Forest vs. XGBoost / LightGBM.
* **Calibration:** Platt Scaling (Sigmoid) or Isotonic Regression evaluated using Brier score and reliability diagrams.
* **Explainability:** TreeSHAP feature attributions rendered as horizontal waterfall charts directly in the Clinician Workspace.
