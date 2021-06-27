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

HOME_DIRECTORY = os.path.expanduser('~')

driver = webdriver.Chrome(executable_path=f"{HOME_DIRECTORY}/Downloads/chromedriver")
#download your driver at https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39%2F

driver.get("https://instagram.com/")
#goes to the instagram page

sleep(4)
#makes the script stop for 4 seconds

username = "your username goes here" #put your instagram username here
password = "your password goes here" #put your instagram passsword here
driver.find_element_by_xpath(("//input[@name=\"username\"]"))\
    .send_keys((username))
    #finds the username text box and types the username variable which we defined already

driver.find_element_by_xpath(("//input[@name=\"password\"]"))\
    .send_keys((password))
    #finds the password text box and types the password variable which we defined already

driver.find_element_by_xpath('//button[@type="submit"]')\
    .click()
    #finds the submit button and clicks it

sleep(4) #makes the code stop for 4 seconds
#makes the code stop for 4 seconds
driver.get("https://instagram.com/maxcodez_/") #goes to the link inputed in the ""
following = driver.find_element_by_partial_link_text("Following") #finds the Following button
following.click() #clicks the following button
sleep(5) #makes the code stop for 5 seconds
for i in range(5): #loops the code below for 5 times
    driver.find_element_by_xpath('//button[text()="Following')\
        .click()
        #clicks the Following button
    driver.find_element_by_xpath('//button[text()="Unfollow')\
        .click()
        #clicks the Unfollow button
    sleep(2) #makes the code stop for 2 seconds

"""
NOTE 
you still lhave to scroll manually so don't be confused if it doesn't scroll down automatic 

"""