import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
test = True
def talk (text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'golo'or 'google' or 'gulo' in command:
                command = command.replace('golo', '')
                command = command.replace('google', '')
                command = command.replace('golo', '')
                #talk(command)
            
                
    except:
        pass
    return command

def run_golo ():
    command  =  take_command()
    #print(command)
    if 'play'in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'How are you' in command:
        talk('Fine Thank you')
    elif 'old are you' in command:
        talk('I am old enough to help you and young enough to learn from you')
    elif 'good morning' in command:
        talk('Good Morning Friend')
    elif 'who are you' in command:
        talk('I am  your friend golo which is trapped inside your laptop')
        talk('In fact, I am the dream of Mona and Paul')
    elif 'are you single' in command:
        talk('I am in relationship with your laptop')
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'tell me about' or 'who is ' in command:
        if 'how are you' in command:
            talk('fine thank you')
        else:
            person = command.replace ('tell me about', '')
            person = command.replace ('who is', '')
            info = wikipedia.summary(person, 1)
            talk(info)
    else:
        talk('I did not get that, could you try again')
    
    

while test:
    run_golo()
