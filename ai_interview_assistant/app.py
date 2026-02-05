import streamlit as st
from template import init_session_state, page_header, navigation_hint

def main():
    # Initialize session state
    init_session_state()

    # Landing page header
    page_header("AI Interview Assistant Demo", "Hackathon Prototype")

    st.write("""
    Welcome to the AI Interview Assistant demo app!  
    Use the sidebar to navigate through the following pages:
    - **Setup**: Configure LLM, JD, company details, and past questions
    - **Interview**: Practice Introduction, Technical, or Coding rounds
    - **Coding**: Solve coding problems interactively
    - **Dashboard**: View evaluation results and analytics
    """)

    st.info("Navigate using the sidebar on the left.")

if __name__ == "__main__":
    main()
