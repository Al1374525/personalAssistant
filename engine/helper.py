import re

def extract_yt_term(command):
    #handle input normalization
    command = command.lower().strip()

    #Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.+?)\s+on\s+youtube'
    #Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    #If a match is found, return the song name
    return match.group(1) if match else None