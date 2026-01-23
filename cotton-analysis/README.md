# 🌱 Agri-Vision: Cotton Crop Maturity & Health Classifier

An end-to-end **Computer Vision system** that analyzes cotton crop images to determine **growth stage**, **health condition**, and **harvest readiness**.
The system is designed to assist farmers and agricultural experts in making **data-driven harvest decisions**.

---

## 🚀 Project Overview

Traditional crop inspection relies on manual observation, which is time-consuming and error-prone.
This project uses **Deep Learning and Computer Vision** to automatically analyze cotton crop images and provide:

- 🌿 **Growth Phase Classification**
- 🐛 **Health / Damage Assessment**
- 🔥 **Visual Explainability (Grad-CAM)**
- 🌐 **Deployed Web Application (Streamlit)**

---

## 🎯 Key Objectives

- Classify cotton crops into **four growth phases**
- Detect crop damage and estimate a **health score (0–100)**
- Provide **visual explanation** of model decisions
- Deploy the system as a **publicly accessible web app**

---

## 🌾 Cotton Growth Phases

| Phase | Description |
|:-----:|:------------|
| **Phase 1** | Vegetative / Budding |
| **Phase 2** | Flowering |
| **Phase 3** | Bursting / Ripped |
| **Phase 4** | Harvest Ready |

---

## 🧠 System Architecture

```
graph TD
    A[Input Image] --> B[Image Preprocessing & Augmentation]
    B --> C[CNN Backbone (MobileNetV2 – Transfer Learning)]
    C --> D[Shared Feature Representation]
    D --> E[Stage Classification]
    D --> F[Health Score Regression]
    E --> G[Grad-CAM Explainability]
    F --> G
    G --> H[Web Deployment (Streamlit UI)]
```
---
## 🧪 Dataset & Preprocessing

- **Collection:** Images collected using **automated Python crawlers**.
- **Structure:** Dataset organized into **8 classes** (Phase × {Healthy, Damaged}).
- **Augmentation:** Applied **robust data augmentation** including:
  - Rotation
  - Brightness / Contrast changes
  - Horizontal flipping
  - Normalization (ImageNet standards)

---

## 🧠 Model Details

- **Backbone:** MobileNetV2 (Pretrained on ImageNet)
- **Learning Strategy:** Transfer Learning
- **Approach:** Multi-Task Learning
  - **Task 1:** Growth Stage Classification (4 classes)
  - **Task 2:** Health Score Prediction (0–100)

---

## 🔥 Explainability with Grad-CAM

To ensure transparency and trust:
- **Grad-CAM heatmaps** are generated.
- Visualize **where the model focuses** while predicting.
- Confirms the model attends to **cotton boll regions**, not background noise.

---

## 🌐 Deployment (Streamlit UI)

The project is deployed as a **Streamlit web application**.

**Features:**
- Upload cotton crop image
- View predicted growth stage
- View health score and damage status
- Visual Grad-CAM heatmap overlay

---

## 🧪 How to Run Locally

### Create virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**macOS/Linux:**
```
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies**
```Bash
pip install -r requirements.txt
```

**Run the Streamlit app**
```Bash
streamlit run streamlit_app.py
```
The app will open at: http://localhost:8501

---
## 📁 Project Structure

```
cotton-analysis/
 ├── dataset/              # Training images
 ├── model.py              # Model architecture definition
 ├── train.py              # Training loop script
 ├── gradcam.py            # Gradient Class Activation Mapping logic
 ├── streamlit_app.py      # Web application entry point
 ├── cotton_model.pth      # Saved model weights
 ├── gradcam_output.jpg    # Temporary output for heatmaps
 ├── requirements.txt      # Python dependencies
 └── README.md             # Project documentation
```
---
## 📊 Sample Output
{ JSON output }
```
JSON
{
  "stage": "Phase 3 (Bursting/Ripped)",
  "is_ripped": true,
  "health_score": 82
}
```

<div style="display: flex; gap: 10px;">
  <img alt="image" src="https://github.com/user-attachments/assets/472ef73d-b98b-474a-ad8e-7467f44058b6" width="49.5%" />
  <img alt="image" src="https://github.com/user-attachments/assets/f10c39ff-7f1e-4e24-9b2b-ab1bdc96dc74" width="49.5%" />  
  <!-- <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f10c39ff-7f1e-4e24-9b2b-ab1bdc96dc74" width="49.5%" />   -->
</div>

---
## ⚠️ Model Limitations & Disclaimer   


The predicted **Health Score** and **Ripped/Damaged status** are derived from a deep learning model trained on a **limited and automatically collected image dataset**. Due to the following factors, predictions may not always be perfectly accurate:

- The training dataset size is relatively small compared to large-scale agricultural datasets.
- Images were collected from diverse online sources, leading to variations in lighting, resolution, background, and crop appearance.
- Certain crop damage patterns (e.g., early-stage pest infestation or subtle discoloration) are visually similar to healthy conditions, making fine-grained discrimination challenging.
- The model has not been trained on region-specific cotton varieties or seasonal variations.

This system is intended as a **decision-support tool**, not a replacement for expert agronomic judgment.  
Future improvements include expanding the dataset, incorporating field-collected images, and refining the health scoring mechanism with domain-specific annotations.

---

## 🛠️ Technologies Used

- **Python** – Core programming language for model development and deployment  
- **PyTorch** – Deep learning framework used to build and train the CNN model  
- **TorchVision** – Pretrained models, image transformations, and utilities  
- **MobileNetV2** – Lightweight CNN backbone used for transfer learning  
- **OpenCV** – Image processing and Grad-CAM heatmap visualization  
- **Streamlit** – Web framework used to deploy the interactive UI  
- **NumPy** – Numerical computations and array operations  
- **Pillow (PIL)** – Image loading and preprocessing  
- **icrawler** – Automated image collection for dataset creation  



---
## 📌 Use Cases
- Precision agriculture
- Harvest time optimization
- Crop health monitoring
- AI-assisted farming decisions

---

## 👤 Author
**Nikhil K**  
Software Development Intern  
Domain: Python Development 

---

## 📌 Acknowledgment
This project was developed as part of an internship program under **console.success**.
