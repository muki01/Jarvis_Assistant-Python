import os
import speech_recognition as sr
from playsound import playsound

import pystray
import PIL.Image
import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
edgeOptions = Options()
edgeOptions.add_argument("--headless")
import time


def TrayIcon():
    image = PIL.Image.open("./VideoEffects/jarvis.png")

    def on_clicked(icon,item):
        if str(item)=="Say Hello":
            print("Hello")
        elif str(item)=="Light":
            msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
            msedge.get ("http://192.168.0.90/")
            time.sleep(1)
            msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
            msedge.quit()
        elif str(item)=="Exit":
            icon.stop()

    icon = pystray.Icon("Jarvis",image,menu=pystray.Menu(
        pystray.MenuItem("Say Hello",on_clicked),
        pystray.MenuItem("Menu",pystray.Menu(
            pystray.MenuItem("Light",on_clicked)
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
playsound("./SoundEffects/open2.mp3")
while True:
    if t1.is_alive()==True:
        start = takecommand()

        if start == "uyan" or  start == "uyan jarvis" or start == "hey jarvis":
            os.startfile('jarvis-turkce.py')

        if start == "wake up" or start == "wake up jarvis":
            os.startfile('jarvis-english.py')
            
    elif t1.is_alive()==False:
        print("exiting")
        exit()