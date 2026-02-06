import os
import sqlite3
import streamlit as st
from template import init_session_state, page_header

# Base directory = folder where app.py lives 
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
DB_PATH = os.path.join(BASE_DIR, "data", "interview_logs.db")


def init_db():
    """Initialize database with users and interviews tables if not exists."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            jd TEXT,
            company TEXT,
            questions TEXT,
            answers TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    conn.close()

def get_users():
    """Fetch all users from DB."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_user(name: str):
    """Add a new user if not exists, return user_id."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO users(name) VALUES (?)", (name,))
    conn.commit()
    cursor.execute("SELECT id FROM users WHERE name=?", (name,))
    user_id = cursor.fetchone()[0]
    conn.close()
    return user_id

def main():
    init_session_state()
    init_db()

    page_header("AI Interview Assistant Demo", "Hackathon Prototype")

    st.write("Select an existing user or register a new one.")

    users = get_users()
    user_names = [row[1] for row in users]

    # Dropdown for existing users
    selected_user = None
    if user_names:
        selected_user = st.selectbox("Choose existing user", ["-- None --"] + user_names)

    # Input for new user
    new_name = st.text_input("Or enter a new name")

    if st.button("Submit"):
        if new_name.strip():
            user_id = add_user(new_name.strip())
            st.session_state.current_user = {"id": user_id, "name": new_name.strip()}
            st.success(f"Welcome, {new_name}! Redirect to Setup page using sidebar.")
        elif selected_user and selected_user != "-- None --":
            # Find user_id from DB
            user_id = [row[0] for row in users if row[1] == selected_user][0]
            st.session_state.current_user = {"id": user_id, "name": selected_user}
            st.success(f"Welcome back, {selected_user}! Redirect to Setup page using sidebar.")
        else:
            st.error("Please select an existing user or enter a new name.")

    # Show current user if logged in
    if "current_user" in st.session_state and st.session_state.current_user:
        st.info(f"Current user: {st.session_state.current_user['name']}")
        st.write("Go to **Setup** page from sidebar to configure interview.")

if __name__ == "__main__":
    main()
