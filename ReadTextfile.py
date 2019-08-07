# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:35:16 2019

@author: Eric
"""
from gtts import gTTS
from pygame import mixer # Load the required library
import easygui
import io

path = easygui.fileopenbox(filetypes = ["*.txt"],default="*.txt")
f = io.open(path, mode="r", encoding="utf-8")    
text = f.read()

tts = gTTS(text=text, lang='de')
path = easygui.filesavebox(msg="MP3 speichern.", title="MP3 speichern", default="*.mp3", filetypes=["*.mp3"])
tts.save(path)

if easygui.ynbox(msg='Shall I play mp3 file?', title=' ', choices=('[<F1>]Yes', '[<F2>]No'), image=None, default_choice='[<F1>]Yes', cancel_choice='[<F2>]No') == True:
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
