"""
Lane-wise Traffic Analytics
---------------------------
Assign vehicles to lanes and compute statistics.
"""

from dataclasses import dataclass


@dataclass
class LaneStatistics:

    lane: str
    vehicle_count: int
    density: str


class LaneAnalyzer:

    def __init__(self):

        self.lanes = {

            "North": 0,
            "South": 0,
            "East": 0,
            "West": 0

        }

    def reset(self):

        for lane in self.lanes:

            self.lanes[lane] = 0

    def update_lane(self, lane_name):

        if lane_name in self.lanes:

            self.lanes[lane_name] += 1

    def get_statistics(self):

        statistics = []

        for lane, count in self.lanes.items():

            if count <= 5:

                density = "LOW"

            elif count <= 15:

                density = "MEDIUM"

            elif count <= 30:

                density = "HIGH"

            else:

                density = "VERY HIGH"

            statistics.append(

                LaneStatistics(

                    lane=lane,
                    vehicle_count=count,
                    density=density

                )

            )

        return statistics