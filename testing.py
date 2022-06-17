# # we have alot of speech recogniser some of these are 
# recognize_bing(): Microsoft Bing Speech
# recognize_google(): Google Web Speech API
# recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
# recognize_houndify(): Houndify by SoundHound
# recognize_ibm(): IBM Speech to Text
# recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
# recognize_wit(): Wit.ai


# out of this seven only sphinx works offline 


# r.recognize_google()

import speech_recognition as sr
# # from guessing_game.py import recognize_speech_from_mic
# r = sr.Recognizer()
# m = sr.Microphone()
# recognize_speech_from_mic(r, m)  # speak after running this line
# {'success': True, 'error': None, 'transcription': 'hello'}
# r = sr.Recognizer()
# r.recognize_google()
# harvard = sr.AudioFile('audio_files_harvard.wav')
# with harvard as source:
#     audio = r.record(source, duration=4)
#     r.recognize_google(audio)
#     # print(audio)


r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    r.recognize_google(audio)
    print(audio)


# a=sr.Microphone.list_microphone_names()
# print(a)

