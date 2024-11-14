import re
import sqlite3
import struct
import time
from playsound import playsound
import eel
import pvporcupine
import pyaudio
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import webbrowser

from engine.helper import extract_yt_term

conn = sqlite3.connect("delta.db")
cursor = conn.cursor()

#Playing assistant sound function


@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    
    # Strip query to get the app name as a single string
    app_name = " ".join(query.split())

    if app_name:
        try:
            # Query to check if there is a matching path in sys_command
            cursor.execute(
                'SELECT path FROM sys_command WHERE name = ?', (app_name,))
            results = cursor.fetchall()

            if results:
                speak("Opening " + query)
                os.startfile(results[0][0])  # Use the path from the first result

            else:
                # Check for URL in web_command table if no path found
                cursor.execute(
                    'SELECT url FROM web_command WHERE name = ?', (app_name,))
                results = cursor.fetchall()
                
                if results:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])  # Use the URL from the first result
                else:
                    # If no matching command or URL, attempt to start as a system command
                    speak("Opening " + query)
                    try:
                        os.system('start ' + query)
                    except FileNotFoundError:
                        speak("File not found")
                    except Exception as e:
                        speak(f"An error occurred: {str(e)}")
        except Exception as e:
            speak(f"Something went wrong: {str(e)}")
    
    
    # if query !="":
    #     speak("Opening "+ query)
    #     os.system("start " + query)
    # else:
    #     speak("not found")
        
        
        

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term is not None:
         speak("Playing "+ search_term +" on YouTube")
         kit.playonyt(search_term)
    else:
        speak("Search term not found")
    #speak("Playing "+search_term+" on YouTube")
    #kit.playonyt(search_term)


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords    
        porcupine=pvporcupine.create(keywords=["delta","alexa"]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                print("hotword detected")

                # pressing shorcut key win+j
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()