


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


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")  
  
    else:
        speak("Good Evening Sir !") 
  
    assname =("jessica 1 point o")
    speak(f"{assname} How can i help you")
    # speak(assname)

def username():
    speak("What should i call you ")
    uname = TakeCommand()
    speak(f"Welcome {uname}")
    # speak(uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome ", uname.center(columns))
    print("#####################".center(columns))
     
    speak(f"How can i Help you, {uname}")

def whoisname():
    speak('can you please repeat your name again')
    a = TakeCommand()
    randomcomment = [f'{a} is a good person, {a} always help others.'    ,    
    f'{a} is a normal person, {a} not  always  help others , because {a} is always busy in his own work , but sometimes {a} can help you in any problem that no one can. ',
    f'{a} is a naughty person, {a} always is in happy mood , full chill no tension .'   , 
    f'{a} is a normal person, {a} not  always  help others , because {a} is a chutiya. ' , 
    f'{a} is a simple and obidient person, {a} is so innocent that sometimes you feel like you are talking with a child , {a} is like a baby.. ',
    f'{a} is a nice person and always want to help other, {a} is always try it best in any situation so that he can achieve his or her goals. , {a} is like a baby.. ',
    ]
    choosecomment = random.choice(randomcomment)
    b = speak(choosecomment)
    return b
    


# anyname = ["aryan" , 'tanishq']

def TaskExe():

    while True:

        query = TakeCommand()

        if 'hello' in query:
            speak("Hello sir, I am jessica,Your Personal AI Assistant,How may I help You.")
            # speak("Your Personal AI Assistant.")
            # speak("How may I help You")

        # elif "jessica" in query:
        #     wishMe() 
            
        elif 'jarvis' in query:
            speak("I'm not jarvis I'm jessica ")

        elif 'know me' in query:
            speak("Sorry, I can't recognize you")
            username()

        elif "how are you" in query:
            speak("I Am Fine Sir!, Whats About You?")
            # speak("Whats About You?")
        
        elif "good morning" in query or "good evening" in query:
            wishMe()

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine,")

        elif "you need a break" in query:
            speak("Ok Sir , You can Call Me Anytime !")
            break

        elif "kya hal hai" in query:
            speak("As i can't speak hindi but stll , Mai badhiya hun aap batao, I'm fine and you")

        elif 'bye' in query:
            speak("Ok sir , Bye !")
            break

        elif "who are you" in query:
            speak("I am your virtual assistant created by Gaurav")

        elif "you came to world" in query:
            speak("Thanks to Gaurav. further It's a secret")

        elif 'love' in query:
            speak("It is 7th sense that destroy all other senses.")

        # Here you can add more who is "name"
        
        



         
        elif 'do you know anish' in query:
            speak('Anish is from kolkata and he has taken cse and his nickname is b,a,b,a,i babai.')

        elif 'do you know aryan' in query:
            speak("Aryan is from Modinagar , he has taken cse and and and his nickname is G,o,c,h,i gochi.")

        elif 'do you know tanishq' in query:
            speak("Tanishq is from rajsthan and he has taken cse and he always help others (mostly girls) and also his nickname is L,o,d,u,, lodu.")

        elif 'do you know' in query:
            whoisname()

        elif 'who is' in query or 'what is' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            # print(results)
            speak(results)



        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com")
        

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")  
            speak(f"Sir, the time is {current_time}")

        elif "date" in query:
            day=datetime.datetime.today().strftime('%A')
            date = datetime.date.today()
            speak(f"It's {day} , {date}")

        elif "day" in query:
            day=datetime.datetime.today().strftime('%A')
            speak(f"it's {day}")

        elif 'joke' in query or 'jokes' in query:
            speak(pyjokes.get_joke())
            

        elif 'ok' in query:
            speak("Is there anything else I can do for you")


        elif "jessica" in query:
            wishMe() 

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()

        elif 'no' in query:
            speak("Ok Bye , you can call me anytime")
            break




        else:
            speak("I can't answer this question right now ask me something else")

        

            
        

        # elif 'news' in query:
             
        #     try:
        #         jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
        #         data = json.load(jsonObj)
        #         i = 1
                 
        #         speak('here are some top news from the times of india')
        #         print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
        #         for item in data['articles']:
                     
        #             print(str(i) + '. ' + item['title'] + '\n')
        #             print(item['description'] + '\n')
        #             speak(str(i) + '. ' + item['title'] + '\n')
        #             i += 1
        #     except Exception as e:
                 
        #         print(str(e))

# wishMe()
# username()
TaskExe()






