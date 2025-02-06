import serial
import time

# Setze die serielle Verbindung mit 115200 Baud
ser = serial.Serial('/dev/serial0', 115200, timeout=1)

def send_command(command):
    """Sendet einen Befehl an den PN532 und gibt die Antwort zurück"""
    ser.write(command)
    time.sleep(0.1)  # Kleine Wartezeit für Antwort
    response = ser.read(64)  # Lese bis zu 64 Bytes der Antwort
    return response

# Testbefehl: "Get Firmware Version"
get_firmware = bytes([0x00, 0x00, 0xFF, 0x04, 0xFC, 0xD4, 0x02, 0x2A, 0x00])

print("📡 Sende GetFirmwareVersion-Befehl an den PN532...")

# Befehl senden und Antwort abrufen
response = send_command(get_firmware)

if response:
    print("✅ Antwort vom PN532 erhalten:", response.hex())
else:
    print("❌ Keine Antwort erhalten. Stelle sicher, dass das Gerät richtig verbunden ist.")

# Verbindung schließen
ser.close()
