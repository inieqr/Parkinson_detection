# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 01:57:14 2022

@author: Anon
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

    
def main():
    
    
    # giving a title
    st.title("Early Detection of Parkinson's Disease")
    
    
    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
      F0 = st.text_input('Average vocal fundamental frequency')
    with col2:
      Fhi = st.text_input('Maximum vocal fundamental frequency')
    with col3:
      Flo = st.text_input('Minimum vocal fundamental frequency')
    with col4:
      Jitter = st.text_input('Jitter ')
    with col1:
      Jitter_Abs = st.text_input('Absolute jitter ')
    with col2:
      RAP = st.text_input('Relative amplitude perturbation')
    with col3:
      PPQ = st.text_input('Five-point period perturbation quotient')
    with col4:
      DDP = st.text_input('Average absolute difference of differences between jitter cycles')
    with col1:
      Shimmer = st.text_input('Local Shimmer')
    with col2:
      Shimmer_dB = st.text_input('Local Shimmer in decibels')
    with col3:
      Shimmer_APQ3 = st.text_input('Three-point amplitude perturbation quotient')
    with col4:
      Shimmer_APQ5 = st.text_input('Five-point amplitude perturbation quotient')
    with col1:
      APQ = st.text_input('11-point amplitude perturbation quotient')
    with col2:
      Shimmer_DDA = st.text_input('Average absolute differences between the amplitudes of consecutive periods')
    with col3:
      NHR = st.text_input('Noise-to-harmonics ratio')
    with col4:
      HNR = st.text_input('Harmonics-to-noise ratio')

    

    # code for Prediction
    parkinson_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Detection Result'):
        parkinson_prediction = loaded_model.predict([[F0, Fhi, Flo, Jitter, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, APQ, Shimmer_DDA, NHR, HNR]])
        
        if (parkinson_prediction[0] == 0):
          parkinson_diagnosis = 'This person does not have Parkinsons Disease'
        else:
          parkinson_diagnosis = 'This person has Parkinsons'

      
    st.success(parkinson_diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    