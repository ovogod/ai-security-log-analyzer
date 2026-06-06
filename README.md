# AI Security Log Analyzer
The tool analyzes firewall, SIEM, and CloudTrail logs to detect threats such as SQL injection, brute force attacks, port scans, and ransomware indicators. It provides summarized threat reports with severity ratings and remediation recommendations.

**AI-Powered Threat Detection Tool** built as part of my journey combining Cybersecurity and Generative AI.

![Demo Screenshot](aisecurity.jpg)  

## Overview

This tool analyzes security logs (firewall, SIEM, CloudTrail, etc.) using Generative AI and returns:
- Clear summary of suspicious activities
- Identified threats with severity ratings (High/Medium/Low)
- Recommended immediate actions and long-term prevention steps

## Features

- Upload log files or use sample data
- Powered by Groq + Llama 3.3 (fast inference)
- Clean, easy-to-read threat analysis
- Built with Python + Streamlit

## Technologies Used

- **Python**
- **Streamlit** (web interface)
- **LangChain**
- **Groq API** (Llama 3.3-70B)
- **dotenv** (environment variables)

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/ovogod/ai-security-log-analyzer.git
   cd ai-security-log-analyzer
   
2. python -m venv venv
venv\Scripts\activate     # Windows
pip install -r requirements.txt

3. Add your Groq API key:
Copy .env.example to .env
Add your key: GROQ_API_KEY=your_key_here

4. streamlit run app.py

Project Purpose
This project demonstrates practical application of Generative AI in Cybersecurity — specifically AI-Enhanced Threat Detection. It supports my professional development in cloud security and AI.
Future Improvements

PDF report export
Support for more log formats (Windows Event Logs, AWS CloudTrail JSON)
Multiple AI model options
Deployment to Streamlit Cloud / Hugging Face


Created by Mckenzie Elie
Cybersecurity & Cloud Security Professional | AI-Enhanced Threat Detection
