# text to speach

import pyttsx3

print("Enter your text:")
n = input()
engine = pyttsx3.init()
engine.say(n)
engine.runAndWait()