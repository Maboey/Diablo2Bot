"""
Fake Input
"""
from win32api import GetSystemMetrics
import keyboard
import mouse
from PIL import ImageGrab
import os

def GetScreenSize():
    screenSize = [GetSystemMetrics(0),GetSystemMetrics(1)]
    print("ScreenSize : X = ", str(screenSize[0]),", Y = ", str(screenSize[1]))
    return screenSize

def ClickXY(x,y):
    mouse.move(x,y)
    mouse.click()

def KeyboardInput(k_input):
    keyboard.press_and_release(k_input)

def GetScreenImage():
    box = ()
    image = ImageGrab.grab()
    image.save(os.getcwd() + '\\ScreenWiew' +'.png', 'PNG')
    return (os.getcwd() + '\\ScreenWiew.png')