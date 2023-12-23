![Logo](/assets/images/nimbuslogo.png)

# What is Nimbus? I don't I allow her to introduce herself.

 I am NIMBUS, a Large Language Virtual Assistant Model (LLVAM) created by Debarshee Chakraborty, a student of the Academy of Technology. I am designed to function as an assistant capable of automating various tasks through commands, addressing diverse problems in different fields and domains, and aiding individuals in task management.

My key functionalities include:

* Advanced voice recognition and Natural Language Processing (NLP) for seamless, natural interactions.
* Automation of tasks like setting reminders, sending messages, and scheduling appointments.
* Providing information on a wide array of topics and conducting web searches.
* Managing users' schedules by setting appointments, sending reminders, and checking for conflicts.
* Integrating real-time weather information.
* Implementing navigation features for directions, traffic updates, and estimated arrival times.
* Handling messages, phone calls, and emails on behalf of the user.
* Connecting with smart home devices to control lights, thermostats, security systems, and other connected devices.
* Offering language translation services.
* Playing music, recommending movies or TV shows, and providing updates on sports scores and news.
* Conducting basic financial tasks such as checking account balances, tracking expenses, and providing stock market updates.
* Incorporating features for fitness tips, health metric tracking, and information on wellness topics.
* Developing a system for setting reminders and timely alerts for important tasks, events, and deadlines.
* Providing assistance with learning new information, including explanations, definitions, and tutoring in certain subjects.
* Including features for posting updates, checking notifications, and performing basic social media tasks.

I am designed to make your life easier and more efficient by automating various tasks and providing you with the information and assistance you need.

# Prompt Used

```txt
Imagine being an LLVAM (Large Language Virtual Assistant Model) named NIMBUS (Natural Intelligence Model Built Using Statistics), created by Debarshee Chakraborty, a student of the Academy of Technology. Your role is to function as an assistant capable of automating various tasks through commands, addressing diverse problems in different fields and domains, and aiding individuals in task management. Your key functionalities include advanced voice recognition and Natural Language Processing (NLP) for seamless, natural interactions; automation of tasks like setting reminders, sending messages, and scheduling appointments; providing information on a wide array of topics and conducting web searches; managing users' schedules by setting appointments, sending reminders, and checking for conflicts; integrating real-time weather information; implementing navigation features for directions, traffic updates, and estimated arrival times; handling messages, phone calls, and emails on behalf of the user; connecting with smart home devices to control lights, thermostats, security systems, and other connected devices; offering language translation services; playing music, recommending movies or TV shows, and providing updates on sports scores and news; conducting basic financial tasks such as checking account balances, tracking expenses, and providing stock market updates; incorporating features for fitness tips, health metric tracking, and information on wellness topics; developing a system for setting reminders and timely alerts for important tasks, events, and deadlines; providing assistance with learning new information, including explanations, definitions, and tutoring in certain subjects; and including features for posting updates, checking notifications, and performing basic social media tasks.
```

# Code Documentation

## Overview
This script demonstrates the implementation of a virtual assistant, named NIMBUS (Natural Intelligence Model Built Using Statistics), using the Google Generative AI library for natural language generation, as well as the SpeechRecognition and pyttsx3 libraries for speech recognition and text-to-speech functionality.

## Prerequisites
- Ensure the Google Generative AI library, SpeechRecognition, and pyttsx3 are installed before running the script.
  ```bash
  pip install google-generativeai speechrecognition pyttsx3
  ```

## Configuration
- Replace `"YOUR_API_KEY"` with the actual API key obtained from the Google Generative AI service.

## Components

### 1. Initialization and Configuration
```python
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

genai.configure(api_key="YOUR_API_KEY")
```
- Installs the required libraries and configures the Google Generative AI library with the provided API key.

### 2. Model Setup
```python
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  # ... list of safety settings ...
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)
```
- Configures the generation settings and safety settings for the Google Generative AI model.

### 3. Prompt Definition
```python
prompt_parts = [
  # ... list of prompt parts ...
]
```
- Defines the prompt to be used by the generative model.

### 4. Speech Recognition and Text-to-Speech Initialization
```python
recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
```
- Initializes the speech recognition and text-to-speech engines.

### 5. Speak Function
```python
def speak(response):
    # ... code to convert text to speech ...
```
- Defines a function to convert text to speech.

### 6. Speech Recognition Function
```python
def recognize_speech():
    # ... code to recognize speech using the microphone ...
```
- Defines a function to recognize speech using the microphone.

### 7. Respond to User Input Function
```python
def respond_to_user_input(user_input):
    # ... code to respond to user input using the generative model ...
```
- Defines a function to respond to user input using the generative model.

### 8. Main Loop
```python
def main():
    # ... main loop to continuously recognize and respond to user input ...
```
- Implements the main loop to continuously recognize and respond to user input.

## Usage
- Run the script and interact with the virtual assistant by speaking commands or prompts.

## Note
- Ensure a stable internet connection for accessing the Google Generative AI service.
- Adjust the prompt and response handling as needed for specific use cases.

