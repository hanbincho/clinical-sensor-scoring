"""ResNetModel
A class to represent the specific type of CNN model used for predicting clinical scores.

This requires the following to be installed within the Python environment:
    * torch
    * torchvision
    * numpy

This file can be imported and contains the following:
    Attributes
    ----------
    * net: a sequence of convolutional, batch normalization, max pooling, and 
        activation layers
    * classifier: a sequence of fully linear connected and dropout layers

    Methods
    -------
    * forward: forward propagation where the input is passed through the network
"""

import torch
import torchvision
import numpy as np
from torch import nn
import torch.nn.functional as F
class ResBlock(nn.Module):
    """
    Component of the ResNet architecture that enables skip connections 

    Parameters
    ----------
    in_channels : int
        The number of input features

    out_channels : int
        The number of output features

    Returns
    ----------
    None
    """
    def __init__(self, in_channels, out_channels, downsample):
        super().__init__()
        if downsample:
            self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=2, padding=1)
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=2),
                nn.BatchNorm2d(out_channels)
            )
        else:
            self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=3, stride=1, padding=1)
            self.shortcut = nn.Sequential()

        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(out_channels)
        self.bn2 = nn.BatchNorm2d(out_channels)

    def forward(self, input):
        shortcut = self.shortcut(input)
        input = nn.ReLU()(self.bn1(self.conv1(input)))
        input = nn.ReLU()(self.bn2(self.conv2(input)))
        input = input + shortcut
        return nn.ReLU()(input)

class ResNet18(nn.Module):
    def __init__(self, input_channels=3, resblock=ResBlock, num_classes=1000):
        super().__init__()
        self.layer0 = nn.Sequential(
            nn.Conv2d(in_channels=input_channels, out_channels=64, kernel_size=7, stride=2, padding=3),
            nn.MaxPool2d(kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU()
         )

        self.layer1 = nn.Sequential(
        resblock(64, 64, downsample=False),
        resblock(64, 64, downsample=False)
        )

        self.layer2 = nn.Sequential(
            resblock(64, 128, downsample=True),
            resblock(128, 128, downsample=False)
        )

        self.layer3 = nn.Sequential(
            resblock(128, 256, downsample=True),
            resblock(256, 256, downsample=False)
        )


        self.layer4 = nn.Sequential(
            resblock(256, 512, downsample=True),
            resblock(512, 512, downsample=False)
        )

        self.gap = torch.nn.AdaptiveAvgPool2d(1)
        self.fc = torch.nn.Linear(512, num_classes)

    def forward(self, input):
        input = self.layer0(input)
        input = self.layer1(input)
        input = self.layer2(input)
        input = self.layer3(input)
        input = self.layer4(input)
        input = self.gap(input)
        input = input.reshape(input.size(0), -1)
        input = self.fc(input)
        input = F.softmax(input, dim=1)
        return input