"""
Intelligent Signal Scheduler
----------------------------
Combines optimization, priority,
and emergency decisions into
one final signal decision.
"""

from dataclasses import dataclass


@dataclass
class ScheduleDecision:

    lane: str
    green_time: int
    reason: str


class SignalScheduler:

    def __init__(self):
        pass

    def schedule(
        self,
        optimized_signals,
        priority_list,
        emergency=None
    ):

        # Highest priority:
        # Emergency Vehicle

        if (
            emergency is not None
            and emergency.emergency_detected
        ):

            return ScheduleDecision(

                lane=emergency.lane,

                green_time=emergency.green_time,

                reason="Emergency Override"

            )

        # Otherwise

        highest = priority_list[0]

        green_time = 30

        for signal in optimized_signals:

            if signal.lane == highest.lane:

                green_time = signal.green_time
                break

        return ScheduleDecision(

            lane=highest.lane,

            green_time=green_time,

            reason="Highest Priority Lane"

        )