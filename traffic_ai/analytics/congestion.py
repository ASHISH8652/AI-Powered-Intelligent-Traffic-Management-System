"""
Congestion Level Analyzer
"""


class CongestionAnalyzer:

    def __init__(self):

        self.status = "Low"

    def update(self, density, average_speed):

        if density > 80 or average_speed < 10:

            self.status = "High"

        elif density > 50 or average_speed < 25:

            self.status = "Medium"

        else:

            self.status = "Low"

    def get_status(self):

        return self.status