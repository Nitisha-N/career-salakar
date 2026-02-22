import streamlit as st
from backend.gemini_client import generate_response

st.set_page_config(page_title="Career Salakar", layout="wide")

st.title("Career Salakar")
st.subheader("Career Strategy Dashboard")

WELCOME_MESSAGE = """Hello. I’m Career Salakar.

Tell me:
- Are you in school, college, or working?
- What field are you exploring or confused about?
"""

# Initialize session
if "messages" not in st.session_state:
    st.session_state.messages = [("assistant", WELCOME_MESSAGE)]

# Clear session properly
if st.button("Clear Session"):
    st.session_state.messages = [("assistant", WELCOME_MESSAGE)]
    st.rerun()

# Display messages
for role, message in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Assistant:** {message}")

st.divider()

# Input section (NO manual clearing)
user_input = st.text_input("Enter your career query:")

if st.button("Submit") and user_input.strip():
    st.session_state.messages.append(("user", user_input))

    response = generate_response(st.session_state.messages)

    st.session_state.messages.append(("assistant", response))

    st.rerun()
