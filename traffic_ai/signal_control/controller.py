"""
Adaptive Signal Controller
--------------------------
Generate green signal timing based on lane traffic.
"""

from dataclasses import dataclass


@dataclass
class SignalDecision:

    lane: str
    vehicles: int
    green_time: int
    priority: int


class AdaptiveSignalController:

    def __init__(self):

        self.minimum_time = 15
        self.maximum_time = 90

    def calculate_green_time(self, vehicles):

        """
        Calculate signal duration.
        """

        if vehicles <= 5:

            return 15

        elif vehicles <= 15:

            return 30

        elif vehicles <= 30:

            return 60

        else:

            return 90

    def calculate_priority(self, vehicles):

        """
        Priority score (0–100).
        """

        return min(100, vehicles * 3)

    def generate(self, lane_statistics):

        decisions = []

        for lane in lane_statistics:

            decisions.append(

                SignalDecision(

                    lane=lane.lane,

                    vehicles=lane.vehicle_count,

                    green_time=self.calculate_green_time(
                        lane.vehicle_count
                    ),

                    priority=self.calculate_priority(
                        lane.vehicle_count
                    )

                )

            )

        return decisions