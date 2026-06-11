
import streamlit as st
if "language" not in st.session_state:
    st.session_state["language"] = "English"

st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "Telugu"],
    key="language"
)

from auth import login_user, register_user
from database import init_db

init_db()

st.set_page_config(
    page_title="StudySync AI",
    page_icon="🎓",
    layout="wide"
)

# SESSION STATE
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

st.title("🎓 StudySync AI")
st.caption("Track • Plan • Perform")

# ======================
# AUTH SYSTEM ONLY
# ======================
if not st.session_state.logged_in:

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(username, password)

            if user:
                st.session_state.logged_in = True
                st.session_state.username = user[1]
                st.success("Login successful")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        st.subheader("Register")
        new_user = st.text_input("Username", key="r1")
        new_pass = st.text_input("Password", type="password", key="r2")

        if st.button("Register"):
            register_user(new_user, new_pass)
            st.success("Registered! Please login.")

# ======================
# AFTER LOGIN → JUST ROUTE
# ======================
else:

    st.sidebar.success(f"Logged in as {st.session_state.username}")

    st.sidebar.info("Use sidebar navigation")

    st.sidebar.divider()

    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()

    st.info("👉 Go to sidebar pages to use the app")
import streamlit as st

if "language" not in st.session_state:
    st.session_state.language = "English"

language = st.sidebar.selectbox(
    "Language",
    ["English", "Hindi", "Telugu"]
)

st.session_state.language = language
    