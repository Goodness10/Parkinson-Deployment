#!/usr/bin/env python
# coding: utf-8

import pickle
park_model = pickle.load(open('park_model_new.sav', 'rb'))

import streamlit as st
import pandas as pd
import numpy as np
#from prediction import predict

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("bg_image.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

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



#page_bg = '''
#    <style>
#    body {
#    background-image: url("https://www.google.com/url?sa=i&url=https%3A%2F%2Fpubs.rsna.org%2Fdoi%2Ffull%2F10.1148%2Fradiol.2021203341&psig=AOvVaw0EDJJs4Gs8rPHz9AgCM6aB&ust=1677848793654000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCICsrvynvf0CFQAAAAAdAAAAABAE.jpg")
#    background-size: cover;
 #   }
  #  </style>
   # '''
# st.markdown(page_bg, unsafe_allow_html=True)
