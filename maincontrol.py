"""
maincontrol.py is responsible for establishing a serial connection with the rocket.
The script will open port /dev/ttyS0 to accept rocket's flight data at 115200 8N1.
There will be a constant stream of data, which will be decoded and read 158 bytes at a time.
The script will then call parseData() from parsedata.py and write "rocketdata.txt".
"""

import os
import serial
import time
import RPi.GPIO as GPIO
from parsedata import parseData

GPIO.setmode(GPIO.BOARD)
flag = open("flag.txt", "w")


def readSerial():
    if os.path.exists("rocketdata.txt"):
        os.remove("rocketdata.txt")
    
    rocketdata = open("rocketdata.txt", "a")
    ser = serial.Serial(port="/dev/ttyGS0", baudrate=115200)

    while True:
        data = ser.read(158).decode()
        dataString = str(data)
        rocketdata.write(dataString)
        # file.write("\n")
        if "D" in dataString:
            print("microgravity environment")
        if "K" in dataString:
            print("rocket landed!")
            break
        # time.sleep(0.07)
    print("break!")

    rocketdata.close()


readSerial()
parseData("rocketdata.txt")
flag.write("1")
flag.close()
