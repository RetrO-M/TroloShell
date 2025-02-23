<p align='center'>
  <b>TroloShell</b><br>  
  <a href="https://github.com/RetrO-M">Github</a> |
  <a href="https://github.com/RetrO-M/TroloShell/issues">Report Bug</a>
</p>

A remote server-client software designed to execute various "troll" commands on a target machine. This software allows the server to control and execute different pranks and actions, such as displaying fake error messages, taking screenshots, controlling the mouse, and more.

## **Features**

```py
SERVER = "IP_LOCAL"
PORT = 4444  
```

### **Server-side**
- **Listening on specific IP and port**
- **Multiple prank commands**:
  - **msgbox**: Show a fake alert message with a random message (e.g., "Fatal Error!", "System error: format C:", etc.).
  - **open_cd**: Open and close the CD/DVD tray.
  - **beep**: Play random beep sounds through the target machine.
  - **screenshot**: Capture and send a screenshot from the target machine.
  - **mouse**: Move the mouse cursor randomly on the screen.
  - **screen**: Turn off the screen and turn it back on.
  - **flash**: Flash the screen by changing wallpaper rapidly.
  - **webcam**: Open the webcam and display a message on the screen for a short time.
  - **robot**: Make the system speak with a robot-like voice.
  - **notepad**: Open Notepad and type a menacing message.
  - **led**: Flash the keyboard LEDs on and off.
  - **sos**: Display SOS Morse code with the keyboard LEDs.

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
client.py  server.py
root:~/# pip3 install pyinstaller
root:~/# pyinstaller client.py --noconsole --onefile
root:~/# cd dist/
root:~/dist/# ls
client.exe
root:~/dist/# 
```
