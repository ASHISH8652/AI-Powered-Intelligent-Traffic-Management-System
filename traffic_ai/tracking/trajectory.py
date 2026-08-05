"""
Vehicle Trajectory Manager
"""

import cv2
from collections import defaultdict


class TrajectoryManager:

    def __init__(self, max_points=50):
        """
        Store the movement history of tracked vehicles.
        """
        self.tracks = defaultdict(list)
        self.max_points = max_points

    def update(self, results):
        """
        Update trajectories using tracking results.
        """

        if not results:
            return

        boxes = results[0].boxes

        if boxes.id is None:
            return

        for box, track_id in zip(boxes.xyxy, boxes.id):

            x1, y1, x2, y2 = box.tolist()

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            track_id = int(track_id)

            self.tracks[track_id].append(
                (center_x, center_y)
            )

            if len(self.tracks[track_id]) > self.max_points:
                self.tracks[track_id].pop(0)

    def get_tracks(self):
        return self.tracks