import streamlit as st
col1,col2 = st.columns(2)


with col1:
  
    data = st.file_uploader("Upload the file here")
with col2:
   
    prompt = st.chat_input("Enter the prompt")