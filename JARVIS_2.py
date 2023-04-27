import pyttsx3
import datetime
import speech_recognition as sr
# import wikipedia
# import webbrowser
import os
# import smtplib


engine = pyttsx3.init('sapi')
voices = engine.getProperty('voices')
print(voices[0].id)

engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("A  very  Good  Morning") 
         
    elif hour >= 12 and hour< 18 :
        speak("Good Afternoon !")

    else:
        speak("Good Evening !")

    speak ("I am  EMMA   an   assistant made by Yesh Sir. How may I help You!")
# def send_Email(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('Youremail@gmail.com', 'Your Password Here')
#     server.sendmail('Youremail@gmail.com', to, content)
#     server.close()
# def takecommand():
#     d = "How may I help you"
#     r = str(input("Enter What You Want To Do"))
#      with sr.Microphone() as source:
#          print("Listening......")
#          r.pause_threshold = 2
#          audio = r.listen(source)
#
#      try:
#          print("Recognizing.....")
#          query = r.recognize_google(audio, language='en-in')
#          query = d
#          print("User said: ",query)
#
#      except Exception as e :
#          print("Say That Again Please .....")

if __name__ == "__main__":
    speak("Naaamaashkaar  useErR ")
    WishMe()
    print("Write Exit to exit Code")
    while True:
        query = str(input(("Enter Input"))).lower()
        if 'harry potter' in query:
            speak("Harry  Potter Is a series of  eight  books written by J K Rowllings  which is based on Magical World")
            speak("Harry  Potter is basically a character who is playing lead role in the series")
            speak("Want to know more about Harry Potter Write Y")
            print("Press \"N\" to exit ")
            x = str(input("Enter Choice")).lower()
            if x =='y':
                speak("Harry potter series is Having eight books whose Names are")
                speak("First")
                speak("Harry Potter And the Philospher Stone OR Harry Potter and the Soccers Stone ")
                print("1 to Play")
                speak("Second")
                speak("Harry Potter And the Chamber of Secrets ")
                print("2 to Play")
                speak("Third")
                speak("Harry Potter And the Prisoner of Azakaban")
                print("3 to Play")
                speak("Fourth")
                speak("Harry Potter And the Goblet of Fire ")
                print("4 to Play")
                speak("Fifth")
                speak("Harry Potter And the Order of Phoinex ")
                print("5 to Play")
                speak("Sixth")
                speak("Harry Potter And The Half BloodPrince ")
                print("6 to Play")
                speak("Seventh")
                speak("Harry Potter And The Deathly Hallows Part 1")
                print("7 to Play")
                speak("Eighth")
                speak("Harry Potter And The Deathly Hallows Part 2")
                print("8 to Play")
                z = int(input("Enter Movie You Want to Play"))
                if z == 1:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\1 Harry Potter and the Philosophers Stone.mkv"
                    os.startfile(cPath)
                elif z == 2:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\2 Harry Potter and the Chamber of Secrets.mkv"
                    os.startfile(cPath)
                elif z == 3:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\3 Harry Potter and the Prisoner of Azkaban.mkv"
                    os.startfile(cPath)
                elif z == 4:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\4 Harry Potter and the Goblet of Fire.mkv"
                    os.startfile(cPath)
                elif z == 5:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\5 Harry Potter and the Order of Phionex.mkv"
                    os.startfile(cPath)
                elif z == 6:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\6 Harry Potter And The Half BloodPrince.mkv"
                    os.startfile(cPath)
                elif z == 7:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\7 Harry Potter And The Deathly Hallows Part 1.mkv"
                    os.startfile(cPath)
                elif z == 8:
                    cPath = "C:\\Users\\hp\\Desktop\\DHRUV\\MOVIES\\Harry Potter\\8 Harry Potter And The Deathly Hallows Part 2.mkv"
                    os.startfile(cPath)
                else:
                    speak("You Pressed Wrong Key")
            elif x == 'n':
                speak("Exit")
            else:
                speak("You Pressed Wrong Key")

        elif 'wikipedia' in query:
            speak('Searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            


        elif 'hi' in query:
            speak("Hi Sir I am Jarvis")
            speak("If you want to know more Write About")
            print("ABOUT")

        # elif 'harry potter' in query:
        #     speak("Hello")
        #     speak("Harry Potter Is a series of 8 books written by J K Rowllingswhich is based on Magical World")
        #     speak("HarryPotter is basically a character who is playing lead role in the series")
        #     speak("Want to know more about Harry Potter Wrete Y")
        #     print("Press \"N\" to exit ")

        elif 'about' in query:
            speak("I   am   Basically   AN   ai   Which   is   Made   on   PYTHON   Language AI Stands For Artificial Intelligence Behind An AI Program the basic idea is ")
            speak("to make Computer code that can talk like a chat bot like,,,,, amazon alexa,,,,google asistant,,,,,,siri. i am made By Yesh SIR")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        
        elif 'play music' in query:
            music_dir = 'E:\\YASH\\MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            sTime = datetime.datetime.now().strftime(" %H %M %S ")
            print(sTime)
            speak(f"sir , the time is {sTime}")

        elif 'open pycharm' in query:
            cPath = "C:\Program Files\JetBrains\PyCharm Community Edition 2019.3.2\bin\\pycharn64.exe"
            os.startfile(cPath)

        elif 'open snake game' in query:
            cPath = "E:\\YASH\\Snake Game\\Snake Game.py"
            os.startfile(cPath)

        elif 'open code' in query:
            caPath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code"
            caPath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(caPath)

        elif 'Send Email' in query:
            try:
                speak("What should i say")
                content = query
                to = "yaaassh@gmail.com"
                send_Email(to, content)
                speak("Email has been Sent")
            except Exception as e:
                print(e)
                speak('Say That Again Please .....')

        elif 'open adobe photoshop' in query:
            caPath = "C:\\Program Files (x86)\\Adobe Photoshop CS6"
            caPath = "C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe"
            os.startfile(caPath)
        elif 'exit' in query:
            speak("Bye user Nice to talk you")
            exit()

        else :
            speak("Bye user Nice to talk you")
            print("Sorry I didnt Catch You Say That Again Please")