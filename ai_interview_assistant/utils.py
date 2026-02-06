import sqlite3

def save_to_db(username, company, round_type, question, answer):
    conn = sqlite3.connect('data/interview_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs 
                 (username TEXT, company TEXT, round TEXT, question TEXT, answer TEXT)''')
    c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?)", 
              (username, company, round_type, question, answer))
    conn.commit()
    conn.close()