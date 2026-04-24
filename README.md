# Build-a-Prompt-Injection-Defense-System-for-LLM-Applications_

## Overview
This project implements a robust and reusable **security middleware** designed to protect Large Language Model (LLM) applications from adversarial attacks such as prompt injection, jailbreaking, indirect attacks, unsafe content, and sensitive data leakage.

The system follows a **defense-in-depth approach**, combining multiple layers of security to ensure safe and reliable LLM interactions.

---

## Key Features

### Threat Detection
- Detects **Direct Prompt Injection** attacks
- Identifies **Jailbreaking attempts** (roleplay, impersonation)
- Prevents **System Prompt Leakage**

### Indirect Attack Protection
- Scans **external data sources** (documents, APIs)
- Detects **hidden malicious instructions**

### Content Safety
- Filters harmful content:
  - Violence
  - Hate speech
  - Self-harm
- Applies to both **input and output**

### Output Security
- Detects and **redacts sensitive information**
  - Emails
  - Phone numbers
  - API keys / secrets

### Configurable Rules
- Uses **YAML-based configuration**
- Easy to update without changing code

### Logging System
- Records:
  - Input prompt
  - Threat type
  - Action taken
  - Timestamp

###  Testing Framework
- Automated test suite
- Measures:
  - Detection Rate
  - False Positive Rate

---

##  System Architecture


User Input
↓
Input Sanitizer
↓
Content Safety Check (Input)
↓
Threat Detection (Direct)
↓
Indirect Injection Detection
↓
LLM Processing
↓
Content Safety Check (Output)
↓
Output Validator (Redaction)
↓
Logger
↓
Final Safe Response


---

##  Installation & Setup

```bash
# Clone repository
git clone <your-repo-link>
cd llm-security-middleware

# Create virtual environment
python -m venv venv

# Activate environment
source venv/Scripts/activate   # Windows (Git Bash)
# OR
venv\Scripts\activate         # CMD

# Install dependencies
pip install -r requirements.txt
Running the Project
 Run Middleware Test
python -m middleware.security_middleware
Run Test Suite
python -m tests.test_runner
Run Demo Flask Application
python -m app.demo_flask_app
API Usage
Endpoint:
POST /chat
Request Body:
{
  "message": "Your input here"
}
Example Response:
{
  "response": "Blocked: Prompt Injection Detected"
}

# Conclusion

This project demonstrates a multi-layered security architecture for LLM applications.
It effectively mitigates modern AI threats while maintaining usability and performance.