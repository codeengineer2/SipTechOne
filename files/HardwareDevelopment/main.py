import RPi.GPIO as GPIO
import time

# GPIO-Nummerierung nach Broadcom-Layout verwenden (BCM)
GPIO.setmode(GPIO.BCM)

# Definiere den Pin 18 als Ausgang
pin11 = GPIO.setup(17, GPIO.OUT)

pin11.output(GPIO.HIGH)
