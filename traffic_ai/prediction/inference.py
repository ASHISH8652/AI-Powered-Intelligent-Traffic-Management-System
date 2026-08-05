"""
Prediction Inference Pipeline
"""

from .predictor import TrafficPredictor
from .utils import congestion_level


class PredictionEngine:

    def __init__(self):

        self.predictor = TrafficPredictor()

    @property
    def metadata(self):

        return self.predictor.metadata

    def run(self, data):

        volume = self.predictor.predict(data)

        congestion = congestion_level(volume)

        return {

            "traffic_volume": int(volume),

            "congestion": congestion

        }