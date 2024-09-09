import requests
import pandas as pd
import streamlit as st

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
    
    with st.spinner('Loading data...'):
        # Read the dataset into a DataFrame
        df = pd.read_csv(output)
        st.write("Dataset Preview:")
        df

except requests.exceptions.RequestException as e:
    st.error(f"Request error: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")


