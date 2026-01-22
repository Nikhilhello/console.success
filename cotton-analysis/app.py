from flask import Flask, request, jsonify
import torch
from torchvision import transforms
from PIL import Image
from model import CottonNet

app = Flask(__name__)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model
model = CottonNet(num_stages=4)
model.load_state_dict(torch.load("cotton_model.pth", map_location=device))
model.eval()
model.to(device)

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

stage_map = {
    0: "Phase 1 (Vegetative/Budding)",
    1: "Phase 2 (Flowering)",
    2: "Phase 3 (Bursting/Ripped)",
    3: "Phase 4 (Harvest Ready)"
}

@app.route("/")
def home():
    return {
        "message": "Cotton Analysis API is running",
        "endpoint": "/predict (POST image)"
    }


@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    img_file = request.files["image"]
    img = Image.open(img_file).convert("RGB")

    input_tensor = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        stage_output, health_output = model(input_tensor)

        stage_idx = stage_output.argmax(dim=1).item()
        health_score = int(health_output.item() * 100)

    response = {
        "stage": stage_map[stage_idx],
        "is_ripped": True if health_score < 60 else False,
        "health_score": health_score
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
