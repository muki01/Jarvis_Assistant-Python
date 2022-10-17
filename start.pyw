import os
import speech_recognition as sr
from playsound import playsound

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.energy_threshold = 6500
        command.dynamic_energy_threshold = True
        audio = command.listen(source,phrase_time_limit=15)

        try:
            query = command.recognize_google(audio, language='tr-TR')

        except Exception:
            return ""

        return query.lower()

playsound("./SoundEffects/open2.mp3")
while True:
    start = takecommand()

    if start == "uyan" or  start == "uyan jarvis" or start == "hey jarvis":
        os.startfile('jarvis-turkce.py')

    if start == "wake up" or start == "wake up jarvis":
        os.startfile('jarvis-english.py')