# JagUnify

JagUnify is a web-based AI chatbot designed to help Texas A&M University–San Antonio students quickly find accurate campus information in one place.

## Purpose

Students often struggle to locate information about advising, financial aid, tutoring, IT support, and campus events because resources are spread across multiple websites. JagUnify solves this by providing a single AI-powered chat interface that gives fast, clear answers using official university sources.

## Features

- AI-powered chatbot
- Web-based chat interface
- Covers core student service categories
- Provides official links for verification
- Simple and student-friendly design

## Setup instructions

- Clone the repo

Create .env file in the root folder with this variable:

```
OPENAI_API_KEY=your_api_key
```

Open command prompt to install required packages:

```
pip install llama-index llama-index-llms-openai chromadb python-dotenv llama-index-vector-stores-chroma
```

Go to /src folder to build vector database to convert texts into embeddings

```
python .\retrieval.py
```

Then run the generator.py file with to test the AI's response:

```
python .\generator.py
```

## Tech Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python
- AI: OpenAI API

## Project Status

This project is currently in the MVP development phase for an academic course.

## Team

- Oscar Hernandez (Team Lead)
- Ian Arredondo
- Christian Hernandez
- Dustin Heagerty
- Trieu Do
