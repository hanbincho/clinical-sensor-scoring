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
    image_file = st.file_uploader("Choose an image file")
    model_file = st.file_uploader("Choose a model file")
    user_batch_size = st.text_input("Batch Size", 1)

    option_train = st.checkbox('Train')
    option_test = st.checkbox('Test')
    option_both = st.checkbox('Both')

with col2:
    text_out = st.text_area("Feedback: ", "Temporary text for now...")

st.write("Current directory: ", os.getcwd())

if image_file is not None:
    st.write(image_file.name)
    # Create a directory and save image file 
    # image_path = os.getcwd()+'/data/download_image/'
    image_path = os.getcwd()+"/data/image/"
    st.write(image_path)
    # Create download directory and save the image
    download_path = os.getcwd()+"/data/download_image/"
    img_to_save = Image.open(image_file)
    img_to_save.save(download_path+image_file.name)


if model_file is not None:
    st.write(model_file.name)
    # model_path = os.getcwd()+'/data/download_model/'+model_file.name
    model_path = os.getcwd()+'/data/model/'+model_file.name
    st.write(model_path)
    download_model_path = os.getcwd()+"/data/download_model/"+model_file.name
    model_data = model_file.getvalue()
    model_to_save = open(download_model_path, "wb")
    model_to_save.write(model_data)
    model_to_save.close()

if option_test:
    data_loader = load_data(download_path, int(user_batch_size))
    pred_score = score_prediction(data_loader, download_model_path)
    for i in range(len(pred_score)):
        st.write("Result for "+ image_file.name + ": " + str(pred_score[i]))
