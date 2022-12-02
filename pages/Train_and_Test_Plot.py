import streamlit as st 
import pandas as pd
import numpy as np

st.set_page_config(page_title="Train and Test Plot")
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

