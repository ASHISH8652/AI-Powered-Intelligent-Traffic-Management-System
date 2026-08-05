"""
Utility functions for detection.
"""

# COCO dataset class IDs
VEHICLE_CLASSES = {
    1: "bicycle",
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck"
}


def is_vehicle(class_id):
    """
    Check whether the detected class is a vehicle.
    """
    return class_id in VEHICLE_CLASSES


def class_name(class_id):
    """
    Convert class ID to readable name.
    """
    return VEHICLE_CLASSES.get(class_id, "unknown")
def get_vehicle_count(results):
    """
    Count detected vehicles in YOLO results.
    """

    count = 0

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])

            if is_vehicle(cls):
                count += 1

    return count