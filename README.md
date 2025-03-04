<p align='center'>
  <b>TroloShell</b><br>  
  <a href="https://github.com/RetrO-M">Github</a> |
  <a href="https://github.com/RetrO-M/TroloShell/issues">Report Bug</a>
</p>

A remote server-client software designed to execute various "troll" commands on a target machine. This software allows the server to control and execute different pranks and actions, such as displaying fake error messages, taking screenshots, controlling the mouse, and more.

## **Features**

```py
SERVER = "YOUR_SERVER_IP" # For example your LOCAL IP
PORT = 4444  
```

### **Server-side**
- **Listening on specific IP and port**
- **Multiple prank commands**:
  - **msgbox**: Show a fake alert message
  - **beep**: Play random beep sounds
  - **mouse**: Move mouse randomly
  - **screenlock**: Lock screen
  - **led**: Flash the keyboard LEDs on and off
  - **errorsound**: Trigger Windows error noise
  - **shakymouse**: Shake the mouse
  - **background**: Flash the screen by changing wallpaper rapidly.
  - **flash**: Turn off the screen and turn it back on
  - **opencd**: Open and close the CD/DVD tray
  - **notification**: Put a notification
  - **webcam**: Turn on the webcam light
  - **robot**: Make the computer speak
  - **notepad**: Launch the NOTEPAD application and post a message
  - **theme**: Change color
  - **shake**: Shake the open windows
  - **flip**: Screen that flips every second

### **Client-side**
- **Connect to the server** and execute received commands.
- **Send back feedback** to the server, including results of commands like screenshots or logs.
- **Execute system commands**, including those that involve sound, graphics, and hardware manipulation.

## **Disclaimer**

### **Ethical Use Only**
This software is designed purely for educational purposes and to demonstrate the concept of remote command execution. It should only be used in environments where you have explicit permission to run pranks and tests. Unauthorized use on machines you do not own or have explicit consent to interact with is illegal and can lead to severe consequences.

### **No Malicious Intent**
The software is not intended to harm systems, disrupt services, or interfere with personal or professional data. It is important to use this tool responsibly, ensuring it does not violate any laws or ethical guidelines.

### **Risk of Misuse**
While the software can be used for harmless fun, it can be misused to prank individuals or organizations without their knowledge or consent. Always ensure that the use of this software is consensual and legal.

## **Installation**

1. **Download** : `git clone https://github.com/RetrO-M/TroloShell` & `cd TroloShell`
2. **Starting the server** : `python3 server.py`

## **Py To Exe**

```bash
root:~/# ls
client.py 
server.py
root:~/# pip3 install pyinstaller
root:~/# pyinstaller client.py --noconsole --onefile
root:~/# cd dist/
root:~/dist/# ls
client.exe
root:~/dist/# 
```
