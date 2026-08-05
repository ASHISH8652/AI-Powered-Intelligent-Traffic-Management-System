from traffic_ai.tracking import VehicleTracker
import cv2

tracker = VehicleTracker()

cap = cv2.VideoCapture("datasets/videos/traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = tracker.track(frame)

    annotated = results[0].plot()

    cv2.imshow("Vehicle Tracking", annotated)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()