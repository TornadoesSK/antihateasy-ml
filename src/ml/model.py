import torch
from torch import nn
from pytorch_lightning import LightningModule
from torchtext.models import RobertaClassificationHead, XLMR_BASE_ENCODER
import torchtext.functional as F

class Net(LightningModule):
    def __init__(self, learning_rate=1e-3):
        super().__init__()
        self.softmax = nn.Softmax(dim=1)

        self.learning_rate = learning_rate
        
        head = RobertaClassificationHead(num_classes=3, input_dim=768)
        self.model = XLMR_BASE_ENCODER.get_model(head=head, freeze_encoder=True)

        self.relu = nn.ReLU()
        self.flatten = nn.Flatten()
        self.conv = nn.Conv2d(1, 32, 3)
        self.fc1 = nn.Linear(50*50, 128)
        self.fc2 = nn.Linear(512, 128)
        self.fc3 = nn.Linear(128, 3)

    def forward(self, x):
        return self.model(x)

    def predict_sentence(self, sentence):
        transformed = XLMR_BASE_ENCODER.transform()(sentence)
        transformed = F.to_tensor(transformed).unsqueeze(0)
        logits = self(transformed).detach()
        return {
            "probs": self.softmax(logits).tolist()[0],
            "class": torch.argmax(logits).item()
        }
