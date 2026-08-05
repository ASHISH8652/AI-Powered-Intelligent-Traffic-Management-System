from traffic_ai.analytics import TrafficDensity

density = TrafficDensity()

tests = [2, 8, 18, 35]

for vehicles in tests:

    result = density.estimate(vehicles)

    print("-" * 40)
    print(f"Vehicles     : {result.vehicle_count}")
    print(f"Density      : {result.density}")
    print(f"Road Status  : {result.road_status}")
    print(f"Signal Time  : {result.signal_time} sec")