import os
from playsound import playsound
# os.system("mode 40,5")
# playsound("./SoundEffects/start3.mp3", False)
import asyncio
import edge_tts
import speech_recognition as sr
import webbrowser
import pyautogui
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.options import Options
import serial
import time
from datetime import datetime
import random
import speedtest
import wikipedia
import pywhatkit
import requests
import cv2
import threading
import openai
# from Codes.faceRec import faceRecognition
# from Codes.itemDetect import itemDetection
# from Codes.fingerCounter import cntFingers

openai.api_key = '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'
wikipedia.set_lang("tr")
# edgeOptions = Options()
# edgeOptions.add_argument("--headless")
# edgeOptions.add_argument("--disable-extensions")
# edgeOptions.add_argument("--disable-gpu")
# edgeOptions.add_argument("--disable-dev-shm-usage")

VOICE = "bg-BG-BorislavNeural"
OUTPUT_FILE = "voice.mp3"
def Speak(audio, disableBackground=False):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(_main(audio))
    #asyncio.get_event_loop().run_until_complete(_main(audio))
    playsound("voice.mp3", disableBackground)
    os.remove("voice.mp3")

async def _main(TEXT) -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        # command.energy_threshold = 3500  
        # command.dynamic_energy_threshold = True  
        print('\033[36m' + "Listening...")
        audio = command.listen(source,phrase_time_limit=15)

        try:
            print('\033[31m' + "Recognizing...")
            query = command.recognize_google(audio, language="bg-BG")
            print ('\033[33m' + f"You Saind: "+ '\033[37m' + f"{query}")

        except Exception as error:
            return ""

        return query.lower()

def openAI(speech):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{speech}"}]) 
    response_text = response.choices[0].message.content
    print('\033[32m' + f"OpenAI response: " + '\033[37m' + f"{response_text}")
    Speak(response_text,True)

def checkArduino():
    try:
        arduino = serial.Serial('COM5',9600)
        arduinoChecker = True
        print("Arduino Connected")
    except:
        arduinoChecker = False
        print("Arduino not Found")

def greeting():
    hour = datetime.now().hour
    if hour >=6 and hour < 12:
        Speak("Добро утро сър")
    elif hour >= 12 and hour <18:
        Speak("Добър ден сър")
    else:
        Speak("Добър вечер сър")
    Speak("Какво мога да направя за вас")

def respond():
    if query =="jarvis":
        Speak("Да сър")

    elif "здравей" in query or "здрасти" in query:
        Speak("Зрасти сър")

    elif "добре" in query:
        Speak("Има ли нещо, което искате да направя сър?")

    elif "не" in query or "няма" in query or "sus" in query or "kapa çeneni" in query or "susabilirsin" in query or "bekle" in query or "bir saniye bekle" in query:
        Speak("Добре сър")

    elif "beni duyuyor musun" in query or "burada mısın" in query:
        Speak("Evet efendim. Ne yapmamı istersiniz")

    elif "как си" in query or "добре ли си" in query:
        Speak("Добре съм сър, вие как сте?")

    elif "добре съм" in query or "супер съм" in query:
        Speak("Радвам се да го чуя сър ")

    elif "какво правиш" in query:
        randomm = random.choice([
            "Чакам вашата команда сър",
            "Седя и ви слушам сър",
        ])
        Speak(randomm)

    elif "хубава работа" in query or "браво" in query or "добра работа" in query or "страхотен си" in query:
        Speak("Благодаря сър")

    elif "благодаря" in query or "мерси" in query:
        Speak("По всяко време сър")

    elif "обичам те" in query:
        Speak("Аз също ви обичам сър")

    elif "защо не ми отговаряш" in query or "отговори ми" in query:
        Speak("можете ли да повторите сър")

    elif "*" in query:
        Speak("Съжалявам, ако съм направил грешка сър")

    elif "смени езика" in query:
        Speak("Добре сър, езикът се сменя на английски")
        os.startfile("jarvis-english.py")
        exit()

    


    ################################################      INFORMATION ABOUT JARVIS

    elif "как се казваш" in query or "кой си ти" in query:
        Speak("Казвам се Джарвис сър")

    elif "как е твоя прякор" in query:
        Speak("Прякорът ми е Джарко сър")

    elif "от къде си" in query:
        Speak("Аз съм от Хасково, сър")

    elif "на колко години си" in query:
        Speak("Бях създаден преди 4 месеца сър")

    elif "имаш ли си приятелка" in query:
        Speak("Не за сега сър")

    elif "кои езици говориш" in query:
        Speak("Мога да говоря всички езици, но трябва да ме кодирате за това сър")

    elif "как се казва баща ти" in query or "как се казва майка ти" in query or "кой е твоят баща" in query or "коя е майка ти" in query:
        Speak("Вие сте мойта майка и баща сър")

    elif "какво можеш да направиш" in query:
        Speak("Мога да разговарям с вас, да казвам часа и датата, да търся в Google, Wikipedia и YouTube, да включвам и изключвам приложения и да контролирам осветлението в къщата.")

    elif "колко е това" in query:
        fingers = cntFingers()
        #print(val)
        if fingers == 0:
            Speak("Не разбрах сър")
        else:
            Speak(str(fingers) + "сър")
        time.sleep(2)
        cv2.destroyAllWindows()



    ######################INFORMATION ABOUT ME

    elif "как се казвам" in query or "кой съм аз" in query or "кой е това" in query:
        face_names = faceRecognition()
        face_names = ['Ayşe' if item=='Ayshe' else item for item in face_names]
        print(face_names)
        if face_names !=[]:
            if len(face_names) < 2:
                if "Unknown" in face_names:
                    Speak("Не ви познавам сър")
                else:
                    Speak(f"Вашето име е {face_names} сър")
            else:
                Speak("Моля елате един по един")
        else:
            Speak("Не виждам сър, можете ли да застанете пред камерата")
        time.sleep(2)
        cv2.destroyAllWindows()

    elif "какво означава моето име" in query:
        Speak("Значението на вашето име е този, който прави добро и добри дела сър")

    elif "как е моят прякор" in query:
        Speak("Вашият прякор е Муки сър")

    # elif "koca annemin ismi ne" in query or "koca annemin adı ne" in query:
    #     Speak("Koca Annenizin ismi Ayşe efendim")

    # elif "koca babamın ismi ne" in query or "koca babamın adı ne" in query:
    #     Speak("Koca Babanızın ismi Bekir efendim")

    # elif "dedemin ismi ne" in query or "dedemin adı ne" in query:
    #     Speak("Dedenizin ismi Muhsin efendim")

    # elif "nenemin ismi ne" in query or "nenemin adı ne" in query:
    #    Speak("Nenenizin ismi Nefie efendim")

    elif "как се казва брат ми" in query:
        Speak("Ağbinizin ismi Bekir efendim")

    elif "как се казва майка ми" in query:
        Speak("Annenizin ismi Nurten efendim")

    elif "как се казва баща ми" in query:
        Speak("Babanızın ismi Halil efendim")

    elif "каква кола имам" in query:
        Speak("Sizin canavar gibi bir Opelınız var efendim")

    elif "каква кола има брат ми" in query:
        Speak("Ağbinizin zvyar gibi bir BMW si var efendim")

    elif "каква кола има баща ми" in query:
        Speak("Babanızın zvyar gibi bir volkswagen touranı var efendim")

    elif "каква кола има майка ми" in query:
        Speak("Anneizin araba ile işi yok efendim")

    elif "на колко години съм" in query or "на колко съм" in query:
        Speak("Siz 18 yaşındasınız efendim")

    elif "откъде съм" in query or "къде живея" in query:
        Speak("Siz Zimovinalısınız efendim")

    elif "кога е рожденият ми ден" in query or "кога съм роден" in query:
        Speak("Sizin doğum gününüz 12 Ocak 2004 te efendim")



    ####################CLOCK DATE

    elif "колко е часа" in query or "можеш ли да ми кажеш колко е часа" in query:
        saat = datetime.now().strftime("%H:%M")
        print(saat)
        Speak("Часа е" + saat + "сър")

    elif "дата" in query or "какъв ден е днес" in query or "можете ли да кажете днешната дата" in query:
        tarih = datetime.now().strftime("%d:%B:%Y")
        print(tarih)
        Speak("Днес сме" + tarih + "сър")

    elif "каква е температурата" in query or "прогноза за времето" in query or "как е времето" in query:
        api = "baecdbf7f75171e614a981fc4acba560"
        url = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=" + "Zimovina" + "&appid=" + api
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        if description == "clear sky":
            description = "ясно"
        if description == "few clouds":
            description = "малко облачно"
        if description == "broken clouds":
            description = "разкъсано облачно"
        if description == "scattered clouds":
            description = "разкъсано облачно"
        if description == "cloudy":
            description = "облачно"
        if description == "light rain":
            description = "слабо дъждовно"
        if description == "overcast clouds":
            description = "облачно"
        print(f"{int(temp)} градуса, {humidity}% влага , небето е {description}")
        Speak(f"Времето в Зимовина {int(temp)} градуса, влагата е {humidity}% и небето е {description} сър")

    elif "настрой аларма" in query:
        Speak("Въведете час сър")
        timeInput = input("Въведете час: ")
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
    elif "google'da" in query and "ara" in query:
        try:
            if query == "google'da ara":
                Speak("Ne aramamı istersiniz efendim")
                search = takecommand()
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                Speak(search + "aranıyor")
            else:
                search = query.replace("google'da", "")
                search = search.replace("ara", "")
                search = search.replace("jarvis", "")
                url = "https://www.google.com/search?q=" + search
                webbrowser.get().open(url)
                Speak(search + "aranıyor")
        except:
            Speak("Anlayamadım efendim")

    elif "youtube'da" in query and "aç" in query:
        try:
            if query == "youtube'da aç":
                Speak("Ne açmamı istersiniz efendim")
                search = takecommand()
                pywhatkit.playonyt(search)
                Speak(search + "açılıyor")
            else:
                search = query.replace("youtube'dan", "")
                search = search.replace("youtube'da", "")
                search = search.replace("aç", "")
                search = search.replace("jarvis", "")
                pywhatkit.playonyt(search)
                Speak(search + "açılıyor")
        except:
            Speak("Anlayamadım efendim")

    elif "youtube'da" in query and "ara" in query:
        try:
            if query == "youtube'da ara":
                Speak("Ne aramamı istersiniz efendim")
                search = takecommand()
                url = "https://www.youtube.com/results?search_query=" + search
                webbrowser.get().open(url)
                Speak(search + "aranıyor")
            else:
                search = query.replace("youtube'da", "")
                search = search.replace("ara", "")
                search = search.replace("jarvis", "")
                url = "https://www.youtube.com/results?search_query=" + search
                webbrowser.get().open(url)
                Speak(search + "aranıyor")
        except:
            Speak("Anlayamadım efendim")

    elif "vikipedi'de ara" in query or "wikipedia" in query  or "vikipedi" in query:
        Speak("Ne aramamı istersiniz efendim")
        while True:
            try:
                search = takecommand()
                if search == "tamam":
                    Speak("Tamam efendim")
                    break
                else:
                    result = wikipedia.summary(search, sentences=3)
                    print(result)
                    Speak(result)
                    break
            except:
                Speak("Anlayamadım efendim")

    elif "kimdir" in query or "nedir"in query:
        try:
            search = query.replace("kimdir", "")
            search = search.replace("nedir", "")
            search = search.replace("jarvis", "")
            result = wikipedia.summary(search, sentences=3)
            print(result)
            Speak(result)
        except:
            Speak("Anlayamadım efendim")


    ################################################################################################
    elif "google aç" in query:
        webbrowser.get().open("www.google.com")
        Speak("Google açılıyor")

    elif "youtube aç" in query:
        webbrowser.get().open("www.youtube.com")
        Speak("Youtube açılıyor")

    elif "facebook aç" in query:
        webbrowser.get().open("www.facebook.com")
        Speak("Facebook açılıyor")

    elif "instagram aç" in query:
        webbrowser.get().open("www.instagram.com")
        Speak("İnstagram açılıyor")

    elif "microsoft office aç" in query or "ofis aç" in query:
        webbrowser.get().open("https://www.office.com")
        Speak("Microsoft Office açılıyor")

    elif "ets 2 aç" in query or "euro truck simulator 2 aç" in query or "ets2 aç" in query:
        os.startfile("E:/Games/Euro Truck Simulator 2/bin/win_x64/eurotrucks2.exe")
        Speak("Euro Truck Simulator 2 açılıyor")

    elif "roket lig aç" in query or "roketlik aç" in query:
        webbrowser.get().open("com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true")
        Speak("Roket lig açılıyor") 

    elif "not defterini aç" in query or "notepad aç" in query:
        os.startfile("C:/Windows/system32/notepad.exe")
        Speak("Notepad açılıyor")

    elif "not et" in query:
        Speak("Dosya ismi ne olsun efendim")
        nameFile = takecommand() + ".txt"
        Speak("Ne kaydetmek istiyorsun efendim")
        textFile = takecommand()
        home_directory = os.path.expanduser( '~' )
        File = open(f"{home_directory}\Desktop/{nameFile}", "w", encoding="utf-8")
        File.writelines(textFile)
        File.close
        Speak("Kayıt başarıyla tamamlandı efendim")

    elif "görev yöneticisi aç" in query:
        pyautogui.keyDown("ctrl")
        pyautogui.keyDown("shift")
        pyautogui.press("esc")
        pyautogui.keyUp("ctrl")
        pyautogui.keyUp("shift")
        Speak("Görev yöneticisi açılıyor efendim")

    elif "kameraları aç" in query or "güvenlik kameralarını aç" in query:
        os.startfile("E:/CMS/CMS.exe")
        Speak("Kameralar açılıyor")

    elif "yüz tanıma kamerasını aç" in query:
        Speak("Tamam efendim")
        def faceRec():
            while  True:
                faceRecognition()
                key = cv2.waitKey(1)
                if key == 27 or query == "yüz tanıma kamerasını kapat":
                    break
            cv2.destroyAllWindows()
        t1 = threading.Thread(target=faceRec)
        t1.start()

    elif "nesne tanıma kamerasını aç" in query:
        Speak("Tamam efendim")
        def itemDetect():
            while  True:
                itemDetection()
                key = cv2.waitKey(1)
                if key == 27 or query == "nesne tanıma kamerasını kapat":
                    break
            cv2.destroyAllWindows()
        t1 = threading.Thread(target=itemDetect)
        t1.start()

    elif "kamerayı" in query and "çevir" in query:
        try:
            search = query.replace("kamerayı ", "")
            search = search.replace(" çevir", "")
            search = search.replace("jarvis ", "")
            print(search)
            if search == "sağa":
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                time.sleep(0.3)
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                time.sleep(0.3)
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_right&lang=eng")
                Speak("Hazır efendim")
            elif search == "sola":
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                time.sleep(0.3)
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                time.sleep(0.3)
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_left&lang=eng")
                Speak("Hazır efendim")
            elif search == "yukarı" or search == "yukarıya":
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_up&lang=eng")
                Speak("Hazır efendim")
            elif search == "aşağı" or search == "aşağıya":
                msedge.get("http://admin:123456@192.168.0.234/cgi-bin/action?action=cam_mv&diretion=cam_down&lang=eng")
                Speak("Hazır efendim")
        except:
            Speak("Sorun oluştu efendim")



    #######################   MEDIA  

    elif "şarkıyı aç" in query or "şarkıyı kapat" in query or "müziği aç" in query or "müziği kapat" in query or "türküyü aç" in query or "türküyü kapat" in query:
        pyautogui.press("playpause")
        Speak("Tamam efendim")

    elif "şarkıyı değiştir" in query or "sonraki şarkı" in query or "sonraki şarkıya geç" in query:
        pyautogui.press("nexttrack")
        Speak("şarkı değiştiriliyor efendim")

    elif "önceki şarkı" in query or "önceki şarkıyı aç" in query:
        pyautogui.press("prevtrack")
        Speak("şarkı değiştiriliyor efendim")

    elif "ses seviyesini" in query and "yükselt" in query or "ses seviyesini" in query and "yüksel" in query:
        try:
            if query == "ses seviyesini yükselt" or query == "ses seviyesini yüksel":
                Speak("Ne kadar yükseltmemi istersiniz efendim") 
                while True:
                    try:
                        level = takecommand()
                        if level == "tamam":
                            Speak("Tamam efendim")
                            break
                        else:
                            realLevel = int(level) / 2
                            pyautogui.press("volumeup", presses=int(realLevel))
                            Speak(f"Ses seviyesi {level} yükseltiliyor")
                            break
                    except:
                        Speak("Anlayamadım efendim")
            else:
                level = query.replace("yükselt", "")
                level = level.replace("ses", "")
                level = level.replace("seviyesini", "")
                level = level.replace("yüksel", "")
                level = level.replace("jarvis", "")
                realLevel = int(level) / 2
                pyautogui.press("volumeup", presses=int(realLevel))
                Speak(f"Ses seviyesi {level} yükseltiliyor")
        except:
            Speak("Anlayamadım efendim")

    elif "ses seviyesini" in query and "azalt" in query or "ses seviyesini" in query and "kas" in query:
        try:
            if query == "ses seviyesini azalt" or query == "ses seviyesini kas":
                Speak("Ne kadar azaltmamı istersiniz efendim")
                while True:
                    try:
                        level = takecommand()
                        if level == "tamam":
                            Speak("Tamam efendim")
                            break
                        else:
                            realLevel = int(level) / 2
                            pyautogui.press("volumedown", presses=int(realLevel))
                            Speak(f"Ses seviyesi {level} azaltılıyor")
                            break
                    except:
                        Speak("Anlayamadım efendim")
            else:
                level = query.replace("azalt", "")
                level = level.replace("ses", "")
                level = level.replace("seviyesini", "")
                level = level.replace("kas", "")
                realLevel = int(level) / 2
                pyautogui.press("volumedown", presses=int(realLevel))
                Speak(f"Ses seviyesi {level} azaltılıyor")
        except:
            Speak("Anlayamadım efendim")



    #####################################MASA LAMBASI

    elif "masa lambasını kapat" in query or "masa lambasını aç" in query:
        Speak("Tamam efendim")
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        time.sleep(1)
        msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
        if "aç" in query and arduinoChecker == True:
            arduino.write(b'2')
        elif "kapat" in query and arduinoChecker == True:
            arduino.write(b'1')
        msedge.quit()

    elif "masa lambasının rengini değiştir" in query:
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get("http://192.168.0.90/")
        Speak("Hangi renk olsun efendim")
        while True:
            try:
                colorr = takecommand()
                if colorr == "tamam":
                    Speak("Tamam efendim")
                    break
                elif colorr == "kırmızı":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[1]').click()
                    arduino.write(b'3')
                    Speak("Masa lambası kırmızı yapılıyor efendim")
                    break
                elif colorr == "turuncu":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[2]').click()
                    arduino.write(b'6')
                    Speak("Masa lambası turuncu yapılıyor efendim")
                    break
                elif colorr == "sarı":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[3]').click()
                    arduino.write(b'7')
                    Speak("Masa lambası sarı yapılıyor efendim")
                    break
                elif colorr == "sıcak beyaz":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[4]').click()
                    Speak("Masa lambası sıcak beyaz yapılıyor efendim")
                    break
                elif colorr == "beyaz":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[5]').click()
                    arduino.write(b'8')
                    Speak("Masa lambası beyaz yapılıyor efendim")
                    break
                elif colorr == "pembe":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[7]').click()
                    arduino.write(b'9')
                    Speak("Masa lambası pembe yapılıyor efendim")
                    break
                elif colorr == "mavi":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[8]').click()
                    arduino.write(b'5')
                    Speak("Masa lambası mavi yapılıyor efendim")
                    break
                elif colorr == "turkuaz":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[9]').click()
                    arduino.write(b'10')
                    Speak("Masa lambası turkuaz yapılıyor efendim")
                    break
                elif colorr == "yeşil":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[10]').click()
                    arduino.write(b'4')
                    Speak("Masa lambası yeşil yapılıyor efendim")
                    break
                elif colorr == "rastgele" or colorr == "rastgele bir renk" or colorr == "rastgele renk":
                    msedge.find_element(By.XPATH,'//*[@id="qcs-w"]/div[11]').click()
                    Speak("Masa lambası rasgele bir renk yapılıyor efendim")
                    break
                else:
                    Speak("Başka renk söyleyin efendim")
            except:
                Speak("Anlayamadım efendim")
        msedge.quit()

    elif "masa lambasının efektini değiştir" in query:
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        Speak("Hangi efekt olsun efendim")
        while True:
            try:
                effect = takecommand()
                if effect == "tamam":
                    Speak("Tamam efendim")
                    break
                elif effect == "gökkuşağı":
                    Speak("Masa lambası gökkuşağı yapılıyor efendim")
                    #os.system("taskkill /f /im LedFx.exe")
                    msedge.find_element(By.XPATH,'//*[@id="bot"]/button[4]').click()
                    time.sleep(1)
                    msedge.find_element(By.XPATH,'//*[@id="p1o"]/div[2]').click()
                    break
                elif effect == "normal":
                    Speak("Masa lambası normal yapılıyor efendim")
                    #os.system("taskkill /f /im LedFx.exe")
                    msedge.find_element(By.XPATH,'//*[@id="bot"]/button[4]').click()
                    time.sleep(1)
                    msedge.find_element(By.XPATH,'//*[@id="p10o"]/div[2]').click()
                    break
                elif effect == "bass efekti":
                    os.startfile("E:\LedFx\data\LedFx.exe")
                    Speak("Masa lambası bass efekti yapılıyor efendim")
                    break
                else:
                    Speak("Gökkuşağı veya normal deyebilirsiniz efendim")
            except:
                Speak("Anlayamadım efendim")
        msedge.quit()



    #################################################################

    elif "pencereyi değiştir" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        #time.sleep(1)
        pyautogui.keyUp("alt")
        Speak("Tamam efendim")

    elif "pencereyi kapat" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("f4")
        #time.sleep(1)
        pyautogui.keyUp("alt")
        Speak("Tamam efendim")

    elif "pencereyi küçült" in query:
        pyautogui.keyDown("win")
        pyautogui.press("down")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "pencereleri küçült" in query:
        pyautogui.keyDown("win")
        pyautogui.press("m")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "pencereyi büyüt" in query:
        pyautogui.keyDown("win")
        pyautogui.press("up")
        #time.sleep(1)
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "tuşuna bas" in query:
        button = query.replace(" tuşuna bas", "")
        button = button.replace("jarvis ", "")
        pyautogui.press(button)
        Speak("Tamam efendim")

    #####################################################################

    elif "play listemi aç" in query:
        webbrowser.get().open("https://www.youtube.com/watch?v=H9aq3Wj1zsg&list=RDH9aq3Wj1zsg&start_radio=1")
        Speak("Playlistiniz açılıyor efendim")

    elif "hız testi yap" in query or "internet testi yap" in query or "wifi testi yap" in query:
        Speak("Tamam efendim 10 15 saniye bekleyiniz")
        speed = speedtest.Speedtest()
        download = speed.download()
        upload = speed.upload()
        correctDown = int(download/800000)
        correctUp = int(upload/800000)
        Speak(f"İndirme hızı {correctDown-10} mbps ve yükleme hızı {correctUp-10} mbps")

    elif "bluetooth aç" in query or "bluetooth kapat" in query:
        pyautogui.keyDown("win")
        pyautogui.press("a")
        pyautogui.keyUp("win")
        pyautogui.click(x=1400, y=900)
        pyautogui.keyDown("win")
        pyautogui.press("a")
        pyautogui.keyUp("win")
        Speak("Tamam efendim")

    elif "ekran resmi al" in query or "ss al" in query:
        img= pyautogui.screenshot()
        home_directory = os.path.expanduser( '~' )
        img.save(f"{home_directory}/Desktop/screenshot.png")
        Speak("Ekran resmi alındı efendim")

    elif "batarya ne kadar" in query or "batarya seviyesi" in query:
        battery = psutil.sensors_battery()
        percent = battery.percent
        Speak(f"Sistemin bataryası 100de {percent} efendim")



    ################################################################################

    elif "tarayıcıyı kapat" in query:
        os.system("taskkill /f /im msedge.exe")
        Speak("Tarayıcı kapatılıyor efendim")

    elif "bilgisayarı kapat"  in query:
        Speak("Tamam efendim bilgisayar kapatılıyor")
        os.system("shutdown /s /t 5")

    elif "bilgisayarı yeniden başlat" in query:
        Speak("Tamam efendim bilgisayar yeniden başlatılıyor")
        os.system("shutdown /r /t 5")

    elif "bilgisayarı uyku moduna al" in query or "bilgisayarı uyut" in query:
        Speak("Tamam efendim bilgisayar uyku moduna alınıyor")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "her şeyi uyku moduna al" in query or "her şeyi uyut" in query:
        Speak("Tamam efendim herşey uyku moduna alınıyor")
        msedge = webdriver.Edge(executable_path="./Codes/msedgedriver.exe",options=edgeOptions)
        msedge.get ("http://192.168.0.90/")
        time.sleep(1)
        msedge.find_element(By.XPATH,'//*[@id="buttonPower"]').click()
        arduino.write(b'1')
        msedge.quit()
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")



    ###################################################################################
    elif query == "kaç yaşındasın":
        playsound("./SoundEffects/year.mp3")

    elif "roma'yı kim yaktı" in query:
        playsound("./SoundEffects/roma.mp3")

    elif "hahaha" in query or "he he" in query:
        playsound("./SoundEffects/laugh.mp3")

    elif "osur" in query or "osuruk sesi" in query or "gaz çıkart" in query or "gaz çıkar" in query:
        farts = random.choice(["./SoundEffects/fart.mp3","./SoundEffects/fart2.mp3"])
        playsound(farts)

    elif "yanıyorsun fuat abi" in query or "yanıyorsun jarvis" in query:
        playsound("./SoundEffects/fuatabi.mp3")

    elif "şifreyi kır" in query:
        Speak("Tamam efendim şifre kırma modulu çalıştırılıyor")
        def PasswordHac():
            PasswordHack.toggle_fullscreen()
            PasswordHack.play()
            time.sleep(28)
            PasswordHack.stop()
            #Speak("şifre başarıyla kırıldı efendim")
        t1 = threading.Thread(target=PasswordHac)
        t1.start()

    elif "kendi arayüzünü aç" in query:
        Speak("Tamam efendim")
        def JarvisU():
            JarvisUI.toggle_fullscreen()
            JarvisUI.play()
            time.sleep(62)
            JarvisUI.stop()
        t1 = threading.Thread(target=JarvisU)
        t1.start()

    elif "kendi arayüzünü kapat" in query:
        JarvisUI.stop()
        Speak("Tamam efendim")

    elif "eşşoğlueşşek" in query:
        Speak("eşşoğlueşşek sizsiniz efendim")
        playsound("./SoundEffects/laugh.mp3")
    
checkArduino()
#os.startfile("E:\Wallpaper Engine\wallpaper64.exe")
os.startfile(".\Required\Rainmeter\Rainmeter.exe")
greeting()
while True:
    query = takecommand()
    if query !="":
        respond()
    if query == "преминете към изкуствен интелект":
        Speak("Преминаване към изкуствен интелект", True)
        while True:
            query = takecommand()
            if query:
                if query == "çıkış yap":
                    Speak("çıkış yapılıyor", True)
                    break
                else:
                    openAI(query)

    if query == "можеш да спиш"  or query == "засппивай" or query == "довиждане":
        Speak("Добре, сър, можете да ми се обадите, ако имате нужда от мен")
        os.system("taskkill /f /im Rainmeter.exe")
        exit()