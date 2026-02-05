import streamlit as st
from template import init_session_state, page_header, save_message, navigation_hint

def setup_page():
    # Initialize session state
    init_session_state()

    # Page header
    page_header("Interview Setup", "Configure your interview preferences")

    # Dropdown for LLM selection
    llm_choice = st.selectbox(
        "Choose Interview Model (LLM)",
        ["DistilBERT (fast)", "GPT4All (local)", "OpenAI GPT-3.5 (API)", "Cohere"]
    )

    # Text inputs for JD and company
    jd = st.text_area("Paste Job Description (JD)", placeholder="Enter JD here...")
    company = st.text_input("Company Name", placeholder="Enter company name...")

    # Previous interview questions
    prev_questions = st.text_area(
        "Previous Interview Questions (optional)",
        placeholder="Enter past questions, one per line..."
    )

    # Save to session state
    if st.button("Save Setup"):
        st.session_state.llm_choice = llm_choice
        st.session_state.jd = jd
        st.session_state.company = company
        st.session_state.prev_questions = prev_questions.splitlines()

        save_message("Setup saved! You can proceed to the Interview page.")

    # Navigation hint
    navigation_hint()

# Run page
if __name__ == "__main__":
    setup_page()
