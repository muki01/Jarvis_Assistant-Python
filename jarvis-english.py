import os
from playsound import playsound
os.system("mode 40,5")
playsound("./SoundEffects/start3.mp3", False)
import pyttsx3
import speech_recognition as sr
from datetime import datetime
import webbrowser
import random
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import serial
import time
import speedtest
import wikipedia
import pywhatkit
import requests
import psutil
import vlc
import cv2
import threading
from Codes.faceRec import faceRecognition
from Codes.itemDetect import itemDetection
from Codes.fingerCounter import cntFingers

#playsound(random.choice(["./SoundEffects/start.mp3","./SoundEffects/start3.mp3"]), False)
JarvisUI = vlc.MediaPlayer("./VideoEffects/JarvisUI.mp4")
PasswordHack = vlc.MediaPlayer("./VideoEffects/Hack.mp4")

try:
    arduino = serial.Serial('COM5',9600)
    arduinoChecker = True
except:
    arduinoChecker = False
    print("Arduino not Found")
wikipedia.set_lang("en")
edgeOptions = Options()
edgeOptions.add_argument("--headless")
edgeOptions.add_argument("--disable-extensions")
#edgeOptions.add_argument("--disable-gpu")
#edgeOptions.add_argument("--disable-dev-shm-usage")

Assistant = pyttsx3.init("sapi5")
voices = Assistant.getProperty("voices")
Assistant.setProperty("voice",voices[1].id)
Assistant.setProperty("rate", 170)

def Speak(audio):
    Assistant.say(audio)
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        command.energy_threshold = 9000  
        command.dynamic_energy_threshold = True  
        print('\033[36m' + "listening...",)
        audio = command.listen(source,phrase_time_limit=15)

        try:
            print('\033[31m' + "Recognizing...")
            query = command.recognize_google(audio, language="en-US")
            print ('\033[37m' + f"You Saind : {query}")

        except Exception:
            return ""

        return query.lower()

def greeting():
    hour = datetime.now().hour
    if hour >=6 and hour < 12:
        Speak("Good morning sir")
    elif hour >= 12 and hour <18:
        Speak("Good afternoon sir")
    else:
        Speak("Good evening sir")
    Speak("What can i do for you")

def respond():

    #################OPENING COMMANDS

    if query =="jarvis":
        Speak("Yes sir")

    elif "hello" in query: #or "hi" in query:
        Speak("Hello sir")

    elif query =="ok":
        Speak("Is there anything you want me to do sir?")

    elif "nope" in query or "no" in query or "nothing" in query or "shut up" in query or "wait" in query or "wait a second" in query:
        Speak("Okay sir")

    elif "can you hear me" in query or "are you here" in query:
        Speak("Yes sir. What do you want me to do")

    elif "how are you" in query or "are you ok" in query:
        Speak("I am fine sir what about you")

    elif "i am fine" in query:
        Speak("I am happy sir")

    elif "what are you doing" in query:
        Speak("I am waiting for your command sir")

    elif "nice job" in query or "bravo" in query or "good job" in query or "you are great" in query or "nice work" in query:
        Speak("Thank you sir")

    elif "thanks" in query or "thank you" in query:
        Speak("Anytime sir")

    elif "i love you" in query:
        Speak("I love you too sir")

    elif "why aren't you answering" in query or "answer" in query:
        Speak("Can you say it again sir")

    elif "*" in query:
        Speak("Sorry if i made a mistake sir")

    elif "change the language" in query:
        Speak("Ok sir the language is getting turkish")
        os.startfile("jarvis-turkce.py")
        exit()



    #################INFORMATION ABOUT JARVIS

    elif "what is your name" in query or "what's your name" in query or "who are you" in query:
        Speak("My name is Jarvis sir")

    elif "what is your nickname" in query or "what's your nickname" in query:
        Speak("My nickname is Jarko sir")

    elif "where are you from" in query:
        Speak("I am from Zimovina sir")

    elif "how old are you" in query:
        Speak("I am 1453 years old sir")

    elif "do you have a girlfriend" in query:
        Speak("Not for now sir")

    elif "which languages can you speak" in query:
        Speak("I can speak all languages but you have to recode me for this sir")

    elif "what is your father's name" in query or "what is your mother's name" in query:
        Speak("My father and mother are both Muksin sir")

    elif "what can you do" in query:
        Speak("I can chat with you, tell the time and date, search on Google, Wikipedia and YouTube, turn apps on and off, and control lights in the house")

    elif "how much is this" in query:
        fingers = cntFingers()
        #print(val)
        if fingers == 0:
            Speak("I can't see sir")
        else:
            Speak(str(fingers) + "sir")
        time.sleep(2)
        cv2.destroyAllWindows()



    ######################INFORMATION ABOUT ME

    elif "what is my name" in query or "what's my name" in query:
        face_names = faceRecognition()
        face_names = ['Ayşe' if item=='Ayshe' else item for item in face_names]
        print(face_names)
        if face_names !=[]:
            if len(face_names) < 2:
                if "Unknown" in face_names:
                    Speak("I don't know you sir")
                else:
                    Speak(f"Your name is {face_names} sir")
            else:
                Speak("Come one by one")
        else:
            Speak("I can't see, sir, can you stand in front of the camera?")
        time.sleep(2)
        cv2.destroyAllWindows()

    elif "what does my name mean" in query:
        Speak("The meaning of your name is the one who does good and good deeds sir")

    elif "what is my nickname" in query or "what's my nickname" in query:
        Speak("Your nickname is Muki sir")

    # elif "what is my grandmother's name" in query or "what's my grandmother's name" in query:
    #     Speak("Koca Annenizin ismi Ayşe efendim")

    # elif "what is my grandfather's name" in query or "what's my grandfather's name" in query:
    #     Speak("Koca Babanızın ismi Bekir efendim")

    #elif "dedemin ismi ne" in query or "dedemin adı ne" in query:
    #    Speak("Dedenizin ismi Muhsin efendim")

    #elif "nenemin ismi ne" in query or "nenemin adı ne" in query:
    #    Speak("Nenenizin ismi Nefie efendim")

    elif "what is my brother's name" in query or "what's my brother's name" in query:
        Speak("Hes name is Bekir sir")

    elif "what is my mother's name" in query or "what's my mother's name" in query:
        Speak("Her name is Nurten sir")

    elif "what is my father's name" in query or "what's my father's name" in query:
        Speak("Hes name is Halil sir")

    #elif "benim nasıl arabam var" in query:
    #    Speak("Sizin canavar gibi bir Opelınız var efendim")

    #elif "abimin nasıl arabası var" in query:
    #    Speak("Ağbinizin zvyar gibi bir BMW si var efendim")

    #elif "babamın nasıl arabası var" in query:
    #    Speak("Babanızın zvyar gibi bir volkswagen touranı var efendim")

    #elif "annemin nasıl arabası var" in query:
    #    Speak("Anneizin araba ile işi yok efendim")

    elif "what is my age" in query or "how old am i" in query or "what's my age" in query:
        Speak("You are 18 years old sir")

    elif "where am i from" in query:
        Speak("You are from Zimovina sir.")

    elif "when is my birthday" in query or "when was i born" in query:
        Speak("Your birthday is January 12, 2004, sir.")



    ####################CLOCK DATE

    elif "what is the time" in query or "what's the time" in query or "what time is it" in query:
        time = datetime.now().strftime("%H:%M")
        print(time)
        Speak("Time is" + time + "sir")

    elif "what day is it" in query or "tell today's date" in query or "what is the date" in query or "what's the date" in query:
        date = datetime.now().strftime("%d:%B:%Y")
        print(date)
        Speak("Today is" + date + "sir")

    elif "what is the temperature" in query or "what's the temperature" in query:
        api = "baecdbf7f75171e614a981fc4acba560"
        url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=" + "Zimovina" + "&appid=" + api
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"{int(temp)} derece, {humidity}% nem , gökyüzü {description}")
        Speak(f"The temperature in Zimovina is {int(temp)} degrees, humidity is {humidity} percent and sky is {description} sir")

    elif "set alarm" in query:
        Speak("Enter time sir")
        timeInput = input("Enter time: ")
        def alarm():
            while True:
                timeReal = datetime.now().strftime("%H:%M")
                time.sleep(1)
                if timeReal == timeInput:
                    playsound("./SoundEffects/alarm.mp3",False)
                    break
        t1 = threading.Thread(target=alarm)
        t1.start()


    #####################OPEN & SEARCH
    elif "search" in query and "on google" in query:
        try:
            if query == "search on google":
                Speak("What do you want me to search sir")
                search = takecommand()
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                Speak("searching" + search)
            else:
                search = query.replace("on google", "")
                search2 = search.replace("search", "")
                url = "https://www.google.com/search?q=" + search2
                webbrowser.get().open(url)
                Speak("searching" + search2)
        except:
            Speak("I don't understand sir")

    elif "search" in query and "on youtube" in query:
        try:
            if query == "search on youtube":
                Speak("What do you want me to search sir")
                search = takecommand()
                url = "https://www.youtube.com/results?search_query=" + search
                webbrowser.get().open(url)
                Speak("searching" + search)
            else:
                search = query.replace("on youtube", "")
                search2 = search.replace("search", "")
                url = "https://www.youtube.com/results?search_query=" + search2
                webbrowser.get().open(url)
                Speak("searching" + search2)
        except:
            Speak("I don't understand sir")

    elif "open" in query and "on youtube" in query:
        try:
            if query == "open on youtube":
                Speak("What do you want me to open sir")
                search = takecommand()
                pywhatkit.playonyt(search)
                Speak("opening" + search)
            else:
                search = query.replace("on youtube", "")
                search2 = search.replace("open", "")
                pywhatkit.playonyt(search2)
                Speak("opening" + search2)
        except:
            Speak("I don't understand sir")

    elif "search on wikipedia" in query or "wikipedia" in query:
        Speak("What do you want me to search sir")
        while True:
            try:
                search = takecommand()
                if search == "ok":
                    Speak("Ok sir")
                    break
                else:
                    result = wikipedia.summary(search, sentences=3)
                    print(result)
                    Speak(result)
                    break
            except:
                Speak("I don't understand sir")

    elif "who is" in query or "what is" in query:
        try:
            search = query.replace("who is", "")
            search2 = search.replace("what is", "")
            print(search2)
            result = wikipedia.summary(search2, sentences=3)
            print(result)
            Speak(result)
        except:
            Speak("I don't understand sir")


    ################################################################################################
    elif "open google" in query:
        webbrowser.get().open("www.google.com")
        Speak("Opening Google")

    elif "open youtube" in query:
        webbrowser.get().open("www.youtube.com")
        Speak("Opening YouTube")

    elif "open facebook" in query:
        webbrowser.get().open("www.facebook.com")
        Speak("Opening Facebook")

    elif "open instagram" in query:
        webbrowser.get().open("www.instagram.com")
        Speak("Opening Instagram")

    elif "open microsoft office" in query or "open office" in query:
        webbrowser.get().open("https://www.office.com")
        Speak("Opening Microsoft Office")

    elif "open ets 2" in query or "open euro truck simulator 2" in query or "open ets2" in query:
        os.startfile("E:/Games/Euro Truck Simulator 2/bin/win_x64/eurotrucks2.exe")
        Speak("Opening Euro Truck Simulator 2")

    elif "open rocket league" in query:
        webbrowser.get().open("com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true")
        Speak("Opening Rocket League") 

    elif "open notepad" in query or "open the notepad" in query:
        os.startfile("C:/Windows/system32/notepad.exe")
        Speak("Opening notepad")

    elif "take a note" in query:
        Speak("What would you like the file name to be sir")
        nameFile = takecommand() + ".txt"
        Speak("what do you want to record sir")
        textFile = takecommand()
        home_directory = os.path.expanduser( '~' )
        File = open(f"{home_directory}\Desktop/{nameFile}", "w", encoding="utf-8")
        File.writelines(textFile)
        File.close
        Speak("The file was saved successfully")

    elif "open task manager" in query:
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("esc")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        Speak("Opening task manager sir")

    elif "open cameras" in query:
        os.startfile("E:/CMS/CMS.exe")
        Speak("Opening cameras sir")

    elif "open face recognition camera" in query:
        Speak("Ok sir")
        def faceRec():
            while  True:
                faceRecognition()
                key = cv2.waitKey(1)
                if key == 27 or query == "close the face recognition camera":
                    break
            cv2.destroyAllWindows()
        t1 = threading.Thread(target=faceRec)
        t1.start()

    elif "open item detection camera" in query:
        Speak("Ok sir")
        def itemDetect():
            while  True:
                itemDetection()
                key = cv2.waitKey(1)
                if key == 27 or query == "close the item detection camera":
                    break
            cv2.destroyAllWindows()
        t1 = threading.Thread(target=itemDetect)
        t1.start()



    #######################   MEDIA

    elif "start the music" in query or "stop the music" in query:
        pyautogui.press("playpause")
        Speak("Ok sir")

    elif "change the music" in query or "next music" in query:
        pyautogui.press("nexttrack")
        Speak("Changing the music sir")

    elif "previous music" in query or "open previous music" in query:
        pyautogui.press("prevtrack")
        Speak("Changing the music sir")

    elif "increase volume by" in query or "raise volume by" in query:
        try:
            if query == "increase volume by" or query == "raise volume by":
                Speak("How much do you want me to raise sir")
                while True:
                    try:
                        level = takecommand()
                        if level == "ok":
                            Speak("Ok")
                            break
                        else:
                            realLevel = int(level) / 2
                            pyautogui.press("volumeup", presses=int(realLevel))
                            Speak(f"Ok sir volume increasing by {level}")
                            break
                    except:
                        Speak("I don't understand sir")
            else:
                level = query.replace("increase volume by", "")
                level2 = level.replace("raise volume by", "")
                realLevel = int(level2) / 2
                pyautogui.press("volumeup", presses=int(realLevel))
                Speak(f"Ok sir volume increasing by {level2}")
        except:
            Speak("I don't understand sir")

    elif "decrease volume by" in query or "reduce volume by" in query:
        try:
            if query == "decrease volume by" or "reduce volume by":
                Speak("How much reduction do you want sir")
                while True:
                    try:
                        level = takecommand()
                        if level == "ok":
                            Speak("Ok sir")
                            break
                        else:
                            realLevel = int(level) / 2
                            pyautogui.press("volumedown", presses=int(realLevel))
                            Speak(f"Ok sir volume reducing by {level}")
                            break
                    except:
                        Speak("I don't understand sir")
            else:
                level = query.replace("decrease volume by", "")
                level2 = level.replace("reduce volume by", "")
                realLevel = int(level2) / 2
                pyautogui.press("volumedown", presses=int(realLevel))
                Speak(f"Ok sir volume reducing by {level2}")
        except:
            Speak("I don't understand sir")



    #####################################MASA LAMBASI

    elif "desk light off" in query or "desk light on" in query or "turn on the desk light" in query or "turn off the desk light" in query:
        Speak("Ok sir")
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        time.sleep(1)
        msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
        if "off" in query and arduinoChecker ==True:
            arduino.write(b'2')
        elif "on" in query and arduinoChecker ==True:
            arduino.write(b'1')
        msedge.quit()

    elif "desk light colour" in query:
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get("http://192.168.0.90/")
        Speak("What color you want to change sir")
        while True:
            try:
                colorr = takecommand()
                if colorr == "ok":
                    Speak("Ok sir")
                    break
                elif colorr == "red":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[1]').click()
                    Speak("Ok sir the desk lamp is changing to red")
                    break
                elif colorr == "orange":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[2]').click()
                    Speak("Ok sir the desk lamp is changing to orange")
                    break
                elif colorr == "yellow":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[3]').click()
                    Speak("Ok sir the desk lamp is changing to yellow")
                    break
                elif colorr == "warm white":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[4]').click()
                    Speak("Ok sir the desk lamp is changing to warm white")
                    break
                elif colorr == "white":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[5]').click()
                    Speak("Ok sir the desk lamp is changing to white")
                    break
                elif colorr == "pink":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[7]').click()
                    Speak("Ok sir the desk lamp is changing to pink")
                    break
                elif colorr == "blue":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[8]').click()
                    Speak("Ok sir the desk lamp is changing to blue")
                    break
                elif colorr == "cyan":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[9]').click()
                    Speak("Ok sir the desk lamp is changing to cyan")
                    break
                elif colorr == "green":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[10]').click()
                    Speak("Ok sir the desk lamp is changing to green")
                    break
                elif colorr == "random" or colorr == "random color":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[11]').click()
                    Speak("Ok sir the desk lamp is changing to random color")
                    break
                else:
                    Speak("Say another color sir")
            except:
                Speak("I don't understand sir")
        msedge.quit()
    
    elif "desk light effect" in query:
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        Speak("Which effect you want to select sir")
        while True:
            try:
                effect = takecommand()
                if effect == "ok":
                    Speak("Ok sir")
                    break
                elif effect == "rainbow":
                    Speak("Ok sir desk lamp is making rainbow")
                    os.system("taskkill /f /im LedFx.exe")
                    msedge.find_element(By.XPATH,'//*[@id="bot"]/button[4]').click()
                    time.sleep(1)
                    msedge.find_element(By.XPATH,'//*[@id="p1o"]/div[2]').click()
                    break
                elif effect == "normal":
                    Speak("Ok sir desk lamp is making normal")
                    os.system("taskkill /f /im LedFx.exe")
                    msedge.find_element(By.XPATH,'//*[@id="bot"]/button[4]').click()
                    time.sleep(1)
                    msedge.find_element(By.XPATH,'//*[@id="p10o"]/div[2]').click()
                    break
                elif effect == "bass effect":
                    os.startfile("E:\LedFx\data\LedFx.exe")
                    Speak("Ok sir desk lamp is making bass effect")
                    break
                else:
                    Speak("You can say rainbow or normal sir")
            except:
                Speak("I don't understand sir")
        msedge.quit()


    #################################################################

    elif "change the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        #time.sleep(1)
        pyautogui.keyUp("alt")
        Speak("Ok sir")

    elif "close the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("f4")
        #time.sleep(1)
        pyautogui.keyUp("alt")
        Speak("Ok sir")

    elif "minimise the window" in query:
        pyautogui.keyDown("win")
        pyautogui.press("down")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Ok sir")

    elif "minimise the windows" in query:
        pyautogui.keyDown("win")
        pyautogui.press("m")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Ok sir")

    elif "maximise window" in query:
        pyautogui.keyDown("win")
        pyautogui.press("up")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Ok sir")

    elif "press the" in query and "button" in query:
        button = query.replace("press the ", "")
        button = button.replace(" button", "")
        pyautogui.press(button)
        Speak("Ok sir")

    #################################################################

    elif "open my playlist" in query:
        webbrowser.get().open("https://www.youtube.com/watch?v=H9aq3Wj1zsg&list=RDH9aq3Wj1zsg&start_radio=1")
        Speak("Opening your playlist sir")

    elif "make speed test" in query:
        Speak("Ok sir wait 10 15 seconds")
        speed = speedtest.Speedtest()
        download = speed.download()
        upload = speed.upload()
        correctDown = int(download/800000)
        correctUp = int(upload/800000)
        Speak(f"Downloading speed is {correctDown-10} megabit per seccong and uploading speed is {correctUp-10} megabit per seccong")

    elif "open the bluetooth" in query or "close the bluetooth" in query:
        pyautogui.keyDown("win")
        pyautogui.press("a")
        pyautogui.keyUp("win")
        pyautogui.click(x=1400, y=900)
        pyautogui.keyDown("win")
        pyautogui.press("a")
        pyautogui.keyUp("win")
        Speak("Ok sir")

    elif "take screenshot" in query or "take ss" in query:
        img= pyautogui.screenshot()
        home_directory = os.path.expanduser( '~' )
        img.save(f"{home_directory}/Desktop/screenshot.png")
        Speak("Screenshot taken sir")

    elif "what is the battery" in query or "battery level" in query:
        battery = psutil.sensors_battery()
        percent = battery.percent
        Speak(f"The battery is {percent} percent sir")


    #################################################################

    elif "close the browser" in query:
        os.system("taskkill /f /im msedge.exe")
        Speak("Web browser is closing sir")

    elif "shut down the computer" in query or "shut down the pc" in query:
        Speak("Ok sir the computer is shutting down")
        os.system("shutdown /s /t 5")

    elif "restart the computer" in query or "restart the pc" in query:
        Speak("Ok sir the computer is restarting")
        os.system("shutdown /r /t 5")

    elif "sleep mode" in query or "put the computer to sleep" in query:
        Speak("Ok sir the computer is going to sleep mode")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "put everything to sleep" in query:
        Speak("Ok sir everything is going to sleep mode")
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        time.sleep(1)
        msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
        #arduino.write(b'1')
        msedge.quit()
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


    #################################################################

    elif "hahaha" in query or "he he" in query:
        playsound("./SoundEffects/laugh.mp3")

    elif "fart" in query or "fart sound" in query:
        farts = random.choice(["./SoundEffects/fart.mp3","./SoundEffects/fart2.mp3"])
        playsound(farts)

    elif "crack the password" in query:
        Speak("Ok sir, the password cracking module is running")
        def PasswordHac():
            PasswordHack.toggle_fullscreen()
            PasswordHack.play()
            time.sleep(28)
            PasswordHack.stop()
            #Speak("şifre başarıyla kırıldı efendim")
        t1 = threading.Thread(target=PasswordHac)
        t1.start()

    elif "open your own interface" in query:
        Speak("Ok sir")
        def JarvisU():
            JarvisUI.toggle_fullscreen()
            JarvisUI.play()
            time.sleep(62)
            JarvisUI.stop()
        t1 = threading.Thread(target=JarvisU)
        t1.start()

    elif "close your own interface" in query:
        JarvisUI.stop()
        Speak("Ok sir")




    elif "connect to the robot" in query:
        Speak("Ok sir connecting to the robot")
        robotIP="http://192.168.0.50"
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        Speak("Ready sir")
        while True:
            try:
                command = takecommand()
                if "go forward" in command:
                    msedge.get (f"{robotIP}/?State=F")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "go back" in command:
                    msedge.get (f"{robotIP}/?State=B")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "turn right" in command:
                    msedge.get (f"{robotIP}/?State=R")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "turn left" in command:
                    msedge.get (f"{robotIP}/?State=L")
                    time.sleep(0.3)
                    msedge.get (f"{robotIP}/?State=S")
                elif "exit" in command:
                    Speak("Ok sir exiting the robot")
                    msedge.quit()
                    break
            except:
                Speak("There was an error sir")

    elif "connect to the camera" in query:
        Speak("Ok sir connect to the camera")
        kameraIP="http://admin:123456@192.168.0.234"
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        Speak("Ready sir")
        while True:
            try:
                command = takecommand()
                if "turn right" in command or "right" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                    Speak("Ready sir")
                elif "turn left" in command or "left" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                    time.sleep(0.3)
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                    Speak("Ready sir")
                elif "up" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_up&lang=eng")
                    Speak("Ready sir")
                elif "down" in command:
                    msedge.get(f"{kameraIP}/cgi-bin/action?action=cam_mv&diretion=cam_down&lang=eng")
                    Speak("Ready sir")
                elif "exit" in command:
                    Speak("Ok sir exiting the camera")
                    msedge.quit()
                    break
            except:
                Speak("There was an error sir")

    
os.startfile(".\Required\Rainmeter\Rainmeter.exe")
greeting()
while True:
    query = takecommand()
    if query !="":
        respond()
                
    if query == "you can sleep"  or query == "sleep" or query == "goodbye" or query == "goodbay":
        Speak("Ok sir, you can call me if you need me")
        os.system("taskkill /f /im Rainmeter.exe")
        exit()
    