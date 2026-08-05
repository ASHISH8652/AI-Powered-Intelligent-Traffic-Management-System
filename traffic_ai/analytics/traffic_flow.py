"""
Traffic Flow Analysis
---------------------
Automatically assigns detected vehicles
to traffic lanes based on position.
"""


class TrafficFlowAnalyzer:

    def __init__(self, frame_width):

        self.frame_width = frame_width

        self.boundaries = [

            frame_width * 0.25,
            frame_width * 0.50,
            frame_width * 0.75

        ]

    def get_lane(self, center_x):

        if center_x < self.boundaries[0]:

            return "North"

        elif center_x < self.boundaries[1]:

            return "West"

        elif center_x < self.boundaries[2]:

            return "East"

        else:

            return "South"

    def get_center(self, box):

        x1, y1, x2, y2 = box

        center_x = int((x1 + x2) / 2)

        center_y = int((y1 + y2) / 2)

        return center_x, center_y