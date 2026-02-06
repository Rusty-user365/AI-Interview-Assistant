import streamlit as st
from template import init_session_state, page_header, navigation_hint
from llm_engine import run_ollama
from voice_module import transcribe_live
from utils import save_to_db

def interview_page():
    init_session_state()
    page_header("Interview Session", "Practice rounds with live voice transcription")

    if not st.session_state.get('jd') or not st.session_state.get('company'):
        st.warning("⚠️ Please complete the Setup page first.")
        navigation_hint()
        return

    # Round Selection
    col1, col2, col3 = st.columns(3)
    with col1: intro_selected = st.checkbox("Introduction", value=True)
    with col2: tech_selected = st.checkbox("Technical")
    with col3: coding_selected = st.checkbox("Coding")
    st.divider()

    # Initialization of state flags
    if "is_recording" not in st.session_state: st.session_state.is_recording = False
    if "stop_now" not in st.session_state: st.session_state.stop_now = False

    # --- 1. Introduction Round ---
    if intro_selected:
        st.subheader("Introduction Round")
        if "intro_q" not in st.session_state:
            st.session_state.intro_q = run_ollama(f"Generate one intro question for {st.session_state.company}.")
        
        st.write(f"**Question:** {st.session_state.intro_q}")
        
        intro_placeholder = st.empty()
        
        # Display the text area (either interactive or updated by live loop)
        intro_val = st.session_state.get("intro_transcript", "")
        intro_placeholder.text_area("Your Answer (Intro)", value=intro_val, height=150, key="intro_static")

        col_l, col_r = st.columns([1, 4])
        with col_l:
            if not st.session_state.is_recording:
                if st.button("🎤 Start Recording", key="start_intro"):
                    st.session_state.is_recording = True
                    st.session_state.stop_now = False
                    st.rerun()
            else:
                if st.button("🛑 Stop", key="stop_intro"):
                    st.session_state.stop_now = True
                    st.session_state.is_recording = False
                    st.rerun()

        if st.session_state.is_recording and not st.session_state.stop_now:
            transcribe_live(intro_placeholder, "Your Answer (Intro)", "intro_transcript")

        if st.button("Save Intro Answer"):
            save_to_db(st.session_state.get('username', 'Guest'), st.session_state.company, 
                       "Introduction", st.session_state.intro_q, st.session_state.get("intro_transcript", ""))
            st.success("✅ Saved!")

    # --- 2. Technical Round ---
    if tech_selected:
        st.divider()
        st.subheader("Technical Round")
        
        if "tech_questions" not in st.session_state:
            raw = run_ollama(f"Generate 3 technical questions for JD: {st.session_state.jd}")
            st.session_state.tech_questions = [q.strip() for q in raw.split("\n") if len(q) > 10][:3]

        for i, q in enumerate(st.session_state.tech_questions, start=1):
            st.markdown(f"**Q{i}:** {q}")
            
            t_placeholder = st.empty()
            t_val = st.session_state.get(f"tech_ans_{i}", "")
            t_placeholder.text_area(f"Response to Q{i}", value=t_val, height=100, key=f"t_static_{i}")

            c1, c2 = st.columns([1, 4])
            with c1:
                # Logic for each individual question's mic
                rec_key = f"is_rec_t_{i}"
                if rec_key not in st.session_state: st.session_state[rec_key] = False
                
                if not st.session_state[rec_key]:
                    if st.button(f"🎤 Record Q{i}", key=f"start_t_{i}"):
                        st.session_state[rec_key] = True
                        st.session_state.stop_now = False
                        st.rerun()
                else:
                    if st.button(f"🛑 Stop Q{i}", key=f"stop_t_{i}"):
                        st.session_state.stop_now = True
                        st.session_state[rec_key] = False
                        st.rerun()
            
            if st.session_state.get(f"is_rec_t_{i}") and not st.session_state.stop_now:
                transcribe_live(t_placeholder, f"Response to Q{i}", f"tech_ans_{i}")

            if st.button(f"Save Answer Q{i}", key=f"save_tech_{i}"):
                save_to_db(st.session_state.get('username', 'Guest'), st.session_state.company, 
                           f"Technical Q{i}", q, st.session_state.get(f"tech_ans_{i}", ""))
                st.success(f"Q{i} Saved!")

    # --- 3. Coding Round ---
    if coding_selected:
        st.divider()
        st.subheader("Coding Round")
        if st.button("Go to Coding Workspace"):
            st.switch_page("pages/3_coding.py")

    navigation_hint()

if __name__ == "__main__":
    interview_page()