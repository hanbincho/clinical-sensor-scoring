from streamlit_extras.switch_page_button import switch_page

import streamlit as st
import pandas as pd
import numpy as np
import io
import os
import re
import matplotlib.pyplot as plt

from prediction_and_training import make_prediction
from prediction_and_training.alexnet_model import AlexNet 

from PIL import Image
from io import BytesIO

# Import required packages
def plot(file):
    """


    Parameters
    ----------
    file : TYPE
        DESCRIPTION.

    Raises
    ------
    ValueError
        DESCRIPTION.

    Returns
    -------
    None.

    """
    ''''''
    # Set default image size to 6 x 4.5 in
    plt.rcParams['figure.figsize'] = (6, 4.5)

    sensor_data = pd.read_csv(file, header=0)

    # Verify if the column names in CSV file conform to required format
    col_regex = re.compile(r'[A-Za-z]{3}-[XYZxyz]')
    dataframe_col_name_check = [col_regex.match(col_name) for col_name in sensor_data.columns]

    if not all(dataframe_col_name_check):
        raise ValueError("One or more column names in CSV file do not match the required format.")

    st.header("Plots from Raw Data")
    image_path = os.getcwd() + '/generated_plots_for_prediction/'
    os.makedirs(image_path, exist_ok=True)
    for col in sensor_data:
        fig = plt.figure()
        st.write('Plot for ' + file.name.split('.')[0] + '-' + col)
        plt.plot(sensor_data[col], 'r')
        plt.xlim(0.0)
        plt.axis('off')

        plt.savefig(image_path + file.name.split('.')[0] + '-' + col + '.png', dpi=600)
        plt.close()
        st.write(fig)

st.set_page_config(page_title="Load Data")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("# Load Data")
st.sidebar.header("Load Data")
col1, col2 = st.columns(2)

with col1:
    patient_input = st.text_input(
        "Patient Name",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )
    if patient_input:
        st.write("You entered: ", patient_input)

    upload_csv = st.file_uploader("Choose a file", key='1')
    if upload_csv:
        plot(upload_csv)



#================================================================

with col2:
    st.markdown("## Predicting with a Pretrained Model")
    predict_pressed = st.button("Predict Scores")

    if predict_pressed:
        st.write('Default training model will be used to predict score.')

        file_path = os.getcwd() + '/senbace/generated_plots_for_prediction/'
        files = os.listdir(file_path)
        data_loader = make_prediction.load_data(file_path, 1)
        model_path = os.getcwd() + '/tests/test_model/alex_net_changed_classes_170eps.pth'
        pred_score = make_prediction.score_prediction(data_loader, model_path)
        # st.write(pred_score)

        for ii in range(len(pred_score)):
            displayed_text = 'Predicted score for {}: {}'.format(files[ii].split('.')[0], pred_score[ii])
            st.write(displayed_text) 

            if patient_input:
                with open(patient_input +'_predicted_scores.txt', 'a') as f:
                    f.write((displayed_text) + '\n')
                f.close()

            else:
                with open(patient_input + '_patient_predicted_scores.txt', 'a') as f:
                    f.write((displayed_text) + '\n')
                f.close()

        st.download_button("Download scores", str(pred_score), file_name = patient_input +'_patient_predicted_scores.txt')

text_out = st.text_area("Feedback: " )


# with open(patient_input + '_patient_predicted_scores.txt', 'a') as f:
#     f.write((text_out) + '\n')
#     f.close()
 
        


