from traffic_ai.ml import TrafficDatasetBuilder

builder = TrafficDatasetBuilder()

builder.append(

    vehicle_count=35,

    lane_counts=[8, 9, 10, 8],

    density="MEDIUM",

    arrival_rate=4.5,

    queue_length=20,

    signal_time=35,

    congestion="MEDIUM"

)

print("Traffic record added successfully.")