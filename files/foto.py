import cv2
import time

# Kamera öffnen
cap = cv2.VideoCapture(0)

# Überprüfen, ob die Kamera geöffnet wurde
if not cap.isOpened():
    print("Kamera konnte nicht geöffnet werden.")
    exit()

# Kamera für 5 Sekunden anzeigen lassen (kannst du anpassen)
start_time = time.time()
while time.time() - start_time < 5:
    # Kamera-Feed anzeigen (optional)
    ret, frame = cap.read()
    if not ret:
        print("Fehler beim Aufnehmen des Kamerabildes.")
        break
    cv2.imshow("Kamera", frame)
    
    # Überprüfen, ob der Benutzer das Fenster schließt (Taste 'q' drücken)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Ein Bild aufnehmen nach 5 Sekunden
ret, frame = cap.read()
if ret:
    cv2.imwrite('bild.jpg', frame)
    print('Bild aufgenommen!')
else:
    print('Fehler beim Aufnehmen des Bildes.')

# Alle Fenster schließen und Kamera freigeben
cap.release()
cv2.destroyAllWindows()
