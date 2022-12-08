import streamlit as st 
import pandas as pd
import numpy as np
import os
from streamlit_extras.switch_page_button import switch_page
from make_prediction import load_data
from make_prediction import score_prediction
from alexnet_model import AlexNet
from PIL import Image
from io import BytesIO


st.set_page_config(page_title="Training a Model and Performing Predictions")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("# Training and Predicting")
st.sidebar.header("Training and Prediction")

col1, col2 = st.columns([2, 1])

with col1:
    # Uploading widgets for needed files
    image_file = st.file_uploader("Choose an image file", accept_multiple_files = True)
    model_file = st.file_uploader("Choose a model file")

    # Text box for batch size with default = 1
    user_batch_size = st.text_input("Batch Size", 1)

    # Button to start prediction
    predict_pressed = st.button("Predict Scores")

with col2:
    # Text input box for feedback
    text_out = st.text_area("Feedback: ", "Temporary text for now...")

if image_file is not None:
    # Check that download directory for image exists
    download_image_path = os.getcwd()+"/senbace/data/"
    if not os.path.exists(download_image_path):
        # If not, make it
        os.makedirs(download_image_path)

    st.write("Loaded: ")
    for i in range(len(image_file)):
        st.write(image_file[i].name)
        # Then save the image
        img_to_save = Image.open(image_file[i])
        img_to_save.save(download_image_path+image_file[i].name)


if model_file is not None:
    st.write("Loaded: ", model_file.name)
    # Check that download directory for model exists
    download_model_path = os.getcwd()+"/senbace/model/"
    if not os.path.exists(download_model_path):
        # If not, make it
        os.makedirs(download_model_path)
    # Then save the model file
    model_data = model_file.getvalue()
    model_to_save = open(download_model_path+model_file.name, "wb")
    model_to_save.write(model_data)
    model_to_save.close()
    

# Perform prediction with pretrained model on uploaded image
if predict_pressed:
    data_loader = load_data(download_image_path, int(user_batch_size))
    pred_score = score_prediction(data_loader, download_model_path+model_file.name)
    # Iterate through all images and print out the corresponding score
    for i in range(len(image_file)):
        st.write("Result for "+ image_file[i].name + ": " + str(pred_score[i]))
        # Delete the downloaded image files
        if os.path.exists(download_image_path+image_file[i].name):
            os.remove(download_image_path+image_file[i].name)
    # Also delete the downloaded model file
        if os.path.exists(download_model_path+model_file.name):
            os.remove(download_model_path+model_file.name)