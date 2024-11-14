import pyttsx3
import speech_recognition as sr
import eel
import time

#Initialize pyttsx3 engine once
#engine = pyttsx3.init('sapi5')
#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
#engine.setProperty('rate', 174) 
#print(voices)


eel.init('www')

def speak(text):
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174) 
    #print(voices)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


@eel.expose
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        eel.DisplayMessage('listening....')
       
       
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        #speak(query)
        #eel.ShowHood()
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = takeCommand()
        print(query)
    else:
        query = message
    
    try:
        
        # query = takeCommand()
        # print(query)
    
        if "open" in query:
        
            from engine.features import openCommand #change this 
            openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
    
        else:
         print("not run")
    except:
        print("error")
    
    eel.ShowHood()
    

#text = takeCommand()
    
#speak(text)
