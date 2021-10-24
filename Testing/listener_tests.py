from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(key))
    check_key(key)

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False

def check_key(key):
    if key in [Key.up, Key.down, Key.left, Key.right]: 
        print('YES')

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()