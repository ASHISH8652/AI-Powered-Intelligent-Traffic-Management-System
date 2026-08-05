"""
Traffic Data Manager
"""

from .state import AppState


class DataManager:

    @staticmethod
    def update_vehicle_count(count):
        AppState.vehicle_count = count

    @staticmethod
    def update_density(density):
        AppState.density = density

    @staticmethod
    def update_prediction(prediction):
        AppState.prediction = prediction

    @staticmethod
    def update_congestion(level):
        AppState.congestion = level

    @staticmethod
    def update_lane_data(data):
        AppState.lane_data = data

    @staticmethod
    def update_fps(fps):
        AppState.fps = fps

    @staticmethod
    def update_recommendation(text):
        AppState.recommendation = text

    @staticmethod
    def get_prediction():
        return AppState.prediction

    @staticmethod
    def get_data():

        return {

            "vehicle_count": AppState.vehicle_count,

            "density": AppState.density,

            "prediction": AppState.prediction,

            "congestion": AppState.congestion,

            "lane_data": AppState.lane_data,

            "fps": AppState.fps,

            "recommendation": AppState.recommendation

        }