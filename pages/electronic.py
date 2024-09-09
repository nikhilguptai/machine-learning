import gdown
import pandas as pd
import streamlit as st

# Direct download URL
url = 'https://drive.google.com/file/d/1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9/view?usp=sharing'
output = 'DatafinitiElectronicsProductsPricingData.csv'

try:
    # Download the file
    gdown.download(url, output, quiet=False)
    st.success("Download completed successfully!")

    # Read the dataset into a DataFrame
    df = pd.read_csv(output)
    st.write("Dataset Preview:")
    st.write(df.head())

except Exception as e:
    st.error(f"An error occurred: {e}")


