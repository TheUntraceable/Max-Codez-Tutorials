"""
in your terminal type the following:

pip install playsound

if this doesn't work type the following

pip3 install playsound

you also need to have a alarm.wav or alarm.mp3 file in the same folder your code is in
this is so that the code can actually find the file and run it


for help go check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials


have fun coding!
"""

import time #import time
from playsound import playsound #import playsound from playsound module
from datetime import datetime #import datetime from datetime module

alarmtime = "10:00" #if you want to be woken up at 10 am (24 hour clock system)
while True: #the code below will run forever
    lcltime = datetime.now().strftime("%H:%M") #define a lcltime variable
    if lcltime == alarmtime: #check if the time is equal to the time you put in the alarmtime variable
        playsound(alarm.wav) #plays alarm.wav, if you have a alarm.mp3 change the code to: playsound(alarm.mp3)
        break #this will break the code.
    else:
        print("it isn't time yet") #prints out that it isn't time yet
        time.sleep(10) #makes the code stop for 10 seconds


