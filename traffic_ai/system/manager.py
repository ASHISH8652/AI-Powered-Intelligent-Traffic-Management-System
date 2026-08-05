"""
Central AI System Manager
"""

from traffic_ai.detection.inference import TrafficInference
from traffic_ai.integration import DataManager
from traffic_ai.prediction.live_prediction import LivePrediction
from traffic_ai.prediction import PredictionEngine
from traffic_ai.utils.logger import system_logger


class AISystemManager:

    def __init__(self):

        self.detector = TrafficInference()

        self.prediction_engine = PredictionEngine()

        self.live_prediction = LivePrediction(
            self.prediction_engine
        )

        system_logger.info(
            "AI System Initialized"
        )

    def process_video(self, video_path, output_path):

        self.detector.detect_video(
            video_path,
            output_path
        )

    def process_image(self, image_path):

        return self.detector.detect_image(
            image_path
        )

    def predict(self):

        prediction = self.live_prediction.predict()

        DataManager.update_prediction(
            prediction
        )

        return prediction

    def get_live_data(self):

        return DataManager.get_data()