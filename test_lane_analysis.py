from traffic_ai.analytics import LaneAnalyzer

lane = LaneAnalyzer()

lane.update_lane("North")
lane.update_lane("North")
lane.update_lane("North")

lane.update_lane("East")
lane.update_lane("East")

lane.update_lane("West")

for info in lane.get_statistics():

    print("=" * 35)
    print("Lane :", info.lane)
    print("Vehicles :", info.vehicle_count)
    print("Density :", info.density)