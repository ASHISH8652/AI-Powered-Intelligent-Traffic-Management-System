"""
Dynamic Traffic Signal Controller
"""

class SignalController:

    def __init__(self):

        self.green_time = 30
        self.current_signal = "North"
        self.emergency_mode = False

    def calculate_green_time(self, density):

        if density <= 20:
            self.green_time = 15

        elif density <= 40:
            self.green_time = 25

        elif density <= 60:
            self.green_time = 35

        elif density <= 80:
            self.green_time = 45

        else:
            self.green_time = 60

        return self.green_time

    def activate_emergency(self, lane):

        self.current_signal = lane
        self.green_time = 90
        self.emergency_mode = True

    def deactivate_emergency(self):

        self.emergency_mode = False

    def update_signal(self, lane):

        if not self.emergency_mode:
            self.current_signal = lane

    def get_signal(self):

        return self.current_signal

    def is_emergency(self):

        return self.emergency_mode