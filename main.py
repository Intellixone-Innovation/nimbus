import speech_recognition as sr
import pyttsx3
from functions import chat  # Import the functions from chat.py

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


# Funtion to speak
def speak(response):
    engine.say(response)
    engine.runAndWait()


# Function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Recognize the speech
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)
        return user_input
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your speech.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the request: {e}")
        return ""


# Function to respond to user input
def respond_to_user_input(user_input):
    user_input = (
        user_input.lower()
    )  # Convert user input to lowercase for case-insensitive comparison

    if "exit" in user_input:
        response = "Goodbye! Exiting..."
        print("Response:", response)
        exit()  # Exit the program

    # Define a list of keyword-response pairs
    keyword_responses = [
        ("hello", "Hello! How can I assist you today?"),
    ]

    # Check if any keyword is present in the user input
    for keyword, reply in keyword_responses:
        if keyword in user_input:
            response = reply
            break  # Exit the loop if a matching keyword is found
        else:
            response = chat.custom_chatbot(user_input)

    print("Response:", response)
    speak(response)


# Main function
def main():
    while True:
        user_input = recognize_speech()
        if user_input:
            respond_to_user_input(user_input)


if __name__ == "__main__":
    main()
