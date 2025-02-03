import RPi.GPIO as GPIO
import time

# GPIO-Nummerierung nach Broadcom-Layout verwenden (BCM)
GPIO.setmode(GPIO.BCM)

# Definiere den Pin 17 als Ausgang
GPIO.setup(17, GPIO.OUT)

# Schalte den Pin 17 auf HIGH
GPIO.output(17, GPIO.HIGH)

# Optional: Warte etwas, damit der HIGH-Zustand sichtbar ist
time.sleep(2)

# Setze den Pin wieder auf LOW (optional)
GPIO.output(17, GPIO.LOW)

# Aufräumen, um die Pins wieder freizugeben
GPIO.cleanup()
