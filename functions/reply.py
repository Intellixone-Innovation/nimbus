import random

# Function to generate a random emoticon
def get_random_emoticon():
    emotions = ["happy", "sad", "angry", "confused", "sleepy"]
    random_emotion = random.choice(emotions)

    emoticons = {
        "happy": "😄",
        "sad": "😢",
        "angry": "😠",
        "confused": "😕",
        "sleepy": "😴"
    }

    return emoticons.get(random_emotion, "😐")  # Default to a neutral emoticon if emotion is not recognized

# Function to explain what dino.ai is
def Introduction():
    return (
        "Nimbus is a fictional AI assistant designed to help users with various tasks. "
        "It can provide information, answer questions, set reminders, and much more. "
        f"{get_random_emoticon()}"
    )

# Function to provide information about the creator
def creator():
    return (
        "Nimbus AI was created by Debarshee Chakraborty, a passionate developer who enjoys building AI-powered applications "
        "to make people's lives easier. "
        f"{get_random_emoticon()}"
    )

# Function to provide information about the startup
def startup():
    return (
        "Numbus AI was created by Intellixone Innovation, a passionate developer who enjoys building AI-powered applications "
        "to make people's lives easier. "
        f"{get_random_emoticon()}"
    )

# Function to provide information about capabilities
def purpose():
    return (
        "Nimbus can perform a wide range of tasks, including answering questions, setting reminders, "
        "providing weather updates, and much more. "
        f"{get_random_emoticon()}"
    )

# Function to explain the technology behind Nimbus
def technology():
    return (
        "Nimbus is powered by advanced natural language processing (NLP) and machine learning technologies. "
        "It uses state-of-the-art AI frameworks to understand and respond to user input. "
        f"{get_random_emoticon()}"
    )
