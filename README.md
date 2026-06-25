# AI Document Assistant

## Overview

AI Document Assistant is an AI-powered application that enables users to upload PDF documents and interact with them using natural language questions. The system extracts text from uploaded PDFs and uses Google's Gemini AI model to generate accurate answers based on the document content.

## Features

* Upload PDF documents
* Extract text from PDFs
* Ask questions related to uploaded documents
* AI-generated answers using Gemini AI
* Interactive document-based chatbot

## Technologies Used

* Python
* FastAPI
* Google Gemini API
* PyPDF
* Uvicorn
* Git
* GitHub

## Project Workflow

1. User uploads a PDF document.
2. The system extracts text from the PDF using PyPDF.
3. Extracted text is stored temporarily.
4. User asks questions about the document.
5. Gemini AI processes the document content and question.
6. The system returns an AI-generated answer.

## Project Structure

AI-Document-Assistant

├── backend

│   ├── main.py

│   ├── chatbot.py

│   ├── pdf_processor.py

│   └── uploads/

├── requirements.txt

└── README.md

## Example Use Cases

* Research Paper Analysis
* Resume Screening
* Invoice Understanding
* Contract Review
* User Manual Assistance
* Academic Document Querying

## Future Enhancements

* Document Summarization
* Semantic Search
* Multiple Document Support
* Chat History
* Web-Based Frontend



