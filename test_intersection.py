import cv2

from traffic_ai.optimization import (
    LanePriorityEngine,
    AdaptiveScheduler,
    SignalController
)

from traffic_ai.simulation import (
    SmartIntersection,
    draw_intersection_dashboard
)

priority = LanePriorityEngine()

scheduler = AdaptiveScheduler()

controller = SignalController()

intersection = SmartIntersection()

priority.update_lane("North",18,72,28)
priority.update_lane("South",9,30,48)
priority.update_lane("East",22,85,17)
priority.update_lane("West",11,42,39)

lane = scheduler.choose_next_lane(
    priority.get_lane_statistics()
)

controller.update_signal(lane)

intersection.update_signal(
    controller.get_signal()
)

image = 255 * \
    __import__("numpy").ones(
        (700,1400,3),
        dtype="uint8"
    )

image = draw_intersection_dashboard(
    image,
    intersection.get_signal_state()
)

cv2.imshow(
    "Smart Intersection",
    image
)

cv2.waitKey(0)

cv2.destroyAllWindows()