import serial
import time

# Serielle Verbindung öffnen
# Prüfe, ob dein Modul /dev/ttyS0 oder /dev/ttyAMA0 verwendet
ser = serial.Serial('/dev/ttyS0', baudrate=115200, timeout=1)


def wakeup():
    # Wake-up Sequence für PN532 (abhängig vom Modul)
    ser.write(b'\x55\x55\x00\x00\x00\x00')  # Testbefehl, je nach Modul
    time.sleep(0.5)


def send_command(command):
    preamble = b'\x00\x00\xFF'  # Preamble für PN532
    length = bytes([len(command)])
    lcs = bytes([~len(command) & 0xFF])  # Length Checksum
    data = command
    dcs = bytes([~sum(command) & 0xFF])  # Data Checksum
    postamble = b'\x00'

    frame = preamble + length + lcs + data + dcs + postamble
    ser.write(frame)


def read_response():
    response = ser.read(64)  # Lese bis zu 64 Bytes
    if response:
        print("Antwort:", response.hex())
    else:
        print("Keine Antwort vom PN532.")


def read_card():
    # Befehl zum Lesen einer NFC-Karte (InListPassiveTarget)
    command = b'\xD4\x4A\x01\x00'
    send_command(command)
    time.sleep(1)
    read_response()


if __name__ == "__main__":
    try:
        wakeup()
        print("Warte auf eine NFC-Karte...")
        while True:
            read_card()
            time.sleep(2)
    except KeyboardInterrupt:
        print("Programm beendet.")
    finally:
        ser.close()
