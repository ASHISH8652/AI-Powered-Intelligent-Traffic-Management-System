"""
Traffic Congestion Prediction
-----------------------------
Predict traffic congestion level
using current vehicle statistics.
"""

from dataclasses import dataclass


@dataclass
class CongestionPrediction:

    vehicle_count: int
    predicted_count: int
    congestion_level: str
    confidence: float


class CongestionPredictor:

    def __init__(self):

        self.growth_factor = 1.20

    def predict(self, vehicle_count):

        predicted = int(
            vehicle_count *
            self.growth_factor
        )

        if predicted < 20:

            level = "LOW"

        elif predicted < 40:

            level = "MEDIUM"

        elif predicted < 60:

            level = "HIGH"

        else:

            level = "VERY HIGH"

        confidence = 0.85

        return CongestionPrediction(

            vehicle_count=vehicle_count,

            predicted_count=predicted,

            congestion_level=level,

            confidence=confidence

        )