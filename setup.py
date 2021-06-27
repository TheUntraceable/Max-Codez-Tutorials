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

from setuptools import setup #imoprt setup from the setuptools module

APP=['main.py'] #define the APP variable, the main.py you can adjust to what your python file is named
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=["py2app"]
)

"""
NOTE
in your terminal you now have to type the following:

python setup.py py2app

if this does not work try the following:

python3 setup.py py2app

this should return a .dmg file

have fun!
"""