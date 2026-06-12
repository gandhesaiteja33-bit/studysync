from utils.session import init_session

init_session()
import streamlit as st
from ai.local_ai import local_ai
from ai.cloud_ai import cloud_ai

st.title("🤖 AI Chat Feature")

mode = st.radio(
    "Choose AI Mode",
    ["Local AI (Ollama)", "Cloud AI"]
)

user_input = st.text_input("Ask something")

if st.button("Send"):

    if not user_input:
        st.warning("Please enter a question")

    elif mode == "Local AI (Ollama)":
        result = local_ai(user_input)
        st.write(result)

    else:
        result = cloud_ai(user_input)
        st.write(result)