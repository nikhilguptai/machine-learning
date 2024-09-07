import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

st.title('🤖This is Machine Learning app')

st.info('This app Social Network Ads Sales')

with st.expander('**Raw data**'):
 df=pd.read_csv('Social_Network_Ads.csv')
 df
 st.write('**X**')

 X = df.filter(items=[col for col in df.columns if col not in ['User ID','Purchased']])
 df['Gender'] = df['Gender'].map({'Male':1,'Female':0})
 X
 st.write('**Y**')
 Y = df.Purchased
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
  #Gender	Age	EstimatedSalary
Gender = st.text_input("Enter 1 for male and 0 for female:")
age = st.text_input("Enter age:")
EstimatedSalary= st.text_input("Enter EstimatedSalary:")
input_data = np.array([[float(Gender), float(age), float(EstimatedSalary)]])

#data frame
data = { 'Gender' : Gender,
        'age' : age,
'EstimatedSalary' : EstimatedSalary, }

input_df = pd.DataFrame(data, index=[0])
input_purchased = pd.concat([input_df, X], axis=0)
with st.expander('Input features'):
  st.write('**Input data**')
  input_df
  st.write('**Combined stocks data**')
  input_purchased
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=2)
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
scalar.fit(X_train)
X_train = scalar.transform(X_train)
X_test = scalar.transform(X_test)
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train,y_train)
y_pred = rfc.predict(X_test)
accuracy_score(y_test,y_pred)
input_np_text = np.asarray(input_df)
def check_purchase(predicion):
    if predicion == 1:
        return "Purchased"
    else:
        return "Not purchased"

if st.button('Predict'):
    predicion = rfc.predict(input_np_text.reshape(1,-1))
    result = check_purchase(predicion)
    st.write(result)
