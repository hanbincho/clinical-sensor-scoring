import torch
import torchvision
import numpy as np
from torch import nn
import torch.nn.functional as F
from tensorflow.keras.utils import load_img
import os
import matplotlib.pyplot as plt
import torchvision.models as models
import make_prediction as pred
import Alexnet_model as cnn

# check if GPU is available for use
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

# if GPU is available, set it to curr_device
if torch.cuda.is_available():
    dev = "cuda:0"
else:
    dev = "cpu"
    
curr_device = torch.device(dev)

def train_model(num_epochs, learning_rate, data_batch_size):
    # Set the seed value
    # Ensure reproducibility for each run
    seed = torch.initial_seed() % (2**32-1)
    np.random.seed(seed)
    torch.manual_seed(seed)

    # create model 
    model = cnn.AlexNet(num_classes=7) # since score can range from 0-20
    model.to(curr_device) # move the model to GPU

    #Definition of hyperparameters
    # num_epochs = 150
    # learning_rate = 0.00001 #0.0000005

    # Define loss function
    error = nn.CrossEntropyLoss()

    # create optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    reg_penalty = 1e-9
    count = 0
    loss_list = []
    iteration_list = []
    accuracy_list = []
    for epoch in range(num_epochs):
        correct = 0
        total = 0
        running_loss = 0
        for i, (images, labels) in enumerate(pred.load_data()):
            model.train()
            train = (images.view(data_batch_size,3,227,227))
            labels = (labels)
            # Clear gradients
            optimizer.zero_grad()
            # Forward propagation
            outputs = model(train)
            # Calculate softmax and cross entropy loss
            loss = error(outputs, labels.long())
            loss_norm = sum(p.pow(2.0).sum() for p in model.parameters()) # formula for L2 regularization
            loss = loss + reg_penalty*loss_norm
            # Calculating gradients
            loss.backward()
            # Update parameters
            optimizer.step()
            count += 1
            running_loss += loss.data
            
            predicted = torch.max(outputs.data, 1)[1]
            correct += (predicted == labels).sum()
            total += len(labels)
        accuracy_list.append(correct/total)
        loss_list.append(running_loss/i+1)
        
    return accuracy_list, loss_list