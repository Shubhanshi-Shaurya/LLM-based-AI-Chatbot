import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("apikey")
genai.configure(api_key=api_key)
 

model = genai.GenerativeModel('gemini-2.5-flash')
 
st.set_page_config(page_title="AI Chatbot", page_icon="♊")
st.title("AI Assistant ")


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])


for message in st.session_state.chat_session.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)
 

if prompt := st.chat_input("Ask anything..."):
    
    with st.chat_message("user"):
        st.markdown(prompt)

    
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        try:
            response = st.session_state.chat_session.send_message(prompt)
            response_placeholder.markdown(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
