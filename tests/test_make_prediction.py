#Import packages
import unittest
import numpy as np
import torch
import os
import tensorflow

# from senbace.make_prediction import load_data
# from senbace.make_prediction import score_prediction
# from senbace.train_model import train_data

from senbace.prediction_and_training import make_prediction 
from senbace.prediction_and_training import train_model 


class TestMakePrediction(unittest.TestCase):
    def test_invalid_path_type(self):
        """
        Edge test for when a string type is not used for images_path
        """
        path_val = 8
        batch_size_val = 1
        with self.assertRaises(TypeError):
            make_prediction.load_data(path_val, batch_size_val)
        return

    def test_nonexistent_path(self):
        """
        Edge test for when a nonexistent path is used for images_path
        """
        path_val = 'thisPathDoesnotExist'
        batch_size_val = 1
        with self.assertRaises(Exception):
            make_prediction.load_data(path_val, batch_size_val)
        return
    
    def test_data_loader_output(self):
        """
        Smoke test to see if load_data function can run
        """
        batch_size_val = 1
        path_val = os.getcwd()+"/tests/test_images/"
        make_prediction.load_data(path_val, batch_size_val)
        return
        
    def test_train_model(self):
        """
        Smoke Test for train model
        """
        smoke_data_loader = make_prediction.load_data(os.getcwd()+"/tests/test_images/", 1)
        train_model.train_data(num_epochs=10, learning_rate=.001, data_batch_size=1,
            user_data_loader = smoke_data_loader)
        return