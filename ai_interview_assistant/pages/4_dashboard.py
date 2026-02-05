import streamlit as st
import pandas as pd
import plotly.express as px
from template import init_session_state, page_header, navigation_hint

def dashboard_page():
    # Initialize session state
    init_session_state()

    # Page header
    page_header("Interview Dashboard", "View evaluation results and progress")

    # Check if any answers exist
    if not st.session_state.answers and not st.session_state.coding_submission:
        st.warning("⚠️ No interview data found. Please complete an interview first.")
        navigation_hint()
        return

    # Current interview summary
    st.subheader("Current Interview Evaluation")
    if st.session_state.answers:
        for round_type, answer in st.session_state.answers.items():
            st.write(f"**{round_type.capitalize()} Answer:** {answer[:100]}...")  # preview
    if st.session_state.coding_submission:
        st.write("**Coding Submission:**")
        st.code(st.session_state.coding_submission, language="python")

    # Placeholder metrics (later replaced with regression analytics)
    st.metric("Answer Length (chars)", sum(len(ans) for ans in st.session_state.answers.values()))
    st.metric("Coding Lines", len(st.session_state.coding_submission.splitlines()))

    # Overall performance (mock data for demo)
    st.subheader("Overall Performance Trends")
    data = pd.DataFrame({
        "Interview": [1, 2, 3, 4],
        "Score": [60, 70, 75, 80]
    })
    fig = px.line(data, x="Interview", y="Score", markers=True, title="Performance Over Time")
    st.plotly_chart(fig, use_container_width=True)

    # Navigation hint
    navigation_hint()

# Run page
if __name__ == "__main__":
    dashboard_page()
