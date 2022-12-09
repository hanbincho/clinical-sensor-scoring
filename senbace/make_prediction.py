"""Predict Scores
This script allows a user to feed in image data and obtain score predictions for each.

This requires the following to be installed within the Python environment:
    * os
    * torch
    * torchvision
    * tensorflow
    * numpy

This file can be imported and contains the following functions:
    * load_data: returns a dataloader type that can be used as an input for predicting
        scores
    * score_prediction: returns a list of values reflecting the score predicted for
      each input
"""
# Import packages for directory navigation
import os

# Import packages for creating machine learning model
import torch
import torchvision

# Import packages needed for data preprocessing
from tensorflow.keras.utils import load_img

# Import packages needed for visualization and assessing performance
import numpy as np

# Definitions for necessary functions
def load_data(images_path, data_batch_size):
    """
    Access image data to create a dataloader for prediction

    Parameters
    ----------
    images_path : str
        An existing directory that contains all the images for prediction
    data_batch_size : int
        A value representing the batch size when creating the data loader for the images

    Returns
    ----------
    data_loader : DataLoader
        A dataloader that represents the dataset of images ready for prediction

    """
    # if GPU is available, set it to curr_device
    if torch.cuda.is_available():
        dev = "cuda:0"
    else:
        dev = "cpu"

    curr_device = torch.device(dev)

    # Check that images_path is a str type
    if isinstance(images_path, str):
        if not os.path.exists(images_path):
            raise Exception("The directory given does not exist!")
    else:
        raise TypeError("images_path must be a string type!")

    # Establish transformations for each dataset

    data_transforms = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Normalize(
        (0.5,), (0.5))
    ])

    # Load images for prediction
    data_img = []
    for img_file in os.listdir(images_path):
        # append labels of images
        img_path = images_path+img_file
        img = load_img(img_path, target_size = (227, 227))
        img = data_transforms(img) # (3 x 227 x 227)
        data_img.append(img)

    data_img = torch.stack(data_img, dim = 0)
    data_labels = np.zeros(len(data_img))

    # Move all tensors to GPU if available
    data_img = data_img.to(curr_device)

    # Convert labels to Tensor type
    data_labels = torch.Tensor(data_labels)

    # Create dataset
    data_for_prediction = torch.utils.data.TensorDataset(data_img, data_labels)

    if len(data_img) % data_batch_size != 0:
        print(len(data_img))
        print(data_batch_size)
        raise ValueError(
            "The value for data_batch_size should evenly divide into the total \
            number of images")

    # Create dataloader
    data_loader = torch.utils.data.DataLoader(data_for_prediction, \
        batch_size = data_batch_size, shuffle = True)

    return data_loader

def score_prediction(test_loader, model):
    """


    Parameters
    ----------
    test_loader : TYPE
        DESCRIPTION.
    model : TYPE
        DESCRIPTION.

    Returns
    -------
    predictions : TYPE
        DESCRIPTION.

    """
    # if GPU is available, set it to curr_device
    if torch.cuda.is_available():
        dev = "cuda:0"
    else:
        dev = "cpu"

    curr_device = torch.device(dev)

    # Use the model to get the data's predicted scores
    best_model = torch.load(model, map_location=torch.device(dev))
    best_model.to(curr_device)

    # Iterate through the test loader and find predictions for each image
    predictions = []
    for _, (test_features, _) in enumerate(test_loader):
        best_model.eval()
        outputs = best_model(test_features)
        # Get predictions from the maximum value
        predicted = torch.max(outputs.data, 1)[1]
        # Convert from tensor to numpy
        predicted = predicted.cpu().detach().numpy()
        predictions.append(predicted+14)

    return predictions
