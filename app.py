#!/usr/bin/env python
# coding: utf-8

import pickle
park_model = pickle.load(open('park_model_new.sav', 'rb'))

import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://cdn.pixabay.com/photo/2016/11/29/05/45/astronomy-1867616_960_720.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url()

# Define the CSS styling
style = """
<style>
div.stInput > div.stTextArea > div[role="textbox"] {
    background-color: #F0F0F0;
}
</style>
"""

# Render the styling
st.markdown(style, unsafe_allow_html=True)

# Create an input box
text_input = st.text_input("Enter some text:")

    
st.title("Classifying Parkinson")
st.markdown("Check your parkinson disease status")

#getting input from the user
col1, col2 = st.columns(2)

with col1:
    PPE = st.text_input('PPE')
with col2:
    spread1 = st.text_input('Spread1')
with col1:
    HNR = st.text_input('HNR')
with col2:
    spread2 = st.text_input('Spread2')

# code for Prediction
park_diagnosis = ''
    
# creating a button for Prediction
if st.button('Parkinson Test Result'):
    park_prediction = park_model.predict([PPE, spread1, spread2, HNR]) 
#MDVP:Jitter(Abs), MDVP:Fo(Hz), spread2, MDVP:APQ , MDVP:Flo(Hz), MDVP:Fhi(Hz), HNR , Shimmer:APQ5])
    if (park_prediction == 1):
        park_diagnosis = 'You have parkinson'
    else:
        park_diagnosis = 'You do not have parkinson'
        
st.success(park_diagnosis)
