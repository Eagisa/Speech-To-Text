import speech_recognition as sr
import pyautogui

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to your voice and type the transcribed text
def listen_and_type():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Use Google Web Speech API to recognize speech
            text = recognizer.recognize_google(audio)
            print(f"Recognized: {text}")

            # Simulate typing the recognized text with a faster typing speed
            pyautogui.typewrite(text)  # Adjust the interval as needed

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        listen_and_type()