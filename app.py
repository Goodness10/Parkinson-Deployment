#!/usr/bin/env python
# coding: utf-8

import pickle
park_model = pickle.load(open('park_model_new.sav', 'rb'))


import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict

st.title("Classifying Parkinson")
st.markdown("To model to check whether a patient has parkinson parkinson")

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
#with col5:
   # MDVP:Jitter(Abs) = st.text_input('MDVP:Jitter(Abs)')
#with col1:
   # MDVP:APQ  = st.text_input('MDVP:APQ')
#with col2:
 #   MDVP:Flo(Hz) = st.text_input('MDVP:Flo(Hz)')
#with col3:
#    MDVP:Fhi(Hz) = st.text_input('MDVP:Fhi(Hz)')
#with col4:
 #   Shimmer:APQ5 = st.text_input('Shimmer:APQ5')
#with col5:
#    MDVP:Fo(Hz) = st.text_input('MDVP:Fo(Hz)')



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
