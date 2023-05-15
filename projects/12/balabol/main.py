import pyttsx3


s = pyttsx3.init()
data = "Привет Эмиль!"
s.say(data)

s.runAndWait()
