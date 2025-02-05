import cv2
import numpy as np
import time

def detect_blue():
    cap = cv2.VideoCapture(0)
    motion_end_time = None
    blue_detected = False
    
    ret, prev_frame = cap.read()
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        diff = cv2.absdiff(prev_gray, gray)
        motion_detected = np.sum(diff > 25) > 5000
        prev_gray = gray
        
        lower_blue = np.array([85, 50, 50])
        upper_blue = np.array([105, 255, 255])
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        blue_percentage = (np.sum(mask > 0) / (frame.shape[0] * frame.shape[1])) * 100
        
        cv2.putText(frame, f'Blau: {blue_percentage:.2f}%', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Frame', frame)
        cv2.imshow('Maske', mask)
        
        if blue_percentage >= 40:
            if not blue_detected:
                print("Erkannt!")
                blue_detected = True
            
            if motion_detected:
                motion_end_time = None
            else:
                if motion_end_time is None:
                    motion_end_time = time.time() + 3
                elif time.time() > motion_end_time:
                    print("Jetzt! (Mehr als 40% und keine Bewegung für 3 Sekunden)")
                    blue_detected = False
                    motion_end_time = None
        else:
            blue_detected = False
            motion_end_time = None
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

detect_blue()
