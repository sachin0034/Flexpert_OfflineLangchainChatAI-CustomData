import streamlit as st
from chatbot import get_response


# Initialize session state for conversation history
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I assist you today?"}
    ]

# Streamlit application
st.title("Flexpert Chatbot")

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("You: "):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from the bot
    response = get_response(prompt)
    # Display bot response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
