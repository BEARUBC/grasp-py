import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import ExponentialLR, ReduceLROnPlateau
from tqdm import tqdm
import pandas as pd
import plotly.express as px


class GripConvNet(nn.Module):
    def __init__(self):
        super().__init__()
        state_n_cs = 4
        self.conv1 = nn.Conv2d(in_channels=state_n_cs, out_channels=state_n_cs * 4, kernel_size=(5, 5))
        self.conv2 = nn.Conv2d(in_channels=state_n_cs * 4, out_channels=state_n_cs * 8, kernel_size=(3, 3))
        self.fc1 = nn.Linear(7200, 1000)
        self.fc2 = nn.Linear(1000, 1000)
        self.fc3 = nn.Linear(1000, 120)
        self.fc4 = nn.Linear(120, 4)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.dropout(x, p=0.55)
        x = F.relu(self.fc2(x))
        x = F.dropout(x, p=0.5)
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x
