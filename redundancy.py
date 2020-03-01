"""
Pretty self-explanatory. redundancy.py checks if maincontrol.py is running.
If it is not running, then it will restart maincontrol.py.
"""

import os
import subprocess
import time

while True:
    if os.path.exists("flag.txt"):
        flagData = open("flag.txt", "r")
        flagStr = flagData.read()
        if flagStr == "1":
            print("flagstr == 1")
            break
    else:
        pass

    # run 'ps -ef | grep [m]aincontrol.py'
    # reason why we use [m] is because of the way grep deals with regex.
    # if we use just 'm', grep will return its own process even when
    # maincontrol.py is not running, which can be misleading.
    p1 = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "'[m]aincontrol.py'"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]

    # decode bytestring
    outputD = output.decode()
    
    # run 'sudo python3 maincontrol.py' if not running
    if outputD == "":
        subprocess.run(["sudo", "python3", "/home/pi/Git Repositories/blue-bx3-rpi0w/maincontrol.py"])
    else:
        pass

    # give a delay so that the RPi0w wont explode :P
    time.sleep(1)
