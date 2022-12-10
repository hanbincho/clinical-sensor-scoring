import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="SenBaCE Landing Page",
    page_icon="👋",
)

st.title('Sensor Based Clinical Evaluations (SenBaCE)')
st.caption('By: Dell Teng, HAnbin Cho,  Prathiba Ramachandran, SangYoon Back, Uzo Uwaoma')

st.markdown(""" **Project Goal**: Currently, there are standard clinical practices where trained physicians visually assess motor 
    impairments of patients. Based off these visual assessments, these physicians assign  
    scores which describes the severity of patients' impairments. To minimize possible biases or
    inconsistencies between assessments, sensor data can be utilized as a more robust and consistent
    means to characterize motor behaviors. However, the outputs of sensor data are not clinically meaningful
    and somewhat difficult to understand without additional filtering and processing.
    By utilizing a publicly available dataset that has collected sensor data and the corresponding clinical
    evaluation scores (U-Limb), and machine learning model techniques, SenBaCE aims to bridge this gap and
    demonstrate a potentially more robust alternative to clinically characterizing motor impairments""")


st.sidebar.success("Select a page above.")

next = st.button("Next")
if next:
    switch_page("Load_Data")
