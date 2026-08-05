"""
Complete AI Pipeline Controller
"""

from traffic_ai.integration import DataManager
from traffic_ai.utils.logger import system_logger

class PipelineController:
    _running = True

    def __init__(self):
        pass

    def start(self):
        PipelineController._running = True
        system_logger.info(
            "Pipeline Started"
        )

    def stop(self):
        PipelineController._running = False
        system_logger.info(
            "Pipeline Stopped"
        )

    def status(self):
        return PipelineController._running

    def get_live_data(self):
        return DataManager.get_data()