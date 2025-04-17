import streamlit as st
import random
import time

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set page config
st.set_page_config(layout="wide")

# Title
st.title("🤖 AI Chatbot")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simulate AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulate typing effect
        responses = [
            "I understand your question. Let me help you with that.",
            "That's an interesting query. Here's what I know about it.",
            "I can help you with that. Here's the information you need.",
            "Let me provide you with a detailed answer.",
            "I'll help you understand this better."
        ]
        
        response = random.choice(responses)
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Add a sidebar with information
with st.sidebar:
    st.header("About the Chatbot")
    st.write("""
    This is a demo chatbot that can help you with:
    - General questions
    - Information about our services
    - Basic troubleshooting
    - Product recommendations
    """)
    
    # Add a clear chat button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()