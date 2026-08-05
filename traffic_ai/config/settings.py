"""
Global Project Settings
"""

from dotenv import load_dotenv
import os

load_dotenv()

# ==========================
# YOLO Configuration
# ==========================

YOLO_MODEL = os.getenv(
    "YOLO",
    "models/yolov8n.pt"
)

CONFIDENCE = 0.30

IOU_THRESHOLD = 0.45

DEVICE = "cpu"

# ==========================
# Video Settings
# ==========================

DEFAULT_FPS = 30

VIDEO_CODEC = "mp4v"

# ==========================
# Prediction Model
# ==========================

MODEL_FILE = os.getenv(
    "MODEL",
    "models/random_forest.pkl"
)

SCALER_FILE = "models/scaler.pkl"

# ==========================
# Dashboard
# ==========================

REFRESH_TIME = 1

MAX_HISTORY = 100

# ==========================
# Logging
# ==========================

LOG_FOLDER = os.getenv(
    "LOG_FOLDER",
    "logs"
)