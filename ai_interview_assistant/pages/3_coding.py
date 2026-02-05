import streamlit as st
from template import init_session_state, page_header, save_message, navigation_hint

def coding_page():
    # Initialize session state
    init_session_state()

    # Page header
    page_header("Coding Round", "Solve coding problems interactively")

    # Check if setup is done
    if not st.session_state.jd or not st.session_state.company:
        st.warning("⚠️ Please complete the Setup page first.")
        navigation_hint()
        return

    # Example coding problem (can be dynamic later)
    st.subheader("Problem Statement")
    st.write("""
    Write a function to check if a given string is a palindrome.
    Example:
    - Input: "madam"
    - Output: True
    """)

    # Code editor (basic text area for now)
    code_submission = st.text_area(
        "Your Code Solution",
        placeholder="Write your Python code here...",
        height=200
    )

    # Save submission
    if st.button("Save Submission"):
        st.session_state.coding_submission = code_submission
        save_message("Coding solution saved!")

    # Navigation hint
    navigation_hint()

# Run page
if __name__ == "__main__":
    coding_page()
