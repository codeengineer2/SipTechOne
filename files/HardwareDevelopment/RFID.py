import time
import board
import busio
from adafruit_pn532.uart import PN532_UART

# Initialisierung der UART-Schnittstelle
uart = busio.UART(board.TX, board.RX, baudrate=115200, timeout=1)

# PN532 über UART initialisieren
nfc = PN532_UART(uart, debug=False)

# Firmware-Version auslesen
ic, ver, rev, support = nfc.firmware_version
print(f'Gefunden PN532 mit Firmware Version: {ver}.{rev}')

# NFC-Reader konfigurieren
nfc.SAM_configuration()

print('Warte auf eine NFC-Karte...')

while True:
    uid = nfc.read_passive_target(timeout=0.5)

    if uid is None:
        continue  # Kein Tag erkannt, weitersuchen

    # UID der Karte anzeigen
    print('Karte erkannt! UID:', ' '.join([hex(i) for i in uid]))
    time.sleep(1)
