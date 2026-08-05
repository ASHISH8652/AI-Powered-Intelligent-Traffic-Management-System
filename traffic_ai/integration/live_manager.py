"""
Live System Manager
Coordinates Detection, Analytics and Prediction.
"""

from traffic_ai.integration import DataManager
from traffic_ai.prediction.live_prediction import LivePrediction
from traffic_ai.prediction import PredictionEngine


class LiveManager:

    def __init__(self):

        self.engine = PredictionEngine()
        self.live_prediction = LivePrediction(self.engine)

    def update(self):

        data = DataManager.get_data()

        if data["vehicle_count"] == 0:
            return

        prediction = self.live_prediction.predict()

        DataManager.update_prediction(prediction)