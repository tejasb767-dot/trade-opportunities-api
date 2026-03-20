# Trade Opportunities API

## Project Overview

Trade Opportunities API is a FastAPI-based backend application that analyzes stock market sectors using real-time news data and AI.

The API fetches financial news related to a given sector, processes the data using an AI model, and returns a structured market analysis report.

The generated report can also be saved as a Markdown (.md) file and downloaded by the user.

This project demonstrates backend API development, external API integration, AI-based analysis, and security implementation.


## Features

- FastAPI backend
- Sector-based market analysis
- External news API integration
- AI analysis using Groq
- Structured JSON response
- Markdown report generation
- Downloadable report file
- API key authentication
- Rate limiting
- Input validation
- Logging


## API Endpoints

### Analyze Sector

GET /analyze/{sector}

Returns structured market analysis.

Example:

/analyze/technology


### Download Report

GET /download/{sector}

Downloads the report as a Markdown file.

Example:

/download/technology


## Authentication

This API requires an API key.

All requests must include the header:

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

1. Install dependencies

pip install -r requirements.txt


2. Run the server

uvicorn main:app --reload


3. Open Swagger UI

http://127.0.0.1:8000/docs


## Example Workflow

1. Enter sector name
2. API fetches latest news
3. AI analyzes the data
4. Structured report returned in JSON
5. Report saved as .md file
6. User can download the file


## Author

Tejas B