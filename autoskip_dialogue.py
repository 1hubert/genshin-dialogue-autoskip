import time
import random

import pyautogui
from pynput.mouse import Controller
from pynput import keyboard
from threading import Thread
from ctypes import windll

RESOLUTION = (1920, 1080)  # Supported: (1920, 1080) and (1024, 768)
PLAYING_ICON_COLOR = (236, 229, 216)

mouse = Controller()

if RESOLUTION == (1920, 1080):
    # Bottom dialogue option dimensions
    MIN_X = 1282
    MAX_X = 1775
    MIN_Y = 774
    MAX_Y = 825

    # Pixel coordinates for white part of the auto play button
    PLAYING_ICON_X = 111
    PLAYING_ICON_Y = 46

    # Pixel coordinates for white part of the speech bubble in bottom dialogue option
    DIALOGUE_ICON_X = 1301
    DIALOGUE_ICON_Y = 808

    # Pixel coordinates near middle of the screen known to be white while the game is loading
    LOADING_SCREEN = (1200, 700)

elif RESOLUTION == (1024, 768):  # Full HD windowed mode, window positioned in the bottom right corner
    # Bottom dialogue option dimensions
    MIN_X = 1584
    MAX_X = 1766
    MIN_Y = 920
    MAX_Y = 942

    # Pixel coordinates for white part of the auto play button
    PLAYING_ICON_X = 954
    PLAYING_ICON_Y = 337

    # Pixel coordinates for white part of the speech bubble in bottom dialogue option
    DIALOGUE_ICON_X = 1587
    DIALOGUE_ICON_Y = 925

    # Pixel coordinates near middle of the screen known to be white while the game is loading
    LOADING_SCREEN = (1450, 790)


def getpixel(x, y):
    dc = windll.user32.GetDC(0)
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc, x, y), 3, 'little'))


def random_interval():
    if random.randrange(1, 7) == 6:
        return random.uniform(0.18, 0.3)
    return random.uniform(0.12, 0.18)


def random_cursor_position():
    x = random.randrange(MIN_X, MAX_X+1)
    y = random.randrange(MIN_Y, MAX_Y+1)
    position = (x, y)
    print('Cursor moved to: ', position)
    return position


def exit_program():
    def on_press(key):
        if str(key) == 'Key.f8':
            main.status = 'run'
            print('RUNNING')

        elif str(key) == 'Key.f9':
            main.status = 'pause'
            print('PAUSED')

        elif str(key) == 'Key.f12':
            main.status = 'exit'
            exit()

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'pause'
    last_reposition = 0
    time_between_repositions = random_interval()*80

    print('-------------')
    print('F8 to start')
    print('F9 to stop')
    print('F12 to quit')
    print('-------------')

    while True:
        while main.status == 'pause':
            time.sleep(0.5)

        if main.status == 'exit':
            print('Main program closing')
            break

        if (getpixel(PLAYING_ICON_X, PLAYING_ICON_Y) == PLAYING_ICON_COLOR or
            getpixel(DIALOGUE_ICON_X, DIALOGUE_ICON_Y) == (255, 255, 255) and
            getpixel(LOADING_SCREEN[0], LOADING_SCREEN[1]) != (255, 255, 255)):

            if time.time() - last_reposition > time_between_repositions:
                last_reposition = time.time()
                time_between_repositions = random_interval()*80
                mouse.position = random_cursor_position()

            time.sleep(random_interval())
            pyautogui.click()
            print('*click*')


Thread(target=main).start()
Thread(target=exit_program).start()
