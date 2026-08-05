# emergency.py

"""
Emergency Vehicle Priority Manager
----------------------------------
Handles emergency vehicle detection and traffic signal priority.
"""

from collections import deque


class EmergencyVehicleManager:
    """
    Manages emergency vehicle requests and
    determines signal priority.
    """

    def __init__(self):
        self.emergency_queue = deque()
        self.active_emergency = None

    def detect_emergency(self, vehicle_class, lane):
        """
        Register an emergency vehicle.

        Parameters
        ----------
        vehicle_class : str
            Type of emergency vehicle
            ('ambulance', 'fire_truck', 'police').

        lane : str
            Lane where the vehicle is detected
            ('North', 'South', 'East', 'West').
        """

        if vehicle_class in ["ambulance", "fire_truck", "police"]:

            request = {
                "vehicle": vehicle_class,
                "lane": lane
            }

            self.emergency_queue.append(request)

    def has_emergency(self):
        """
        Check if any emergency vehicle is waiting.
        """
        return len(self.emergency_queue) > 0

    def get_priority_lane(self):
        """
        Return the lane that should immediately
        receive the green signal.
        """

        if not self.has_emergency():
            return None

        self.active_emergency = self.emergency_queue.popleft()

        return self.active_emergency["lane"]

    def clear_priority(self):
        """
        Clear the currently active emergency.
        """
        self.active_emergency = None

    def get_active_emergency(self):
        """
        Return the currently active emergency vehicle.
        """

        return self.active_emergency
    def process_emergency(self, controller):
        """
        Activate emergency mode in the signal controller.
        """
        if self.has_emergency():
            lane = self.get_priority_lane()
            controller.activate_emergency(lane)