# Autoban (typing)
# Made by Xornotor
# Let's defeat this bots!

import time
from pynput.keyboard import Key, Controller
from pynput import keyboard
keyboard = Controller() 

time.sleep(5)

file = open("banlist.txt", "r")
linhas = file.readlines()

for linha in linhas:
    keyboard.type(linha)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.3)
