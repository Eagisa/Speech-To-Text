import os
import speech_recognition as sr
from datetime import datetime
import logging

# Get the user's home directory
user_home = os.path.expanduser('~')

# Define the path to the log folder and log file
log_folder_path = os.path.join(user_home, 'AppData', 'Local', 'SpeechToText', 'logs')
log_file_path = os.path.join(log_folder_path, 'Microphone.log')

# Create the log folder if it doesn't exist
if not os.path.exists(log_folder_path):
    os.makedirs(log_folder_path)

# Configure the logging settings
logging.basicConfig(filename=log_file_path, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to your voice and save the transcribed text to a txt file
def listen_and_save_to_file(filename):
    try:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            # Use Google Web Speech API to recognize speech
            text = recognizer.recognize_google(audio)

        # Save the recognized text to the specified file, overwriting previous content
        with open(filename, 'w') as file:
            file.write(text)

    except sr.UnknownValueError:
        # Log the date and time of the "could not understand audio" event
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %I:%M:%S %p")  # Updated time format
        logging.error(f"Could not understand audio at {current_time}")

    except sr.RequestError as e:
        logging.error(f"RequestError occurred: {e}")

if __name__ == "__main__":
    file_path = os.path.join(user_home, 'AppData', 'Local', 'SpeechToText', 'speech.txt')

    try:
        while True:
            listen_and_save_to_file(file_path)
    except KeyboardInterrupt:
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %I:%M:%S %p")  # Updated time format
        logging.error(f"Program terminated. {current_time}")