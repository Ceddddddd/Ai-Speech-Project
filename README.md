# AI Web Application

## Overview
This Mistral AI web application leverages the Web Speech API to provide a seamless user experience for recording speech, transcribing it into text, and performing various operations such as translation and summarization. Users can interact with the transcribed text by asking questions and receive responses. The application also features a basic login and registration system for user authentication, adding an extra layer of security.

## Notes
> **Note 1**: Make sure to set up your environment variables in the `.env` file correctly to ensure the application runs smoothly.
> **Note 2**: If you're experiencing issues with audio recording, check your browser's microphone permissions.
> **Note 3**: You should configure your own API key in mistral ai official site.
> **Note 4**: The Mistral ai being used is run in the cloud and free resulting to slower response if you wanted for much faster response you can apply for the paid ones.

## Features
- **Speech Recording**: Record audio using the Web Speech API.
- **Transcript Display**: Automatically display the transcribed speech in real-time.
- **Language Selection**: Users can select the output language for translation.
- **Text-to-Voice**: Convert the transcribed text to voice in the selected language.
- **Text-to-Text Translation**: Translate the transcribed text into the selected output language.
- **Question Answering**: Users can ask questions related to the transcript.
- **Summarization**: Provide a concise summary of the transcribed text.
- **User Authentication**: Basic login and registration system for secure access.
- **Security**: Django have built-in protections against common attacks, i ensure that all forms have CSRF protection and SQL injection immunity

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python and Django (https://docs.djangoproject.com/en/5.1/intro/install/)
- **APIs**: Web Speech API and Mistral AI (https://docs.mistral.ai/getting-started/quickstart/) 
- **Database**: PostgreSQL

## Installation
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```powershell
   git clone <repository-url>
   cd <project-directory>

2. **Create a Virtual Environment**:
   ```powershell
   python -m venv venv
   source venv/bin/activate (for linux)
   
3. **Install Dependencies**:
   ```powershell
   pip install django
   pip install mistralai

## USAGE
To run the project locally, follow these steps:

1. **Clone the Repository**:
   ```powershell
   python manage.py runserver

2. **Open the Application**:
   -Navigate to http://localhost:8000 (or the port specified) in your web browser

3. **Authentication**:
   -You should go to registration first before you can enter the main page as it is a protected url and requires login

