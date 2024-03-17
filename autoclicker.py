from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener
import time
import threading
import sys

mouse = Controller()

keybind = input("\nSet keybind to start/stop clicking \n> ").strip()
click_type = int(input("\n1 = Single-click \n2 = Double-click \n> ").strip())
delay = float(input("\nClicking speed: ").strip())
end_kb = input("\nSet keybind to end program: ").strip()
hotkey = KeyCode(char = keybind)
quit = KeyCode(char = end_kb)

clicking = False
end = False


def autoclicker():

    while True:

        if clicking:
            mouse.click(Button.left, click_type)

        if end:
            break
        
        time.sleep(delay)


def toggle(key):
    global clicking, end

    if key == hotkey:
        clicking = not clicking

    if key == quit:
        clicking = False
        end = False
        sys.exit()


thread = threading.Thread(target = autoclicker)
thread.start()

with Listener(on_press = toggle) as listener:
    while not end:
        listener.join()