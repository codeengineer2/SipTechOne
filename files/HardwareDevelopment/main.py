from gpiozero import OutputDevice
from time import sleep

# Definiere den Pin, der mit IN1 des Relais verbunden ist
# BCM-Pin-Nummerierung: Pin 22 entspricht GPIO 22
def run(parameter):
    relay = OutputDevice(22, active_high=True, initial_value=False)
    if parameter == "Cola":
        print("Cola run")
    while True:
        # Pumpe einschalten
        relay.on()  # Relais schließt, Pumpe läuft
        print("Pumpe AN")
        sleep(5)    # 5 Sekunden warten

        # Pumpe ausschalten
        relay.off()  # Relais öffnet, Pumpe aus
        print("Pumpe AUS")
        sleep(5)    # 5 Sekunden warten
