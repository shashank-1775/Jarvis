import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis Sir. Please tell me how may I help you")
    print("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def openapp(query):
    dict_app = {'vscode': 'C:\Users\nawaz\Desktop\Visual Studio Code.lnk',
                'spotify': 'C:\Users\nawaz\Desktop\Spotify.lnk'}
    a = query.replace('open', '').strip()
    for name, path in dict_app.items():
        if a in name:
            os.startfile(rf'{path}')


if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'find' in query:
            query = query.replace("find", "").strip()
            speak(f"Searching Google for {query}")
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)

        elif 'play' in query:
            video = query.replace('play', '').strip()
            speak(f'Playing {video} on YouTube')
            results = YoutubeSearch(video, max_results=1).to_dict()
            video_id = results[0]['id']
            webbrowser.open(f'https://www.youtube.com/watch?v={video_id}')
        elif 'stop' in query or 'exit' in query or 'quit' in query or 'good night' in query:
            speak("Goodbye Sir. Have a nice day.")
            break

        elif 'open' in query:
            openapp(query)

        else:

            print("No query matched")
