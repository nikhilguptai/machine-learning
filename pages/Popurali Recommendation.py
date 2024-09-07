import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
movies = pd.read_csv('tmdb_5000_movies.csv')
movies = movies[['title','overview','popularity','vote_count']]
movies

