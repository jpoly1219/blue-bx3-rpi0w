import serial
import time
from parsedata import parseData


def readSerial():
    file = open("rocketdata.txt", "w")
    ser = serial.Serial(port="/dev/ttyS0", baudrate=115200)

    while True:
        data = ser.read(158).decode()
        dataString = str(data)
        file.write(dataString)
        # file.write("\n")
        if "D" in dataString:
            print("microgravity environment")
        if "J" in dataString:
            print("rocket landed!")
            break
        # time.sleep(0.07)
    print("break!")

    file.close()


readSerial()
parseData()
