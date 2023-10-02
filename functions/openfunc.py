import webbrowser
import subprocess
import os

# Function to open a website
def open_website(website_url):
    try:
        website_url = website_url
        
        # Specify the path to the Google Chrome executable (change this to your Chrome installation path)
        chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

        # Set the web browser to Google Chrome
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        
        webbrowser.get('chrome').open_new(website_url)
        return f"Opening {website_url} in your web browser."
    except Exception as e:
        return f"An error occurred while opening the website: {str(e)}"

# Function to open an application
def open_app(app_name):
    try:
        # Replace the placeholders with the actual commands to open the apps on your system.
        # You should customize these commands based on your operating system and app locations.
        if "notepad" in app_name.lower():
            subprocess.Popen(["notepad.exe"])
            return "Opening Notepad."
        elif "calculator" in app_name.lower():
            subprocess.Popen(["calc.exe"])
            return "Opening Calculator."
        else:
            return f"Sorry, I don't know how to open {app_name}."
    except Exception as e:
        return f"An error occurred while opening the app: {str(e)}"

# Function to handle user requests to open websites or apps
def handle_open_request(input_text):
    if "open website" in input_text.lower():
        # Extract the website URL from the user's input (e.g., "open website www.example.com")
        words = input_text.split()
        if len(words) >= 3:
            website_url = words[2]
            return open_website(website_url)
        else:
            return "Please provide a valid website URL."

    elif "open app" in input_text.lower():
        # Extract the app name from the user's input (e.g., "open app Notepad")
        words = input_text.split()
        if len(words) >= 3:
            app_name = " ".join(words[2:])
            return open_app(app_name)
        else:
            return "Please provide the name of the app you want to open."

    else:
        return "I'm not sure how to respond to that."