from gpiozero import OutputDevice
from time import sleep


relay1 = OutputDevice(23, active_high=True, initial_value=False)
relay2 = OutputDevice(24, active_high=True, initial_value=False)
relay1.on()
relay2.on()


def run(parameter):
    zeiteinzeln = 80 # 65
    zeitgesamt = 40 # 33

    if parameter == "Cola":
        relay1.off()
        print("Cola läuft")
        sleep(zeiteinzeln)
        relay1.on()
        print("Cola stoppt")
    elif parameter == "Fanta":
        relay2.off()
        print("Fanta läuft")
        sleep(zeiteinzeln)
        relay2.on()
        print("Fanta stoppt")
    elif parameter == "Spezi":
        relay1.off()
        relay2.off()
        print("Spezi läuft - Beide Relays an")
        sleep(zeitgesamt)
        relay1.on()
        relay2.on()
        print("Spezi stoppt - beide beendet")