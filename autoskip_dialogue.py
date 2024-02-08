from random import randrange, uniform
from threading import Thread
from typing import Union
from time import sleep
import os

import vgamepad as vg
from win32api import GetSystemMetrics
from dotenv import load_dotenv, find_dotenv, set_key
from pyautogui import pixel, click
from pynput.mouse import Controller
from pynput.keyboard import Key, KeyCode, Listener

# Initial setup
os.system('cls')
load_dotenv()
print('Welcome to Genshin Impact Dialogue Skipper for gamepads\n')

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

# Pixel coordinates for pink pixel of the autoplay button (DualShock 4 Square and Xbox 'X'). eng
DS4_ENG_AUTOPLAY_ICON_X: int = width_adjust(1450)
DS4_ENG_AUTOPLAY_ICON_Y: int = height_adjust(1010)
XBOX_ENG_AUTOPLAY_ICON_X: int = width_adjust(1444)
XBOX_ENG_AUTOPLAY_ICON_Y: int = height_adjust(1006)

# Pixel coordinates for blue pixel of the confirm button (DualShock 4 cross and Xbox 'B'). eng
DS4_ENG_CONFIRM_ICON_X: int = width_adjust(1683)
DS4_ENG_CONFIRM_ICON_Y: int = height_adjust(1013)
XBOX_ENG_CONFIRM_ICON_X: int = width_adjust(1624)
XBOX_ENG_CONFIRM_ICON_Y: int = height_adjust(1008)

# Pixel coordinates for pink pixel of the autoplay button (DualShock 4 square and Xbox 'X'). rus
DS4_RUS_AUTOPLAY_ICON_X: int = width_adjust(1432)
DS4_RUS_AUTOPLAY_ICON_Y: int = height_adjust(1010)
XBOX_RUS_AUTOPLAY_ICON_X: int = width_adjust(1444)
XBOX_RUS_AUTOPLAY_ICON_Y: int = height_adjust(1006)

# Pixel coordinates for blue pixel of the confirm button (DualShock 4 cross and Xbox 'B'). rus
DS4_RUS_CONFIRM_ICON_X: int = width_adjust(1628)
DS4_RUS_CONFIRM_ICON_Y: int = height_adjust(1013)
XBOX_RUS_CONFIRM_ICON_X: int = width_adjust(1624)
XBOX_RUS_CONFIRM_ICON_Y: int = height_adjust(1005)

# Pixel coordinates for white part of the speech bubble in bottom dialogue option. (DualShock 4 and Xbox)
DS4_DIALOGUE_ICON_X: int = width_adjust(1300)
DS4_DIALOGUE_ICON_Y: int = height_adjust(770)
XBOX_DIALOGUE_ICON_X: int = width_adjust(1300)
XBOX_DIALOGUE_ICON_Y: int = height_adjust(770)

# Pixel coordinates near middle of the screen known to be white while the game is loading.
LOADING_SCREEN_X: int = width_adjust(1200)
LOADING_SCREEN_Y: int = height_adjust(700)

def define_ui() -> str:
    """
    Check autoplay and confirm (square and cross) buttons pixels for DS4 UI, and autoplay icon pixel for keyboard and
    mouse UI. Works for 1920x1080 game resolution.
    :return: String value that defines UI
    """
    ui = ''

    if pixel(DS4_ENG_AUTOPLAY_ICON_X, DS4_ENG_AUTOPLAY_ICON_Y) == (204, 114, 238) and pixel(DS4_ENG_CONFIRM_ICON_X, DS4_ENG_CONFIRM_ICON_Y) == (56, 161, 229):
        ui = 'DS4_ENG'
    elif pixel(DS4_RUS_AUTOPLAY_ICON_X, DS4_RUS_AUTOPLAY_ICON_Y) == (204, 114, 238) and pixel(DS4_RUS_CONFIRM_ICON_X, DS4_RUS_CONFIRM_ICON_Y) == (56, 161, 229):
        ui = 'DS4_RUS'
    elif pixel(XBOX_ENG_AUTOPLAY_ICON_X, XBOX_ENG_AUTOPLAY_ICON_Y) == (50, 175, 255) and pixel(XBOX_ENG_CONFIRM_ICON_X, XBOX_ENG_CONFIRM_ICON_Y) == (56, 161, 229):
        ui = 'XBOX_ENG'
    elif pixel(XBOX_RUS_AUTOPLAY_ICON_X, XBOX_RUS_AUTOPLAY_ICON_Y) == (50, 175, 255) and pixel(XBOX_RUS_CONFIRM_ICON_X, XBOX_ENG_CONFIRM_ICON_Y) == (56, 161, 229):
        ui = 'XBOX_RUS'

    return ui


def random_interval() -> float:
    """
    Return a random interval between 0.12 and 0.18 seconds, or 0.18 and 0.3 seconds if a 6 is rolled.
    :return: A random interval between 0.12 and 0.18 seconds, or 0.18 and 0.3 seconds if a 6 is rolled.
    """

    return uniform(0.18, 0.3) if randrange(1, 7) == 6 else uniform(0.12, 0.18)


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


def is_dialogue() -> bool:
    """
    Check if dialogue icon is present or not
    :return: Boolean True if dialogue icon is present, otherwise False
    """
    if pixel(DS4_DIALOGUE_ICON_X, DS4_DIALOGUE_ICON_Y) == (255, 255, 255) \
            and pixel(LOADING_SCREEN_X, LOADING_SCREEN_Y) != (255, 255, 255):
        return True

    if pixel(XBOX_DIALOGUE_ICON_X, XBOX_DIALOGUE_ICON_Y) == (255, 255, 255) \
            and pixel(LOADING_SCREEN_X, LOADING_SCREEN_Y) != (255, 255, 255):
        return True

    return False


def select_last_dialogue_option(gamepad: Union[vg.VDS4Gamepad, vg.VX360Gamepad]) -> None:
    """
    Press 'up' on the gamepad to select the bottom dialogue option
    :param gamepad: Virtual gamepads Xbox and DS4
    :return: None
    """
    ds4_buttons = vg.DS4_BUTTONS
    xbox_buttons = vg.XUSB_BUTTON

    if isinstance(gamepad, vg.VDS4Gamepad):
        button = ds4_buttons.DS4_BUTTON_CROSS
        method_name = 'press_button'
        dpad_direction = vg.DS4_DPAD_DIRECTIONS.DS4_BUTTON_DPAD_NORTH
    elif isinstance(gamepad, vg.VX360Gamepad):
        button = xbox_buttons.XUSB_GAMEPAD_B
        method_name = 'press_button'
        dpad_direction = None
    else:
        print('Unsupported gamepad, skipping...')
        return

    method = getattr(gamepad, method_name)
    method(button.value)

    if dpad_direction:
        gamepad.directional_pad(direction=dpad_direction)
        gamepad.update()
        sleep(random_interval())

    gamepad.reset()
    gamepad.update()
    sleep(random_interval())


def press_cross(gamepad: Union[vg.VDS4Gamepad, vg.VX360Gamepad]) -> None:
    """
    Press 'cross or B' on the gamepad to select the bottom dialogue option
    :param gamepad: Virtual gamepads Xbox and DS4
    :return: None
    """
    ds4_buttons = vg.DS4_BUTTONS
    xbox_buttons = vg.XUSB_BUTTON

    if isinstance(gamepad, vg.VDS4Gamepad):
        button = ds4_buttons.DS4_BUTTON_CROSS
    elif isinstance(gamepad, vg.VX360Gamepad):
        button = xbox_buttons.XUSB_GAMEPAD_B
    else:
        print('Unsupported gamepad, skipping...')
        return

    gamepad.report.wButtons |= button.value

    gamepad.update()
    sleep(random_interval())
    gamepad.reset()
    gamepad.update()
    sleep(random_interval())


def main() -> None:
    """
    Skip Genshin Impact dialogue when it's present based on the colors of some specific pixels.
    :return: None
    """

    main.status = 'pause'
    ds4_gamepad = vg.VDS4Gamepad()
    xbox_gamepad = vg.VX360Gamepad()

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

        if define_ui() == 'DS4_ENG' or is_dialogue():
            if is_dialogue():
                select_last_dialogue_option(ds4_gamepad)
            press_cross(ds4_gamepad)

        if define_ui() == 'DS4_RUS' or is_dialogue():
            if is_dialogue():
                select_last_dialogue_option(ds4_gamepad)
            press_cross(ds4_gamepad)

        if define_ui() == 'XBOX_ENG' or is_dialogue():
            if is_dialogue():
                select_last_dialogue_option(xbox_gamepad)
            press_cross(xbox_gamepad)

        if define_ui() == 'XBOX_RUS' or is_dialogue():
            if is_dialogue():
                select_last_dialogue_option(xbox_gamepad)
            press_cross(xbox_gamepad)

            click()

if __name__ == '__main__':
    mouse = Controller()
    Thread(target=main).start()
    Thread(target=exit_program).start()
