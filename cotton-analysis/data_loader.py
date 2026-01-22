import torch
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Image size for CNN
IMG_SIZE = 224
BATCH_SIZE = 16

# 🔹 TRAIN DATA AUGMENTATION
train_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.RandomHorizontalFlip(p=0.5),
    transforms.RandomRotation(30),
    transforms.ColorJitter(
        brightness=0.3,
        contrast=0.3,
        saturation=0.2
    ),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# 🔹 VALIDATION (NO AUGMENTATION)
val_transforms = transforms.Compose([
    transforms.Resize((IMG_SIZE, IMG_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# 🔹 LOAD DATASETS
train_dataset = datasets.ImageFolder(
    root="dataset/train",
    transform=train_transforms
)

val_dataset = datasets.ImageFolder(
    root="dataset/val",
    transform=val_transforms
)

# 🔹 DATA LOADERS
train_loader = DataLoader(
    train_dataset,
    batch_size=BATCH_SIZE,
    shuffle=True
)

val_loader = DataLoader(
    val_dataset,
    batch_size=BATCH_SIZE,
    shuffle=False
)

print("✅ Data loaders created successfully")
print("Classes:", train_dataset.classes)
