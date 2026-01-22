import torch
import cv2
import numpy as np
from torchvision import transforms
from PIL import Image
from model import CottonNet

# -------------------------
# CONFIG
# -------------------------
IMAGE_PATH = "sample.jpg"   # put one cotton image here
MODEL_PATH = "cotton_model.pth"
IMG_SIZE = 224

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# -------------------------
# LOAD MODEL
# -------------------------
model = CottonNet(num_stages=4)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.eval()
model.to(device)

# -------------------------
# HOOKS
# -------------------------
features = []
gradients = []

def forward_hook(module, input, output):
    features.append(output)

def backward_hook(module, grad_in, grad_out):
    gradients.append(grad_out[0])

# Register hooks on LAST conv layer
target_layer = model.backbone.features[-1]
target_layer.register_forward_hook(forward_hook)
target_layer.register_backward_hook(backward_hook)

# -------------------------
# IMAGE PREPROCESSING
# -------------------------
transform = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

img = Image.open(IMAGE_PATH).convert("RGB")
input_tensor = transform(img).unsqueeze(0).to(device)

# -------------------------
# FORWARD + BACKWARD
# -------------------------
stage_output, _ = model(input_tensor)
pred_class = stage_output.argmax(dim=1)

model.zero_grad()
stage_output[0, pred_class].backward()

# -------------------------
# GRAD-CAM CALCULATION
# -------------------------
grads = gradients[0].cpu().data.numpy()[0]
fmap = features[0].cpu().data.numpy()[0]

weights = np.mean(grads, axis=(1, 2))
cam = np.zeros(fmap.shape[1:], dtype=np.float32)

for i, w in enumerate(weights):
    cam += w * fmap[i]

cam = np.maximum(cam, 0)
cam = cam / cam.max()
cam = cv2.resize(cam, (IMG_SIZE, IMG_SIZE))

# -------------------------
# HEATMAP OVERLAY
# -------------------------
heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)
original = cv2.resize(np.array(img), (IMG_SIZE, IMG_SIZE))

overlay = cv2.addWeighted(original, 0.6, heatmap, 0.4, 0)

cv2.imwrite("gradcam_output.jpg", overlay)
print("✅ Grad-CAM image saved as gradcam_output.jpg")
