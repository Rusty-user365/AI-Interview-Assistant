import streamlit as st

def init_session_state():
    """
    Initialize session state variables if they don't exist yet.
    This ensures all pages can safely access them.
    """
    defaults = {
        "llm_choice": None,
        "jd": "",
        "company": "",
        "prev_questions": [],
        "answers": {},
        "coding_submission": "",
        "analytics": {}
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

def page_header(title: str, subtitle: str = ""):
    """
    Render a consistent header across all pages.
    """
    st.title(title)
    if subtitle:
        st.caption(subtitle)

def save_message(msg: str):
    """
    Display a success message after saving data.
    """
    st.success(msg)

def navigation_hint():
    """
    Show navigation instructions for users.
    """
    st.info("Use the sidebar to navigate between Setup, Interview, Coding, and Dashboard pages.")
