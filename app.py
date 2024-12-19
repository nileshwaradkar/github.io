from langchain_openai.chat_models.base import ChatOpenAI
from langchain_ollama.chat_models import ChatOllama
import streamlit as st

#llm = ChatOllama(model="llama3.1")

llm = ChatOpenAI(
     model="gemini-1.5-flash",
     base_url="https://generativelanguage.googleapis.com/v1beta/",
     api_key="AIzaSyBDvIJBakJMwV037cnabC2n3dXdEBzFoj4"
 )

st.title("Chatbot")

if "model" not in st.session_state:
    st.session_state.model = "gemini-1.5-flash"
    
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=":material/person:" if message["role"] == "human" else "ai"):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter your message: "):
    st.session_state.messages.append({"role": "human", "content": prompt})
    with st.chat_message("human",avatar=":material/person:"):
        st.markdown((prompt))
        
    with st.chat_message("ai"):
        response = llm.invoke(prompt).content
        st.markdown(response)
        
    
    st.session_state.messages.append({"role": "ai", "content": response})

