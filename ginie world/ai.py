from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os
import subprocess
import ecapture
import wolframalpha
import json
import requests
import pyaudio

# speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)# 0 = male, 1 = female
activationword = 'computer'# single word
def speak(text, rate = 120):
    engine.setProperty('rate',rate)
    engine.say(text)
    engine.runAndWait()
def parseCommand():
    listener = sr.Recognizer()
    print('listenig of command')


    with sr.Microphone() as source:
        listener.pause_threshold = 2
        input_speech = listener.listen(source)

        try:
            print('reconizing speech...')
            query = listener.recognize_google(input_speech, language='en_gb')
            print(f'the input speech was: {query}')

        except Exception as exception:
            print('say what')
            speak('say what')
            print(exception)
            return 'None'
        
        return query
    if __name__ == '__main__' :
        speak('all systems normal.')
        while True:
            # parse as a list
            query = parseCommand().lower().split() 
            if query[0] == activationword:
                query.pop(0)
                #list commands
                if query[0] == 'say':
                    if 'hello' in query:
                        speak('hi, dog') 
                    else:
                        query.pop(0)#remove say
                        speech = ''.join(query)
                        speak(speech)
