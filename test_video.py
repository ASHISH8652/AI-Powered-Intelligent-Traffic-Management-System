from traffic_ai.detection import TrafficInference

engine = TrafficInference()

engine.detect_video(
    "datasets/videos/traffic.mp4",
    "outputs/videos/detected_traffic.mp4"
)