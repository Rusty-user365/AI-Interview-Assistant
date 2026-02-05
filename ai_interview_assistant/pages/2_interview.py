import streamlit as st
from template import init_session_state, page_header, save_message, navigation_hint

def interview_page():
    # Initialize session state
    init_session_state()

    # Page header
    page_header("Interview Session", "Select and practice different interview rounds")

    # Check if setup is done
    if not st.session_state.jd or not st.session_state.company:
        st.warning("⚠️ Please complete the Setup page first.")
        navigation_hint()
        return

    # Select round type
    round_type = st.radio(
        "Choose Interview Round",
        ["Introduction", "Technical", "Coding"]
    )

    # Display questions based on round type
    if round_type == "Introduction":
        st.subheader("Introduction Round")
        st.write("Tell me about yourself and why you want to join "
                 f"{st.session_state.company}.")
        answer = st.text_area("Your Answer", placeholder="Type or speak your response here...")
        if st.button("Save Answer"):
            st.session_state.answers["introduction"] = answer
            save_message("Introduction answer saved!")

    elif round_type == "Technical":
        st.subheader("Technical Round")
        st.write("Based on the JD, explain your understanding of key skills required.")
        answer = st.text_area("Your Answer", placeholder="Type or speak your response here...")
        if st.button("Save Answer"):
            st.session_state.answers["technical"] = answer
            save_message("Technical answer saved!")

    elif round_type == "Coding":
        st.subheader("Coding Round")
        st.write("Proceed to the Coding page for problem-solving.")
        st.info("Navigate to the Coding page from the sidebar.")

    # Navigation hint
    navigation_hint()

# Run page
if __name__ == "__main__":
    interview_page()
