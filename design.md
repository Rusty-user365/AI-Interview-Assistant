

## 1. System Architecture

The AI Interview Assistant is organized into modular components. The following diagram illustrates the flow of data and responsibilities across the system:

```
+-------------------+
|   Student (User)  |
+-------------------+
        |
        v
+-------------------+
|   Streamlit UI    |
| - Voice Input     |
| - Text Input      |
| - Code Editor     |
| - Dashboard       |
+-------------------+
        |
        v
+---------------------------+
|       Backend API         |
|   (FastAPI / Flask)       |
|---------------------------|
| Interview Orchestrator    |
| NLP Engine (JD-aware Qs)  |
| TTS / ASR Module          |
| Coding Evaluation Module  |
+---------------------------+
        |
        v
+-------------------+
|   Database Layer  |
| - Transcripts     |
| - Answers         |
| - Scores          |
| - Job Context     |
+-------------------+
        |
        v
+-------------------+
|  Analytics Engine |
| - Per-Interview   |
| - Cumulative      |
| - Visualization   |
+-------------------+
        |
        v
+-------------------+
|   Feedback & UI   |
| - Reports         |
| - Recommendations |
| - Progress Trends |
+-------------------+
```

### Explanation of Components
- **Student (User)** → The end‑user interacts with the system through voice or text.  
- **Streamlit UI** → Provides a simple, intuitive interface for interview setup, answering questions, coding practice, and viewing dashboards.  
- **Backend API (FastAPI/Flask)** → Orchestrates the interview flow, generates JD‑aware questions, handles speech/text conversion, and evaluates coding answers.  
- **Database Layer (SQLite/PostgreSQL)** → Stores transcripts, answers, scores, and job context securely for later analysis.  
- **Analytics Engine** → Processes stored data to generate per‑interview metrics and cumulative performance trends.  
- **Feedback & UI** → Presents reports, recommendations, and progress trends back to the student via the dashboard.  

---

# 📄 Design Document

## 1. 🏗️ System Architecture
The solution is structured into modular components:

- **Frontend (UI/UX)** → Streamlit‑based interface with panels for preferences, interview, coding, and dashboard.  
- **Backend Orchestrator** → Python modules managing interview flow, question delivery, and evaluation.  
- **Voice Module** → ASR (speech recognition) + TTS for spoken interaction.  
- **LLM Engine** → Lightweight models for Q&A and coding evaluation.  
- **Analytics Engine** → Regression‑based models for per‑interview and overall performance tracking.  
- **Data Layer** → SQLite/PostgreSQL for storing interview logs, transcripts, and scores.  

---

## 2. 🔄 Process Flow
1. **User Login / Preferences**  
   - Select LLM, input JD/company, choose interview type.  
2. **Interview Session**  
   - Questions delivered via text + TTS.  
   - Answers captured via speech or text.  
   - Coding round with integrated editor.  
3. **Evaluation**  
   - Per‑interview analytics generated (time, length, tone, pauses, depth).  
   - Regression models compute overall performance trends.  
4. **Dashboard**  
   - Visual breakdown of strengths, weaknesses, and progress trends.  
   - Comparison across multiple sessions.  

---

## 3. 🎨 UI Design
- **Preferences Panel** → Dropdowns for LLM selection, JD/company input, start button.  
- **Interview Panel** → Question display, voice prompt, answer capture, stop button.  
- **Coding Panel** → Problem statement + code editor.  
- **Dashboard Panel** → Charts (pie, line, bar) showing analytics and performance trends.  

---

## 4. ⚙️ Technology Stack
- **Frontend** → Streamlit, Plotly/Altair for charts.  
- **Backend** → Python (FastAPI/Flask optional for modular APIs).  
- **Voice** → SpeechRecognition, gTTS.  
- **LLM** → DistilBERT, GPT4All, or other small inference models.  
- **Analytics** → scikit‑learn regression models, pandas.  
- **Storage** → SQLite/PostgreSQL.  

---

## 5. 🚀 Future Enhancements
- Cloud deployment with Docker + CI/CD.  
- Integration with larger LLMs for advanced evaluation.  
- Expanded analytics (domain‑specific scoring, behavioral clustering).  

---

## 📌 Document Metadata
- **Document Version**: 1.0  
- **Last Updated**: February 5, 2026  
- **Status**: Draft for Review  

---
