import streamlit as st

from utils.session import init_session
from auth import login_user, register_user
from database import init_db
<<<<<<< HEAD
from utils.translator import get_text, init_language

# ======================
# INIT
# ======================
init_session()
=======
from utils.translator import get_text

# ======================
# DATABASE INIT
# ======================
>>>>>>> 7be08339f0b4bb56e9fa86178491f055a22b52b4
init_db()
init_language()

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title=get_text("app_title"),
    page_icon="🎓",
    layout="wide"
)

# ======================
<<<<<<< HEAD
# SIDEBAR LANGUAGE
# ======================
=======
# SESSION STATE
# ======================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
>>>>>>> 7be08339f0b4bb56e9fa86178491f055a22b52b4

# Streamlit controls this automatically
language = st.sidebar.selectbox(
    get_text("language"),
    ["English", "Hindi", "Telugu"],
    key="language"
)

<<<<<<< HEAD
# NOTE:
# No set_language() needed
# Translator reads st.session_state["language"]

# ======================
# SIDEBAR USER INFO
=======
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
>>>>>>> 7be08339f0b4bb56e9fa86178491f055a22b52b4
# ======================
if st.session_state.get("logged_in", False):
    st.sidebar.success(
        f"{get_text('logged_in_as')} {st.session_state.get('username', '')}"
    )

<<<<<<< HEAD
    st.sidebar.info(get_text("sidebar_navigation"))

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
if not st.session_state.get("logged_in", False):

    tab1, tab2 = st.tabs([
        get_text("login"),
        get_text("register")
    ])

    # LOGIN
    with tab1:
        st.subheader(get_text("login"))

        username = st.text_input(get_text("username"), key="login_username")
        password = st.text_input(get_text("password"), type="password", key="login_password")

        if st.button(get_text("login"), key="login_button"):
            success, user = login_user(username, password)

            if success:
                st.session_state.logged_in = True
                st.session_state.username = user[1]
                st.success(get_text("login_success"))
                st.rerun()
            else:
                st.error(get_text(user))

    # REGISTER
    with tab2:
        st.subheader(get_text("register"))

        new_user = st.text_input(get_text("username"), key="register_username")
        new_pass = st.text_input(get_text("password"), type="password", key="register_password")

        if st.button(get_text("register"), key="register_button"):
            success, msg = register_user(new_user, new_pass)

            if success:
                st.success(get_text(msg))
            else:
                st.error(get_text(msg))

else:
=======
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

>>>>>>> 7be08339f0b4bb56e9fa86178491f055a22b52b4
    st.info(get_text("go_to_sidebar"))