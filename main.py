import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
import datetime
import wikipedia
import subprocess
import pyjokes

import database

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
k = input("dont input anything please this is test")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
    except:
        pass
    return command


def take_response():
    try:
        with sr.Microphone() as source:
            print('awaiting response...')

            voice = listener.listen(source)
            response = listener.recognize_google(voice)
            response = response.lower()
            if 'test' in response:
                response = response.replace('test', 'test received')
    except:
        pass
    return response


def morning():
    talk('good morning sir')
    talk('would you like me to begin your startup command?')
    response = take_response()
    print(response)
    if 'yes' in response:
        subprocess.Popen(r"C:\Users\Iain\AppData\Local\Discord\app-1.0.9001\Discord.exe")
        subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
        date = datetime.datetime.now().strftime('%A %B %d')
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(date)
        talk('today is' + date)
        if 'Saturday' in date and 'am' in time:
            talk("you have advanced game development at 12 pm")
        talk(pyjokes.get_joke())

    elif 'no' in response:
        talk(database.responses_yes[random.randrange(0, 3)])
        run_ai()

    else:
        run_ai()

def date():
    date = datetime.datetime.now().strftime('%A %B %d')
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(date)
    talk('today is' + date)
    if 'Saturday' in date and 'am' in time:
        talk("you have advanced game development at 12 pm")

def run_ai():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        time = time.replace(':', '')
        talk('the time is' + time)
        print(time)

    elif 'how are' in command:
        talk(database.response_howareyou[random.randrange(0, len(database.response_howareyou))])
    elif 'good morning' in command:
        morning()
    elif 'date' or 'day' in command:
        date()

    elif 'thank you' in command:
        talk("you're welcome sir")

    else:
        talk('try again.')



while True:
    run_ai()



# names: Jarvis, Adam, Eve, HAL, Ares,
