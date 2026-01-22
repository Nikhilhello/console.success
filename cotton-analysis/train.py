import torch
import torch.nn as nn
import torch.optim as optim
from model import CottonNet
from data_loader import train_loader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = CottonNet(num_stages=4).to(device)

# Loss functions
stage_criterion = nn.CrossEntropyLoss()
health_criterion = nn.MSELoss()

optimizer = optim.Adam(model.parameters(), lr=0.0001)

EPOCHS = 10

for epoch in range(EPOCHS):
    model.train()
    total_loss = 0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        # 🔹 FIXED LABEL LOGIC
        stage_labels = (labels // 2).to(device)          # 0–3
        health_labels = (labels % 2 == 0).float()         # healthy=1, damaged=0
        health_labels = health_labels.unsqueeze(1).to(device)

        optimizer.zero_grad()

        stage_preds, health_preds = model(images)

        stage_loss = stage_criterion(stage_preds, stage_labels)
        health_loss = health_criterion(health_preds, health_labels)

        loss = stage_loss + health_loss
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch [{epoch+1}/{EPOCHS}] Loss: {total_loss:.4f}")

torch.save(model.state_dict(), "cotton_model.pth")
print("✅ Model training completed & saved")
