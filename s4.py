import speech_recognition as sr

def dan(audio):
    for i in dir(audio):
        print(i)


r = sr.Recognizer()
# print(sr.Microphone.list_microphone_names())

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=0.1) 
    audio = r.listen(source)

    
try:
    recognized_speech = r.recognize_google(audio, language=
   
"uk-UA")
    print(recognized_speech)
except sr.UnknownValueError:
    print("Unable to recognize speech")