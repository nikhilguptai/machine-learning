import requests
import pandas as pd
import streamlit as st
import io

# Direct download URL
file_id = '1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9'
url = f'https://drive.google.com/uc?export=download&id={file_id}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Check if request was successful

    if 'content-disposition' in response.headers:
        content_disposition = response.headers['content-disposition']
        filename = content_disposition.split('filename=')[1].strip('"')
    else:
        filename = 'DatafinitiElectronicsProductsPricingData.csv'

    df = pd.read_csv(io.StringIO(response.text))
    st.write("Dataset Preview:")
    st.write(df.head())
except requests.exceptions.RequestException as e:
    st.error(f"Request error: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")
