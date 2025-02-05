import json
from gpiozero import OutputDevice
from time import sleep

with open("drinkstime.json", "r") as file:
    config = json.load(file)

drinks = config["drinks"]


def run_drink(drink_name):
    drink = drinks[drink_name]
    pumps = drink["pumps"]

    if len(pumps) == 1:
        pump = OutputDevice(pumps[0]["pin"], active_high=True, initial_value=False)
        pump.on()
        print(f"Pumpe an Pin {pumps[0]['pin']} startet für {pumps[0]['duration']} Sekunden.")
        sleep(pumps[0]["duration"])
        pump.off()
        print(f"Pumpe an Pin {pumps[0]['pin']} stoppt.")
    elif len(pumps) == 2:
        pump1 = OutputDevice(pumps[0]["pin"], active_high=True, initial_value=False)
        pump2 = OutputDevice(pumps[1]["pin"], active_high=True, initial_value=False)

        pump1.on()
        print(f"Pumpe an Pin {pumps[0]['pin']} startet.")
        pump2.on()
        print(f"Pumpe an Pin {pumps[1]['pin']} startet.")

        sleep(pumps[0]["duration"])

        pump1.off()
        print(f"Pumpe an Pin {pumps[0]['pin']} stoppt.")
        pump2.off()
        print(f"Pumpe an Pin {pumps[1]['pin']} stoppt.")


