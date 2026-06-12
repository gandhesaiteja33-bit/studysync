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
    # get selected language safely
    lang = st.session_state.get("language", "English")

    # get language dictionary, fallback to English
    lang_dict = LANGUAGES.get(lang, EN)

    # get translated value
    value = lang_dict.get(key)

    # fallback chain (VERY IMPORTANT)
    if value is None:
        value = EN.get(key)

    if value is None:
        value = key  # last fallback

    return value