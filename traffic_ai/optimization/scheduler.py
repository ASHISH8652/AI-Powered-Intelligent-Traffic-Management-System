"""
Adaptive Traffic Signal Scheduler
---------------------------------
Schedules traffic signals using lane priority,
waiting time, and emergency overrides.
"""


class AdaptiveScheduler:

    def __init__(self):

        self.waiting_time = {
            "North": 0,
            "South": 0,
            "East": 0,
            "West": 0
        }

        self.current_lane = None

    def update_waiting_time(self, active_lane):

        for lane in self.waiting_time:

            if lane == active_lane:
                self.waiting_time[lane] = 0
            else:
                self.waiting_time[lane] += 1

    def choose_next_lane(self, lane_statistics):

        best_lane = None
        best_score = -1

        for lane, stats in lane_statistics.items():

            if not stats:
                continue

            score = (
                stats["priority_score"]
                +
                (self.waiting_time[lane] * 2)
            )

            if score > best_score:

                best_score = score
                best_lane = lane

        self.current_lane = best_lane

        return best_lane

    def get_waiting_time(self):

        return self.waiting_time