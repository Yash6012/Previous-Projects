import pygame
from pygame import mixer
import  time
mixer.init()
mixer.music.load('E:\Python Tricks\Dil Ka Telephone bajta Ring Ring Ra Ra Ring.mp3')

hour = int(input('Enter Hour'))
minu = int(input('Enter Minutes'))
sec = int(input('Enter Second'))
sn = int(input('Enter time to Snooz'))
print('Alarm is Set For :::  ',str(hour) , ":",str(minu),":",str(sec))
tt = False
while not tt:
    if time.localtime().tm_hour == hour and time.localtime().tm_min == minu and time.localtime().tm_sec == sec:
        print("Wake UP")
        mixer.music.play()
