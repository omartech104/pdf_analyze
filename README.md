# PDF Analyzer

A simple terminal-based PDF analyzer built with Python, Rich, and the Groq API.

You give it a PDF file, and it lets you ask questions about the content in a chat-like interface.

Nothing too fancy — just a lightweight project for reading PDFs and querying them with an LLM.

---

## Features

- Read text from PDF files
- Ask questions about the document
- Clean terminal UI using Rich
- Powered by Groq models
- Simple single-file setup

---

## Requirements

- Python 3.9+
- A Groq API key

---

## Installation

Clone the project or download the file.

Install dependencies:

```bash
pip install groq rich PyPDF2 python-dotenv
````
---

## How to add the API key?

Create a .env file in the project folder:

env
```
GROQ_API_KEY=your_api_key_here
```

You can get an API key from:

https://console.groq.com
