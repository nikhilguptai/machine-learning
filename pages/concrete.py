import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


st.title('🤖This is Machine Learning app')

st.info('This app predict concrete strenght')

with st.expander('**Raw data**'):
 df=pd.read_csv('concrete_data.csv')
 df
 v=df.isnull().sum()
 st.write('**Null value**')
 v
 st.write('**Duplicate Value**')
 df.drop_duplicates(inplace=True)
 u=df.duplicated().sum()
 
 u
 st.write('**X**')

 X = df.drop(columns=['concrete_compressive_strength'])

 X
 st.write('**Y**')
 Y = df.concrete_compressive_strength
 Y
with st.expander('Data Visualization'):
 st.write('***Data **')
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
  #cement	blast_furnace_slag	fly_ash	water	superplasticizer	coarse_aggregate	fine_aggregate	age	concrete_compressive_strength
cement = st.text_input("Enter cement:")
blast_furnace_slag = st.text_input("Enter blast_furnace_slag:")
fly_ash = st.text_input("Enter fly_ash:")
water = st.text_input("Enter water:") 
superplasticizer = st.text_input("Enter superplasticizer:")
coarse_aggregate = st.text_input("Enter coarse_aggregate:")
fine_aggregate = st.text_input("Enter fine_aggregate:")
age = st.text_input("Enter age:")
def convert_to_numeric(value):
    try:
        return float(value)
    except ValueError:
        return np.nan  # Handle conversion errors

input_data = np.array([[convert_to_numeric(cement),
                        convert_to_numeric(blast_furnace_slag),
                        convert_to_numeric(fly_ash),
                        convert_to_numeric(water),
                        convert_to_numeric(superplasticizer),
                        convert_to_numeric(coarse_aggregate),
                        convert_to_numeric(fine_aggregate),
                        convert_to_numeric(age)]])
#data frame
data = { 'cement' : cement,
        'blast_furnace_slag' : blast_furnace_slag,
        'fly_ash' : fly_ash,
        'water' : water,
        'superplasticizer' : superplasticizer,
        'coarse_aggregate' : coarse_aggregate,
        'fine_aggregate' : fine_aggregate,
        'age' : age,}

input_df = pd.DataFrame(data, index=[0])
input_strenght = pd.concat([input_df, X], axis=0)
with st.expander('Input features'):
  st.write('**Input data**')
  input_df
  st.write('**Combined  data**')
  input_strenght
 
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

