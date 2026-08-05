"""
Queue Length Prediction
-----------------------
Estimate queue size after the
next signal cycle.
"""

from dataclasses import dataclass


@dataclass
class QueuePrediction:

    lane: str

    current_queue: int

    arriving: int

    departing: int

    predicted_queue: int


class QueuePredictor:

    def __init__(self):

        self.departure_rate = 10

    def predict(

        self,

        lane,

        current_queue,

        arrival_rate,

        green_time

    ):

        departing = int(

            self.departure_rate *

            (green_time / 30)

        )

        predicted = (

            current_queue +

            arrival_rate -

            departing

        )

        predicted = max(predicted, 0)

        return QueuePrediction(

            lane=lane,

            current_queue=current_queue,

            arriving=arrival_rate,

            departing=departing,

            predicted_queue=predicted

        )