from pynput.mouse import Button, Controller
import cv2, time, atexit, pyautogui, sys, numpy as np, pandas as pd
from mss import mss
from PIL import Image

clicked = False
r = g = b = xpos = ypos = 0
img = None

purple = orange = 0

boundaries = [
	([229, 165, 231 ], [250, 194, 254]),
    ([233, 210, 130], [247, 235, 203])
]

img = None

def refreshImage():
    global img
    # img = np.array(ImageGrab.grab(bbox=(0,150,1800,1080)))
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # return img
    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        #img = sct_img
        img = np.float32(Image.frombytes('RGB', sct_img.size,sct_img.bgra, 'raw', 'BGRX'))

def maskImage():
    global purple, orange
    initRef = 0
    baseColor = 0
    recurse = True
    time = 0
    while (time < 24) and (recurse):
        time += 1
        refreshImage()
        color = 0
        for (lower, upper) in boundaries:
            lower = np.array(lower, dtype= "uint8")
            upper = np.array(upper, dtype = "uint8")

            mask = cv2.inRange(img, lower, upper)
            grayMask = cv2.cvtColor(mask, cv2.IMREAD_GRAYSCALE)
            if initRef < 25:
                baseColor += np.sum(grayMask == 255)
                initRef += 1
            elif initRef == 25:
                baseColor = baseColor/25
                initRef += 1
            else:
                if (np.sum(grayMask == 255) > baseColor * 1.0107) and (color == 1):
                    print("You have an orange 5-star weapon!")
                    recurse = False
                    orange += 1 
                    break
                elif (np.sum(grayMask == 255) > baseColor * 1.0107) and (color == 0):
                    print("You have a purple 4-star character!")
                    recurse = False
                    purple += 1
                    break
            


            print(np.sum(grayMask == 255))


            output = cv2.bitwise_and(img, img, mask = mask)
            cv2.imshow('Color Recognition App', output)
        if cv2.waitKey(16) & 0xFF == 27:
            break

mouse= Controller()
#while True:
#    print("The mouse position is " + str(mouse.position))
#    time.sleep(3)
    
#mouse.position = (10,20)

def theAutoclicker():
    cv2.namedWindow('Color Recognition App')
    time.sleep(3)
    pyautogui.keyDown('f3')
    pyautogui.keyUp('f3')
    time.sleep(2)
    print("escape")
    while True:
        time.sleep(.64)
        mouse.position = (1378, 1014)
        pyautogui.click()
        time.sleep(2)
        maskImage()
        print("You got " + str(purple) + "purples and " + str(orange) + " oranges so far.")
        time.sleep(3)
        mouse.position = (1834, 51)
        pyautogui.click()

try:
    theAutoclicker()
except KeyboardInterrupt:
    print("Stopping Auto-Gocha")
    print("You got " + str(purple) + " purples and " + str(orange) + " oranges this time.")
    sys.exit(0)
#maskImage()

