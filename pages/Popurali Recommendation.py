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




url = 'https://drive.google.com/file/d/1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9/view?usp=sharing'


movies = pd.read_csv(url)

