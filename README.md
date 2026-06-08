# Automated Email Summarizer

## Project Overview

The Automated Email Summarizer is a Python-based automation project that retrieves unread emails from Gmail, summarizes their content, generates a daily digest, and sends the digest back to the user via email. The entire workflow is automated using APScheduler.

This project demonstrates:

* Gmail API Integration
* OAuth2 Authentication
* Email Processing
* Text Cleaning
* Automated Summarization
* SMTP Email Delivery
* Job Scheduling
* Logging and Error Handling

---

## Architecture

```text
Gmail API
     │
     ▼
Fetch Unread Emails
     │
     ▼
Extract Sender, Subject, Body
     │
     ▼
Clean Email Content
     │
     ▼
Summarize Email Content
     │
     ▼
Generate Daily Digest
     │
     ▼
Send Digest via SMTP
     │
     ▼
Schedule using APScheduler
```

---

## Project Structure

```text
Email_Summarizer/
│
├── .env
├── app.log
├── cleaner.py
├── credentials.json
├── digest_generator.py
├── email_sender.py
├── gmail_reader.py
├── main.py
├── requirements.txt
├── scheduler.py
├── summarizer.py
├── test_reader.py
├── token.json
└── README.md
```

---

## Features

### Gmail Authentication

* Uses OAuth2 authentication.
* Generates and stores access tokens securely.
* Uses Gmail API to access mailbox data.

### Email Extraction

* Fetches the latest unread emails.
* Extracts:

  * Sender
  * Subject
  * Email Body

### Email Cleaning

* Removes HTML tags.
* Removes unnecessary spaces and formatting.

### Email Summarization

* Summarizes email content using Sumy.
* Generates concise summaries for easier reading.

### Digest Generation

* Combines summaries into a single report.
* Creates a daily email digest.

### Email Delivery

* Sends digest through Gmail SMTP.
* Uses Gmail App Password authentication.

### Scheduling

* Automates execution using APScheduler.
* Can run daily at a specified time.

### Logging

* Logs important events to app.log.
* Records:

  * Pipeline start
  * Emails processed
  * Errors
  * Digest generation
  * Email delivery

---

## Technologies Used

* Python 3.x
* Gmail API
* Google OAuth2
* Sumy
* NLTK
* BeautifulSoup4
* APScheduler
* SMTP
* python-dotenv

---

## Installation

### 1. Clone Repository

```bash
git clone <repository_url>
cd Email_Summarizer
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
```

### 3. Activate Virtual Environment

Linux/Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Gmail API Setup

1. Create a project in Google Cloud Console.
2. Enable Gmail API.
3. Configure OAuth Consent Screen.
4. Create OAuth Client ID (Desktop Application).
5. Download credentials.json.
6. Place credentials.json in the project root.

---

## Environment Variables

Create a `.env` file:

```env
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password
```

---

## Running the Application

### Execute Pipeline Manually

```bash
python main.py
```

### Run Scheduler

```bash
python scheduler.py
```

---

## APScheduler Configuration

Example daily schedule:

```python
scheduler.add_job(
    run_email_pipeline,
    trigger='cron',
    hour=8,
    minute=0
)
```

This executes the pipeline every day at 8:00 AM.

---

## Logging

View logs:

```bash
cat app.log
```

Monitor logs in real time:

```bash
tail -f app.log
```

---

## Error Handling

The project includes:

* Email-level exception handling
* Pipeline-level exception handling
* Logging of all errors and failures

This ensures that a single failed email does not stop the entire workflow.

---

## Future Enhancements

* Mark processed emails as read
* Store digest history in a database
* Support multiple email providers
* Deploy as a Docker container
* Integrate OpenAI API for advanced summarization
* Build a web dashboard for monitoring

---

## Author

Prabha Chary

Python Automation | Data Engineering | Backend Development
