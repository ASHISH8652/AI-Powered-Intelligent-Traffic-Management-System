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

from traffic_ai.optimization import SignalController

from traffic_ai.detection.visualize import (
    draw_signal_information
)

tracker = VehicleTracker()

cap = cv2.VideoCapture("datasets/videos/traffic.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

speed = SpeedEstimator(fps=fps)

density = TrafficDensity()

stats = TrafficStatistics()

congestion = CongestionAnalyzer()

controller = SignalController()

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = tracker.track(frame)

    speed.update(results)

    density.update(frame, results)

    avg_speed = stats.average_speed(speed)

    congestion.update(
        density.density_percentage(),
        avg_speed
    )

    green = controller.calculate_green_time(
        density.density_percentage()
    )

    frame = results[0].plot()

    frame = draw_signal_information(
        frame,
        controller.get_signal(),
        green
    )

    cv2.imshow(
        "Dynamic Traffic Signal",
        frame
    )

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()