from gpiozero import OutputDevice
from time import sleep


relay1 = OutputDevice(23, active_high=True, initial_value=False)
relay2 = OutputDevice(24, active_high=True, initial_value=False)
relay1.off()
relay2.off()