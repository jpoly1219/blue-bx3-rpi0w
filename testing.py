import datetime
import time

x = 0

while x < 50:
    print(datetime.datetime.now())
    time.sleep(0.5)
    x += 1

raise Exception("nyehhh")
