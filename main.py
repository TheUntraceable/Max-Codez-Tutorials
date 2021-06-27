"""
in your terminal type the following:

pip install pyautogui

if this doesn't work type the following

pip3 install pyautogui

if this also doesn't work check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""
import pyautogui, time #imports pyautogui and time
time.sleep(5) #makes the script stop for 5 seconds
f = open("script.txt", "r") #opens the script.txt file
for word in f:
    #loops for every word in f
    pyautogui.typewrite(word) #types every word in f
    pyautogui.press("enter") #presses enter to send 'word'