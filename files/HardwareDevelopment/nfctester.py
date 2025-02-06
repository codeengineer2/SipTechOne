import nfc

clf = nfc.ContactlessFrontend('/dev/serial0')

if clf:
    print("PN532 erkannt!")
    clf.close()
else:
    print("Fehler beim Erkennen des PN532")
