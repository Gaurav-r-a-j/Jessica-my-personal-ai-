
import pyttsx3
import speech_recognition as sr

# from jesica import speak


engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
print('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    print("   ")
    engine.say(audio)
    print(f": {audio}  ")
    print("   ")
    engine.runAndWait()



# Speak("hello how are you")

def takecommand():
    command= sr.Recognizer()
    with sr.Microphone() as source:
        print ('listening.....')
        command.pause_threshold =1
        command.energy_threshold = 4000

        audio = command.listen(source)

        try:
            print('Recognizing...')
            query = command.recognize_google(audio, language='en-in')
            print(f' You said:  {query}')

        except Exception as Error:
            print("i am uable to hear you")
            # return "none"


        return query


query = takecommand()


if 'hello' in query:
    Speak('Hello sir')

else:
    Speak("no command found")