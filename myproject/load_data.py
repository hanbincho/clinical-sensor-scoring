from streamlit_extras.switch_page_button import switch_page
import streamlit as st 
import pandas as pd
import numpy as np

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
    loca_option = st.selectbox(
       "Specify Location",
       ("Location 1", "Location 2", "Location 3"),
    )
    model_option = st.selectbox(
       "Select Model",
       ('Model 1', 'Model 2', 'Upload a model'),
    )
    if (model_option == 'Upload a model'):
       upload_model = st.file_uploader("Choose a file")
    if (patient_input and loca_option and model_option):
       if st.button("Analyze"):
          with col2:
              st.write("Plots will be here")

next = st.button("Next")
if next:
    switch_page("Plot")
