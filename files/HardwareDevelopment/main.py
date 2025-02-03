import RPi.GPIO as GPIO
import time

# GPIO-Nummerierung nach Broadcom-Layout verwenden (BCM)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)

GPIO.output(27, GPIO.HIGH)

time.sleep(2)

GPIO.output(27, GPIO.LOW)

# Aufräumen, um die Pins wieder freizugeben
GPIO.cleanup()
