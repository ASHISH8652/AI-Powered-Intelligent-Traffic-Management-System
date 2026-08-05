from traffic_ai.analytics import LaneAnalyzer
from traffic_ai.signal_control import AdaptiveSignalController

lane = LaneAnalyzer()

for _ in range(3):
    lane.update_lane("North")

for _ in range(12):
    lane.update_lane("South")

for _ in range(22):
    lane.update_lane("East")

for _ in range(38):
    lane.update_lane("West")

controller = AdaptiveSignalController()

decisions = controller.generate(
    lane.get_statistics()
)

print("=" * 60)

for decision in decisions:

    print(f"""
Lane        : {decision.lane}
Vehicles    : {decision.vehicles}
Priority    : {decision.priority}
Green Time  : {decision.green_time} sec
""")