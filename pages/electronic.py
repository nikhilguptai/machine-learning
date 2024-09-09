import requests
import pandas as pd
import streamlit as st

# Direct download URL
file_id = '1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9'
url = f'https://drive.google.com/uc?export=download&id={file_id}'
output = 'DatafinitiElectronicsProductsPricingData.csv'

try:
    # Download the file
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors

    # Save the file
    with open(output, 'wb') as f:
        f.write(response.content)
    
    st.write("Download completed successfully!")

    # Read the dataset into a DataFrame
    df = pd.read_csv(output)
    df




