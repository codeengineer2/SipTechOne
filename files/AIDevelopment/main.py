import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

cap = cv2.VideoCapture(0)

finger_connections = [
    # Daumen: 1->2, 2->3, 3->4
    (1, 2), (2, 3), (3, 4),
    # Zeigefinger: 5->6, 6->7, 7->8
    (5, 6), (6, 7), (7, 8),
    # Mittelfinger: 9->10, 10->11, 11->12
    (9, 10), (10, 11), (11, 12),
    # Ringfinger: 13->14, 14->15, 15->16
    (13, 14), (14, 15), (15, 16),
    # Kleiner Finger: 17->18, 18->19, 19->20
    (17, 18), (18, 19), (19, 20)
]

finger_landmark_indices = set()
for connection in finger_connections:
    finger_landmark_indices.update(connection)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            h, w, _ = frame.shape
            
            for connection in finger_connections:
                start = hand_landmarks.landmark[connection[0]]
                end = hand_landmarks.landmark[connection[1]]
                start_point = (int(start.x * w), int(start.y * h))
                end_point = (int(end.x * w), int(end.y * h))
                cv2.line(frame, start_point, end_point, (0, 255, 0), 2)
            
            for idx in finger_landmark_indices:
                lm = hand_landmarks.landmark[idx]
                center = (int(lm.x * w), int(lm.y * h))
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
    
    cv2.imshow("Finger Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()