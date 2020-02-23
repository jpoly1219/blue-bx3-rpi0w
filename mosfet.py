"""
mosfet.py is a module that provides two functions mosfetOn() and mosfetOff().
mosfetOn() checks for current flight state of the rocket. If flight state
D is reached, the function then sends a 3.3V logic level through a GPIO pin,
and maintains that logic level. mosfetOff() stops once flight state H is reached.
"""

# import RPi.GPIO as GPIO


# GPIO.setmode(GPIO.BOARD)
# GPIO.output(16, GPIO.OUT)

def mosfetOn():
    pass

def mosfetOff():
    pass
