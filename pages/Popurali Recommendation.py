import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os
os.system('pip install gdown')
import gdown



file_id = '1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9'

# Google Drive download link
url = f'https://drive.google.com/uc?id={file_id}'

# Output file path
output = 'DatafinitiElectronicsProductsPricingData.csv'

# Download the dataset from Google Drive
gdown.download(url, output, quiet=False)

# Load the dataset into a pandas DataFrame
movies = pd.read_csv(output)

