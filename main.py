"""
in your terminal type the following:

pip install pyautogui

if this doesn't work type the following

pip3 install pyautogui

if this also doesn't work check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""

import pyautogui, time #import the modules pyautogui and time
time.sleep(5) #this is the delay before it starts clicking
for i in range(200): #the code below will loop 200 times (in this case it will click 200 times)
    pyautogui.leftClick() #left clicks