import cv2

from traffic_ai.tracking import (
    VehicleTracker,
    TrajectoryManager,
    VehicleCounter
)

from traffic_ai.detection.visualize import (
    draw_trajectories,
    draw_counting_line,
    draw_vehicle_count
)

tracker = VehicleTracker()

trajectory = TrajectoryManager()

counter = VehicleCounter(line_position=400)

cap = cv2.VideoCapture("datasets/videos/traffic.mp4")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = tracker.track(frame)

    trajectory.update(results)

    counter.update(results)

    frame = results[0].plot()

    frame = draw_trajectories(
        frame,
        trajectory.get_tracks()
    )

    frame = draw_counting_line(
        frame,
        400
    )

    frame = draw_vehicle_count(
        frame,
        counter.get_count()
    )

    cv2.imshow(
        "Traffic Counter",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()