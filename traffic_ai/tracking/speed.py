"""
Vehicle Speed Estimator
"""

import math
from collections import defaultdict


class SpeedEstimator:

    def __init__(self, fps=30, pixels_per_meter=10):

        self.fps = fps
        self.pixels_per_meter = pixels_per_meter

        self.previous_positions = {}

        self.vehicle_speeds = defaultdict(float)

    def update(self, results):

        if not results:
            return

        boxes = results[0].boxes

        if boxes.id is None:
            return

        for box, track_id in zip(boxes.xyxy, boxes.id):

            x1, y1, x2, y2 = box.tolist()

            center = (
                int((x1 + x2) / 2),
                int((y1 + y2) / 2)
            )

            track_id = int(track_id)

            if track_id in self.previous_positions:

                previous = self.previous_positions[track_id]

                pixel_distance = math.dist(
                    previous,
                    center
                )

                meter_distance = (
                    pixel_distance /
                    self.pixels_per_meter
                )

                speed_mps = meter_distance * self.fps

                speed_kmph = speed_mps * 3.6

                self.vehicle_speeds[track_id] = speed_kmph

            self.previous_positions[track_id] = center

    def get_speed(self, track_id):

        return self.vehicle_speeds.get(track_id, 0)