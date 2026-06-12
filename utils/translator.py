import streamlit as st

from translations.en import LANG as EN
from translations.hi import LANG as HI
from translations.te import LANG as TE

LANGUAGES = {
    "English": EN,
    "Hindi": HI,
    "Telugu": TE
}

def get_text(key):
    lang = st.session_state.get("language", "English")
    return LANGUAGES.get(lang, EN).get(key, key)