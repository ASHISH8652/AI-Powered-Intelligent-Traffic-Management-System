from traffic_ai.analytics import LaneAnalyzer
from traffic_ai.signal_control import PriorityEngine

lane = LaneAnalyzer()

for _ in range(35):
    lane.update_lane("North")

for _ in range(12):
    lane.update_lane("South")

for _ in range(8):
    lane.update_lane("East")

for _ in range(4):
    lane.update_lane("West")

waiting = {

    "North": 15,

    "South": 90,

    "East": 30,

    "West": 10

}

engine = PriorityEngine()

priority = engine.calculate_priority(

    lane.get_statistics(),

    waiting

)

print("=" * 60)

for lane in priority:

    print(f"""
Lane      : {lane.lane}
Vehicles  : {lane.vehicles}
Waiting   : {lane.waiting_time} sec
Priority  : {lane.priority_score:.1f}
""")