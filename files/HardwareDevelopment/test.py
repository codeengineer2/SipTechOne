from gpiozero import OutputDevice
from time import sleep


relay1 = OutputDevice(23, active_high=True, initial_value=False)
relay2 = OutputDevice(24, active_high=True, initial_value=False)




def run(parameter):
    zeiteinzeln = 67
    zeitgesamt = 33

    if parameter == "Cola":
        relay1.on()
        print("Cola läuft")
        sleep(zeiteinzeln)
        relay1.off()
        print("Cola stoppt")
    elif parameter == "Fanta":
        relay2.on()
        print("Fanta läuft")
        sleep(zeiteinzeln)
        relay2.off()
        print("Fanta stoppt")
    elif parameter == "Spezi":
        relay1.on()
        relay2.on()
        print("Mezzo läuft - Beide Relays an")
        sleep(zeitgesamt)
        relay1.off()
        relay2.off()
        print("Mezzo stoppt - beide beendet")

