# import cv2
# import numpy as np

# def detect_shadow(gray):
#     """
#     Detect shadow regions using adaptive thresholding
#     """
#     inv = cv2.bitwise_not(gray)

#     shadow_mask = cv2.adaptiveThreshold(
#         inv,
#         255,
#         cv2.ADAPTIVE_THRESH_MEAN_C,
#         cv2.THRESH_BINARY,
#         15,
#         3
#     )

#     return shadow_mask

# # def shadow_area(mask):
# #     """
# #     Calculate occluded shadow area in pixels
# #     """
# #     return cv2.countNonZero(mask)
# def shadow_area(mask):
#     contours, _ = cv2.findContours(
#         mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
#     )

#     total_area = 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 500:  # ignore small noise
#             total_area += area

#     return total_area


import cv2
import numpy as np

# def detect_shadow(gray, face_box):
#     """
#     Detect shadow ONLY inside face region
#     """
#     mask = np.zeros_like(gray)

#     if face_box is None:
#         return mask

#     x, y, w, h = face_box
#     face_roi = gray[y:y+h, x:x+w]

#     inv = cv2.bitwise_not(face_roi)

#     shadow_roi = cv2.adaptiveThreshold(
#         inv,
#         255,
#         cv2.ADAPTIVE_THRESH_MEAN_C,
#         cv2.THRESH_BINARY,
#         15,
#         4
#     )

#     mask[y:y+h, x:x+w] = shadow_roi
#     return mask
def detect_shadow(gray, face_box):
    """
    More sensitive shadow detection inside face region
    """
    mask = np.zeros_like(gray)

    if face_box is None:
        return mask

    x, y, w, h = face_box
    face_roi = gray[y:y+h, x:x+w]

    # Increase contrast
    face_roi = cv2.equalizeHist(face_roi)

    inv = cv2.bitwise_not(face_roi)

    shadow_roi = cv2.adaptiveThreshold(
        inv,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,  # MORE sensitive
        cv2.THRESH_BINARY,
        11,
        2
    )

    mask[y:y+h, x:x+w] = shadow_roi
    return mask


# def shadow_area(mask):
#     contours, _ = cv2.findContours(
#         mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
#     )

#     total_area = 0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area > 800:  # stronger noise rejection
#             total_area += area

#     return total_area
def shadow_area(mask):
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    total_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 300:  # LOWER threshold (important)
            total_area += area

    return total_area


