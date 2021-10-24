from pynput.keyboard import Key, Listener

def on_press(key):
    print('{0} pressed'.format(key))
    if str(key) == 'Key.esc':
        return False
    check_key(key)

def check_key(key):
    if key in [Key.up, Key.down, Key.left, Key.right]: 
        print('YES')
    

# Collect events until released
with Listener(
        on_press=on_press) as listener:
    listener.join()