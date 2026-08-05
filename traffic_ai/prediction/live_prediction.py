"""
Live Prediction Engine
"""

from traffic_ai.integration import DataManager


class LivePrediction:

    def __init__(self, engine):

        self.engine = engine

    def predict(self):

        data = DataManager.get_data()

        features = {

            "vehicle_count": data["vehicle_count"],

            "density": data["density"],

            "lane_data": data["lane_data"],

            "fps": data["fps"]

        }

        prediction = self.engine.predict_live(
            features
        )

        DataManager.update_prediction(
            prediction
        )

        return prediction