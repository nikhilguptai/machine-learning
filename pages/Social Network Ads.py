import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

st.title('🤖This is Machine Learning app')

st.info('This app Social Network Ads Sales')

with st.expander('**Raw data**'):
 df=pd.read_csv('Social_Network_Ads.csv')
 df
 st.write('**X**')

 X = df.filter(items=[col for col in df.columns if col not in ['User ID','Purchased']])
 X['Gender'] = df['Gender'].map({'Male':1,'Female':0})
 X
 st.write('**Y**')
 Y = df.Purchased
 Y
with st.expander('Data Visualization'):
 st.write('***Data **')
 corr = X.corr()
 sns.heatmap(corr,annot=True,cmap='coolwarm',cbar=True)
 sns.pairplot(df)
 for i in X.columns:
  plt.figure(figsize=(10,6))
  sns.distplot(X[i])
  plt.title(i)
  st.pyplot(plt)
  #Gender	Age	EstimatedSalary
Gender = st.selectbox("Gender", options=[0, 1])
age = st.number_input("Age", min_value=0, max_value=120, value=25)
EstimatedSalary= st.text_input("Enter EstimatedSalary:")
input_data = np.array([[Gender,age,EstimatedSalary]])

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

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=2)
X_train = np.asarray(X_train)
Y_train = np.asarray(Y_train)



scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)


rfc = RandomForestClassifier()
rfc.fit(X_train,Y_train)
Y_pred = rfc.predict(X_test)
accuracy_score(Y_test,Y_pred)
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
