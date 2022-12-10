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
from .make_prediction import load_data
from .alexnet_model import AlexNet

def train_data(num_epochs, learning_rate, data_batch_size, user_data_loader):
    """

    Parameters
    ----------
    num_epochs : TYPE
        DESCRIPTION.
    learning_rate : TYPE
        DESCRIPTION.
    data_batch_size : TYPE
        DESCRIPTION.
    user_data_loader : TYPE
        DESCRIPTION.

    Returns
    -------
    accuracy_list : TYPE
        DESCRIPTION.
    loss_list : TYPE
        DESCRIPTION.

    """
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
    model = AlexNet(num_classes=7) # since score can range from 0-20
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
