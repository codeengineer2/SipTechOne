import RPi.GPIO as GPIO
import time

# GPIO-Nummerierung nach Broadcom-Layout verwenden (BCM)
GPIO.setmode(GPIO.BCM)

GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)



GPIO.output(27, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
time.sleep(10)
GPIO.output(22, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
time.sleep(10)
# Aufräumen, um die Pins wieder freizugeben
GPIO.cleanup()
