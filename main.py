"""
in your terminal type the following:

pip install selenium

if this doesn't work type the following

pip3 install selenium

if this also doesn't work check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""

from selenium import webdriver #import webdriver from the selenium module
from time import sleep #import sleep from the time module
import os #imports the os module

HOME_DIRECTORY = os.path.expanduser('~') #gets your home directory

driver1 = webdriver.Chrome(executable_path=f"{HOME_DIRECTORY}/Downloads/chromedriver")
driver2 = webdriver.Chrome(executable_path=f"{HOME_DIRECTORY}/Downloads/chromedriver")
driver3 = webdriver.Chrome(executable_path=f"{HOME_DIRECTORY}/Downloads/chromedriver") 
#download your driver at https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39%2F


CHANNEL_LINK = "put your video link here"
driver1.get(CHANNEL_LINK) #opens the channel link with driver 1
driver2.get(CHANNEL_LINK) #opens the channel link with driver 2
driver3.get(CHANNEL_LINK) #opens the channel link with driver 3

while True:
    #the code below will loop forever
    sleep(60) #makes the code stop for 60 seconds (1 minute)
    driver1.refresh() #refreshes the web page driver 1 is at 
    driver2.refresh() #refreshes the web page driver 2 is at
    driver3.refresh() #refreshes the web page driver 3 is at