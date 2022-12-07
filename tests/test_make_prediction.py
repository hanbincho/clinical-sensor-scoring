#Import packages
import unittest
import numpy as np
import torch
import os
import tensorflow
from senbace import make_prediction as mk
from senbace import alexnet_model as cnn
from senbace import train_model as tm


#from src.Model.make_prediction import score_prediction

class TestMakePrediction(unittest.TestCase):
    def test_invalid_path_type(self):
        """
        Edge test for when a string type is not used for images_path
        """
        path_val = 8
        batch_size_val = 1
        with self.assertRaises(TypeError):
            mk.load_data(path_val, batch_size_val)
        return

    def test_nonexistent_path(self):
        """
        Edge test for when a nonexistent path is used for images_path
        """
        path_val = 'thisPathDoesnotExist'
        batch_size_val = 1
        with self.assertRaises(Exception):
            mk.load_data(path_val, batch_size_val)
        return
    
    def test_data_loader_output(self):
        """
        Smoke test for data loader type.
        """
        batch_size_val = 1
        path_val = os.getcwd()
        #load = mk.load_data(path_val, batch_size_val) # need actual path
        #np.testing.assert_almost_equal(type(load), torch)
        mk.load_data(path_val, batch_size_val)
    
    def test_predict_type(self):
        """
        One shot test for predict type.
        """
        batch_size_val = 1
        path_val = os.getcwd()
        model = cnn.forward()
        load = mk.load_data(path_val, batch_size_val)
        predict = mk.score_prediction(load, model)
        np.testing.assert_almost_equal(type(predict), tensor) 
        
    def test_train_model():
        """
        Smoke Test for train model
        """
        tm.train_model(num_epochs=10, 
                       learning_rate=.001, 
                       data_batch_size=1)
        

