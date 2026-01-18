import cv2
import numpy as np

def compute_shadow_intensity_matrix(gray, face_box):
    """
    Returns a normalized shadow intensity matrix for the face region.
    Higher values = more shadow (light loss)
    """
    if face_box is None:
        return None, None

    x, y, w, h = face_box
    face_roi = gray[y:y+h, x:x+w]

    # Normalize illumination
    face_norm = cv2.equalizeHist(face_roi)

    # Estimate light reference as max intensity
    light_ref = np.max(face_norm)

    # Shadow intensity = light loss
    shadow_matrix = light_ref - face_norm
    shadow_matrix = shadow_matrix.astype(np.float32)

    # Normalize to [0,1]
    shadow_matrix /= (np.max(shadow_matrix) + 1e-6)

    return shadow_matrix, (x, y, w, h)
