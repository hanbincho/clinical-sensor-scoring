import unittest

from src.Model import load_data
from src.Model import score_prediction

class TestMakePrediction(uinttest.TestCase):
    def test_invalid_path(self):
        """
        Edge test for when an invalid path is fed into load_data
        """

        return