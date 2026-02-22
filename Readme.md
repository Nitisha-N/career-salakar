# Career Salakar – AI-Powered Career Strategy Assistant

## Overview
Career Salakar is an AI-driven career guidance assistant built using Streamlit and Google Gemini 2.5 Flash.
It helps users explore career decisions through structured reflection, guided questioning, and conversational interaction.

The application is deployed on AWS EC2 and supports session-based conversation memory using SQLite.

---

## Tech Stack
- Python 3.9+
- Streamlit
- Google Gemini 2.5 Flash API
- SQLite (conversation storage)
- AWS EC2 (deployment)
- Git & GitHub (version control)

---

## Features
- Interactive AI-powered career guidance
- Structured prompt engineering
- Persistent chat memory using SQLite
- Minimal and clean Streamlit UI
- Cloud deployment on AWS EC2
- Secure API key handling via environment variables

---

## Project Structure

career-salakar/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
└── backend/
    ├── config.py
    ├── gemini_client.py
    ├── memory.py
    └── prompt_builder.py

---

## How to Run Locally

1. Clone the repository:
   git clone https://github.com/Nitisha-N/career-salakar.git
   cd career-salakar

2. Create virtual environment:
   python -m venv venv
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Set your API key:
   export GOOGLE_API_KEY=your_api_key_here

5. Run the application:
   streamlit run app.py

---

## Deployment

The application is deployed on AWS EC2 using:
- nohup for background execution
- Public binding (0.0.0.0)
- Streamlit server configuration

Live URL:
http://13.60.98.146:8501

---

## Author
Nitisha N
GitHub: https://github.com/Nitisha-N
