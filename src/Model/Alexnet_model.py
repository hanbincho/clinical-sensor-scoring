# Import packages for creating machine learning model
import torch
import torchvision
import numpy as np
from torch import nn
import torch.nn.functional as F

#Create the CNN Model
class AlexNet(nn.Module):
    """
    Neural network model consisting of layers propsed by AlexNet paper.
    """
    def __init__(self, num_classes=1, p_drop=0.5):
        """
        Define and allocate layers for this neural net.
        Args:
            num_classes (int): number of classes to predict with this model
        """
        super(AlexNet, self).__init__()
        
        # convolutional and max pooling layers
        self.net = nn.Sequential(
            # Input: (n x 227 x 227 x 3)
            # Convolutional layer 1 w/ max pooling
            # (n x 55 x 55 x 96)
            nn.Conv2d(in_channels=3, out_channels=96, kernel_size=11, stride=4, padding=0),
            nn.ReLU(),
            nn.BatchNorm2d(num_features=96),
            # (n x 27 x 27 x 96)
            nn.MaxPool2d(kernel_size=3, stride=2),
            
            # Convolutional layer 2 w/ max pooling 
            # (n x 27 x 27 x 256)
            nn.Conv2d(in_channels=96, out_channels=256, kernel_size=5, stride=1, padding=2),
            nn.ReLU(),
            nn.BatchNorm2d(num_features=256),
            
            # (n x 13 x 13 x 256)
            nn.MaxPool2d(kernel_size=3, stride=2) ,
            
            # Convolutional layer 3 
            # (n x 13 x 13 x 384)
            nn.Conv2d(in_channels=256, out_channels=384, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(num_features=384),
            
            # Convolutional layer 4 
            # (n x 13 x 13 x 384)
            nn.Conv2d(in_channels=384, out_channels=384, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(num_features=384),
            
            # Convolutional layer 5 
            # (n x 13 x 13 x 256)
            nn.Conv2d(in_channels=384, out_channels=256, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.BatchNorm2d(num_features=256),
            
            
            # Max pooling layer 
            # (n x 6 x 6 x 256)
            nn.MaxPool2d(kernel_size=3, stride=2)
        )
        
        # 3 fully connected layers
        self.classifier = nn.Sequential(
            # Input: (n x 9216)
            # Dropout layer 1
            nn.Dropout(p=p_drop),
            
            # Fully connected layer 1 
            # (n x 4096)
            nn.Linear(9216, 4096),
            nn.ReLU(),
            
            # Dropout layer 2
            nn.Dropout(p=p_drop),
            
            # Fully connected layer 2 
            # (n x 4096)
            nn.Linear(4096, 4096),
            nn.ReLU(),
            
            # Fully connected layer 3 
            # (n x 1000)
            nn.Linear(4096, 1000),
            nn.ReLU(),

            # Fully connected layer 4
            nn.Linear(1000, num_classes)
        )
       
        # initialize bias
        
        self.init_bias()

    def init_bias(self):
        # Initialize weights according to original paper
        for layer in self.net:
            if isinstance(layer, nn.Conv2d):
                nn.init.normal_(layer.weight, mean=0, std=0.01)
                nn.init.constant_(layer.bias, 0)
        # changed indices due to variability in layers 
        nn.init.constant_(self.net[4].bias, 1)
        nn.init.constant_(self.net[11].bias, 1)
        nn.init.constant_(self.net[14].bias, 1)

    def forward(self, x):
        x = self.net(x)
        # reduce the dimensions for linear layer input
        x = torch.flatten(x, start_dim=1)
        x = self.classifier(x)
        out = F.softmax(x, dim=1)
        return out