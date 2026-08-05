"""
Traffic Statistics
"""


class TrafficStatistics:

    def average_speed(self, speed_estimator):

        speeds = list(speed_estimator.vehicle_speeds.values())

        if len(speeds) == 0:

            return 0

        return sum(speeds) / len(speeds)