# from datetime import datetime

# All module pasted from geeksforgeeks site 
# import wolframalpha
from urllib.request import urlopen
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
# import winshell
import pyjokes
# import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
# from client.textui import progress
# from ecapture import ecapture as ec
# from bs4 import BeautifulSoup
# import win32com.client as wincl
# from urllib.request import urlopen

listener = sr.Recognizer()
engine = pyttsx3.init('nsss')
voices = engine.getProperty('voice')
engine.setProperty('voice','com.apple.speech.synthesis.voice.samantha')


def speak(audio):
    print("   ")
    engine.say(audio)
    print(f": {audio}  ")
    print("   ")
    engine.runAndWait()

def TakeCommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        command.pause_threshold = 1
        command.energy_threshold = 4000
        audio = command.listen(source)
        print('done')



        try:
            print("Recongnizing...")
            query = command.recognize_google(audio,language='en-in')
            # query = command.recognize_google(audio,language='hi')
            print(f"You said : {query}")


        except Exception as error:
            return 'none'

        return query.lower()
# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# from datetime import datetime

# now = datetime.now()

# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)
# import datetime


# current_time = datetime.datetime.now().strftime("%H:%M:%S")
# print("Current Time =", current_time)


# day=datetime.datetime.today().strftime('%A')
# print(day)

# import webbrowser
# webbrowser.open('https://google.com', new=2)
# randomcomment = [f'{a} is a good person, {a} always help others and , {a} is a very kind person']

def whoisname():
    speak('can you please repeat your name again')
    a = TakeCommand()
    randomcomment = [f'{a} is a good person, {a} always help others and , {a} is a very kind person' , f'{a} is a normal person, {a} not  always help others because ,{a} is always busy in his own work and , but still {a} is a very kind person' , f'{a} is a naughty person, {a} always is in happy mode full chill no tension and , {a} is also a very kind person']
    choosecomment = random.choice(randomcomment)
    
    b = speak(choosecomment)
    return b



# whoisname()


def TaskExe():

    while True:

        query = TakeCommand()

        if 'hello' in query:
            speak("Hello sir, I am jessica,Your Personal AI Assistant,How may I help You.")
            # speak("Your Personal AI Assistant.")
            # speak("How may I help You")

        elif 'who is' in query or 'do you know' in query:
            whoisname()

        elif 'joke' in query or 'jokes' in query:
            speak(pyjokes.get_joke())



# speak('good')

TaskExe()


