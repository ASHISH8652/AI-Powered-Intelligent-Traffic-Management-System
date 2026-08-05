from traffic_ai.optimization import (
    LanePriorityEngine,
    AdaptiveScheduler
)

priority = LanePriorityEngine()
scheduler = AdaptiveScheduler()

priority.update_lane("North", 18, 75, 22)
priority.update_lane("South", 12, 40, 38)
priority.update_lane("East", 20, 82, 15)
priority.update_lane("West", 10, 30, 45)

for cycle in range(5):

    lane = scheduler.choose_next_lane(
        priority.get_lane_statistics()
    )

    scheduler.update_waiting_time(lane)

    print("=" * 40)
    print("Cycle :", cycle + 1)
    print("Green Lane :", lane)
    print("Waiting Time :")
    print(scheduler.get_waiting_time())