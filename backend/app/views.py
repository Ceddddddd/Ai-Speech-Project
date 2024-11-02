# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
import json
from mistralai import Mistral
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
api_key = "dJw9FNiIt7tRfiVtWvWEfkqtDoBTgagI"
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

def home(request):
    form = LoginForm()
    return render(request, 'app/login.html',{'form': form})

def registerForm(request):
    form = RegistrationForm()
    return render(request, 'app/register.html',{'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate the user with username and password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # Correctly passing the request and user
                return redirect('main')  # Redirect to home or dashboard
            else:
                messages.error(request, 'Username or password is incorrect.')
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})

@login_required
def main_page(request):
    return render(request, 'app/index.html')

def register(request):
    print('register triggered')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('form is post')
        if form.is_valid():
            print('form is valid')
            form.save()  # Save the user
            messages.success(request, 'Registration successful!')
            return redirect('home')  # Redirect to a success page
        else:
            messages.error(request, 'Please correct the error below.')
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})



@csrf_exempt  
def summarize(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            transcript = data.get('transcript', '')
            language = data.get('outputLanguage', '')
            chat_response = client.chat.complete(
                model= model,
            messages = [
                {
                    "role": "user",
                    "content": f"Speak and reply in {language} language and then summarize the following transcript in a concise paragraph, focusing only on the main points without any additional information:\n\n{transcript}",
                },
            ]

            )
            summary = chat_response.choices[0].message.content 
            return JsonResponse({'summary': summary})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt  # You may want to handle CSRF protection properly in production
def question(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            transcript = data.get('transcript', '')
            question = data.get('question', '')
            chat_response = client.chat.complete(
                model= model,
            messages = [
                {
                    "role": "user",
                    "content": f"Base on this transcript {transcript}, answer this question {question} make it concise and clean",
                },
            ]

            )
            answer = chat_response.choices[0].message.content 
            return JsonResponse({'answer': answer})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt 
def translate(request):
     if request.method == 'POST':
        try:
            data = json.loads(request.body)
            text = data.get('text', '')
            targetLanguage = data.get('targetLanguage', '')
            chat_response = client.chat.complete(
                model= model,
            messages = [
                {
                    "role": "user",
                    "content": f"Translate this transcript '{text}' using the language of {targetLanguage}. Strictly only reply with the translated things and nothing more",
                },
            ]

            )

            answer = chat_response.choices[0].message.content 
            return JsonResponse({'translatedText': answer})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
     return JsonResponse({'error': 'Invalid request method'}, status=405)