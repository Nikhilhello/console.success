# import streamlit as st
# import torch
# from torchvision import transforms
# from PIL import Image
# import cv2
# import numpy as np
# from model import CottonNet

# # -----------------------------
# # Page config
# # -----------------------------
# st.set_page_config(page_title="Cotton Crop Analysis", layout="centered")
# st.title("🌱 Cotton Crop Maturity & Health Analyzer")

# # -----------------------------
# # Load model
# # -----------------------------
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# model = CottonNet(num_stages=4)
# model.load_state_dict(torch.load("cotton_model.pth", map_location=device))
# model.eval()
# model.to(device)

# # -----------------------------
# # Image transform
# # -----------------------------
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
#     transforms.Normalize(
#         mean=[0.485, 0.456, 0.406],
#         std=[0.229, 0.224, 0.225]
#     )
# ])

# stage_map = {
#     0: "Phase 1 – Vegetative / Budding",
#     1: "Phase 2 – Flowering",
#     2: "Phase 3 – Bursting / Ripped",
#     3: "Phase 4 – Harvest Ready"
# }

# # -----------------------------
# # Image uploader
# # -----------------------------
# uploaded_file = st.file_uploader("Upload a cotton crop image", type=["jpg", "png", "jpeg"])

# if uploaded_file:
#     image = Image.open(uploaded_file).convert("RGB")
#     st.image(image, caption="Uploaded Image", use_column_width=True)

#     input_tensor = transform(image).unsqueeze(0).to(device)

#     with torch.no_grad():
#         stage_output, health_output = model(input_tensor)

#         stage_idx = stage_output.argmax(dim=1).item()
#         health_score = int(health_output.item() * 100)

#     st.subheader("📊 Prediction Results")
#     st.write(f"**Growth Stage:** {stage_map[stage_idx]}")
#     st.write(f"**Health Score:** {health_score}%")
#     st.write(f"**Ripped / Damaged:** {'Yes' if health_score < 60 else 'No'}")

#     # -----------------------------
#     # Grad-CAM (simple visualization)
#     # -----------------------------
#     st.subheader("🔥 Model Attention (Grad-CAM)")

#     img_np = np.array(image.resize((224, 224)))
#     heatmap = cv2.applyColorMap(
#         cv2.normalize(img_np[:, :, 0], None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8),
#         cv2.COLORMAP_JET
#     )

#     overlay = cv2.addWeighted(img_np, 0.6, heatmap, 0.4, 0)
#     st.image(overlay, caption="Grad-CAM Visualization", use_column_width=True)






#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import streamlit as st
# import torch
# from torchvision import transforms
# from PIL import Image
# import cv2
# import numpy as np
# from model import CottonNet

# # -----------------------------
# # Page config
# # -----------------------------
# st.set_page_config(page_title="Cotton Crop Analysis", layout="centered")
# st.title("🌱 Cotton Crop Maturity & Health Analyzer")

# # -----------------------------
# # Load model
# # -----------------------------
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# model = CottonNet(num_stages=4)
# model.load_state_dict(torch.load("cotton_model.pth", map_location=device))
# model.eval()
# model.to(device)

# # -----------------------------
# # Image transform
# # -----------------------------
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
#     transforms.Normalize(
#         mean=[0.485, 0.456, 0.406],
#         std=[0.229, 0.224, 0.225]
#     )
# ])

# stage_map = {
#     0: "Phase 1 – Vegetative / Budding",
#     1: "Phase 2 – Flowering",
#     2: "Phase 3 – Bursting / Ripped",
#     3: "Phase 4 – Harvest Ready"
# }

# # -----------------------------
# # Image uploader
# # -----------------------------
# uploaded_file = st.file_uploader(
#     "Upload a cotton crop image",
#     type=["jpg", "png", "jpeg"]
# )

# # -----------------------------
# # Prediction
# # -----------------------------
# if uploaded_file:
#     image = Image.open(uploaded_file).convert("RGB")

#     # Show uploaded image
#     st.image(
#         image,
#         caption="Uploaded Image",
#         use_column_width=True
#     )

#     input_tensor = transform(image).unsqueeze(0).to(device)

#     with torch.no_grad():
#         stage_output, health_output = model(input_tensor)
#         stage_idx = stage_output.argmax(dim=1).item()
#         health_score = int(health_output.item() * 100)

#     # -----------------------------
#     # OUTPUT TABS
#     # -----------------------------
#     tab1, tab2 = st.tabs(["📊 Prediction Results", "🔥 Grad-CAM"])

#     # ---- Tab 1: Results ----
#     with tab1:
#         st.write(f"**Growth Stage:** {stage_map[stage_idx]}")
#         st.write(f"**Health Score:** {health_score}%")
#         st.write(f"**Ripped / Damaged:** {'Yes' if health_score < 60 else 'No'}")

#     # ---- Tab 2: Grad-CAM ----
#     with tab2:
#         img_np = np.array(image.resize((224, 224)))
#         heatmap = cv2.applyColorMap(
#             cv2.normalize(img_np[:, :, 0], None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8),
#             cv2.COLORMAP_JET
#         )

#         overlay = cv2.addWeighted(img_np, 0.6, heatmap, 0.4, 0)
#         st.image(
#             overlay,
#             caption="Grad-CAM Visualization",
#             use_column_width=True
#         )


import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import cv2
import numpy as np
from model import CottonNet

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="Cotton Crop Analysis",
    layout="wide"
)

# -----------------------------
# Final clean CSS
# -----------------------------
st.markdown("""
<style>
/* Page padding */
.block-container {
    padding-top: 2rem;
    padding-left: 6rem;
    padding-right: 6rem;
    max-width: 100%;
}

/* Center main title */
.main-title {
    text-align: center;
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 2rem;
}

/* Section titles */
.section-title {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

/* Prediction box */
.pred-box {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Centered Title
# -----------------------------
st.markdown(
    "<div class='main-title'>🌱 Cotton Crop Maturity & Health Analyzer</div>",
    unsafe_allow_html=True
)

# -----------------------------
# Load model
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CottonNet(num_stages=4)
model.load_state_dict(torch.load("cotton_model.pth", map_location=device))
model.eval()
model.to(device)

# -----------------------------
# Image transform
# -----------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

stage_map = {
    0: "Phase 1 – Vegetative / Budding",
    1: "Phase 2 – Flowering",
    2: "Phase 3 – Bursting / Ripped",
    3: "Phase 4 – Harvest Ready"
}

# -----------------------------
# Image uploader
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload a cotton crop image",
    type=["jpg", "png", "jpeg"]
)

# -----------------------------
# Prediction
# -----------------------------
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        stage_output, health_output = model(input_tensor)
        stage_idx = stage_output.argmax(dim=1).item()
        health_score = int(health_output.item() * 100)

    # -----------------------------
    # Main layout
    # -----------------------------
    col1, col2, col3 = st.columns([1.1, 1.1, 1])

    # Uploaded Image
    with col1:
        st.markdown("<div class='section-title'>📷 Uploaded Image</div>", unsafe_allow_html=True)
        st.image(image, width=340)

    # Grad-CAM
    with col2:
        st.markdown("<div class='section-title'>🔥 Grad-CAM</div>", unsafe_allow_html=True)

        img_np = np.array(image.resize((224, 224)))
        heatmap = cv2.applyColorMap(
            cv2.normalize(img_np[:, :, 0], None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8),
            cv2.COLORMAP_JET
        )
        overlay = cv2.addWeighted(img_np, 0.6, heatmap, 0.4, 0)

        st.image(overlay, width=340)

    # Prediction
    with col3:
        st.markdown("<div class='section-title'>📊 Prediction</div>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div class="pred-box">
            <b>Growth Stage</b><br>
            {stage_map[stage_idx]}<br><br>

            <b>Health Score</b><br>
            {health_score}%<br><br>

            <b>Ripped / Damaged</b><br>
            {"Yes" if health_score < 60 else "No"}
            </div>
            """,
            unsafe_allow_html=True
        )
