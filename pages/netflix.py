import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


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
 v=df.isnull().sum()
 st.write('**Null value**')
 v
 st.write('**Duplicate Value**')
 df.drop_duplicates(inplace=True)
 u=df.duplicated().sum()
 
 u
with st.expander('Data Visualization'):
 st.write('**Data **')
 corr = df.corr()

 st.header('Correlation Heatmap')
 fig, ax = plt.subplots()
 sns.heatmap(corr, annot=True, cmap='coolwarm', cbar=True, ax=ax)
 st.pyplot(fig)

# Pairplot
 st.header('Pairplot')
 pairplot_fig = sns.pairplot(df)
 st.pyplot(pairplot_fig)
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
input_data = np.array([[Open,High,Low,Adj_Close,Volume,year,month,day]])

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
 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)

model = LinearRegression()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

r2 = r2_score(Y_test, Y_pred)

st.write("R-squared (R2):", r2)
st.write(f"Input shape: {input_data.shape}")

# Make the prediction when the user clicks a button
if st.button('Predict'):
    try:
        prediction = model.predict(input_data)
        # Display the prediction
        st.write("Prediction:", prediction)
    except ValueError as e:
        st.error(f"Error during prediction: {e}")



if st.button('R2 score'):
 st.write("R-squared (R2):", r2)


