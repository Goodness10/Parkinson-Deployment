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

page_bg_img = '''
<style>
body {
background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.journalofparkinsonsdisease.com%2Fclinical-application-brain-mri-diagnostic-work-parkinsonism&psig=AOvVaw1UHvpe6DbXIaAxt2WhYBrx&ust=1677845464542000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCPCFgsmbvf0CFQAAAAAdAAAAABAE");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


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
