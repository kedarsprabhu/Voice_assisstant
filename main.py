import pyttsx3 as p
import speech_recognition as sr
import randfacts
from selenium_web import *
from ytb_aud import *
from news import *
from jokes import *
from weather import *
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 180)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return ("afternoon")
    else:
        return ("evening")

today=datetime.datetime.now()
r = sr.Recognizer()

speak("Hello, good"+ wish()+",I'm your voice assistant")
speak("Today is"+today.strftime("%d")+"of"+ today.strftime("%B")+" and its" +(today.strftime("%I"))+(today.strftime("%M"))+(today.strftime("%p")))
speak("Temperature in Kumta is" + str(temp()) +"degree celsius" + "and" + str(des()))
speak("How are you doing today?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening")
    audio = r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" and "good" and "well" in text:
    speak("I am having a good day too")
speak("What can I do for you?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("What information are you looking for?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening..")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    print("searching for {} in wikipedia".format(infor))
    speak("searching for {} in wikipedia".format(infor))


    assist = infow()
    assist.get_info(infor)
elif "play" and "video" in text2:
    speak("Which video you want me to play?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening..")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("Playing {} on youtube".format(vid))
    speak("Playing {} on youtube".format(vid))
    assist = music()
    assist.play(vid)

elif "news" in text2:
    print("Sure. Reading latest news")
    speak("Sure. Reading latest news")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("Sure thing")
    x=randfacts.getFact()
    print(x)
    speak("Did you know that?"+ x)

elif "joke" in text2:
    speak("Laughter on the way")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])


