import cv2

from traffic_ai.tracking import (
    VehicleTracker,
    VehicleCounter,
    TrajectoryManager,
    SpeedEstimator
)

from traffic_ai.analytics import (
    TrafficDensity,
    TrafficStatistics,
    CongestionAnalyzer
)

from traffic_ai.detection.visualize import (
    draw_trajectories,
    draw_counting_line,
    draw_vehicle_count,
    draw_speed,
    draw_traffic_status
)

tracker = VehicleTracker()
trajectory = TrajectoryManager()
counter = VehicleCounter(400)

cap = cv2.VideoCapture("datasets/videos/traffic.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

speed = SpeedEstimator(fps=fps)

density = TrafficDensity()
stats = TrafficStatistics()
congestion = CongestionAnalyzer()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = tracker.track(frame)

    trajectory.update(results)

    counter.update(results)

    speed.update(results)

    density.update(frame, results)

    avg_speed = stats.average_speed(speed)

    congestion.update(
        density.density_percentage(),
        avg_speed
    )

    frame = results[0].plot()

    frame = draw_trajectories(
        frame,
        trajectory.get_tracks()
    )

    frame = draw_counting_line(frame,400)

    frame = draw_vehicle_count(
        frame,
        counter.get_count()
    )

    frame = draw_speed(
        frame,
        results,
        speed
    )

    frame = draw_traffic_status(
        frame,
        density.density_percentage(),
        avg_speed,
        congestion.get_status()
    )

    cv2.imshow(
        "Traffic Analytics",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()