import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Main",
    page_icon="👋",
)

st.write("# Clinical Sensor Scoring")

st.sidebar.success("Select a page above.")

next = st.button("Next")
if next:
    switch_page("Load_Data")
