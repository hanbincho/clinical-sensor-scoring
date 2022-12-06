#Import packages
import unittest
import numpy as np
import torch
from src.Model import make_prediction as mk
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
    
    # def test_normalize_image_size(self):
    #     """
    #     Oneshot test for image is 227x227 size.
    #     """
    #     batch_size_val = 1
    #     mk.load_data(path_val, batch_size_val)
    #     image_size = img.shape()
    #     np.testing.assert_almost_equal(image_size, (227,227))

