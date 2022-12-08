#Import packages
import unittest
import numpy as np
import torch
import os
import tensorflow
from senbace import load_data
from senbace import train_data
from senbace import AlexNet
#from src.Model.make_prediction import score_prediction

class TestMakePrediction(unittest.TestCase):
    def test_invalid_path_type(self):
        """
        Edge test for when a string type is not used for images_path
        """
        path_val = 8
        batch_size_val = 1
        with self.assertRaises(TypeError):
            load_data(path_val, batch_size_val)
        return

    def test_nonexistent_path(self):
        """
        Edge test for when a nonexistent path is used for images_path
        """
        path_val = 'thisPathDoesnotExist'
        batch_size_val = 1
        with self.assertRaises(Exception):
            load_data(path_val, batch_size_val)
        return
    
    # def test_data_loader_output(self):
    #     """
    #     Smoke test to see if load_data function can run
    #     """
    #     batch_size_val = 1
    #     path_val = os.getcwd()+"/WRA/"
    #     load_data(path_val, batch_size_val)
    #     return
    
    # def test_predict_type(self):
    #     """
    #     Smoke test to see if score_prediction function can run
    #     """
    #     batch_size_val = 1
    #     path_val = os.getcwd()+"/clinical-sensor-scoring/WRA/"
    #     # model = forward() # model should be a path to a .pth file type
    #     load = load_data(path_val, batch_size_val)
    #     predict = score_prediction(load, model)
    #     np.testing.assert_almost_equal(type(predict), int) 
        
    def test_train_model():
        """
        Smoke Test for train model
        """
        train_data(num_epochs=10, 
                       learning_rate=.001, 
                       data_batch_size=1)
        return
        

