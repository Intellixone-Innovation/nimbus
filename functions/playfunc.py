# NEEDS SETUP

import subprocess
import webbrowser
from pytube import YouTube
import pygame

# Initialize the Pygame mixer for audio playback
pygame.mixer.init()

# Function to play a YouTube video
def play_youtube_video(video_url):
    try:
        yt = YouTube(video_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()
        video_file = yt.title + ".mp4"
        subprocess.Popen(["mpv", video_file])  # Assuming 'mpv' is installed for video playback
        return f"Playing video: {yt.title}"

    except Exception as e:
        return f"An error occurred while playing the YouTube video: {str(e)}"

# Function to play a local music file
def play_local_music(music_file):
    try:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play()
        return f"Playing music: {music_file}"

    except pygame.error as e:
        return f"An error occurred while playing the music: {str(e)}"

# Function to handle user requests to play videos or music
def handle_play_request(input_text):
    if "play video from YouTube" in input_text.lower():
        # Extract the YouTube video URL from the user's input
        words = input_text.split()
        if len(words) >= 5:
            video_url = " ".join(words[4:])
            return play_youtube_video(video_url)
        else:
            return "Please provide a valid YouTube video URL."

    elif "play music" in input_text.lower():
        # Extract the local music file path from the user's input
        words = input_text.split()
        if len(words) >= 3:
            music_file = " ".join(words[2:])
            return play_local_music(music_file)
        else:
            return "Please provide the path to a valid music file."

    else:
        return "I'm not sure how to respond to that."

# You can add more functions to handle specific video or music sources as needed.
