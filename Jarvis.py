import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCMD():
    reco = sr.Recognizer()
    with sr.Microphone(device_index=3) as src:
        print('Listening...')
        reco.pause_threshold = .5
        audio = reco.listen(src)

    try:
        print('Recognizing...')
        query = reco.recognize_google(audio,language='en-us')
        print(query)
    except Exception as e:
        print(e)
        print('Say that again')
        
        return 'None'

if __name__ == "__main__":
    speak("Hello Sir")
    
    while True:
        q = takeCMD()