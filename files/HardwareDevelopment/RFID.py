import serial
import time

# Öffne den UART-Port (prüfe, ob /dev/serial0, /dev/ttyS0 oder /dev/ttyAMA0 verwendet wird)
ser = serial.Serial('/dev/serial0', baudrate=115200, timeout=1)


# Senden von Daten über UART
def send_data(data):
    ser.write(data.encode('utf-8'))
    print(f"Gesendet: {data}")


# Empfangen von Daten über UART
def receive_data():
    if ser.in_waiting > 0:  # Prüfen, ob Daten im Puffer sind
        incoming_data = ser.read(ser.in_waiting).decode('utf-8', errors='ignore')
        print(f"Empfangen: {incoming_data}")


try:
    while True:
        # Sende eine Nachricht alle 5 Sekunden
        send_data("Hallo PN532!\n")
        time.sleep(1)

        # Empfange und zeige eingehende Daten
        receive_data()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgramm beendet.")
finally:
    ser.close()
