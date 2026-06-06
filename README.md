# ai-security-log-analyzer
The tool analyzes firewall, SIEM, and CloudTrail logs to detect threats such as SQL injection, brute force attacks, port scans, and ransomware indicators. It provides summarized threat reports with severity ratings and remediation recommendations.
# AI Security Log Analyzer

**AI-Powered Threat Detection Tool** built as part of my journey combining Cybersecurity and Generative AI.

![Demo Screenshot](screenshot-analysis.png)  
*(Add your best screenshot here after uploading it)*

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
