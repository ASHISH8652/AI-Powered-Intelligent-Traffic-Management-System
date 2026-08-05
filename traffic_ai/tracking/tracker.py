"""
Multi-Object Vehicle Tracker
Uses YOLOv8 Track Mode (ByteTrack)
"""

from ultralytics import YOLO


class VehicleTracker:
    """
    Vehicle tracking using YOLOv8 + ByteTrack.
    """

    def __init__(
        self,
        model_path="yolov8n.pt",
        confidence=0.30
    ):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def track(self, frame):
        """
        Track vehicles in a single frame.

        Returns
        -------
        list
            YOLO tracking results.
        """

        results = self.model.track(
            source=frame,
            persist=True,
            tracker="bytetrack.yaml",
            conf=self.confidence,
            verbose=False
        )

        return results