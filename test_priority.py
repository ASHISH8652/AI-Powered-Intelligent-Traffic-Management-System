from traffic_ai.optimization import LanePriorityEngine

priority = LanePriorityEngine()

priority.update_lane(
    lane="North",
    vehicle_count=18,
    density=72,
    average_speed=24
)

priority.update_lane(
    lane="South",
    vehicle_count=10,
    density=38,
    average_speed=42
)

priority.update_lane(
    lane="East",
    vehicle_count=24,
    density=85,
    average_speed=15
)

priority.update_lane(
    lane="West",
    vehicle_count=8,
    density=25,
    average_speed=48
)

best_lane = priority.get_priority_lane()

print("Priority Lane :", best_lane)
print()

for lane, data in priority.get_lane_statistics().items():
    print(lane)
    print(data)
    print("-" * 40)