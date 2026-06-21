import streamlit as st

from ai.cloud_ai import cloud_ai
from ai.local_ai import local_ai
from utils.session import init_session
from utils.translator import get_text as _

# Initialize session
init_session()

st.title(_("chat_title") or "🤖 AI Chat Feature")

mode = st.radio(
    _("choose_ai_mode") or "Choose AI Mode", ["Local AI (Ollama)", "Cloud AI"]
)

user_input = st.text_input(_("ask_something") or "Ask something")

if st.button(_("send") or "Send"):
    if not user_input:
        st.warning(_("enter_question") or "Please enter a question")

    else:
        with st.spinner(_("processing") or "Thinking..."):
            if mode == "Local AI (Ollama)":
                result = local_ai(user_input)
            else:
                result = cloud_ai(user_input)

            st.success(result)
