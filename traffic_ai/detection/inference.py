"""
Traffic Inference Engine
------------------------
Runs vehicle detection on images/videos and updates
the shared application state.
"""

import time
import cv2
import os
from traffic_ai.config import VIDEO_CODEC
from traffic_ai.integration import PipelineController

from .detector import VehicleDetector
from .visualize import draw_boxes, draw_information
from .utils import get_vehicle_count

from traffic_ai.analytics.density import TrafficDensity
from traffic_ai.analytics.lane_analytics import LaneAnalyzer
from traffic_ai.analytics.traffic_flow import TrafficFlowAnalyzer

from traffic_ai.integration import DataManager
from traffic_ai.integration.live_manager import LiveManager

from traffic_ai.utils.logger import (
    detection_logger,
    error_logger
)
class TrafficInference:

    def __init__(self):

        self.detector = VehicleDetector()

        self.density = TrafficDensity()

        self.lane_analyzer = LaneAnalyzer()

        self.live_manager = LiveManager()

    # =====================================================
    # IMAGE DETECTION
    # =====================================================

    def detect_image(self, image_path):

        if not os.path.exists(image_path):
            raise FileNotFoundError(
                f"Image file not found: {image_path}"
            )

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Cannot read image (invalid image format or corrupt file): {image_path}"
            )

        results = self.detector.detect(image)

        output = draw_boxes(image, results)

        return output

    # =====================================================
    # VIDEO DETECTION
    # =====================================================

    def detect_video(self, video_path, output_path):

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise FileNotFoundError(
                f"Cannot open video: {video_path}"
            )

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        fps_video = cap.get(cv2.CAP_PROP_FPS)

        writer = cv2.VideoWriter(

            output_path,

            cv2.VideoWriter_fourcc(*VIDEO_CODEC),

            fps_video,

            (width, height)

        )

        flow = TrafficFlowAnalyzer(width)

        pipeline = PipelineController()
        pipeline.start()

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            start = time.time()

            try:

                # ---------------------------------------------
                # YOLO Detection
                # ---------------------------------------------

                results = self.detector.detect(frame)

                frame = draw_boxes(frame, results)

                # ---------------------------------------------
                # Vehicle Count
                # ---------------------------------------------

                vehicle_count = get_vehicle_count(results)

                detection_logger.info(
                    f"Processing Frame | Vehicles={vehicle_count}"
                )

                # ---------------------------------------------
                # Traffic Density
                # ---------------------------------------------

                density = self.density.estimate(
                    vehicle_count
                )

                # ---------------------------------------------
                # Lane Analytics
                # ---------------------------------------------

                self.lane_analyzer.reset()

                for result in results:

                    boxes = result.boxes.xyxy.cpu().numpy()

                    for box in boxes:

                        center_x, center_y = flow.get_center(box)

                        lane = flow.get_lane(center_x)

                        self.lane_analyzer.update_lane(
                            lane
                        )

                lane_statistics = (
                    self.lane_analyzer.get_statistics()
                )

                # ---------------------------------------------
                # FPS
                # ---------------------------------------------

                fps = 1 / (time.time() - start)

                # ---------------------------------------------
                # Congestion Level
                # ---------------------------------------------

                if vehicle_count < 20:
                    congestion = "Low"

                elif vehicle_count < 50:
                    congestion = "Medium"

                elif vehicle_count < 80:
                    congestion = "High"

                else:
                    congestion = "Severe"

                # ---------------------------------------------
                # Recommendation
                # ---------------------------------------------

                if congestion == "Low":

                    recommendation = (
                        "Traffic Flow Normal"
                    )

                elif congestion == "Medium":

                    recommendation = (
                        "Increase Green Signal"
                    )

                elif congestion == "High":

                    recommendation = (
                        "Optimize Signal Timing"
                    )

                else:

                    recommendation = (
                        "Open Alternate Route"
                    )

                # ---------------------------------------------
                # Update Shared State
                # ---------------------------------------------

                DataManager.update_vehicle_count(
                    vehicle_count
                )

                DataManager.update_density(
                    density
                )

                DataManager.update_lane_data(
                    lane_statistics
                )

                DataManager.update_fps(
                    round(fps, 2)
                )

                self.live_manager.update()

                DataManager.update_congestion(
                    congestion
                )

                DataManager.update_recommendation(
                    recommendation
                )

                # ---------------------------------------------
                # Draw Dashboard Information
                # ---------------------------------------------

                frame = draw_information(

                    frame,

                    vehicle_count,

                    fps,

                    density,

                    lane_statistics

                )

                writer.write(frame)

                cv2.imshow(
                    "Traffic Detection",
                    frame
                )

                if cv2.waitKey(1) == 27:
                    break

            except Exception as e:

                error_logger.error(str(e))

                continue

        pipeline.stop()

        cap.release()

        writer.release()

        cv2.destroyAllWindows()