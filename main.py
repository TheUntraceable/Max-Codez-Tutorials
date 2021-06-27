"""
in your terminal type the following:

pip install pyautogui

if this doesn't work type the following

pip3 install pyautogui

if this also doesn't work check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""


import pyautogui, time #import pyautogui and time. 

time.sleep(5) #makes the script stop for 5 seconds.

f = open("script.txt", "r") #makes f equal to the text in script.txt.

for word in f: #makes a loop for each word in f.

    pyautogui.typewrite(word) #types the word it got from f.

    pyautogui.press("enter") #pressed enter key.