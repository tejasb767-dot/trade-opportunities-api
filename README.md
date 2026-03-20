# Trade Opportunities API

## Project Overview

Trade Opportunities API is a FastAPI backend that analyzes stock market sectors using real-time news data and AI.

The API fetches financial news, sends it to Groq AI for analysis, and returns a structured market report.
Reports can also be downloaded as Markdown files.

This project demonstrates:

* FastAPI backend development
* External API integration
* AI-based analysis using Groq
* Authentication using API key
* Rate limiting
* Environment variable handling using .env

---

## Project Setup

### 1. Clone repository

git clone <repo-url>

cd trade-opportunities-api-main

---

### 2. Create virtual environment (recommended)

python -m venv venv

venv\Scripts\activate

---

### 3. Install dependencies (IMPORTANT ORDER)

Due to Groq + httpx version conflict, install dependencies in this order.

pip install httpx==0.27.0

pip install groq==0.9.0

pip install -r requirements.txt

---

## Environment Setup (.env file)

Create a file named `.env` in the project root folder.

Location:

trade-opportunities-api-main/.env

Add the following values:

API_KEY=tejas123
GROQ_API_KEY=GIVEN_IN_PDF_SENT TO YOU
NEWS_API_KEY=GIVEN_IN_PDF SENT TO YOU
RATE_LIMIT=3

Note:

The `.env` file is not included in GitHub for security reasons.
Please create it manually before running the server.

---

## Run Server

python -m uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000

---

## Open Swagger UI

http://127.0.0.1:8000/docs

---

## Authentication

All requests must include header:

x-api-key: tejas123

Example:

curl -X GET "http://127.0.0.1:8000/analyze/technology" ^
-H "x-api-key: tejas123"

---

## API Endpoints

GET /analyze/{sector}

Example sectors:

technology
pharmaceuticals
agriculture
banking
energy

GET /download/{sector}

Downloads report as Markdown file.

---

## Technologies Used

Python
FastAPI
Uvicorn
Groq API
News API
SlowAPI
Pydantic
Dotenv
httpx

---

## Author

Tejas B

---
