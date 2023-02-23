from random import randrange, uniform
from threading import Thread
from typing import Tuple, Union
from time import sleep, time

import pyautogui
from pynput.mouse import Controller
from pynput.keyboard import Key, KeyCode, Listener

# Dimensions of bottom dialogue option.
BOTTOM_DIALOGUE_MIN_X: int = 1300
BOTTOM_DIALOGUE_MAX_X: int = 1700
BOTTOM_DIALOGUE_MIN_Y: int = 790
BOTTOM_DIALOGUE_MAX_Y: int = 800

# Pixel coordinates for white part of the autoplay button.
PLAYING_ICON_X: int = 111
PLAYING_ICON_Y: int = 46

# Pixel coordinates for white part of the speech bubble in bottom dialogue option.
DIALOGUE_ICON_X: int = 1301
DIALOGUE_ICON_Y: int = 808

# Pixel coordinates near middle of the screen known to be white while the game is loading.
LOADING_SCREEN_X: int = 1200
LOADING_SCREEN_Y: int = 700


def get_pixel(x: int, y: int) -> Tuple[int, int, int]:
    """
    Return the RGB value of a pixel.
    :param x: The x coordinate of the pixel.
    :param y: The y coordinate of the pixel.
    :return: The RGB value of the pixel.
    """

    return pyautogui.pixel(x, y)


def random_interval() -> float:
    """
    Return a random interval between 0.12 and 0.18 seconds, or 0.18 and 0.3 seconds if a 6 is rolled.
    :return: A random interval between 0.12 and 0.18 seconds, or 0.18 and 0.3 seconds if a 6 is rolled.
    """

    return uniform(0.18, 0.3) if randrange(1, 7) == 6 else uniform(0.12, 0.18)


def random_cursor_position() -> Tuple[int, int]:
    """
    The cursor is moved to a random position in the bottom dialogue option.
    :return: A random (x, y) in range of the bottom dialogue option.
    """

    x: int = randrange(BOTTOM_DIALOGUE_MIN_X, BOTTOM_DIALOGUE_MAX_X + 1)
    y: int = randrange(BOTTOM_DIALOGUE_MIN_Y, BOTTOM_DIALOGUE_MAX_Y + 1)

    return x, y


def exit_program() -> None:
    """
    Listen for keyboard input to start, stop, or exit the program.
    :return: None
    """

    def on_press(key: (Union[Key, KeyCode, None])) -> None:
        """
        Start, stop, or exit the program based on the key pressed.
        :param key: The key pressed.
        :return: None
        """

        key_pressed: str = str(key)

        if key_pressed == 'Key.f8':
            main.status = 'run'
            print('RUNNING')
        elif key_pressed == 'Key.f9':
            main.status = 'pause'
            print('PAUSED')
        elif key_pressed == 'Key.f12':
            main.status = 'exit'
            exit()

    with Listener(on_press=on_press) as listener:
        listener.join()


def main() -> None:
    """
    Skip Genshin Impact dialogue when it's present based on the colors of 3 specific pixels.
    :return: None
    """

    main.status = 'pause'
    last_reposition: float = 0.0
    time_between_repositions: float = random_interval() * 80

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

        if get_pixel(PLAYING_ICON_X, PLAYING_ICON_Y) == (236, 229, 216) or get_pixel(DIALOGUE_ICON_X,
                                                                                     DIALOGUE_ICON_Y) == (
                255, 255, 255) and get_pixel(LOADING_SCREEN_X, LOADING_SCREEN_Y) != (255, 255, 255):
            if time() - last_reposition > time_between_repositions:
                last_reposition = time()
                time_between_repositions = random_interval() * 80
                mouse.position = random_cursor_position()

            sleep(random_interval())
            pyautogui.click()


if __name__ == "__main__":
    mouse = Controller()
    Thread(target=main).start()
    Thread(target=exit_program).start()
