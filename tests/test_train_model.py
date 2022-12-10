#Import packages
import unittest
import os
from senbace.make_prediction import load_data
from senbace.train_model import train_data


class TestTrainModel(unittest.TestCase):
 
    def test_smoke1(self):
        """Smoke test: making sure model runs when all 3 parameters are given"""
        num_epochs = 10
        learning_rate = 0.0001
        data_batch_size = 32
        smoke_data_loader = load_data(os.getcwd()+"/tests/test_images/", 1)
        accuracy_list, loss_list = train_data(num_epochs, learning_rate,data_batch_size,smoke_data_loader)
        self.assertIsNotNone(accuracy_list)
        self.assertIsInstance(accuracy_list, list)
        self.assertIsNotNone(loss_list)
        self.assertIsInstance(loss_list, list)

    def test_data_batch_size(self):
        """
        Parameter 1 Test: Edge test for when a batch size is in float
        """
        num_epochs = 10
        learning_rate = 0.0001
        data_batch_size = -19.00
        smoke_data_loader = load_data(os.getcwd()+"/tests/test_images/", 1)
        with self.assertRaises(ValueError):
            train_data(num_epochs, learning_rate,data_batch_size,smoke_data_loader)
        return
    
    def test_check_epochs(self):
        """
        Parameter 2 Test: Edge test when epoch is 0
        """
        num_epochs = 0
        learning_rate = 0.0001
        data_batch_size = 19
        smoke_data_loader = load_data(os.getcwd()+"/tests/test_images/", 1)
        with self.assertRaises(ValueError):
            train_data(num_epochs, learning_rate,data_batch_size,smoke_data_loader)
        return

    def test_check_learning_rate(self):
        """
        Parameter 3 Test: Edge test when learning rate is negative
        """
        num_epochs = 10
        learning_rate = -0.0001
        data_batch_size = 19
        smoke_data_loader = load_data(os.getcwd()+"/tests/test_images/", 1)
        with self.assertRaises(ValueError):
            train_data(num_epochs, learning_rate,data_batch_size,smoke_data_loader)
        return