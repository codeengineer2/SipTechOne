from gpiozero import OutputDevice
from time import sleep



relay1 = OutputDevice(23, active_high=True, initial_value=False)
relay2 = OutputDevice(24, active_high=True, initial_value=False)


relay1.on()
relay2.on()
print("relay1 IN1 on")
print("relay2 IN2 on")
sleep(5)
print("relay1 IN1 stoppt")
print("relay2 IN2 stoppt")
relay1.off()
relay2.off()