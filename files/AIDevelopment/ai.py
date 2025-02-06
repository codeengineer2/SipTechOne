import cv2
import numpy as np
import time

def detect_blue():
    cap = cv2.VideoCapture(0)
    timer_start = None
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
        
        lower_blue = np.array([35, 50, 50])
        upper_blue = np.array([100, 255, 255])
        
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        blue_percentage = (np.sum(mask > 0) / (frame.shape[0] * frame.shape[1])) * 100
        cv2.putText(frame, f'Blau: {blue_percentage:.2f}%', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        #cv2.imshow('Frame', frame)
        #cv2.imshow('Maske', mask)
        
        if blue_percentage >= 40:
            if motion_detected:
                timer_start = None
            else:
                if timer_start is None:
                    timer_start = time.time()
                elif time.time() - timer_start >= 3:
                    print("end")
                    return 1
                    timer_start = None
        else:
            timer_start = None
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()
