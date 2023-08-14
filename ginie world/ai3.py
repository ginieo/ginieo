from datetime import datetime 
import speech_recognition as sr
import pyttsx3
from logging.config import listen
import webbrowser
import wolframalpha
import wikipedia
import pyaudio
# speech engine initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 = male, 1 = female
activationWord = 'computer' # single word

# configure browser
# set the path
chrome_path = r"C:\Program Files\Google\Chrom e\Application\114.0.5735.134\chrome.exe.sig"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

def speak(text, rate = 120):
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()
    
def parseCommand():
    listener = sr.Recognizer()
    print('listening for a command')
    
    with sr.Microphone() as source:
        listener .pause_threshold = 2
        input_speech = listener.listen(source)
    
    try:
        print('Recognizing speech....')
        query = listener.recognize_google( input_speech, language='en_gb')
        print(f'the input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return'None'
    
    return query

# main loop
if __name__ =='__main__':
    speak('All systems nominal.')
    
    while True:
        #parse as a list
        query = parseCommand().lower().split()
        
        if query[0] == activationWord:
            query.pop(0)
            
            #list commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('hello')
                else: 
                    query.pop(0)# remove
                speech = ' '.join(query)
                speak(speech)
                
            # navigation
            if query[0] == 'go' and query[1] == 'to':
                speak('opening..,')
                query = ' '.join(query[2:])
                webbrowser.get('chrome').open_new(query)
                
           # wikipedia
             if query[0]      
                