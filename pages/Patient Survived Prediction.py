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

st.info('This app Social Network Ads Sales')
df = pd.read_csv('haberman.csv',header=None, names=['age','operational_year','exil_node','survival'])
M = df
df.drop_duplicates(inplace=True)
X = df.drop("survival",axis=1)
y = df['survival']
with st.expander('**Raw data**'):
  M
  st.write('**X**')
  X
  st.write('**Y**')
  y
with st.expander('**Data**'):
  st.write('**'Data Visualization**')
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
  
  # Scatter plot
  st.subheader('Age vs Survival Scatter Plot')
  fig, ax = plt.subplots()
  sns.scatterplot(x=df['age'], y=df['survival'], ax=ax)
  st.pyplot(fig)
  




X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)


sclr = StandardScaler()
sclr.fit(X_train)
X_train = sclr.transform(X_train)
X_test = sclr.transform(X_test)

dtc = DecisionTreeClassifier()
dtc.fit(X_train,y_train)
dtc.predict(X_test)


def pred(age,oy,en):
    features = np.array([[age,oy,en]])
    features = sclr.fit_transform(features)
    pred = dtc.predict(features).reshape(1,-1)
    return pred[0]


age = 50
oy = 61
en = 2

res = pred(age,oy,en)
