"""This python script creates the main page of Sensor Based Clinical Evaluation
It also creates a sidebar and a button for navigation across different pages.
"""
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="SenBaCE Landing Page",
    page_icon="👋",
)

st.title('Sensor Based Clinical Evaluations (SenBaCE)')
st.caption('By: Dell Teng, Hanbin Cho,  Prathiba Ramachandran, SangYoon Back, Uzo Uwaoma')

st.markdown(""" **Project Goal**: To minimize inconsistensies and bias in clinician-assigned
    scores based of data from EMG & kinematic sensors for assessing motor skills/impairments of patients.
    """)

st.sidebar.success("Select a page above.")

next_page = st.button("Next")
if next_page:
    switch_page("Load_Data")
