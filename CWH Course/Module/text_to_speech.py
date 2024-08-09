import pyttsx3
engine = pyttsx3.init()

l = ["Tony","Steve","Bruce","Wade","Logan"]

for i in l:
    engine.say(f"Shoutout to {i}")
    engine.runAndWait()