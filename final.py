# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led = 12  # GPIO number where the led is connected

# Tell the GPIO module to use GPIO numbering used by processor
GPIO.setmode(GPIO.BCM)

# Set GPIO no 12 to output mode
GPIO.setup(led, GPIO.OUT)

# Blink some leds
while True:
    GPIO.output(led, False)
    sleep(1)  # Sleep for 1 second
    GPIO.output(led, True)
    sleep(1)
