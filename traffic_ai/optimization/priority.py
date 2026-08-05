"""
Lane Priority Engine
--------------------
Calculates the priority score for each lane.
"""


class LanePriorityEngine:

    def __init__(self):

        self.lanes = {
            "North": {},
            "South": {},
            "East": {},
            "West": {}
        }

    def update_lane(
        self,
        lane,
        vehicle_count,
        density,
        average_speed
    ):

        speed_factor = max(0, 100 - average_speed)

        priority_score = (
            (0.50 * density)
            + (0.30 * vehicle_count)
            + (0.20 * speed_factor)
        )

        self.lanes[lane] = {
            "vehicle_count": vehicle_count,
            "density": density,
            "average_speed": average_speed,
            "priority_score": priority_score
        }

    def get_priority_lane(self):

        best_lane = None
        best_score = -1

        for lane, data in self.lanes.items():

            if not data:
                continue

            if data["priority_score"] > best_score:

                best_score = data["priority_score"]
                best_lane = lane

        return best_lane

    def get_lane_statistics(self):

        return self.lanes