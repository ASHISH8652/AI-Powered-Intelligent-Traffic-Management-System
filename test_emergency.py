from traffic_ai.optimization import (
    SignalController,
    EmergencyVehicleManager,
    LanePriorityEngine
)

controller = SignalController()

priority = LanePriorityEngine()

emergency = EmergencyVehicleManager()

priority.update_lane(
    "North",
    14,
    65,
    28
)

priority.update_lane(
    "South",
    9,
    35,
    45
)

priority.update_lane(
    "East",
    22,
    82,
    18
)

priority.update_lane(
    "West",
    12,
    50,
    30
)

best_lane = priority.get_priority_lane()

controller.update_signal(best_lane)

print("Normal Signal")
print("-------------------")
print("Green Lane :", controller.get_signal())
print()

emergency.detect_emergency(
    "ambulance",
    "South"
)

emergency.process_emergency(
    controller
)

print("Emergency Mode")
print("-------------------")
print("Green Lane :", controller.get_signal())
print("Emergency :", controller.is_emergency())
print("Green Time :", controller.green_time)