"""
Lane Priority Engine
--------------------
Calculate lane priority using
vehicle count and waiting time.
"""

from dataclasses import dataclass


@dataclass
class LanePriority:

    lane: str
    vehicles: int
    waiting_time: int
    priority_score: float


class PriorityEngine:

    def __init__(self):

        self.vehicle_weight = 2.0
        self.wait_weight = 0.5

    def calculate_priority(
        self,
        lane_statistics,
        waiting_times
    ):

        priorities = []

        for lane in lane_statistics:

            waiting = waiting_times.get(
                lane.lane,
                0
            )

            score = (

                lane.vehicle_count
                * self.vehicle_weight

                +

                waiting
                * self.wait_weight

            )

            priorities.append(

                LanePriority(

                    lane=lane.lane,

                    vehicles=lane.vehicle_count,

                    waiting_time=waiting,

                    priority_score=score

                )

            )

        priorities.sort(

            key=lambda x: x.priority_score,

            reverse=True

        )

        return priorities