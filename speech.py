import speech_recognition as sr
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        query = d
        print("User said: ",query)

    except Exception as e :
        print("Say That Again Please .....")