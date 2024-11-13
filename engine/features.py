import re
import sqlite3
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import os
import pywhatkit as kit
import webbrowser

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

def extract_yt_term(command):
    #Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.+?)\s+on\s+youtube'
    #Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    #If a match is found, return the song name
    return match.group(1) if match else None