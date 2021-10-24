from pynput.mouse import Controller
from pynput import keyboard
from threading import Thread
import time, random, pyautogui
from ctypes import windll


RESOLUTION = (1024, 768)
LOADING_SCREEN = (1450, 790)
PLAYING_ICON_COLOR = (236, 229, 216)


if RESOLUTION == (1024, 768):
    # bottom dialogue option for 1024*768 windowed
    MIN_X = 1584
    MAX_X = 1766
    MIN_Y = 920
    MAX_Y = 942

    PLAYING_ICON_X = 954
    PLAYING_ICON_Y = 337
    
    DIALOGUE_ICON_X = 1587
    DIALOGUE_ICON_Y = 925
    

dc= windll.user32.GetDC(0)
mouse = Controller()


def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, "little"))


def random_interval():
    if random.randrange(1,7) == 6:
        return random.uniform(0.18, 0.3)
    return random.uniform(0.12, 0.18)


def random_cursor_position():
    x = random.randrange(MIN_X, MAX_X+1)
    y = random.randrange(MIN_Y, MAX_Y+1)
    position = (x, y)
    print("Cursor moved to: ", position)
    return position


def exit_program():
    def on_press(key):
        if str(key) == 'Key.f8':
            main.status = 'run'
            print("RUNNING")

        elif str(key) == 'Key.f9':
            main.status = 'pause'
            print("PAUSED")

        elif str(key) == 'Key.f12':
            main.status = 'exit'
            exit()
    
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def main():
    main.status = 'pause'
    last_reposition = 0
    time_between_reposition = random_interval()*10

    print('-------------')
    print("F8 to start")
    print("F9 to stop")
    print("F12 to quit")
    print('-------------')

    while True:
        while main.status == 'pause':
            time.sleep(0.5)

        if main.status == 'exit':
            print('Main program closing')
            break
        
        temp=getpixel(PLAYING_ICON_X, PLAYING_ICON_Y)==PLAYING_ICON_COLOR or getpixel(DIALOGUE_ICON_X, DIALOGUE_ICON_Y)==(255,255,255) and getpixel(LOADING_SCREEN[0],LOADING_SCREEN[1])!=(255,255,255)
        if temp:
            if time.time() - last_reposition > time_between_reposition:
                last_reposition = time.time()
                time_between_reposition = random_interval()*10
                mouse.position = random_cursor_position()
            time.sleep(random_interval())
            pyautogui.click()
            print("*click*")
        
    
Thread(target=main).start()
Thread(target=exit_program).start()

