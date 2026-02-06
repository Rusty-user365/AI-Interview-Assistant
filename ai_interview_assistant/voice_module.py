import whisper
import sounddevice as sd
import numpy as np
import streamlit as st

# Load tiny for live speed
model = whisper.load_model("base")  # or "tiny" for faster but less accurate

def transcribe_live(placeholder, label, state_key, total_duration=60, samplerate=16000):
    """
    Records audio in chunks and updates the UI live.
    """
    # Initialize the transcript from session state to avoid resets
    full_transcript = st.session_state.get(state_key, "")
    chunk_duration = 2 
    
    # Range requires integers, so we ensure total_duration is an int
    for i in range(0, int(total_duration), chunk_duration):
        # Check if the user pressed the stop button
        if st.session_state.get("stop_now", False):
            break
            
        try:
            # Record chunk
            audio_chunk = sd.rec(int(chunk_duration * samplerate), samplerate=samplerate, channels=1, dtype=np.float32)
            sd.wait()
            
            # Transcribe chunk
            audio_data = np.squeeze(audio_chunk)
            result = model.transcribe(audio_data, fp16=False)
            
            chunk_text = result["text"].strip()
            if chunk_text:
                full_transcript += " " + chunk_text
                # Update session state immediately
                st.session_state[state_key] = full_transcript.strip()
                # Update the UI placeholder
                placeholder.text_area(label, value=st.session_state[state_key], height=150, key=f"lp_{state_key}_{i}")
        except Exception as e:
            st.error(f"Audio Error: {e}")
            break
            
    return st.session_state.get(state_key, "")