from streamlit_extras.switch_page_button import switch_page

import streamlit as st
import pandas as pd
import numpy as np
import io
import os
import re
import matplotlib.pyplot as plt
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src/data_processing'))
import process_data


# Import required packages
def plot(file):
    st.set_header("Plots from Raw Data")
    # Set default image size to 6 x 4.5 in
    plt.rcParams['figure.figsize'] = (6, 4.5)

    sensor_data = pd.read_csv(file, header=0)

    # Check if provided file/path exists

    # Verify if the column names in CSV file conform to required format
    col_regex = re.compile(r'[A-Za-z]{3}-[XYZxyz]')
    dataframe_col_name_check = [col_regex.match(col_name) for col_name in sensor_data.columns]

    if not all(dataframe_col_name_check):
        raise ValueError("One or more column names in CSV file do not match the required format.")
    with col2:
        for col in sensor_data:
            fig = plt.figure()
            plt.plot(sensor_data[col], 'r')
            plt.xlim(0.0)
            plt.axis('off')
            # plt.savefig(upload_csv.split('.')[0] + '-' + col + '.png', dpi=600)
            # plt.close()
            st.write(fig)
            plt.savefig('image')


st.set_page_config(page_title="Load Data")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("# Load Data")
st.sidebar.header("Load Data")
col1, col2 = st.columns([3, 4])

with col1:
    patient_input = st.text_input(
        "Patient Name",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
    if patient_input:
        st.write("You entered: ", patient_input)
    loca_option = st.selectbox(
        "Specify Location",
        ("Location 1", "Location 2", "Location 3", "Upload a CSV file"),
    )
    model_option = st.selectbox(
        "Select Model",
        ('Model 1', 'Model 2', 'Upload a model'),
    )
    if (model_option == 'Upload a model'):
        upload_model = st.file_uploader("Choose a file")

    if (loca_option == 'Upload a CSV file'):
        upload_csv = st.file_uploader("Choose a file")
        if upload_csv:
            plot(upload_csv)

        # if os.path.exists(file) != True:
        # raise FileNotFoundError("Provided file does not exist.")
        # if upload_csv:

    # if patient_input and loca_option and model_option:
    #   if st.button("Analyze"):
    #      with col2:
    #         st.write("Plots will be here")

next = st.button("Next")
if next:
    switch_page("Plot")
