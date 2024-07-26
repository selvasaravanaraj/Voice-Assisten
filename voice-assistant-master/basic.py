import wikipedia                 #wikipedia model for searching result for the word                               
import pyttsx3                   #this model is to convert text to voice
import speech_recognition as sr  #this model is to recognize the voice
repeater=1
def speak(string):               #function to convert text to voice using pyttsx3 module
    engine = pyttsx3.init()
    engine.say(string)
    engine.runAndWait()
def query():                     #function to recognize the user voice using speech_recognition
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio=r.listen(source)
            text=r.recognize_google(audio)
        return (text)
    except:
        speak("the word is not clear,tell again")
        print("Tell Again ")
def search():                                    #function to search for the word in wikipedia 
    speak("tell about the word to search")
    print("Tell the word")
    text=query().lower()
    if text == "stop" or text == "thank you":
        print("Bye")
        return 1
    else:
        print("Searching for the ", text)
        try:
            result = wikipedia.summary(text, sentences=1)
            print("Wikipedia search result ", result)
            speak(result)
        except:
            speak("Tell again clearly or result is not found in wikipedia")
        finally:
            return 0

speak("hi user,i am your chat bot")                 
while(repeater==1):
    checker=search()
    if checker==1:
        repeater=0
speak("It is my pleasure to help you,see you again, bye")
