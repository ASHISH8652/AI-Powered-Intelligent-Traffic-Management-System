import logging
import os

from traffic_ai.config import LOG_FOLDER

LOG_DIR = LOG_FOLDER

os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name, filename):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    file_handler = logging.FileHandler(

        os.path.join(LOG_DIR, filename)

    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


system_logger = get_logger(
    "system",
    "system.log"
)

prediction_logger = get_logger(
    "prediction",
    "prediction.log"
)

detection_logger = get_logger(
    "detection",
    "detection.log"
)

error_logger = get_logger(
    "error",
    "error.log"
)