# Import packages for creating machine learning model
import torch 
import torchvision

# Import packages needed for data preprocessing
import os 
import pandas as pd
from tensorflow.keras.utils import load_img 
import matplotlib as plt

# Import packages needed for visualization and assessing performance
import numpy as np 

# Definitions for necessary functions
def load_data(images_path, data_batch_size):
    """ Access image data and the pre-trained model, if available

    Parameters
    ----------
    images_path : str
        An existing directory that contains all the images for prediction
    data_batch_size : int
        A value representing the batch size when creating the data loader for the images

    Returns
    ----------
    DataLoader 
        A dataloader that represents the dataset of images ready for prediction

    
    """
    # check if GPU is available for use
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # if GPU is available, set it to curr_device
    if torch.cuda.is_available():
        dev = "cuda:0"
    else:
        dev = "cpu"
        
    curr_device = torch.device(dev)

    # Check that images_path is a str type
    if isinstance(images_path, str):
        if not(os.path.exists(images_path)):
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
    for imgFile in os.listdir(images_path):
        split_test = (imgFile.split('_'))
        subj_ID = int(split_test[0].replace('S', ''))
        # append labels of images
        imgPath = images_path+imgFile
        img = load_img(imgPath, target_size = (227, 227))
        img = data_transforms(img) # (3 x 227 x 227)
        data_img.append(img)

    data_img = torch.stack(data_img, dim = 0)
    data_labels = np.zeros(len(data_img))

    # Move all tensors to GPU if available
    data_img = data_img.to(curr_device)

    # Create dataset
    data_for_prediction = torch.utils.data.TensorDataset(data_img, data_labels)

    if len(data_img) % data_batch_size != 0:
        raise ValueError(
            "The value for data_batch_size should evenly divide into the total number of images")

    # Create dataloader
    data_loader = train_loader = torch.utils.data.DataLoader(data_for_prediction, batch_size = data_batch_size,
                                          shuffle = True)

    return data_loader

def score_prediction(test_loader, model):
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # if GPU is available, set it to curr_device
    if torch.cuda.is_available():
        dev = "cuda:0"
    else:
        dev = "cpu"
        
    curr_device = torch.device(dev)
    # load the first batch of test_loader
    test_features, test_labels = next(iter(test_loader))

    # Use the model to get the data's predicted scores
    best_model = torch.load(model)
    best_model.to(curr_device)
    outputs = best_model(test_features)

    # Get predictions from the maximum value
    predicted = torch.max(outputs.data, 1)[1]

    # plot the first 10 test images
    # have the title contain the predicted score and actual score
    # for i in range(10):
    #     pic = test_features[i]
    #     pic = torch.tensor(pic).cpu()
    #     pic = pic.permute(1, 2, 0) # display a PyTorch tensor as an image (i.e. make channels the last dimension)
    #     plt.figure()
    #     plt.imshow(pic)
    #     pred_score = predicted[i]

    #     title = 'Predicted FMA-UE Score = %f; Actual FMA-UE Score = %f'% (pred_score.item(), test_labels[i])
    #     plt.title(title)
    
    return predicted