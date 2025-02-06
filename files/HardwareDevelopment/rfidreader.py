import time
import board
import busio
import binascii
from adafruit_pn532.i2c import PN532_I2C

# I2C-Schnittstelle initialisieren
i2c = busio.I2C(board.SCL, board.SDA)

# PN532 per I2C ansprechen
# Adresse 0x24 ist Standard, wenn dein PN532-Modul etwas anderes vorgibt,
# kannst du hier mit "address=0xXX" anpassen.
pn532 = PN532_I2C(i2c, debug=False)

# Versions-Info auslesen
ic, ver, rev, support = pn532.firmware_version
print("PN532 gefunden! Firmware-Version: {}.{}".format(ver, rev))

# PN532 konfigurieren (SAM = Security Access Module)
pn532.SAM_configuration()

print("Warte auf ein NFC-Tag... (Drücke STRG+C zum Beenden)")

while True:
    # Auf ein passives NFC-Tag warten (timeout in Sekunden)
    uid = pn532.read_passive_target(timeout=0.5)
    if uid is not None:
        # UID ausgeben
        print("NFC-Tag erkannt! UID = {}".format(binascii.hexlify(uid).upper()))
        time.sleep(1)
    time.sleep(0.1)
