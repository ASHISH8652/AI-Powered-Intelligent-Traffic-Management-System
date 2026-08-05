"""
Dynamic Signal Optimizer
------------------------
Calculate adaptive green signal durations.
"""

from dataclasses import dataclass


@dataclass
class OptimizedSignal:

    lane: str
    vehicles: int
    green_time: int


class SignalOptimizer:

    def __init__(
        self,
        minimum_green=15,
        maximum_green=90,
        weight=2
    ):

        self.minimum_green = minimum_green
        self.maximum_green = maximum_green
        self.weight = weight

    def optimize(self, lane_statistics):

        optimized = []

        for lane in lane_statistics:

            green = self.minimum_green + (
                lane.vehicle_count * self.weight
            )

            green = max(
                self.minimum_green,
                min(green, self.maximum_green)
            )

            optimized.append(

                OptimizedSignal(

                    lane=lane.lane,

                    vehicles=lane.vehicle_count,

                    green_time=green

                )

            )

        return optimized