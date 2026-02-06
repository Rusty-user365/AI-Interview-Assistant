import streamlit as st
from template import init_session_state, page_header, save_message, navigation_hint
from llm_engine import run_ollama
from utils import save_to_db  # Added database support

def coding_page():
    init_session_state()
    page_header("Coding Round", "Solve coding problems interactively")

    if not st.session_state.get('jd') or not st.session_state.get('company'):
        st.warning("⚠️ Please complete the Setup page first.")
        navigation_hint()
        return

    # 1. Difficulty Selection
    difficulty = st.select_slider(
        "Select Difficulty Level",
        options=["Easy", "Medium", "Hard"],
        value="Medium"
    )

    # Function to fetch question from LLM
    def generate_coding_question():
        with st.status("🛠️ Generating coding challenge...", expanded=True) as status:
            prompt = (
                f"Generate a {difficulty} level coding interview question for a candidate "
                f"applying to {st.session_state.company}. The question should be relevant to "
                f"this job description: {st.session_state.jd}. "
                "Provide a clear problem statement, input/output examples, and constraints."
            )
            question = run_ollama(prompt)
            status.update(label="Challenge Generated!", state="complete", expanded=False)
            return question

    # 2. Initial Question Generation Logic
    if "current_coding_problem" not in st.session_state:
        st.session_state.current_coding_problem = generate_coding_question()

    # 3. Display Question
    st.subheader("Problem Statement")
    st.markdown(st.session_state.current_coding_problem)

    # 4. Generate More Button
    if st.button("Generate Different Question"):
        st.session_state.current_coding_problem = generate_coding_question()
        # Clear previous submission when new question is generated
        st.session_state.coding_submission = ""
        st.rerun()

    st.divider()

    # 5. Code Editor
    st.subheader("Your Solution")
    code_submission = st.text_area(
        "Python Editor",
        value=st.session_state.get("coding_submission", ""),
        placeholder="def solution():\n    # Write your code here...",
        height=300,
        key="coding_input_area" # Explicit key for stability
    )

    # 6. Action Buttons
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("Save Submission"):
            st.session_state.coding_submission = code_submission
            # Saving to Database logic
            save_to_db(
                st.session_state.get('username', 'Guest'),
                st.session_state.get('company', 'Unknown'),
                "Coding Round",
                st.session_state.current_coding_problem,
                code_submission
            )
            save_message("Coding solution saved to database!")
    
    with col2:
        if st.button("Analyze Code"):
            if not code_submission.strip():
                st.warning("Please write some code first.")
            else:
               
                with st.spinner("Analyzing logic and errors..."):
                    # STERN TEACHER PROMPT: Strict constraints to stop code rewrites
                    analysis_prompt = (
                        f"SYSTEM: You are a strict technical interviewer. You provide minimal, blunt feedback. "
                        f"DO NOT rewrite the code. DO NOT add try-except blocks. DO NOT add comments. "
                        f"DO NOT give a 'correct version' unless the student's code is completely broken.\n\n"
                        f"CHALLENGE: {st.session_state.current_coding_problem}\n"
                        f"STUDENT_CODE:\n{code_submission}\n\n"
                        f"TASK:\n"
                        f"1. If the code works: Only say 'Your code looks solid for this task.'\n"
                        f"2. If the code fails: Say 'Your code does not perform the task due to...' and explain the error in under 60 words.\n"
                        f"3. If there is a syntax error: Point it out briefly."
                    )
                    feedback = run_ollama(analysis_prompt,model="gemma3:4b")
                    st.info(f"**Feedback:**\n{feedback}")

    navigation_hint()

if __name__ == "__main__":
    coding_page()