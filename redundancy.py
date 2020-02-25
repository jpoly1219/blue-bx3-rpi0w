"""
Pretty self-explanatory. redundancy.py checks if maincontrol.py is running.
If it is not running, then it will restart maincontrol.py.
"""

import os
import subprocess
import time

while True:
    p1 = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "[m]aincontrol.py"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    outputD = output.decode()
    
    if outputD == "":
        subprocess.run(["sudo", "python3", "testing.py"])
    else:
        pass

    time.sleep(1)
