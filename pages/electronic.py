import requests
import pandas as pd
import streamlit as st
import os

# Direct download URL
file_id = '1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9'
url = f'https://drive.google.com/uc?export=download&id={file_id}'
output = 'DatafinitiElectronicsProductsPricingData.csv'

try:
    with st.spinner('Downloading file...'):
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful

        with open(output, 'wb') as f:
            f.write(response.content)
    
    st.success("Download completed successfully!")
    
    # Check if file exists and is not empty
    if os.path.exists(output):
        with open(output, 'r') as file:
            content = file.read()
            st.write("File content preview:")
            st.write(content[:500])  # Show the first 500 characters
    
    # Load and display the dataset
    try:
        with st.spinner('Loading data...'):
            df = pd.read_csv(output)
            if df.empty:
                st.warning("The DataFrame is empty.")
            else:
                st.write("Dataset Preview:")
                st.write(df.head())
    except Exception as e:
        st.error(f"An error occurred while loading the DataFrame: {e}")

except requests.exceptions.RequestException as e:
    st.error(f"Request error: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")
