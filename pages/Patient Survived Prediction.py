import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

st.title('🤖This is Machine Learning app')

st.info('This app is for patient Survival prediction')
df = pd.read_csv('haberman.csv',header=None, names=['age','operational_year','exil_node','survival'])
v=df.isnull().sum()

df.drop_duplicates(inplace=True)
u=df.duplicated().sum()
M = df
X = df.drop("survival",axis=1)
y = df['survival']
with st.expander('**Raw data**'):
  M
  st.write('**X**')
  X
  st.write('**Y**')
  y
  st.write('**Null value**')
  v
  st.write('**Duplicate Value**')
  u
with st.expander('**Data Visualization**'):
  st.write('**Data Visualization**')
  corr = df.corr()
  st.subheader('Correlation Heatmap')
  fig, ax = plt.subplots()
  sns.heatmap(corr, annot=True, cbar=True, cmap='plasma', ax=ax)
  st.pyplot(fig)
  
  # Distribution plot
  st.subheader('Distribution of Operational Year')
  fig, ax = plt.subplots()
  sns.histplot(df['operational_year'], kde=True, ax=ax)
  st.pyplot(fig)

  # Histogram of age
  st.subheader('Histogram of Age')
  fig, ax = plt.subplots()
  sns.histplot(df['age'], kde=False, ax=ax)
  st.pyplot(fig)

  st.subheader('Age vs operational_year  Scatter Plot')
  fig, ax = plt.subplots()
  sns.scatterplot(x=df['age'], y=df['operational_year'], ax=ax)
  st.pyplot(fig)
  # Scatter plot
  st.subheader('Age vs Survival Scatter Plot')
  fig, ax = plt.subplots()
  sns.scatterplot(x=df['age'], y=df['survival'], ax=ax)
  st.pyplot(fig)

age = st.number_input("Age", min_value=1, max_value=120, value=30)
operational_year = st.number_input("Operational Year", min_value=1900, max_value=2024, value=1960)
exil_node = st.number_input("Number of Exil Nodes", min_value=0, max_value=50, value=1)

input_data = np.array([[age,operational_year,exil_node]])

#data frame
data = { 'age' : age,
         'operational_year' : operational_year,
          'exil_node' : exil_node, }

input_df = pd.DataFrame(data, index=[0])
input_survival = pd.concat([input_df, X], axis=0)
with st.expander('Input features'):
  st.write('**Input data**')
  input_df
  st.write('**Combined stocks data**')
  input_survival
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
sclr = StandardScaler()
sclr.fit(X_train)
X_train = sclr.transform(X_train)
X_test = sclr.transform(X_test)
dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
dtc.predict(X_test)


def predict_survival(input_data):
    input_scaled = sclr.transform(input_data)  # Scale the input data
    prediction = dtc.predict(input_scaled)  # Predict survival
    return prediction[0]

# Button to make the prediction
if st.button('Predict'):
    result = predict_survival(input_data)
    if result == 1:
        st.success("The model predicts that the patient will survive.")
    else:
        st.error("The model predicts that the patient will not survive.")
