import pyttsx3
import datetime as dt
import speech_recognition as sr
import pyaudio
import wikipedia



import webbrowser
import smtplib
import os


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(dt.datetime.now().hour)

    if hour>=0 and hour<12:
        speak('Good Morning!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon!')
    
    else:
        speak('Good Evening!')
    
    speak('How may I help You Sir')
        
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        audio = r.listen(source)

    try:
        print("Reconizing......")
        query = r.recognize_google(audio,language='en-in')
        print("user said: ", query)
    
    except Exception as e:
        print("Please Repeat Your Command")
        return "None"
    return query.lower()


Dict = {'apoorv': 'apurv91099@gmail.com'}
def sendEmail(to,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('apurvraj91099@gmail.com','test34*%')
    server.sendmail('apurvraj91099@gmail.com',to,message)
    server.close()


if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'close' in query:
            exit()

        elif 'time' in query:
            time=dt.datetime.now().strftime("%H:%M:%S")
            speak("The time is",time)

        elif 'wikipedia' in query:
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia', "")
            result = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(result)
        
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'send email' in query:
            try:
                speak("Please Say the receivers name ")
                name = takeCommand()
                speak("Please Say the Message")
                message = takeCommand()
                to = Dict[name]
                sendEmail(to,message)
                speak("Email has been sent")
            except Exception as e:
                speak("Sorry the email cannot be sent")
        
        elif 'open vscode' in query:
            path = "C:\\Users\\apurv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
            


