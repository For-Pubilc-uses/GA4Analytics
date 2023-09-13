import streamlit as st
# Page confi & style
st.set_page_config(
    page_title="GA4 Analysis Platform",
    page_icon="🤔",
    initial_sidebar_state ='expanded',
    layout="wide"
)

with open('style.css') as style_sheet:
    st. markdown(f"<style>{style_sheet.read()}</style>",unsafe_allow_html=True)
   
st.markdown(""" 
    <style>
        .css-10pw50.egzxvld1{
        
            visibility: hidden;
        }
        #MainMenu > button > svg
        {
            visibility: hidden;
        }
    </style>
            
""",unsafe_allow_html=True)
