from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
import pandas as pd
import streamlit as st

# Setup Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'path/to/service_account.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)

# File ID of the Google Drive file
FILE_ID = '1T8v5XIHM4Tsq-18MJsTYWBmmvg18-pR9'
request = service.files().get_media(fileId=FILE_ID)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)

done = False
while done is False:
    status, done = downloader.next_chunk()
    st.write(f"Download {int(status.progress() * 100)}%.")

fh.seek(0)
df = pd.read_csv(fh)
st.write("Dataset Preview:")
st.write(df.head())
