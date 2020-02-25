"""
Pretty self-explanatory. redundancy.py checks if maincontrol.py is running.
If it is not running, then it will restart maincontrol.py.
"""

import os
import subprocess
import time

while True:
    p1 = subprocess.Popen(["ps", "-ef"], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["grep", "maincontrol.py"], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0]
    print(output)
    time.sleep(1)
