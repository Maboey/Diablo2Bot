"""
Fake Input
"""
from win32api import GetSystemMetrics
import keyboard
import mouse
from PIL import ImageGrab
from PIL import Image
import os
import time

def GetScreenSize():
    screenSize = [GetSystemMetrics(0),GetSystemMetrics(1)]
    return screenSize

def ClickXY(x,y):
    mouse.move(x,y)
    time.sleep(0.1)
    mouse.click()

def KeyboardInput(k_input):
    keyboard.press_and_release(k_input)

def GetScreenPixels():
    box = ()
    image = ImageGrab.grab()
    image.save(os.getcwd() + '\\ScreenWiew' +'.png', 'PNG')
    screenView = Image.open(os.getcwd() + '\\ScreenWiew.png')
    return screenView.load()
