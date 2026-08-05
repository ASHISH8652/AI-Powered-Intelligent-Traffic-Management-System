"""
Vehicle Counter
"""

import cv2


class VehicleCounter:

    def __init__(self, line_position=400):

        self.line_position = line_position

        self.counted_ids = set()

        self.total_count = 0

    def update(self, results):

        if not results:
            return

        boxes = results[0].boxes

        if boxes.id is None:
            return

        for box, track_id in zip(boxes.xyxy, boxes.id):

            x1, y1, x2, y2 = box.tolist()

            center_y = int((y1 + y2) / 2)

            track_id = int(track_id)

            if (
                center_y > self.line_position
                and track_id not in self.counted_ids
            ):

                self.counted_ids.add(track_id)

                self.total_count += 1

    def get_count(self):

        return self.total_count