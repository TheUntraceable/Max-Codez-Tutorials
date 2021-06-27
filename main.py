"""
in your terminal type the following:

pip install discord

if this doesn't work type the following

pip3 install discord

if this also doesn't work check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""
import discord #imports the discord module

client = discord.Client() #defines the client

keywords = ["max", "help", "pyautogui", "hello", "hi"] #the words which triggers the bot

@client.event #on a event trigger
async def on_message(message):
    #in this case the trigger is on_message
    for i in range(len(keywords)):
        #a loop which lasts for the lenght of the keywords list
        if keywords[i] in message.content:
            #if a keyword is in the message
            for j in range(20):
                #loops the code below 20 times
                await message.channel.send("get spammed LOSER")
                #sends get spammed LOSER 20 times
                


client.run("your token goes in here")