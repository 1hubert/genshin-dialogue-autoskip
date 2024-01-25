import os
from random import randint, uniform
from threading import Thread
from typing import Tuple, Union
from time import perf_counter, sleep
from win32api import GetSystemMetrics

from pyautogui import click, getActiveWindowTitle, pixel
from pynput.mouse import Controller
from pynput.keyboard import Key, KeyCode, Listener
from dotenv import find_dotenv, load_dotenv, set_key

# Initial setup
os.system('cls')
load_dotenv()
print('Welcome to Genshin Impact Dialogue Skipper\n')

# Check if either screen dimension is missing from .env
if os.environ['WIDTH'] == '' or os.environ['HEIGHT'] == '':
    # Detect and set screen dimensions
    SCREEN_WIDTH = GetSystemMetrics(0)
    SCREEN_HEIGHT = GetSystemMetrics(1)

    # In case the resolution is not correct, ask for the correct resolution
    print(f'Detected Resolution: {SCREEN_WIDTH}x{SCREEN_HEIGHT}')
    print('Is the resolution correct? (y/n)')
    response = input()

    if response.lower().startswith('n'):
        print('Enter resolution width: ', end='')
        SCREEN_WIDTH = int(input())
        print('Enter resolution height: ', end='')
        SCREEN_HEIGHT = int(input())
        print('\nNew resolution set to ' + str(SCREEN_WIDTH) + 'x' + str(SCREEN_HEIGHT) + '\n')

    # Write changes to .env file
    dotenv_file = find_dotenv()
    set_key(dotenv_file, "WIDTH", str(SCREEN_WIDTH), quote_mode="never")
    set_key(dotenv_file, "HEIGHT", str(SCREEN_HEIGHT), quote_mode="never")
else:
    # Read screen dimensions from .env
    SCREEN_WIDTH = int(os.getenv('WIDTH'))
    SCREEN_HEIGHT = int(os.getenv('HEIGHT'))

def width_adjust(x: int) -> int:
    """Adjust variables to the width of the screen."""
    return int(x/1920 * SCREEN_WIDTH)

def height_adjust(y: int) -> int:
    """Adjust variables to the height of the screen."""
    return int(y/1080 * SCREEN_HEIGHT)

# Dimensions of bottom dialogue option
BOTTOM_DIALOGUE_MIN_X = width_adjust(1300)
BOTTOM_DIALOGUE_MAX_X = width_adjust(1700)
BOTTOM_DIALOGUE_MIN_Y = height_adjust(790)
BOTTOM_DIALOGUE_MAX_Y = height_adjust(800)

# Pixel coordinates for white part of the autoplay button
PLAYING_ICON_X = width_adjust(84)
PLAYING_ICON_Y = height_adjust(46)

# Pixel coordinates for white part of the speech bubble in bottom dialogue option
DIALOGUE_ICON_X = width_adjust(1301)
DIALOGUE_ICON_LOWER_Y = height_adjust(808)
DIALOGUE_ICON_HIGHER_Y = height_adjust(790)

# Pixel coordinates near middle of the screen known to be white while the game is loading
LOADING_SCREEN_X = width_adjust(1200)
LOADING_SCREEN_Y = height_adjust(700)


def random_interval() -> float:
    """
    Return a random interval between 0.12 and 0.18 seconds, or 0.18 and 0.2 seconds if a 6 is rolled.
    :return: A random interval between 0.12 and 0.18 seconds, or 0.18 and 0.3 seconds if a 6 is rolled.
    """

    return uniform(0.18, 0.2) if randint(1, 6) == 6 else uniform(0.12, 0.18)


def random_cursor_position() -> Tuple[int, int]:
    """
    The cursor is moved to a random position in the bottom dialogue option.
    :return: A random (x, y) in range of the bottom dialogue option.
    """

    x = randint(BOTTOM_DIALOGUE_MIN_X, BOTTOM_DIALOGUE_MAX_X)
    y = randint(BOTTOM_DIALOGUE_MIN_Y, BOTTOM_DIALOGUE_MAX_Y)

    return x, y


def on_press(key: (Union[Key, KeyCode, None])) -> None:
    """
    Start, stop, or exit the program based on the key pressed.
    :param key: The key pressed.
    :return: None
    """

    key_pressed = str(key)

    if key_pressed == 'Key.f8':
        main.status = 'run'
        print('RUNNING')
    elif key_pressed == 'Key.f9':
        main.status = 'pause'
        print('PAUSED')
    elif key_pressed == 'Key.f12':
        main.status = 'exit'
        exit()


def main() -> None:
    """
    Skip Genshin Impact dialogue when it's present based on the colors of 3 specific pixels.
    :return: None
    """

    def is_genshinimpact_active():
        """Check if Genshin Impact is the active window."""
        return getActiveWindowTitle() == "Genshin Impact"

    def is_dialogue_playing():
        return pixel(PLAYING_ICON_X, PLAYING_ICON_Y) == (236, 229, 216)

    def is_dialogue_option_available():
        # Confirm loading screen is not white
        if pixel(LOADING_SCREEN_X, LOADING_SCREEN_Y) == (255, 255, 255):
            return False

        # Check if lower dialogue icon pixel is white
        if pixel(DIALOGUE_ICON_X, DIALOGUE_ICON_LOWER_Y) == (255, 255, 255):
            return True

        # Check if higher dialogue icon pixel is white
        if pixel(DIALOGUE_ICON_X, DIALOGUE_ICON_HIGHER_Y) == (255, 255, 255):
            return True

        return False

    main.status = 'pause'
    last_reposition = 0.0
    time_between_repositions = random_interval() * 40

    print('-------------\n'
          'F8 to start\n'
          'F9 to stop\n'
          'F12 to quit\n'
          '-------------')

    while True:
        while main.status == 'pause':
            sleep(0.5)

        if main.status == 'exit':
            print('Main program closing')
            break

        if is_genshinimpact_active() and (is_dialogue_playing() or is_dialogue_option_available()):
            if perf_counter() - last_reposition > time_between_repositions:
                last_reposition = perf_counter()
                time_between_repositions = random_interval() * 40
                mouse.position = random_cursor_position()

            click()


if __name__ == "__main__":
    mouse = Controller()
    Thread(target=main).start()

    with Listener(on_press=on_press) as listener:
        listener.join()
