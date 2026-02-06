import streamlit as st
import sqlite3
from template import init_session_state, page_header, save_message, navigation_hint

DB_PATH = "data/interview_logs.db"

def get_user_interviews(user_id: int):
    """Fetch previous interviews for a given user."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, jd, company, questions FROM interviews WHERE user_id=?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def save_interview(user_id: int, jd: str, company: str, questions: str):
    """Save a new interview record for the user."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO interviews(user_id, jd, company, questions, answers) VALUES (?, ?, ?, ?, ?)",
        (user_id, jd, company, questions, "")
    )
    conn.commit()
    conn.close()

def setup_page():
    # Initialize session state
    init_session_state()

    # Page header
    page_header("Interview Setup", "Configure interview preferences")

    # Ensure user is logged in
    if "current_user" not in st.session_state or not st.session_state.current_user:
        st.warning("⚠️ No user selected. Please go back to App page to register.")
        return

    user = st.session_state.current_user
    st.info(f"Current user: {user['name']}")

    # Option to switch user
    if st.button("Change User"):
        st.session_state.current_user = None
        st.success("User cleared. Go back to App page to register a new user.")
        return

    # Default LLM (Ollama Gemma)
    llm_choice = st.selectbox(
        "Choose Interview Model (LLM)",
        ["Ollama Gemma 3:270m (default)", "DistilBERT (fast)", "GPT4All (local)", "OpenAI GPT-3.5 (API)", "Cohere"],
        index=0
    )

    # Option to select previous interview
    interviews = get_user_interviews(user["id"])
    if interviews:
        st.subheader("Previous Interviews")
        options = {f"Interview {row[0]} - {row[2]}": row for row in interviews}
        selected = st.selectbox("Select a previous interview to reuse", list(options.keys()))
        if st.button("Load Previous Interview"):
            jd, company, questions = options[selected][1], options[selected][2], options[selected][3]
            st.session_state.llm_choice = llm_choice
            st.session_state.jd = jd
            st.session_state.company = company
            st.session_state.prev_questions = questions.splitlines()
            save_message("Previous interview loaded! You can proceed to Interview page.")
            return

    # New interview setup
    st.subheader("New Interview Setup")
    jd = st.text_area("Paste Job Description (JD)", placeholder="Enter JD here...")
    company = st.text_input("Company Name", placeholder="Enter company name...")
    prev_questions = st.text_area("Previous Interview Questions (optional)", placeholder="Enter past questions...")

    if st.button("Save Setup"):
        st.session_state.llm_choice = llm_choice
        st.session_state.jd = jd
        st.session_state.company = company
        st.session_state.prev_questions = prev_questions.splitlines()

        # Save to DB
        save_interview(user["id"], jd, company, prev_questions)
        save_message("Setup saved! You can proceed to Interview page.")

    navigation_hint()

# Run page
if __name__ == "__main__":
    setup_page()
