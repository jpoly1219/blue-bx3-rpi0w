import serial


SERIAL_PORT = "/dev/ttyS0"
SERIAL_RATE = 115200


def readSerial():
    file = open("rocketdata.txt", "w")
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)

    while True:
        data = ser.readline().decode("utf-8")
        print(data)
        file.write(data)

    file.close()


readSerial()
