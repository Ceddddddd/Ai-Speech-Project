# AI Web Application

## Overview
This Mistral AI web application leverages the Web Speech API to provide a seamless user experience for recording speech, transcribing it into text, and performing various operations such as translation and summarization. Users can interact with the transcribed text by asking questions and receive responses. The application also features a basic login and registration system for user authentication, adding an extra layer of security.

You can run demo the website here: https://transcribetitan.pythonanywhere.com/

## Prerequisites

- Basic knowledge of Django and JavaScript.
- A Django project set up with views to handle AJAX requests.
- Django version 2.x or higher.

## Notes

1. **Environment Variables**: 
   - Ensure that your environment variables are set up correctly in the `.env` file. This is crucial for the application to run smoothly.

2. **Audio Recording Issues**:
   - If you encounter problems with audio recording, please check your browser's microphone permissions to ensure that they are correctly configured.

3. **API Key Configuration**:
   - You need to configure your own API key, which can be obtained from the Mistral AI official site. Ensure this is set up before using the application.

4. **Mistral AI Performance**:
   - The Mistral AI being utilized operates in the cloud and is available for free. Please note that this may result in slower response times. If you require faster responses, consider applying for a paid plan.


## Features
- **Speech Recording**: Record audio using the Web Speech API.
- **Transcript Display**: Automatically display the transcribed speech in real-time.
- **Language Selection**: Users can select the output language for translation.
- **Text-to-Voice**: Convert the transcribed text to voice in the selected language.
- **Text-to-Text Translation**: Translate the transcribed text into the selected output language.
- **Question Answering**: Users can ask questions related to the transcript.
- **Summarization**: Provide a concise summary of the transcribed text.
- **User Authentication**: Basic login and registration system for secure access.
- **Security**: Django have built-in protections against common attacks, i ensure that all forms have CSRF protection and SQL injection immunity. The sample is also HTTP secured and Cross Origin Resource sharing only allows the given sub domain

## Technologies Used
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python and Django (https://docs.djangoproject.com/en/5.1/intro/install/)
- **APIs**: Web Speech API and Mistral AI (https://docs.mistral.ai/getting-started/quickstart/) 
- **Database**: SQLite

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
   Navigate to http://localhost:8000 (or the port specified) in your web browser

3. **Authentication**:
   You should go to registration first before you can enter the main page as it is a protected url and requires login

