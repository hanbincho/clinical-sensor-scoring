# Import required modules
import unittest
from senbace import process_data
import os

class TestGeneratePlots(unittest.TestCase):


    def test_smoke1():
        """
        Checks if `process_data` module runs without no problems.

        The names of the columns in the correct format, but in upper-case.
        """
        process_data.generate_plots(os.getcwd() + 'tests/random_test_signals/smoke_test_signal1.csv')

    def test_smoke2():
        """
        This checks if `process_data` module runs without no problems.

        The names of the columns in the correct format, but in lower-case.
        """
        process_data.generate_plots(os.getcwd() + 'tests/random_test_signals/smoke_test_signal2.csv')

    def test_edge_case1(self):
        """
        This checks if `process_data` throws a ValueError for wrong column names.

        The supplied csv file has column names that are not in the required
        format as specified in the `process_data` Docstring.
        """
        with self.assertRaises(ValueError):
            process_data.generate_plots(os.getcwd() + 'tests/random_test_signals/edge_case_test_signal1.csv')

    def test_edge_case2(self):
        """
        This checks if `process_data` throws a ValueError for wrong column names.

        The supplied csv file has column names that are not in the required
        format as specified in the `process_data` Docstring.
        The format for this
        is different from that used in the test above.
        """
        with self.assertRaises(ValueError):
            process_data.generate_plots(os.getcwd() + 'tests/random_test_signals/edge_case_test_signal2.csv')