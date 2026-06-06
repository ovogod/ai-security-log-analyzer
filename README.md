# AI Security Log Analyzer

**AI-Powered Threat Detection Tool**  
Built as part of my Cybersecurity + Generative AI learning journey.

![AI Security Log Analyzer Demo](demo-screenshot.png)

## Overview

This web application analyzes security logs (firewall, SIEM, AWS CloudTrail, etc.) using Generative AI and delivers clear, actionable threat intelligence.

**Key Capabilities:**
- Detects threats such as SQL injection, brute force attacks, port scans, webshell uploads, and ransomware indicators
- Provides severity ratings (High/Medium/Low)
- Gives immediate remediation steps and long-term prevention advice

## Technologies Used

- Python + Streamlit
- LangChain
- Groq (Llama 3.3-70B)
- dotenv

## How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/ovogod/ai-security-log-analyzer.git
   cd ai-security-log-analyzer
   
2. Install dependencies: 
pip install -r requirements.txt

3. Add your Groq API key (create .env file):
Copy .env.example to .env
Add your key: GROQ_API_KEY=your_key_here

4. Run the app:
streamlit run app.py

Project Purpose
This project demonstrates practical application of Generative AI in Cybersecurity — specifically AI-Enhanced Threat Detection. It supports my professional development in cloud security and AI.
Future Improvements

PDF report export
Support for more log formats (Windows Event Logs, AWS CloudTrail JSON)
Multiple AI model options
Deployment to Streamlit Cloud / Hugging Face


Created by Mckenzie Elie
Cybersecurity & Cloud Security Professional | AI-Enhanced Threat Detection
