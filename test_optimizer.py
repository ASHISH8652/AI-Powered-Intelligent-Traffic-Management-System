from traffic_ai.analytics import LaneAnalyzer
from traffic_ai.signal_control import SignalOptimizer

lane = LaneAnalyzer()

for _ in range(6):
    lane.update_lane("North")

for _ in range(18):
    lane.update_lane("South")

for _ in range(28):
    lane.update_lane("East")

for _ in range(40):
    lane.update_lane("West")

optimizer = SignalOptimizer()

signals = optimizer.optimize(
    lane.get_statistics()
)

print("=" * 60)

for signal in signals:

    print(
        f"{signal.lane:6}"
        f" | Vehicles: {signal.vehicles:2}"
        f" | Green: {signal.green_time} sec"
    )