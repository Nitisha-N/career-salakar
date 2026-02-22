# Career Salakar – AI-Powered Career Guidance Assistant

Career Salakar is an interactive AI-based career guidance chatbot built using Streamlit and Google Gemini API. It helps users explore career paths, clarify confusion, and receive structured guidance through conversational memory and contextual prompts.

Features

•	Conversational AI powered by Google Gemini

•	Session-based memory (multi-turn chat)

•	Structured prompt engineering for career clarity

•	Clear session functionality

•	Clean dark UI built with Streamlit

•	Secure API key handling using environment variables

Tech Stack

•	Python 3.11+

•	Streamlit

•	Google Gemini API

•	python-dotenv

•	SQLite (for session memory)

Project Structure

career\_salakar/

│

├── app.py

├── backend/

│   ├── memory.py

│   ├── prompt\_builder.py

│   └── gemini\_client.py

├── requirements.txt

└── README.md



Note: .env file is intentionally excluded for security reasons.

Setup Instructions

1\. Install Dependencies

pip install -r requirements.txt

2\. Create Environment Variable

Create a .env file in the root directory and add:



GOOGLE\_API\_KEY=your\_google\_api\_key\_here



Important:

\- Do NOT add quotes

\- Do NOT commit the .env file

\- Keep your API key private

3\. Run the Application

streamlit run app.py

App runs at: http://localhost:8501

Deployment (Streamlit)

Set the GOOGLE\_API\_KEY as an environment variable on the deployment platform. Do NOT upload the .env file. Ensure requirements.txt is included.

Model Used

Google Gemini (e.g., gemini-2.5-flash or gemini-1.5-flash) for dynamic greeting generation and contextual career guidance.

How Memory Works

•	Each session generates a unique user\_id

•	Messages are stored in SQLite

•	Recent conversation history is injected into the prompt builder

•	Enables multi-turn contextual conversations

Author

Nitu



