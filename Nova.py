import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import psutil
import pyjokes
import random
import json 
import requests
from urllib.request import urlopen
import urllib
import wolframalpha
from time import *
from time import sleep
import time

engine = pyttsx3.init()
#wolframalpha_app_id = Please enter your API code here!

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("sir now is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("Today is")
    speak(day)
    speak(month)
    speak(year)

def greetings():
    speak("welcome back")
    time() 
    date()
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour<12:
        speak("Good morning sir!")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir" )
    elif hour>=18 and hour<24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Nova at your service. ready to obey you!")
    speak('hope your doing good')


def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold=1
        audio =r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")

        return  'None'
    return query

def music():
    songs_dir = 'Enter your directory address'
    songs = os.listdir(songs_dir)
    speak("playing music...")
    no = random.randint(1,31)
    os.startfile(os.path.join(songs_dir, songs[no]))


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())



if __name__ == "__main__":
    print("                                                    NOVA                                               ")
    sleep(2)
    print("Nova is ready...")
    greetings()
    talk()
    while True:
        query=take_command().lower()

        if  'time now' in query:
            time()

        if 'date' in query:
            date()

        if 'about yourself' in query:
            print("hey there! i am Nova an  intelligent personal assistant. I can perform tasks or services for an individual based on commands or questions. i am able to interpret human speech and respond via synthesized voices.")
            print("you can ask me any question and media playback via voice, and manage other basic tasks such as email, calculation and calendars with verbal commands")
            print("what you want me to do?")
            speak("hey there! i am Nova an  intelligent personal assistant. I can perform tasks ,or services for an individual based on commands or questions. i am able to interpret human speech and respond via synthesized voices.")
            speak("you can ask me any question ,and media playback via voice, and manage other basic tasks such as email, calculation and calendars with verbal commands")
            speak("what you want me to do?")

        if 'wikipedia' in query:
            speak("searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        if 'send email' in query:
            try:     
                sender_email = "Enter sender's mail id"
                speak("please enter to whom you want the mail is for:")
                recv = input(str("please enter to whom you want the mail is for:"))
                rec_email = recv
                speak("please enter the password")
                password = input(str("Please enter your password : "))
                speak("please say what is the message")
                message = take_command() 
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, password)
                print("Login success")
                server.sendmail(sender_email, rec_email, message)
                speak("the message is.."+message)
                print("Email has been sent to ", rec_email)
                speak("Email has been sent to "+rec_email)
                speak('message success')
            except Exception as e :
                print(e)
                speak('unable to send mail sir!')

        if 'ok google' in query:
            speak('what should i search')
            search = take_command().lower()
            speak("searching..."+search)
            wb.open('https://www.google.com/search?q='+search)
        
        if 'search in chrome' in query:
            speak('what should i search')
            search = take_command().lower()
            chromepath = '%s'#Please enter the chrome path here(.exe %s)
            speak("searching..."+search)
            wb.get(chromepath).open_new_tab(search+'.com')

        if 'open youtube' in query:
            speak("what should i search")
            search = take_command().lower()
            speak("here we go to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search)
        

        if 'sign out' in query:
            os.system("shutdown -l")

        if 'shutdown' in query:
            os.system("shutdown /s /t 1")

        if 'restart' in query:
            os.system("shutdown /r /t 1")


        if 'music' in query:    
            speak('Here is your favorite')
            music()
        
        
        if 'remember that' in query:
            speak('what should i remember sir?')
            data = take_command()
            speak("you said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()


        if 'do you know anything' in query:
            remember=open('data.txt','r')
            speak('You have a new remainder, That is'+remember.read())


        if 'cpu' in query:
            cpu()

        if 'funny' in query:
            jokes()

        if 'open ms word' in query:
            speak("opening... ms word")
            msword = r'"C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE"'#Please enter your MSOffice address here
            os.startfile(msword)

        if 'news' in query:
            try:
                url = "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=250217591d704f679c" #Please enter your API URL here
                resp_text = urllib.request.urlopen(url).read().decode("UTF-8")
                data = json.loads(resp_text)
                i=1
                current_date = datetime.datetime.today().strftime("%A")
                speak(str(current_date)+"headline")
                print("<<<<<<<<<<<<<<<<<TOP HEADLINES>>>>>>>>>>>>>>>")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1 


            except Exception as e:
                print(str(e))

        
        if 'where is' in query:
            query = query.replace("where is","")
            location = query
            speak("user asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place/"+location)

        if 'what is'in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No Result Found")
                speak("No Result Found")

        if 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The Answer is: "+answer) 
            speak("The Answer is: "+answer)

        if 'stop listening' in query:
            speak("for how many seconds you want me to stop listening sir?")
            ans = int(take_command())
            print(ans)
            speak("okay")
            sleep(ans)


        if 'close' in query:
            speak("goodbye sir... have a good time")
            quit()
os.system("pause")
input("Press enter to close program")