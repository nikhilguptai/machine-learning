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
import gdown

# URL for direct download
url = 'https://drive.google.com/uc?export=download&id=1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9'

# File name for saving
output = 'DatafinitiElectronicsProductsPricingData.csv'

# Download the file
gdown.download(url, output, quiet=False)


with st.expander('**Raw data**'):
 df=pd.read_csv('DatafinitiElectronicsProductsPricingData.csv')
 df
