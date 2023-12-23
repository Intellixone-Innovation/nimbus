# Install the client library and import necessary modules.
import google.generativeai as genai  # Import the generative AI client library
import speech_recognition as sr  # Import the SpeechRecognition library
import pyttsx3  # Import the text-to-speech library

# Configure the generative AI client with your API key
genai.configure(api_key="YOUR_API_KEY")

# Set up the model generation configuration and safety settings
generation_config = {
  "temperature": 0.5,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
  {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Initialize the generative model
model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Define prompt parts for model input
prompt_parts = [
  "Imagine being an LLVAM (Large Language Virtual Assistant Model) named NIMBUS...",
  "Now do a greeting.",
]

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

# Function to speak a given response using the text-to-speech engine
def speak(response):
    engine.say(response)
    engine.runAndWait()

# Function to recognize speech using the SpeechRecognition library
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

# Function to respond to user input using the generative model
def respond_to_user_input(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitive comparison

    if "exit" in user_input:
        response = "Goodbye! Exiting..."
        print("Response:", response)
        speak(response)
        exit()  # Exit the program

    # Generate a response using the generative model
    response = model.generate_content(prompt_parts)

    print("Response:", response)
    speak(response)

# Main function that continuously listens for user input and responds
def main():
    while True:
        user_input = recognize_speech()
        if user_input:
            respond_to_user_input(user_input)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
