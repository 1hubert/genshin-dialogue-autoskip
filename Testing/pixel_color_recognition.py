from ctypes import windll
dc= windll.user32.GetDC(0)

def getpixel(x,y):
    return tuple(int.to_bytes(windll.gdi32.GetPixel(dc,x,y), 3, 'little'))


print(getpixel(951,280))
print(getpixel(954, 335))