# import cv2

# from core.camera import Camera
# from core.light_source import estimate_light_direction
# from core.shadow_detection import detect_shadow, shadow_area
# from core.depth_estimation import estimate_depth_cm
# from core.action_classifier import classify_action
# from core.visualizer import draw_overlay, show_heatmap
# from core.face_region import detect_face


# def main():
#     cam = Camera()

#     while True:
#         frame = cam.read()
#         if frame is None:
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#         # Shadow detection
#         shadow_mask = detect_shadow(gray)
#         area = shadow_area(shadow_mask)

#         # Depth estimation
#         depth = estimate_depth_cm(area)

#         # Action classification
#         action = classify_action(depth)

#         # Overlay visuals
#         draw_overlay(frame, depth, action)

#         # Display windows
#         cv2.imshow("ShadowDepthVision - Live Feed", frame)
#         cv2.imshow("Shadow Mask", shadow_mask)

#         # Heatmap
#         show_heatmap(gray)

#         if cv2.waitKey(1) & 0xFF == 27:  # ESC key
#             break

#     cam.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()



import cv2

from core.camera import Camera
from core.shadow_detection import detect_shadow, shadow_area
from core.depth_estimation import estimate_depth_cm
from core.action_classifier import classify_action
from core.visualizer import draw_overlay, show_heatmap
from core.face_region import detect_face


def main():
    cam = Camera()

    while True:
        frame = cam.read()
        if frame is None:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 1. Detect face region
        face_box = detect_face(gray)

        # 2. Detect shadow ONLY inside face region
        shadow_mask = detect_shadow(gray, face_box)

        # 3. Compute occluded shadow area
        area = shadow_area(shadow_mask)
        # print("Shadow Area:", area, "Depth:", depth)


        # 4. Physics-based depth estimation
        depth = estimate_depth_cm(area)

        print("Shadow Area:", area, "Depth:", depth)


        # 5. Action classification
        action = classify_action(depth)

        # 6. Draw face bounding box (for demo clarity)
        if face_box is not None:
            x, y, w, h = face_box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 7. Overlay depth and action
        draw_overlay(frame, depth, action)

        # 8. Display outputs
        cv2.imshow("ShadowDepthVision - Live Feed", frame)
        cv2.imshow("Shadow Mask (Face Region Only)", shadow_mask)

        # 9. Shadow intensity heatmap
        show_heatmap(gray)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()



