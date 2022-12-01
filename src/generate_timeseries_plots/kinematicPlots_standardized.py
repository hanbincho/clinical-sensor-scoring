# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:22:53 2022

@author: udu
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count


# Specify the patient directory to generate plots for
patient_direc = 'Healthy/'  # set as 'Stroke/' or 'Healthy/'

# =================================================================================== #
# NOTHING CHANGES BELOW THIS LINE
direc = 'G:\\.shortcut-targets-by-id\\1rAoOFon9LiqsSDkMfuwsccmTlPz119bS\\clinical_sensor_score_predictions_CSE583\\data\\MHH/Data/kinematic/'
data_direc = os.path.join(direc, patient_direc)
plots_direc = os.path.join(direc, 'zScoreStandardizedPlots/' + patient_direc)
os.makedirs(plots_direc, exist_ok=True)

sensor_labels = ['WRA', 'WRB', 'RU1', 'RU2', 'RU3', 'RU4',
                  'ELB_M', 'ELB_L', 'H1', 'H2', 'H3', 'H4',
                  'H5', 'H6', 'SA1', 'SA2', 'SA3', 'CS1',
                  'CS2', 'CS3', 'CS4']

# Create directories for each kinematic sensor position
for label in sensor_labels:
    os.makedirs(plots_direc + label + '/', exist_ok=True)

axes = ['X', 'Y', 'Z']
dataFrame_col_labels = []

for label in sensor_labels:
    for axis in axes:
        dataFrame_col_labels.append(label + '-' + axis)

# Set default image size to 6 x 4.5 in
plt.rcParams['figure.figsize'] = (6, 4.5)


def generate_kinematic_plots(file):

    if "static" not in file:
        data = pd.read_csv(data_direc + file, header=None, skiprows=2)

        # Some files have additional columns beyond the relevant 63, so we'd drop the extra columns
        data = data.loc[:, :62]

        # Set names of each column based on sensor type and axis.
        data.columns = dataFrame_col_labels

        # Perform feature scaling on data by mean normalization and standardization.
        # Note that Pandas runs the command below on a column-by-column basis.
        normalized_data = (data - data.mean()) / data.std()

        for ii in range(data.shape[1]):
            plt.plot(normalized_data[dataFrame_col_labels[ii]], 'r')
            plt.xlim(0.0)
            plt.axis('off')
            plt.savefig(plots_direc + sensor_labels[ii // 3] + '/' + file.split('.')[0] + '_' + dataFrame_col_labels[ii] + '.png', dpi=600)
            plt.close()


'''
About 100,000 plots to generate, we'd make use of Python's multiprocessing
package to speed up the process.
'''
# Extract files for all senor recordings
sensor_data_files = os.listdir('MHH/Data/kinematic/' + patient_direc)

# Assign three-quarters the number of CPU cores for parallel processing
processes = int(0.75 * cpu_count())

if __name__ == '__main__':
    with Pool(processes=processes) as pool:
        pool.map(generate_kinematic_plots, sensor_data_files)
        pool.close()

