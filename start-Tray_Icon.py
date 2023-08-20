import os
import speech_recognition as sr
import requests

import pystray
import PIL.Image
import threading
import time

def TrayIcon():
    image = PIL.Image.open("./VideoEffects/jarvis.png")

    def on_clicked(icon,item):
        if str(item)=="Led On":
            requests.get("http://192.168.0.90/win&T=1")
        elif str(item)=="Led Off":
            requests.get("http://192.168.0.90/win&T=0")
        elif str(item)=="Exit":
            os.system("taskkill /f /im Rainmeter.exe")
            os.system("taskkill /f /im wallpaper64.exe")
            icon.stop()

    icon = pystray.Icon("Jarvis",image,menu=pystray.Menu(
        pystray.MenuItem("Menu",pystray.Menu(
            pystray.MenuItem("Led On",on_clicked),
            pystray.MenuItem("Led Off",on_clicked)
        )),
        pystray.MenuItem("Exit",on_clicked),
    ))
    icon.run()

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

t1 = threading.Thread(target=TrayIcon)
t1.start()
#playsound("./SoundEffects/open2.mp3")
while True:
    if t1.is_alive()==True:
        start = takecommand()

        if start == "uyan" or  start == "uyan jarvis" or start == "hey jarvis":
            os.startfile('turkce.py')

        if start == "wake up" or start == "wake up jarvis":
            os.startfile('english.py')
            
    elif t1.is_alive()==False:
        print("exiting")
        exit()