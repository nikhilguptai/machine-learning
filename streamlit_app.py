import streamlit as st
import pandas as pd
 
df=read_csv('https://drive.google.com/file/d/1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9/view?usp=sharing')
df
st.set_page_config(
    page_title="Multi-Page App",
    page_icon=":rocket:",
)


st.title('🤖This is Machine Learning app')


st.info('This app builds machine learning model')
st.info('Please select any one from Sidebar which you want to Predict')
st.markdown("**This app consist Prediction model thats are:-**")
st.write('**Concrete strenght Prediction**')

st.write('**Netflix stock Prediction**')
st.write('**Patient Survival Prediction**')
st.write('**Social Network Ads purchased Prediction**')









  
 
