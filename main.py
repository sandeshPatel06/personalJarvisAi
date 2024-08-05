import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

# Initialize the speech engine    
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Function to convert text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Function to wish the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning')
    elif hour >= 12 and hour < 15:
        speak('Good afternoon')
    else:
        speak('Good evening...')
    speak("hello sir... Tell me how may I help you")

def take_command():
    """Function to take voice commands from the user"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print("Sorry...")
            speak('Say that again please...')
            return "None"
    return query.lower()

def send_email(to, content):
    """Function to send an email"""
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail before using this code
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('your-email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    
     wish_me()
     while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak('Opening YouTube')
            webbrowser.open("https://www.youtube.com")
        
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("https://www.google.com")
        
        elif 'open whatsapp' in query:
            speak('Opening WhatsApp')
            webbrowser.open("https://web.whatsapp.com")
        
        elif 'open gmail' in query:
            speak('Opening Gmail')
            webbrowser.open("https://mail.google.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\Music'  # Change this 
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                to = "recipient-email@gmail.com"  # Change this to the recipient's email address
                send_email(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("I am not able to send this email")
        
        elif 'stop listening' in query:
            speak('Stopping. Have a nice day!')
            break
        
        elif 'hello' in query:
            speak('Hello sir...')
        
        elif 'how are you' in query:
            speak('I am fine, and you sir?')
        
        elif 'fine' in query or 'good' in query:
            speak('That is good to hear.')
        
        elif 'open code' in query:
            code_path = ""  # Change this to the path of your code editor
            os.startfile(code_path)
        
        elif 'set reminder' in query:
            speak("What shall I remind you about?")
            reminder = take_command()
            speak(f"Reminder set for: {reminder}")
        
        elif 'weather' in query:
            speak("Checking the weather...")
            webbrowser.open("https://www.weather.com")
        
        elif 'news' in query:
            speak("Fetching the latest news...")
            webbrowser.open("https://news.google.com")
        
        elif 'joke' in query:
            speak("Why don't scientists trust atoms? Because they make up everything!")
        
        elif 'search' in query:
            query = query.replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        
        elif 'location' in query:
            query = query.replace("location", "")
            webbrowser.open(f"https://www.google.com/maps/place/{query}")
        
        elif 'how r u' in query:
            speak('I am fine, and you sir?')
            

        # Add more commands as needed
