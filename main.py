"""
you don't have to run any command in your terminal for this code.

if you need any help check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""

import shutil, os, time
from view_bot.main import HOME_DIRECTORY

HOME_DIRECTORY = os.path.expanduser('~') #gets your home directory

source = f"{HOME_DIRECTORY}/Downloads"
dest = f"{HOME_DIRECTORY}/Desktop"

files = os.listdir(source)

while True: #forever run the code below
    if [f for f in os.listdir(source) if not f.startswith('.')] == []: #checks if the source does not start with .
        print('empty') #prints 'empty' to your console

    else: #else do the code below
        for f in files: #makes a loop for how many files are in downloads
            if not f.startswith("."): #checks if the file name starts with .
                shutil.move(source+f, dest) #moves the file
