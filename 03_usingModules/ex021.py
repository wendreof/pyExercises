# [PT-BR] Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import time
from pygame import mixer

mixer.init()
mixer.music.load("Kalimba.wav") #This module dont play Mp3 on Linux
mixer.music.set_volume(50)
mixer.music.play()
time.sleep(30)






