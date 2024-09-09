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
 df=pd.read_csv('DatafinitiElectronicsProductsPricingData.csv')
 df
