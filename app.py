from utils.session import init_session

init_session()
import streamlit as st

from auth import login_user, register_user
from database import init_db
from utils.translator import get_text

# ======================
# DATABASE INIT
# ======================
init_db()

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="StudySync AI",
    page_icon="🎓",
    layout="wide"
)

# ======================
# SESSION STATE
# ======================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "language" not in st.session_state:
    st.session_state.language = "English"

# ======================
# SIDEBAR (FIXED)
# ======================

# ❗ Language selector MUST NOT use get_text()
st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "Telugu"],
    key="language"
)

# Sidebar content (reactive)
if st.session_state.logged_in:

    st.sidebar.success(
        f"{get_text('logged_in_as')} {st.session_state.username}"
    )

    st.sidebar.info(get_text("sidebar_navigation"))

    st.sidebar.divider()

    if st.sidebar.button(get_text("logout"), key="logout_button"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

# ======================
# HEADER
# ======================
st.title(get_text("app_title"))
st.caption(get_text("app_caption"))

# ======================
# AUTH SYSTEM
# ======================
if not st.session_state.logged_in:

    tab1, tab2 = st.tabs([
        get_text("login"),
        get_text("register")
    ])

    # ----------------------
    # LOGIN TAB
    # ----------------------
    with tab1:

        st.subheader(get_text("login"))

        username = st.text_input(
            get_text("username"),
            key="login_username"
        )

        password = st.text_input(
            get_text("password"),
            type="password",
            key="login_password"
        )

        if st.button(get_text("login"), key="login_button"):

            user = login_user(username, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.username = user[1]

                st.success(get_text("login_success"))
                st.rerun()

            else:
                st.error(get_text("invalid_credentials"))

    # ----------------------
    # REGISTER TAB
    # ----------------------
    with tab2:

        st.subheader(get_text("register"))

        new_user = st.text_input(
            get_text("username"),
            key="register_username"
        )

        new_pass = st.text_input(
            get_text("password"),
            type="password",
            key="register_password"
        )

        if st.button(get_text("register"), key="register_button"):

            register_user(new_user, new_pass)

            st.success(get_text("registered_success"))

else:

    st.info(get_text("go_to_sidebar"))