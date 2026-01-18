# Physics-Based Vision: Shadow-Depth Action Recognition

## 1. Overview
This project implements a **physics-based action recognition system** that estimates the **3D distance between a hand and the face** using **shadow geometry and illumination physics**, rather than relying on facial or hand keypoints.

The system analyzes the **shadow cast by a hand on the face under a single dominant light source** to infer depth and classify actions such as **Touching Face / Eating**. It is designed as a **fully offline, real-time Python application** using classical computer vision techniques.

---

## 2. Key Objectives
* **Depth Estimation:** Estimate hand-to-face **depth (Z-distance)** using shadow occlusion.
* **Algorithm:** Avoid reliance on **keypoints or deep learning**; use pure signal processing.
* **Physics:** Apply **physical principles of light attenuation**.
* **Visualization:** Generate a **shadow intensity matrix (heatmap)**.
* **Performance:** Perform **real-time action classification**.
* **Privacy/Efficiency:** Run **fully offline** with no APIs or internet usage.

---

## 3. Core Idea: The Physics of Shadows
When a hand approaches the face, it blocks incoming light and creates a shadow on the facial surface. As the hand moves closer:

1.  The **shadow area increases**.
2.  Light **intensity loss becomes stronger**.
3.  The **estimated depth decreases**.

Using this relationship, depth is estimated with a physics-inspired formulation:

$$Z \propto \frac{1}{\sqrt{A_{shadow}}}$$

Where:
* $Z$ is the estimated Depth.
* $A_{shadow}$ is the area of the shadow occlusion.

This enables indirect but meaningful 3D distance estimation using illumination behavior.

---

## 4. System Features
* 📷 **Real-time Processing:** Live webcam video analysis.
* 👤 **ROI Focus:** Face-region–restricted shadow detection.
* 🌑 **Shadow Computation:** Occlusion area calculation and intensity mapping.
* 📊 **Heatmap:** Shadow intensity spatial illumination matrix.
* 📏 **Depth Logic:** Physics-based depth estimation (calibrated to cm).
* 🚨 **Action Trigger:** Classification based on depth thresholds.

---

## 5. Technology Stack
* **Language:** Python 3.10+
* **Computer Vision:** OpenCV (`cv2`)
* **Computation:** NumPy
* **Visualization:** Matplotlib
* **Face Detection:** Haar Cascade (Classical detection, non-DL)

**Constraints:**
* No deep learning models (CNNs/Transformers).
* No keypoint detection (MediaPipe/OpenPose).
* No internet or external APIs.

---

## 6. Project Structure

```text
ShadowDepthVision/
│
├── main.py                   # Entry point for the application
│
├── core/                     # Core logic modules
│   ├── camera.py             # Webcam handling
│   ├── face_region.py        # ROI extraction using Haar Cascades
│   ├── shadow_detection.py   # Image processing for shadow isolation
│   ├── depth_estimation.py   # Physics-based Z-distance logic
│   ├── action_classifier.py  # Threshold-based state machine
│   └── visualizer.py         # UI and Heatmap generation
│
├── utils/                    # Helper functions
│   ├── constants.py          # Calibration parameters and thresholds
│   └── geometry.py           # geometric transformations
│
├── outputs/                  # Generated results
│   ├── screenshots/
│   └── heatmaps/
│
├── requirements.txt          # Dependency list
└── README.md                 # Project documentation
```


---

## Installation
Install the required dependencies using:

```bash
pip install -r requirements.txt
```
## Running the Application

Start the real-time system using:

```bash
python main.py
```

Here is the text formatted in Markdown, ready to copy and paste.

Markdown

## 7. Installation
1. **Clone the repository** (if applicable) or navigate to the project directory.
2. **Install dependencies** using pip:

```bash
pip install -r requirements.txt
Ensure your requirements.txt includes: opencv-python, numpy, and matplotlib.

8. Running the Application
Start the real-time system by running the main script:

```Bash
python main.py
```

---


## Expected Output
- Live webcam feed with depth overlay
- Shadow mask highlighting occluded facial regions
- Shadow intensity heatmap visualization
- Action status displayed as:
  - `No Action`
  - `Touching Face / Eating`

---

## Demo
The demo video demonstrates:
- Shadow-based depth estimation
- Transition from **No Action** to **Touching Face / Eating**
- Real-time physics-based reasoning
- Fully offline system behavior

---
📺 **YouTube Demo Link:**  
*([YouTube link](fttttttttttt))*

## 🌐 GitHub Repository
🔗 **GitHub Repository Link:**  
*([public GitHub repository link](https://github.com/Nikhilhello/console.success/tree/main/Shadow_Depth_Vision))*


---

## 🏁 Conclusion
This project demonstrates a **physics-based approach to action recognition** by leveraging **shadow geometry and illumination behavior** instead of traditional facial or hand keypoints.

By analyzing the **shadow cast by a hand on the face under a single dominant light source**, the system is able to estimate **hand-to-face depth** and classify actions such as **Touching Face / Eating** in real time. The use of a **shadow intensity matrix** and a physics-inspired depth model highlights how classical computer vision and physical reasoning can be combined effectively.

The solution operates **fully offline**, requires **no deep learning models**, and remains robust under occlusion scenarios where keypoint-based methods often fail. This work serves as a **mini research implementation**, showcasing the potential of physics-driven vision techniques for interpretable and efficient action recognition systems.


---

## 👤 Author
**Nikhil K**  
Software Development Intern  
Domain: Python Development 

---

## 📌 Acknowledgment
This project was developed as part of an internship program under **console.success**.
