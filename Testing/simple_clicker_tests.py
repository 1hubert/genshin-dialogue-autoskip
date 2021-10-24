from pynput.mouse import Button, Controller
import cv2, time, atexit, pyautogui, sys, numpy as np, pandas as pd
from mss import mss
from PIL import Image

mouse = Controller()

def simple_left_click():
    time.sleep(0.512)
    pyautogui.click()
    time.sleep(0.234)

def left_click_with_position():
    time.sleep(1)
    mouse.position = (1891, 613)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    pyautogui.keyDown("esc")
    pyautogui.keyUp("esc")

def simple_space():
    time.sleep(1)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')





