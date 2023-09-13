import streamlit as st
import pandas as pd
from utility import *
from pageConfiguration import *

st.title("Langchain :violet[Pandas]")

uploaded_file = st.file_uploader("Choose a :violet[**CSV file**]", type="csv")

if uploaded_file is not None:
    col1,col2 = st.columns([1.4,1])

    with col1:
        st.info("CSV Uploaded successfully!! 🥳")
        df = pd.read_csv(uploaded_file)
        st.dataframe(df)

    with col2:
        st.info("Chat with dataframe")
        input_text = st.text_area("Enter your query")
        if input_text is not None:
            if st.button('Send'):
                st.info("Your question: " +  input_text)
                with st.spinner('Wait for it...'):
                    result = askBot(df,input_text)
                    st.info(f':violet[{result}]')


