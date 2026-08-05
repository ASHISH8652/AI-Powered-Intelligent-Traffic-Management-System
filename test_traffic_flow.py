from traffic_ai.analytics import TrafficFlowAnalyzer

flow = TrafficFlowAnalyzer(frame_width=1280)

boxes = [

    (40, 60, 160, 200),

    (340, 90, 470, 220),

    (720, 110, 830, 250),

    (1100, 150, 1220, 290)

]

for box in boxes:

    center_x, center_y = flow.get_center(box)

    lane = flow.get_lane(center_x)

    print("=" * 40)

    print("Box :", box)

    print("Center :", (center_x, center_y))

    print("Assigned Lane :", lane)