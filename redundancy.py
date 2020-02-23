"""
Pretty self-explanatory. redundancy.py checks if maincontrol.py is running.
If it is not running, then it will restart maincontrol.py.
"""

import os
import subprocess
import time

while True:
    processRn = subprocess.run(["ps", "-ef", "|", "grep", "maincontrol.py"])
    print(processRn)
    time.sleep(1)
