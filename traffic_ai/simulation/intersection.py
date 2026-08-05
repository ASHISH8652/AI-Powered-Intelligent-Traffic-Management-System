"""
Four-Way Smart Intersection
---------------------------
Coordinates traffic flow across four lanes.
"""


class SmartIntersection:

    def __init__(self):

        self.lanes = [
            "North",
            "South",
            "East",
            "West"
        ]

        self.signal_state = {

            "North": "RED",
            "South": "RED",
            "East": "RED",
            "West": "RED"

        }

    def update_signal(self, green_lane):

        for lane in self.signal_state:

            self.signal_state[lane] = "RED"

        self.signal_state[green_lane] = "GREEN"

    def get_signal_state(self):

        return self.signal_state