"""
Detector Test
"""

from traffic_ai.detection.detector import VehicleDetector
import cv2


def test_detector():

    detector = VehicleDetector()

    image = cv2.imread(
        "assets/test.jpg"
    )

    results = detector.detect(image)

    print("Detection Successful")

    print(results)


if __name__ == "__main__":

    test_detector()