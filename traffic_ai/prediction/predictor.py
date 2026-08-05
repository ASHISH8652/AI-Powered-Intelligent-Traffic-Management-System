"""
Traffic Volume Prediction Engine
--------------------------------
Loads the trained Random Forest model
and predicts traffic volume.
"""

import pandas as pd

from traffic_ai.prediction.model_loader import ModelLoader


class TrafficPredictor:

    def __init__(self):

        loader = ModelLoader()

        self.model = loader.load()

        self.feature_names = loader.get_features()

        self.features = self.feature_names

        self.metadata = loader.get_metadata()

    def predict(self, data):

        for feature in self.feature_names:

            if feature not in data:

                data[feature] = 0

        X = pd.DataFrame(
            [data]
        )[self.feature_names]

        prediction = self.model.predict(X)[0]

        return prediction
    
    