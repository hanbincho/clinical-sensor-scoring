# Import packages for creating machine learning model
import torch 
import torchvision

# Import packages needed for data preprocessing
import os 
import pandas as pd
from tensorflow.keras.utils import load_img 

# Import packages needed for visualization and assessing performance
import numpy as np 

# Definitions for necessary functions
def load_data(images_path, data_batch_size):
    """ Access image data and the pre-trained model, if available

    Parameters
    ----------
    images_path : 
    data_batch_size : int
    model_path :

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

    # Create dataloader
    data_loader = train_loader = torch.utils.data.DataLoader(data_for_prediction, batch_size = data_batch_size,
                                          shuffle = True)

    return data_loader


