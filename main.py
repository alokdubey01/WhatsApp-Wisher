import os
import webbrowser as wb
import pyautogui as pg
import pyttsx3
import time

def browser():
    wb.open("http://web.whatsapp.com/")

def search():
    for i in range(1):
        pg.write("Good morning")
        time.sleep(0)
        pg.press("enter")

browser()
search()
