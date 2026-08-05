"""
AI Signal Forecasting
---------------------
Predict optimal traffic signal timing
using traffic analytics.
"""

from dataclasses import dataclass


@dataclass
class SignalForecast:

    lane: str

    vehicle_count: int

    congestion: str

    predicted_queue: int

    green_time: int

    confidence: float


class SignalForecaster:

    def forecast(

        self,

        lane,

        vehicle_count,

        congestion,

        predicted_queue

    ):

        green_time = 30

        if congestion == "LOW":

            green_time = 20

        elif congestion == "MEDIUM":

            green_time = 30

        elif congestion == "HIGH":

            green_time = 45

        elif congestion == "VERY HIGH":

            green_time = 60

        if predicted_queue > 30:

            green_time += 10

        elif predicted_queue > 20:

            green_time += 5

        green_time = min(green_time, 90)

        confidence = 0.90

        return SignalForecast(

            lane=lane,

            vehicle_count=vehicle_count,

            congestion=congestion,

            predicted_queue=predicted_queue,

            green_time=green_time,

            confidence=confidence

        )