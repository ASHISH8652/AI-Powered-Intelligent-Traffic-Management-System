"""
=========================================================
Central AI System Manager
AI-Powered Intelligent Traffic Management System
=========================================================
"""

from traffic_ai.detection.inference import TrafficInference
from traffic_ai.integration import DataManager
from traffic_ai.prediction.live_prediction import LivePrediction
from traffic_ai.prediction import PredictionEngine
from traffic_ai.utils.logger import system_logger


class AISystemManager:

    def __init__(self):

        system_logger.info("Initializing AI System...")

        # ==================================================
        # AI Modules
        # ==================================================

        self.detector = TrafficInference()

        self.prediction_engine = PredictionEngine()

        self.live_prediction = LivePrediction(
            self.prediction_engine
        )

        # ==================================================
        # Shared Session Data
        # ==================================================

        self.uploaded_file = None

        self.detections = None

        self.analytics = None

        self.prediction = None

        self.monitoring = None

        self.report = None

        system_logger.info("AI System Ready")

    # ======================================================
    # Upload
    # ======================================================

    def set_uploaded_file(self, file):

        self.uploaded_file = file

    # ======================================================
    # Image Detection
    # ======================================================

    def process_image(self, image_path):

        self.detections = self.detector.detect_image(
            image_path
        )

        return self.detections

    # ======================================================
    # Video Detection
    # ======================================================

    def process_video(self, video_path, output_path):

        self.detector.detect_video(
            video_path,
            output_path
        )

        self.detections = output_path

        return output_path

    # ======================================================
    # Analytics
    # ======================================================

    def generate_analytics(self):

        if self.detections is None:

            return None

        self.analytics = DataManager.get_data()

        return self.analytics

    # ======================================================
    # Prediction
    # ======================================================

    def predict(self):

        self.prediction = self.live_prediction.predict()

        DataManager.update_prediction(
            self.prediction
        )

        return self.prediction

    # ======================================================
    # Monitoring
    # ======================================================

    def monitor(self):

        self.monitoring = DataManager.get_data()

        return self.monitoring

    # ======================================================
    # Complete Pipeline
    # ======================================================

    def run_pipeline(self):

        self.generate_analytics()

        self.predict()

        self.monitor()

        self.report = {

            "detections": self.detections,

            "analytics": self.analytics,

            "prediction": self.prediction,

            "monitoring": self.monitoring,

        }

        return self.report

    # ======================================================
    # Live Data
    # ======================================================

    def get_live_data(self):

        return DataManager.get_data()

    # ======================================================
    # Reset
    # ======================================================

    def reset(self):

        self.uploaded_file = None

        self.detections = None

        self.analytics = None

        self.prediction = None

        self.monitoring = None

        self.report = None

        system_logger.info("Session Reset")