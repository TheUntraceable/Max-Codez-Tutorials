"""
NOTE
this only works on mac.

NOTE
this only works with certain modules like tkinter, so you have a UI


########################################
in your terminal type the following:


pip install py2app

if this doesn't work type the following

pip3 install py2app

if this also doesn't work check the readme.md at https://github.com/rewind-time/Max-Codez-Tutorials

have fun coding!
"""

import tkinter, random #imports tkinter module and the random module
jokes = ["yo momma so fat she rolls to work", "yo momma so ugly even her forhead jiggles when she walks"]
number = random.randrange(0, 2)

window = tkinter.Tk() #defining the window variable
window.geometry('700x200') #getting the screen width en height
tkinter.Label(window, text=jokes[number], font='Helvetica 16 bold').pack() #setting up a label and packing it into the window
window.mainloop() #runs the mainloop


