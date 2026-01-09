# 🚦 Autonomous Traffic Signal Optimization using Reinforcement Learning

---

## 📌 Project-01 Overview
Traffic congestion is a critical issue in modern cities due to **static, timer-based traffic signals** that do not adapt to real-time traffic conditions.  
This project demonstrates a **professional traffic signal simulation** that compares:

- **Traditional Timer-Based Traffic Control (Before AI)**
- **AI-Optimized Adaptive Traffic Control (After AI)**

The system dynamically adjusts traffic signals based on **vehicle queue density** and includes **emergency vehicle (ambulance) priority handling** to ensure realistic and practical traffic management.

---
<img width="1530" height="1080" alt="image" src="https://github.com/user-attachments/assets/f48aa06a-dd97-4f71-bc5b-25435e983555" />

<div style="display: flex; gap: 10px;">
  <img src="https://github.com/user-attachments/assets/d35229d6-fcda-4035-bf91-dfd9c3bfe030" width="49.5%" />
  <img src="https://github.com/user-attachments/assets/4eb2befc-6023-4b55-85a8-a176bf30578e" width="49.5%" />
</div>


---

## 🎯 Project Objectives
- Simulate a realistic **4-way traffic intersection**
- Compare **traditional vs AI-optimized traffic signal control**
- Minimize **average vehicle waiting time**
- Improve traffic throughput
- Implement **emergency vehicle priority**
- Provide a **clear, professional, and explainable simulation**

---

## 🧠 Key Features

### 1️⃣ Traditional Traffic Control (Before AI)
- Fixed timer-based signal switching
- No awareness of traffic congestion
- Causes unnecessary waiting during low-traffic conditions
- Used as a baseline for comparison

---

### 2️⃣ AI-Optimized Traffic Control (After AI)
- Adaptive signal switching based on:
  - Vehicle queue length
  - Real-time congestion levels
- Dynamically prioritizes busier lanes
- Reduces total waiting time
- Improves traffic flow efficiency

---

### 3️⃣ Emergency Vehicle Priority 🚑
- Ambulance vehicles are detected dynamically
- Traffic signals immediately prioritize the ambulance direction
- Green signal is maintained until the ambulance clears the intersection
- Overrides both traditional and AI logic safely
- Simulates real-world emergency handling

---

### 4️⃣ Professional Traffic Simulation
- Realistic vehicle movement with acceleration and braking
- Collision avoidance between vehicles
- Red, Yellow, and Green traffic light states
- Live statistics dashboard
- On-road waiting indicators
- Interactive mode switching for demonstration

---

## 🛠️ Technology Stack
- **Programming Language:** Python  
- **Simulation & Visualization:** PyGame  
- **AI Logic:** Reinforcement Learning–inspired adaptive control  
- **Environment:** Custom-built traffic simulation  
- **Platform:** Windows  

---

## 📂 Project Structure
```
Traffic-RL/
│
├── env/
│   └── traffic_env.py
│
├── agent/
│   └── dqn_agent.py
│
├── models/
│   └── traffic_dqn.pth
│
├── plots/
│   ├── training_reward.png
│   └── static_vs_ai.png
│
├── professional_simulation.py   # Final professional demo
├── train.py
├── compare.py
├── static_controller.py
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Required Libraries
```bash
pip install pygame torch numpy matplotlib
```

### 2️⃣ Run the Professional Simulation
```bash
python professional_simulation.py
```

---

## 🎮 Simulation Controls

| Key | Action |
|----|-------|
| `SPACE` | Switch between Traditional & AI mode |
| `R` | Reset all statistics |
| `A` | Spawn an ambulance |
| `Close Window` | Exit the simulation |

---

## 🔄 Simulation Modes

### 🔴 Traditional Mode (Before AI)
- Fixed signal timing
- No congestion awareness
- Higher average waiting time
- Used as baseline reference

---

### 🟢 AI Optimized Mode (After AI)
- Adaptive signal switching
- Responds to vehicle queue density
- Reduces unnecessary waiting
- Improves traffic efficiency

---

## 📊 Performance Evaluation
The system performance is evaluated by comparing **Traditional vs AI-Optimized control** using:
- Average waiting time
- Number of vehicles passed
- Queue lengths
- Visual and statistical comparison

---

### 📈 Result Summary
- AI-based control consistently reduces cumulative waiting time
- Handles uneven traffic distribution more efficiently
- Performs significantly better than static timer-based signals

Performance graphs are available in the `plots/` directory.

---

## 🚑 Emergency Vehicle Handling
- Emergency vehicles (ambulances) are detected in real time
- Traffic signals immediately prioritize the ambulance route
- Green signal is held until the ambulance safely passes
- Simulates real-world emergency traffic behavior

---

## 🎥 Demo Video
A working demo video demonstrating:
- Before AI vs After AI traffic behavior
- Live statistics dashboard
- Emergency vehicle priority handling

📺 **YouTube Demo Link:**  
*([YouTube link](https://youtu.be/Q5RxgqOfbsI?si=xme_Jsdrfyn72Z1f))*

---

## 🌐 GitHub Repository
🔗 **GitHub Repository Link:**  
*([public GitHub repository link](https://github.com/Nikhilhello/console.success/tree/main/Traffic-RL))*

---

## 🔗 LinkedIn Submission
This project is submitted as part of **Phase 2: Project 1 – Traffic RL**.  
The project has been shared on LinkedIn and tagged with **@console.success**.

---

## 🏁 Conclusion
This project presents a **professional, explainable, and practical approach** to traffic signal optimization using AI-inspired adaptive control.  
It clearly demonstrates the limitations of static traffic systems and highlights the advantages of intelligent traffic management with emergency handling.

---

## 👤 Author
**Nikhil K**  
Software Development Intern  
Domain: Python Development 

---

## 📌 Acknowledgment
This project was developed as part of an internship program under **console.success**.
