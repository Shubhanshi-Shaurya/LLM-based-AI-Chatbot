# AI Chatbot using LLM 

A real-time, conversational AI chatbot built with **Python**, **Google Gemini 2.5 Flash**, and **Streamlit**. This project demonstrates the integration of Large Language Models (LLMs) into a functional web application with session-based memory.

---

##  Features
- **API Integeration:** Integrated Pretrained LLM model using API Requests .
- **Generative AI Responses:** Powered by the Google Gemini 2.5 Flash model for fast and accurate completions.
- **Context Awareness:** Maintains conversation history within a session using `st.session_state`.
- **Modern UI/UX:** Clean user interface using Streamlit’s native chat components.
- **Security Best Practices:** Implements sensitive data handling using `st.secrets` to keep API keys secure.

---

##  Tech Stack
- **Language:** Python 
- **AI Model:** Google Gemini 2.5 Flash
- **Framework:** Streamlit
- **Environment Management:** Virtualenv, TOML Secrets

---

##  Project Structure
```text
chatbot/
├── .env      
├── venv/                 
├── app.py               
├── requirements.txt  
├──.gitignore    
└── README.md    
         
```

---

##  Future Enhancements 
- **Context-Based Chatbot:** Remember Conversation .
- **Domain Chatbot:** Specialized in specific Industry , Example-HR Chatbot/Finance Chatbot etc.
- **PDF Chatbot:** Upload PDF and ask questions .

