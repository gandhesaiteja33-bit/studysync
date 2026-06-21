import streamlit as st
<<<<<<< HEAD

from utils.session import init_session
from utils.translator import get_text as _
from ai.local_ai import local_ai
from ai.cloud_ai import cloud_ai

# ======================
# INIT SESSION
# ======================
init_session()

# ======================
# TITLE
# ======================
st.title(_("chat_title") or "🤖 AI Chat Feature")

# ======================
# AI MODE
# ======================
mode = st.radio(
    _("choose_ai_mode") or "Choose AI Mode",
    ["Local AI (Ollama)", "Cloud AI"]
)

# ======================
# INPUT
# ======================
user_input = st.text_input(_("ask_something") or "Ask something")

# ======================
# SEND BUTTON
# ======================
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
=======
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
>>>>>>> 7be08339f0b4bb56e9fa86178491f055a22b52b4
