"""Train model
This script allows a user to train a model from scratch using a personal dataset.

This requires the following to be installed within the Python environment:
    * torch
    * numpy

This file can be imported and contains the following functions:
    * train_data: returns a list of accuracies and losses when training the model
"""
import torch
import numpy as np
from torch import nn
import os
from .alexnet_model import AlexNet
from .resnet_model import ResNet18
from .resnet_model import ResBlock
os.sys.path.append('../')

def train_data(num_epochs, learning_rate, data_batch_size, user_data_loader, model_type):
    """
    Train the AlexNet model with user specific hyperparameters and datset

    Parameters
    ----------
    num_epochs : int
        A value representing the number of training cycles for the machine learning
        model
    learning_rate : double
        A value representing the step size of each iteration while optimizing the loss 
        function
    data_batch_size : int
        A value representing the number of images used for training during an iteration
    user_data_loader : Dataloader
        A dataloader containing the images to be used for model training
    model_type : str
        The type of model to be used for training. Either "AlexNet" for AlexNet or 
        "ResNet" for ResNet

    Returns
    -------
    accuracy_list : list
        A list of training accuracies recorded during training of the model
    loss_list : list
        A list of training lossess recorded during training of the model

    """
    if (num_epochs <= 0): #
        raise ValueError("Speicfy epochs greater than 0")
    # # checking for learning rate
    elif (learning_rate <= 0): 
        raise ValueError("Speicfy learning rate greater than 0")
    elif (data_batch_size <= 0):
        raise ValueError("Specify batch size greater than 0, cannot take negative value")

    # if GPU is available, set it to curr_device
    if torch.cuda.is_available():
        DEV = "cuda:0"
    else:
        DEV = "cpu"

    curr_device = torch.device(DEV)

    # Set the seed value
    # Ensure reproducibility for each run
    seed = torch.initial_seed() % (2**32-1)
    np.random.seed(seed)
    torch.manual_seed(seed)

    # create model
    if model_type == "AlexNet":
        model = AlexNet(num_classes=7) 
    elif model_type == "ResNet":
        model = ResNet18(num_classes=7)
    model.to(curr_device) # move the model to GPU

    # Define loss function
    error = nn.CrossEntropyLoss()

    # create optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    reg_penalty = 1e-9
    count = 0
    loss_list = []
    accuracy_list = []
    for _ in range(num_epochs):
        correct = 0
        total = 0
        running_loss = 0
        for i, (images, labels) in enumerate(user_data_loader):
            model.train()
            train = (images.view(data_batch_size,3,227,227))
            # Clear gradients
            optimizer.zero_grad()
            # Forward propagation
            outputs = model(train)
            # Calculate softmax and cross entropy loss
            loss = error(outputs, labels.long())
            # formula for L2 regularization
            loss_norm = sum(p.pow(2.0).sum() for p in model.parameters())
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
