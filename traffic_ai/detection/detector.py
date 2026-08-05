"""
Vehicle Detection Engine
------------------------
Loads a YOLOv8 model and performs object detection.
"""

from ultralytics import YOLO

from traffic_ai.config import CONFIDENCE, YOLO_MODEL


class VehicleDetector:
    """
    Reusable YOLOv8 vehicle detector.
    """

    def __init__(self, model_path=YOLO_MODEL, confidence=CONFIDENCE):
        self.model = YOLO(model_path)
        self.confidence = confidence

    def detect(self, image):
        """
        Run object detection on an image.

        Parameters
        ----------
        image : str | numpy.ndarray
            Image path or OpenCV image.

        Returns
        -------
        list
            YOLO prediction results.
        """

        results = self.model.predict(
            source=image,
            conf=self.confidence,
            verbose=False
        )

        return results