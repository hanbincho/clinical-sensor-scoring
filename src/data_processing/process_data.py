# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:22:53 2022

@author: udu
"""

# Import required packages
import os
import re
import pandas as pd
import matplotlib.pyplot as plt


def generate_plots(file):
    """
    This function generates plots for the sensor readings records of a particular patient.


    Parameters
    ----------
    file : str, path object or file-like object.
        # CSV file containing the records form one record for a patient.

            * The CSV file must contain readings from only one sensor at a particular location on the patient's anatomy.

            * The CSV file should be named using a user-preferred scheme which distinguishes patients.

            * The CSV file must contain n number of columns depending on the number of axes recorded using the sensor.

            * The first row of the CSV file must specify an identifying tag for the sensor readings.
                    * Format of the tag should be ###-$, where;
                        * ### should be replaced by a 3 letter abbreviation for the sensor location; and
                        * $ should be replaced by the axis of measurement for the sensor.
                        * For example WRA-X to denote readings from the WRA sensor in the x-axis.

    Returns
    -------
    Saves PNG images of generated plots.

    """

    if os.path.exists(file) != True:
        raise FileNotFoundError("Provided file does not exist.")

    # Set default image size to 6 x 4.5 in
    plt.rcParams['figure.figsize'] = (6, 4.5)

    sensor_data = pd.read_csv(file, header=0)

    # Check if provided file/path exists
    if os.path.exists(file) != True:
        raise FileNotFoundError("Provided file does not exist.")

    # Verify if the column names in CSV file conform to required format
    col_regex = re.compile(r'[A-Za-z]{3}-[XYZxyz]')
    dataframe_col_name_check = [col_regex.match(col_name) for col_name in sensor_data.columns]

    if not all(dataframe_col_name_check):
        raise ValueError("One or more column names in CSV file do not match the required format.")

    for col in sensor_data:
        plt.plot(sensor_data[col], 'r')
        plt.xlim(0.0)
        plt.axis('off')
        plt.savefig(file.split('.')[0] + '-' + col + '.png', dpi=600)
        plt.close()



if __name__ == '__main__':
    generate_plots('01_1_1.csv')
