# DRINK WATER REMINDER

import os
import time
import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate',150)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def notification():
    while True:
        os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')
        engine.say("Time to drink water")
        engine.runAndWait()
        
        time.sleep(5)

notification()