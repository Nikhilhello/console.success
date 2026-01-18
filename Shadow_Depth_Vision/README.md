# Physics-Based Vision: Shadow-Depth Action Recognition

## Overview
This project implements a **physics-based action recognition system** that estimates the **3D distance between a hand and the face** using **shadow geometry and illumination physics**, rather than relying on facial or hand keypoints.

The system analyzes the **shadow cast by a hand on the face under a single dominant light source** to infer depth and classify actions such as **Touching Face / Eating**.  
It is designed as a **fully offline, real-time Python application** using classical computer vision techniques.

---

## Key Objectives
- Estimate hand-to-face **depth (Z-distance)** using shadow occlusion
- Avoid reliance on **keypoints or deep learning**
- Apply **physical principles of light attenuation**
- Generate a **shadow intensity matrix (heatmap)**
- Perform **real-time action classification**
- Run **fully offline** with no APIs or internet usage

---

## Core Idea
When a hand approaches the face, it blocks incoming light and creates a shadow on the facial surface.

As the hand moves closer:
- The **shadow area increases**
- Light **intensity loss becomes stronger**
- The **estimated depth decreases**

Using this relationship, depth is estimated with a physics-inspired formulation:

