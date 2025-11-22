from pynput import mouse
from pynput import keyboard
import time
import threading



mouse_controller = mouse.Controller()
clicking = False

def click_left():
    while clicking:
        mouse_controller.click(mouse.Button.left)
        time.sleep(delay)

def click_right():
    while clicking:
        mouse_controller.click(mouse.Button.right)
        time.sleep(delay)

def on_press_left(key):
    global clicking
    try:
        if key == keyboard.Key.insert:
            clicking = not clicking
            if clicking:
                print("Clicking started")
                threading.Thread(target=click_left, daemon=True).start()
            else:
                print("Clicking stopped")
    except AttributeError:
        pass

def on_press_right(key):
    global clicking
    try:
        if key == keyboard.Key.insert:
            clicking = not clicking
            if clicking:
                print("Clicking started")
                threading.Thread(target=click_right, daemon=True).start()
            else:
                print("Clicking stopped")
    except AttributeError:
        pass


welcomeMessage = """
==================================
            pyclicker
==================================
"""


print(welcomeMessage)

delay = int(input("Type the delay you want in seconds: "))

print(f"The clicker is set to be ran at {delay} seconds.")
print("Clicking will now start/stop when you press the 'insert' key...")

with keyboard.Listener(on_press=on_press_left) as listener:
    listener.join()
