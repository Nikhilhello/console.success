import torch
import torch.nn as nn
from torchvision import models

class CottonNet(nn.Module):
    def __init__(self, num_stages=4):
        super(CottonNet, self).__init__()

        # 🔹 Load pretrained MobileNetV2
        self.backbone = models.mobilenet_v2(pretrained=True)

        # 🔹 Remove original classifier
        in_features = self.backbone.classifier[1].in_features
        self.backbone.classifier = nn.Identity()

        # 🔹 Stage classification head (4 classes)
        self.stage_head = nn.Sequential(
            nn.Linear(in_features, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_stages)
        )

        # 🔹 Health score head (0–1)
        self.health_head = nn.Sequential(
            nn.Linear(in_features, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

    def forward(self, x):
        features = self.backbone(x)

        stage_output = self.stage_head(features)
        health_output = self.health_head(features)

        return stage_output, health_output
