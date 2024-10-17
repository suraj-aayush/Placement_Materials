import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("hello sir, please speak ")
    audio = r.listen(source)
    text = r.recognize_google(audio)

    print(f"text you said is: {text}")  