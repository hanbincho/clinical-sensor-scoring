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


st.set_page_config(page_title="Pretrained Model Predictions")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("# Predicting with a Pretrained Model")
st.sidebar.header("Pretrained Prediction")

col1, col2 = st.columns([2, 1])

with col1:
    # Uploading widgets for needed files
    image_file = st.file_uploader("Choose an image file")
    model_file = st.file_uploader("Choose a model file")

    # Text box for batch size with default = 1
    user_batch_size = st.text_input("Batch Size", 1)

    # Button to start prediction
    st.button("Predict Scores")

with col2:
    # Text input box for feedback
    text_out = st.text_area("Feedback: ", "Temporary text for now...")

if image_file is not None:
    st.write("Loaded: ", image_file.name)
    # Download uploaded image in current working directory
    download_path = os.getcwd()+"/data/download_image/"
    img_to_save = Image.open(image_file)
    img_to_save.save(download_path+image_file.name)


if model_file is not None:
    st.write("Loaded: ", model_file.name)
    # Download uploaded model in current working directory
    download_model_path = os.getcwd()+"/data/download_model/"+model_file.name
    model_data = model_file.getvalue()
    model_to_save = open(download_model_path, "wb")
    model_to_save.write(model_data)
    model_to_save.close()

# Perform prediction with pretrained model on uploaded image
if st.button:
    data_loader = load_data(download_path, int(user_batch_size))
    pred_score = score_prediction(data_loader, download_model_path)
    for i in range(len(pred_score)):
        st.write("Result for "+ image_file.name + ": " + str(pred_score[i]))
        st.image(img_to_save)
