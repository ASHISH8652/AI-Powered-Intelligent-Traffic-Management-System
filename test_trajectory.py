import cv2

from traffic_ai.tracking import (
    VehicleTracker,
    TrajectoryManager
)

from traffic_ai.detection.visualize import draw_trajectories

tracker = VehicleTracker()
trajectory = TrajectoryManager()

cap = cv2.VideoCapture("datasets/videos/traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = tracker.track(frame)

    trajectory.update(results)

    annotated = results[0].plot()

    annotated = draw_trajectories(
        annotated,
        trajectory.get_tracks()
    )

    cv2.imshow("Vehicle Trajectories", annotated)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()