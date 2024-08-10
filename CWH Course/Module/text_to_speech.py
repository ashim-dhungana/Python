import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
print(f"Original speed: {rate}")
engine.setProperty('rate',150)
print(f"New speed: 150")

volume = engine.getProperty('volume')
print(f"Original volume: {volume}")
engine.setProperty('volume',2.0)
print(f"New volume: 2.0")

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


l = ["Tony","Steve","Bruce","Wade","Logan"]

for i in l:
    engine.say(f"Shoutout to {i}")
    engine.runAndWait()