# Trade Opportunities API

## Project Overview

Trade Opportunities API is a FastAPI-based backend application that analyzes stock market sectors using real-time financial news data and AI.

The API searches for market news related to a given sector, sends the collected data to an AI model (Groq), and returns a structured market analysis report.

The report can also be saved as a Markdown (.md) file and downloaded by the user.

This project demonstrates backend API development, external API integration, AI-based analysis, authentication, rate limiting, and secure environment handling.


## Features

- FastAPI backend
- Sector-based market analysis
- External News API integration
- AI analysis using Groq API
- Structured JSON response
- Markdown report generation
- Downloadable report file
- API key authentication
- Rate limiting (SlowAPI)
- Input validation
- Logging enabled
- Secure environment variables (.env)


## API Endpoints


### Analyze Sector

GET /analyze/{sector}

Returns structured market analysis for a sector.

Example:

/analyze/technology


### Download Report

GET /download/{sector}

Downloads the report as a Markdown file.

Example:

/download/technology


## Authentication

This API requires an API key.

All requests must include header:

x-api-key: tejas123


Example:

curl -X GET "http://127.0.0.1:8000/analyze/technology" \
-H "x-api-key: tejas123"



## Security Measures

- API key authentication
- Rate limiting (5 requests per minute)
- Input validation
- Error handling
- Logging enabled
- Secrets stored in .env
- .env ignored using .gitignore



## Technologies Used

- Python
- FastAPI
- Uvicorn
- Requests
- Groq API (AI)
- News API
- SlowAPI (rate limiting)
- Pydantic
- Dotenv



## How to Run

Install dependencies

pip install -r requirements.txt


Run server

uvicorn main:app --reload


Open Swagger UI

http://127.0.0.1:8000/docs



## Example Workflow

1. User enters sector name
2. API fetches latest news using News API
3. Data sent to Groq AI for analysis
4. Structured report returned in JSON
5. Report saved as Markdown (.md)
6. User downloads report file



## Author

Tejas B