"""
Vehicle Arrival Rate Prediction
-------------------------------
Estimate future vehicle arrivals
using historical observations.
"""

from dataclasses import dataclass


@dataclass
class ArrivalPrediction:

    history: list

    average_arrival_rate: float

    predicted_next_count: int


class ArrivalRatePredictor:

    def __init__(self):

        self.history = []

        self.window_size = 10

    def update(self, vehicle_count):

        self.history.append(vehicle_count)

        if len(self.history) > self.window_size:

            self.history.pop(0)

    def predict(self):

        if len(self.history) < 2:

            return ArrivalPrediction(

                history=self.history,

                average_arrival_rate=0,

                predicted_next_count=0

            )

        differences = []

        for i in range(1, len(self.history)):

            differences.append(

                self.history[i] -

                self.history[i - 1]

            )

        average_rate = sum(differences) / len(differences)

        prediction = int(

            self.history[-1] +

            average_rate

        )

        return ArrivalPrediction(

            history=self.history.copy(),

            average_arrival_rate=round(average_rate, 2),

            predicted_next_count=prediction

        )