import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_extras.switch_page_button import switch_page

arr = np.random.normal(1, 1 , size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)
st.set_page_config(page_title="Plot")
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

st.markdown("# Plot")
st.sidebar.header("Load Plot")
col1, col2 = st.columns([4, 4])
prev = st.button("prev")
next = st.button("Next")
if next:
    switch_page("Fma")
if prev:
    switch_page("load data")
with col1:
    st.header('Healthy')
    st.pyplot(fig)


with col2:
    st.header('Stroke')
    st.pyplot(fig)
