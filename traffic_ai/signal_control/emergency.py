"""
Emergency Vehicle Priority System
---------------------------------
Detect emergency vehicles and
generate signal override decisions.
"""

from dataclasses import dataclass


@dataclass
class EmergencyDecision:

    emergency_detected: bool

    vehicle_type: str

    lane: str

    action: str

    green_time: int


class EmergencyPriority:

    """
    Emergency vehicle controller.
    """

    def __init__(self):

        self.green_corridor_time = 90

        self.emergency_classes = [

            "ambulance",

            "fire truck",

            "police"

        ]

    def detect(self, detected_objects):

        """
        detected_objects

        Example

        [

            ("car","North"),

            ("bus","East"),

            ("ambulance","South")

        ]
        """

        for vehicle, lane in detected_objects:

            if vehicle.lower() in self.emergency_classes:

                return EmergencyDecision(

                    emergency_detected=True,

                    vehicle_type=vehicle,

                    lane=lane,

                    action="OVERRIDE SIGNAL",

                    green_time=self.green_corridor_time

                )

        return EmergencyDecision(

            emergency_detected=False,

            vehicle_type="",

            lane="",

            action="NORMAL OPERATION",

            green_time=0

        )