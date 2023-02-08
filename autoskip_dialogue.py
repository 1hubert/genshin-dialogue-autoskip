import time
import random

import pyautogui
from pynput.mouse import Controller
from pynput import keyboard
from threading import Thread

# Dimensions of bottom dialogue option.
MIN_X = 1300
MAX_X = 1700
MIN_Y = 790
MAX_Y = 800

# Pixel coordinates for white part of the auto play button.
PLAYING_ICON_X = 111
PLAYING_ICON_Y = 46

# Pixel coordinates for white part of the speech bubble in bottom dialogue option.
DIALOGUE_ICON_X = 1301
DIALOGUE_ICON_Y = 808

# Pixel coordinates near middle of the screen known to be white while the game is loading.
LOADING_SCREEN = (1200, 700)


def getpixel(x, y):
    """Return a tuple with RGB values of a pixel in location (x, y)."""
    return pyautogui.pixel(x, y)


def random_interval():
    """Return a small randomized float from range (0.12, 0.3).
    The way the float is randomized is made to be slightly more unpredictable.
    """
    if random.randrange(1, 7) == 6:
        return random.uniform(0.18, 0.3)
    return random.uniform(0.12, 0.18)


def random_cursor_position():
    """Move cursor to a random position in range of the bottom dialogue option."""
    x = random.randrange(MIN_X, MAX_X + 1)
    y = random.randrange(MIN_Y, MAX_Y + 1)
    position = (x, y)
    return position


def exit_program():
    """Listen to keyboard presses and set status of the main function accordingly."""

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
    """Skip Genshin Impact dialogue when it's present based on the colors of 3 specific pixels."""
    main.status = 'pause'
    last_reposition = 0
    time_between_repositions = random_interval() * 80

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

        if (getpixel(PLAYING_ICON_X, PLAYING_ICON_Y) == (236, 229, 216) or
                getpixel(DIALOGUE_ICON_X, DIALOGUE_ICON_Y) == (255, 255, 255) and
                getpixel(LOADING_SCREEN[0], LOADING_SCREEN[1]) != (255, 255, 255)):

            if time.time() - last_reposition > time_between_repositions:
                last_reposition = time.time()
                time_between_repositions = random_interval() * 80
                mouse.position = random_cursor_position()

            time.sleep(random_interval())
            pyautogui.click()


if __name__ == "__main__":
    mouse = Controller()
    Thread(target=main).start()
    Thread(target=exit_program).start()
