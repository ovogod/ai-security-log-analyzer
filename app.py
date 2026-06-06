import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.title("🔒 AI Security Log Analyzer")
st.write("Upload security logs and get AI-powered threat analysis")

# Initialize LLM - Updated model (June 2026)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # Current strong model
    temperature=0.3,
    api_key=os.getenv("GROQ_API_KEY")
)

# Sample logs if user doesn't upload
sample_log = """[2026-06-05 09:15:23] FAILED LOGIN user=admin src_ip=185.22.45.67
[2026-06-05 09:16:01] SQL Injection attempt detected: SELECT * FROM users WHERE id=1' OR '1'='1
[2026-06-05 09:20:45] Port scan from 45.67.89.12 on ports 22,80,443"""

uploaded_file = st.file_uploader("Upload your log file (txt)", type="txt")

if uploaded_file:
    log_content = uploaded_file.read().decode()
else:
    log_content = sample_log
    st.info("Using sample logs for demo")

if st.button("Analyze Logs"):
    with st.spinner("AI is analyzing threats..."):
        prompt = f"""
        You are a senior cybersecurity analyst. Analyze the following security logs and provide:
        1. Summary of suspicious activities
        2. Potential threats identified (with severity: Low/Medium/High)
        3. Recommended immediate actions
        4. Long-term prevention suggestions

        Logs:
        {log_content}
        """

        response = llm.invoke(prompt)
        st.subheader("🛡️ AI Analysis")
        st.write(response.content)