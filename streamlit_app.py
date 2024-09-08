import streamlit as st


st.set_page_config(
    page_title="Multi-Page App",
    page_icon=":rocket:",
)
st.title('🤖This is Machine Learning app')
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f0f5;  /* Light gray background */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.info('This app builds machine learning model')
st.info('Please select any one from Sidebar which you want to Predict')
st.markdown("**This app consist Prediction model thats are:-**")
st.write('**Concrete strenght Prediction**')

st.write('**Netflix stock Prediction**')
st.write('**Patient Survival Prediction**')
st.write('**Social Network Ads purchased Prediction**')









  
 
