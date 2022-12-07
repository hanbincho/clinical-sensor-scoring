# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:31:15 2022

"""

# Import required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_random_signal(n_row, n_col, col_label, file_name):
    # signal = np.random.rand(n_row, n_col)
    signal = np.random.randn(n_row, n_col)
    signal_dataframe = pd.DataFrame(signal, columns=col_label)
    signal_dataframe.to_csv(file_name, index=False)

    for col in signal_dataframe:
        plt.figure()
        plt.plot(signal_dataframe[col])
        plt.xlim(0.0)


create_random_signal(200, 3, ['ABC-X', 'DEF-Y', 'GHI-Z'], 'smoke_test_signal1.csv')
create_random_signal(150, 3, ['abc-x', 'opq-y', 'lst-z'], 'smoke_test_signal2.csv')
create_random_signal(300, 3, ['ABC-X', 'DEFMNO-Y', 'GHI-Z'], 'edge_case_test_signal1.csv')
create_random_signal(200, 3, ['ABC-V', 'MNO-Y', 'GHI-Z'], 'edge_case_test_signal2.csv')

