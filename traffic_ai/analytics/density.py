"""
Traffic Density Estimation Module
---------------------------------

This module converts vehicle count into
traffic density levels.
"""

from dataclasses import dataclass


@dataclass
class DensityResult:
    """
    Stores traffic density information.
    """

    vehicle_count: int
    density: str
    road_status: str
    signal_time: int
    color: tuple


class TrafficDensity:

    """
    Estimate traffic density from vehicle count.
    """

    def __init__(self):

        self.low_limit = 5
        self.medium_limit = 15
        self.high_limit = 30

    def estimate(self, vehicle_count):

        """
        Estimate density level.
        """

        if vehicle_count <= self.low_limit:

            return DensityResult(
                vehicle_count=vehicle_count,
                density="LOW",
                road_status="Smooth",
                signal_time=25,
                color=(0, 255, 0)
            )

        elif vehicle_count <= self.medium_limit:

            return DensityResult(
                vehicle_count=vehicle_count,
                density="MEDIUM",
                road_status="Moderate",
                signal_time=40,
                color=(0, 255, 255)
            )

        elif vehicle_count <= self.high_limit:

            return DensityResult(
                vehicle_count=vehicle_count,
                density="HIGH",
                road_status="Congested",
                signal_time=60,
                color=(0, 165, 255)
            )

        else:

            return DensityResult(
                vehicle_count=vehicle_count,
                density="VERY HIGH",
                road_status="Heavy Traffic",
                signal_time=90,
                color=(0, 0, 255)
            )