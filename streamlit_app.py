import streamlit as st
import pandas as pd

st.title('🤖This is Machine Learning app')

st.info('This app builds machine learning model')
with st.expander('**Raw data**'):
 df=pd.read_csv('NFLX.csv')
 df
 st.write('**X**')
 df['Date'] = pd.to_datetime(df['Date'])
 df['year'] = df['Date'].dt.year
 df['month'] = df['Date'].dt.month
 df['day'] = df['Date'].dt.day
 Xx=df.drop('Date',axis=1,inplace=True)
 X=Xx.drop('Close',axis=1)
