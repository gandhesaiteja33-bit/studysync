import streamlit as st


def init_session():
    if "language" not in st.session_state:
        st.session_state.language = "English"

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "username" not in st.session_state:
        st.session_state.username = ""
