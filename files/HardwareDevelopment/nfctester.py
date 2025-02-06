import serial

# Öffne die serielle Verbindung mit 115200 Baud
ser = serial.Serial('/dev/ttyS0', 115200, timeout=1)

# Sende einen Befehl an den PN532 (GetFirmwareVersion)
get_firmware = bytes([0x00, 0x00, 0xFF, 0x04, 0xFC, 0xD4, 0x02, 0x2A, 0x00])
ser.write(get_firmware)

# Lese Antwort
response = ser.read(16)
print("Antwort vom PN532:", response.hex())

# Schließe Verbindung
ser.close()
