from traffic_ai.analytics import LaneAnalyzer

from traffic_ai.signal_control import (
    SignalOptimizer,
    PriorityEngine,
    EmergencyPriority,
    SignalScheduler
)

lane = LaneAnalyzer()

for _ in range(20):
    lane.update_lane("North")

for _ in range(12):
    lane.update_lane("South")

for _ in range(8):
    lane.update_lane("East")

for _ in range(35):
    lane.update_lane("West")

waiting = {

    "North":20,

    "South":40,

    "East":10,

    "West":5

}

optimizer = SignalOptimizer()

optimized = optimizer.optimize(
    lane.get_statistics()
)

priority = PriorityEngine()

priority_list = priority.calculate_priority(

    lane.get_statistics(),

    waiting

)

emergency = EmergencyPriority()

decision = emergency.detect(

    [

        ("car","North"),

        ("truck","East")

    ]

)

scheduler = SignalScheduler()

final = scheduler.schedule(

    optimized,

    priority_list,

    decision

)

print("="*60)

print("Lane :", final.lane)

print("Green Time :", final.green_time)

print("Reason :", final.reason)