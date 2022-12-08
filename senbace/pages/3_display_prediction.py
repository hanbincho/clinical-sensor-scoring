import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Display Prediction")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("# Train and Test Plot")
st.sidebar.header("Train and Test Plot")
col1, col2 = st.columns([4, 1])

with col1:
    st.header('Plot')

with col2:
    option_train = st.checkbox('Train')
    option_test = st.checkbox('Test')
    option_both = st.checkbox('Both')

override = st.button("Update Score")
if override:
    st.write("override the score")

feedback = st.text_area('Feedback here')
st.write('your feedback:', feedback)
prediction_page = st.radio('choose a prediction page', ('pretrained prediction', 'training and prediction'))
prev = st.button("previous Page")
next = st.button("next page")
if prev:
    switch_page("show training plot")
if prediction_page == 'pretrained prediction':
    next_page = "pretrained prediction"
if prediction_page == 'training and prediction':
    next_page = "training and prediction"
if next:
    switch_page(next_page)

