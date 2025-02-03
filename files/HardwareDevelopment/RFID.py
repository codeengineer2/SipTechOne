import time
import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# I2C-Schnittstelle initialisieren
i2c = busio.I2C(board.SCL, board.SDA)

# PN532 initialisieren
pn532 = PN532_I2C(i2c, debug=False)

# Firmware-Version auslesen
ic, ver, rev, support = pn532.firmware_version
print(f'Gefunden PN532 mit Firmware Version: {ver}.{rev}')

# NFC-Leser konfigurieren
pn532.SAM_configuration()

print('Warte auf eine NFC-Karte...')

while True:
    uid = pn532.read_passive_target(timeout=0.5)

    if uid is None:
        continue  # Kein Tag gefunden, weiter suchen

    # UID der Karte ausgeben
    print('Karte erkannt! UID:', ' '.join([hex(i) for i in uid]))
    time.sleep(1)
