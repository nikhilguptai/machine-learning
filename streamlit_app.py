import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
 X = df.filter(items=[col for col in df.columns if col not in ['Date', 'Close']])
 X
 st.write('**Y**')
 Y = df.Close
 Y
with st.expander('Data Visualization'):
 st.write('***Data **')
 corr = df.corr()
 sns.heatmap(corr,annot=True,cmap='coolwarm',cbar=True)
 sns.pairplot(df)
 for i in df.columns:
  plt.figure(figsize=(10,6))
  sns.distplot(df[i])
  plt.title(i)
  st.pyplot(plt)
Open = st.text_input("Enter Open:")
High = st.text_input("Enter High:")
Low = st.text_input("Enter Low:")
Adj_Close = st.text_input("Enter Adj_Close:") 
Volume = st.text_input("Enter Volume:")
year = st.text_input("Enter year:")
month = st.text_input("Enter month:")
day = st.text_input("Enter Day:")

#data frame
data = { 'Open' : Open,
        'High' : High,
        'Low' : Low,
        'Adj_Close' : Adj_Close,
        'Volume' : Volume,
        'year' : year,
        'month' : month,
        'day' : day,}
input_df = pd.DataFrame(data, index=[0])
input_stocks = pd.concat([input_df, X], axis=0)
with st.expander('Input features'):
  st.write('**Input data**')
  input_df
  st.write('**Combined stocks data**')
  input_stocks







  
 
