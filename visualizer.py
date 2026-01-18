import cv2
import numpy as np
import matplotlib.pyplot as plt

plt.ion()

def draw_overlay(frame, depth, action):
    cv2.putText(
        frame,
        f"Depth: {depth} cm",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        action,
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

def show_heatmap(gray):
    """
    Display shadow intensity heatmap
    """
    norm = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)
    plt.clf()
    plt.imshow(norm, cmap='inferno')
    plt.title("Shadow Intensity Heatmap")
    plt.axis('off')
    plt.pause(0.001)

def show_shadow_matrix(shadow_matrix):
    if shadow_matrix is None:
        return

    plt.clf()
    plt.imshow(shadow_matrix, cmap="inferno")
    plt.colorbar(label="Normalized Light Loss")
    plt.title("Shadow Intensity Matrix (Face Region)")
    plt.axis("off")
    plt.pause(0.001)
