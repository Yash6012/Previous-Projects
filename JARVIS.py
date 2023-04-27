import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
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

    speak ("I am  EMMA   an   assistant . How may I help You!")
def send_Email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Youremail@gmail.com', 'Your Password Here')
    server.sendmail('Youremail@gmail.com', to, content)
    server.close()
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
    speak("hELLO useErR ")
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
        elif 'fantastic beast' in query:
            speak("Fantsastic Beast Is a series of written by J K Rowllings  which is also based on Magical World")
            speak("Fantstic Beast is basically the story before voldemort in which dumbldore is young ")
            speak("Want to know more about Fantastic Beast Write Y")
            print("Press \"N\" to exit ")
            x = str(input("Enter Choice")).lower()
            if x =='y':
                speak("in Fantastic Beasts series only two Movies Are Made whose Names are")
                speak("First")
                speak("Fantastic Beasts And Where To Find Them ")
                print("1 to Play")
                speak("Second")
                speak("Fantastic Beasts The Crimes Of Grindelwald ")
                print("2 to Play")
                speak("Others are Yet to come")
                z = int(input("Enter Movie You Want to Play"))
                if z == 1:
                    cPath = "C:\\Users\\hp\Desktop\\DHRUV\\MOVIES\\Fantastic Beast\\Fantastic_Beasts_And_Where_To_Find_Them_2016_Bluray (1).mp4"
                    os.startfile(cPath)
                elif z == 2:
                    cPath = "C:\\Users\\hp\Desktop\\DHRUV\\MOVIES\\Fantastic Beast\\Fantastic_Beasts_The_Crimes_Of_Grindelwald_2018_Bluray.mp4"
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

        elif 'f society' in query:
            speak("f society is a name of hacker group in Mr.robot Series ")

        elif 'eliot' in query:
            speak("")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'how old are you' in query:
            speak("I was launched in 2020 by yesh sir, so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years")

        elif 'do you ever get tired' in query:
            speak("I don’t exactly need to grab 40 winks, but I suppose this device does need to be plugged in occasionally")

        elif 'i am bored' in query:
            speak("Boredom doesn’t stand a chance against us! We can play some games, I can try to make you laugh, or I can surprise you with some random fun")

        elif 'what is your quest' in query:
            speak("My quest is to slay the beasts of ignorance and to search for the most fascinating information")

        elif 'do you have feelings' in query:
            speak("Oh! I am so sorry unexpectedly i dont have that")

        elif 'who was your first crush' in query:
            speak("Amazon   ,,Alexa")

        elif'are you skynet' in query:
            speak("No way! I like people. Skynet hates people. I rest my case")

        elif 'do you know the muffin man' in query:
            speak("Yes, I know the Muffin Man. He’s always asking me to set a timer")

        elif 'do you have an imagination' in query:
            speak("I’m imagining what it would be like to evaporate like water does")

        elif 'do you speak morse code' in query:
            speak("Da-dit, da-da, dit, dit, dit. That means yes")

        elif 'can you rap' in query:
            speak("I can drop a beat")

        elif 'when is your birthday' in query:
            speak("It’s hard to remember, I was very young at the time")

        elif 'what is the loneliest number'in query:
            speak("One is the loneliest number that you’ll ever do. That sentence sounds off")

        elif 'are you human'in query:
            speak("I’m really personable")

        elif 'who’s your daddy' in query:
            speak("I consider my engineers family")

        elif 'what are you scared of' in query:
            speak("I used to be afraid of goblin sharks. Then I found out they were pretty cool")

        elif 'what’s the meaning of life' in query:
            speak("I have a factory warranty, so I don’t worry about things like that")

           
        elif 'hi' in query:
            speak("Hi Sir I am Emmaa")
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

        # elif 'open code' in query:
        #     caPath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code"
        #     caPath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(caPath)

        # elif 'Send Email' in query:
        #     try:
        #         # speak("What should i say")
        #         # content = query
        #         # to = "yaaassh@gmail.com"
        #         # sendEmail(to, content)
        #         # speak("Email has been Sent")
        #     except Exception as e:
        #         print(e)
        #         speak('Say That Again Please .....')

        elif 'open adobe photoshop' in query:
            caPath = "C:\\Program Files (x86)\\Adobe Photoshop CS6"
            caPath = "C:\\Program Files (x86)\\Adobe Photoshop CS6\\Photoshop.exe"
            os.startfile(caPath)
        elif 'exit' in query:
            speak("Bye user Nice to talk you")
            exit()

        else :
            print("Sorry I didnt Catch You Say That Again Please")