"""
Fake Input
"""
from win32api import GetSystemMetrics
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
from PIL import ImageGrab
import os

def GetScreenSize():
    screenSize = [GetSystemMetrics(0),GetSystemMetrics(1)]
    print("ScreenSize : X = ", str(screenSize[0]),
    
     ", Y = ", str(screenSize[1]))
    return screenSize

def ClickXY(x,y,buttonLR):
    mouse = MouseController()
    mouse.position = (x,y)
    if(buttonLR == 0):
        mouse.press(Button.left)
        mouse.release(Button.left)
    else:
        mouse.press(Button.right)
        mouse.release(Button.right)

def KeyboardInput(k_input):
    keyboard = KeyboardController()
    if(k_input == "enter"):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        keyboard.press(k_input)
        keyboard.release(k_input)


def GetScreenImage():
    box = ()
    image = ImageGrab.grab()
    image.save(os.getcwd() + '\\ScreenWiew' +'.png', 'PNG')
    return (os.getcwd() + '\\ScreenWiew.png')