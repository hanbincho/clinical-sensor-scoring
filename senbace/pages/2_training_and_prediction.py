import streamlit as st 
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from prediction_and_training import make_prediction
from prediction_and_training import train_model
from PIL import Image


# st.set_page_config(page_title="Training a Model and Performing Predictions")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.sidebar.header("Training and Prediction")

st.markdown("# Upoad files")

# Uploading widgets for needed files
image_file = st.file_uploader("Choose an image file(s)", accept_multiple_files = True)
score_file = st.file_uploader("Choose a scores file", accept_multiple_files = False)

st.markdown("# Hyperparameters")

# Text boxes for hyperparameters
user_batch_size = st.text_input("Batch Size", 1)

# Remaining text boxes for hyperparameters
user_num_epochs = st.text_input("Epochs", 1)
user_lr = st.text_input("Learning Rate", 1e-5)

if image_file is not None:
    # Check that download directory for image exists
    download_image_path = os.getcwd()+"/senbace/uploadedData/images/"
    if not os.path.exists(download_image_path):
        # If not, make it
        os.makedirs(download_image_path)

    st.write("Loaded: ")
    for i in range(len(image_file)):
        st.write(image_file[i].name)
        # Then save the image
        img_to_save = Image.open(image_file[i])
        img_to_save.save(download_image_path+image_file[i].name)

if score_file is not None:
    # Check that download directory for scores file exists
    download_score_path = os.getcwd()+"/senbace/uploadedData/scores/"
    if not os.path.exists(download_score_path):
        # If not, make it
        os.makedirs(download_score_path)

    st.write("Loaded: ", score_file.name)
    # Then save the scores file
    scores_data = pd.read_csv(score_file)
    scores_data.to_csv(download_score_path+score_file.name)
    st.write(scores_data)

# Selection of the type of model to train with
user_model_type = st.radio("Select a model to predict with:", ("AlexNet", "ResNet"))

# Button to start prediction
train_pressed = st.button("Train Model")
    
# When user presses button, create dataloader and start training
if train_pressed:
    training_dataloader = make_prediction.load_data(download_image_path, int(user_batch_size), \
        download_score_path+score_file.name)


    st.write("Data loader was created!")

    # Facing some kind of import issue here...
    train_acc, train_loss = train_model.train_data(int(user_num_epochs), float(user_lr), \
        int(user_batch_size), training_dataloader, user_model_type)
    st.write("Model was trained!")

    st.markdown("# Results of trained model")

    fig, ax = plt.subplots(2, 1, constrained_layout=True)
    ax[0].plot(range(1, len(train_acc)+1), train_acc)
    ax[0].set_title('Training Results')
    ax[0].set_ylabel('Training Accuracy (%)')
    ax[1].plot(range(1, len(train_loss)+1), train_loss)
    ax[1].set_title('Training Loss vs Epoch')
    ax[1].set_xlabel('Epochs')
    ax[1].set_ylabel('Training Loss')

    st.pyplot(fig)
    
    # Also delete the downloaded files/directory
    for i in range(len(image_file)):
        # Delete the downloaded image files
        if os.path.exists(download_image_path+image_file[i].name):
            os.remove(download_image_path+image_file[i].name)
    # Also delete the downloaded model file
        if os.path.exists(download_score_path+score_file.name):
            os.remove(download_score_path+score_file.name)


