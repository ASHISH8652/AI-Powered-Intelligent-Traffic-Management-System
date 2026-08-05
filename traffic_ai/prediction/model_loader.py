"""
Model Loader
"""

import joblib
import json
import os

from traffic_ai.config import MODEL_FILE


class ModelLoader:

    def __init__(self):

        self.model = None

        self.features = None

        self.metadata = None

    def load(self):

        self.model = joblib.load(MODEL_FILE)

        self.features = joblib.load(
            "models/feature_columns.pkl"
        )

        with open(
            "models/metadata.json"
        ) as f:

            self.metadata = json.load(f)

        return self.model

    def get_features(self):

        return self.features

    def get_metadata(self):

        return self.metadata