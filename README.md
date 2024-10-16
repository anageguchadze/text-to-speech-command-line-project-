# text-to-speech-command-line-project-


This project converts text or PDF content into speech using Google's Text-to-Speech (gTTS) library. You can input text manually or provide a URL to a PDF file, and the program will convert the content into speech in various supported languages.

## Features
- Convert user-input text into speech.
- Download a PDF from a URL and convert the PDF content to speech.
- Supports multiple languages: English, French, Spanish, Portuguese.
- Text is truncated to a maximum of 500 characters for processing.

## Requirements

Ensure you have the following installed:

- **Python 3.x**  
- **Required Libraries**: Install them via `pip`:
  ```bash
  pip install gTTS pypdf requests
