from ctypes import windll
import time

dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, 'little'))



time.sleep(1)
print(getpixel(111,46))
time.sleep(1)
print(getpixel(111,46))
time.sleep(1)
print(getpixel(111,46))