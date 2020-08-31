import speech_recognition as speech_recog
import pyttsx3
import time

engine = pyttsx3.init()

recog = speech_recog.Recognizer()
mic = speech_recog.Microphone()
speech_recog.Microphone.list_microphone_names()
words = []

for i in range(0,10):
    print("")
while True:
    with mic as audio_file:
        print("Bot-san on line...")

        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)

        print("Converting Speech to Text")
        text = recog.recognize_google(audio)
        print("You said: " + text)
        engine.say(text)
        engine.runAndWait()
    time.sleep(3)
