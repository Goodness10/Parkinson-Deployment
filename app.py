#!/usr/bin/env python
# coding: utf-8

import pickle
park_model = pickle.load(open('park_model_new.sav', 'rb'))

import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict

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

def set_background_image(image):
    page_bg = '''
    <style>
    body {
    background-image: url("'''+image+'''");
    background-size: cover;
    }
    </style>
    '''
    st.markdown(page_bg, unsafe_allow_html=True)
# Set the background image
set_background_image("https://www.google.com/url?sa=i&url=https%3A%2F%2Fradiologykey.com%2Fstructural-mri-in-idiopathic-parkinson-disease-and-parkinsonism%2F&psig=AOvVaw2i0TCJ2s9VHHUq9rLkKrfH&ust=1677847039633000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKig_rehvf0CFQAAAAAdAAAAABAJ.png");
