**🌟 AI‑Interview‑Assistant**
#📄 AI Interview Assistant – Requirements Document

## 1. 🎯 Purpose
The **AI Interview Assistant** is designed to simulate real interview scenarios (voice + coding) for students and professionals.  
It provides **per‑interview analytics** and **overall performance tracking** to help users improve both technical and communication skills.

---

## 2. ⚙️ Functional Requirements
- **Interview Setup**
  - Select preferred LLM (default suggested).  
  - Input Job Description (JD) and company details.  
  - Choose interview type (full, coding‑only, skip intro).  

- **Question Delivery**
  - Display questions on screen (text).  
  - Deliver questions via Text‑to‑Speech (TTS).  
  - Capture answers via speech recognition or text input.  

- **Coding Round**
  - Integrated code editor for solving problems.  
  - Real‑time evaluation using smaller LLM models.  

- **Analytics**
  - Per‑interview metrics: time taken, answer length, technical depth, pauses, tone, communication style.  
  - Overall performance tracking across multiple interviews.  
  - Dashboard visualization of strengths, weaknesses, and progress trends.  

- **Data Storage**
  - Store questions, answers, scores, and domains securely.  
  - Maintain interview history for cumulative analysis.  

---

## 3. 🛡️ Non‑Functional Requirements
- **Performance** → Fast response using lightweight models for Q&A and evaluation.  
- **Scalability** → Modular design to allow future integration with larger models or cloud APIs.  
- **Security** → Secure storage of transcripts and analytics.  
- **Usability** → Simple, intuitive UI built with Streamlit.  
- **Portability** → Runs locally on mid‑range hardware without GPU dependency.  

---

## 4. 🔧 Constraints
- Analytics may take longer to process (batch mode with regression models).  
- Limited to smaller/faster LLMs for local inference.  
- No webcam‑based cheating detection (focus on practice only).  

---

## 📌 Document Metadata
*Document Version*: 1.0  
*Last Updated*: February 5, 2026  
*Status*: Draft for Review  
