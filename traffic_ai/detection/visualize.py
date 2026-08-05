import cv2
from .utils import class_name, is_vehicle


def draw_boxes(image, results):
    """
    Draw vehicle detections on an image.
    """

    for result in results:

        boxes = result.boxes

        for box in boxes:

            cls = int(box.cls[0])

            if not is_vehicle(cls):
                continue

            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            label = f"{class_name(cls)} {conf:.2f}"

            cv2.putText(
                image,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    return image
# def draw_information(image, vehicle_count, fps):
#     """
#     Draw vehicle count and FPS on frame.
#     """

#     cv2.putText(
#         image,
#         f"Vehicles : {vehicle_count}",
#         (20, 40),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.8,
#         (0, 255, 255),
#         2
#     )

#     cv2.putText(
#         image,
#         f"FPS : {fps:.2f}",
#         (20, 80),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.8,
#         (255, 255, 0),
#         2
#     )

#     return image
"""
Visualization Utilities
-----------------------
Draw traffic analytics on video frames.
"""




def draw_information(
    frame,
    vehicle_count,
    fps,
    density_result,
    lane_statistics
):
    """
    Draw traffic analytics on frame.
    """

    cv2.rectangle(frame, (10, 10), (420, 250), (30, 30, 30), -1)

    y = 35

    cv2.putText(
        frame,
        f"Vehicle Count : {vehicle_count}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    y += 30

    cv2.putText(
        frame,
        f"Density : {density_result.density}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        density_result.color,
        2
    )

    y += 30

    cv2.putText(
        frame,
        f"Road Status : {density_result.road_status}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    y += 30

    cv2.putText(
        frame,
        f"Suggested Signal : {density_result.signal_time} sec",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    y += 30

    cv2.putText(
        frame,
        f"FPS : {fps:.2f}",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    y += 40

    cv2.putText(
        frame,
        "Lane Statistics",
        (20, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    y += 30

    for lane in lane_statistics:

        cv2.putText(
            frame,
            f"{lane.lane}: {lane.vehicle_count} ({lane.density})",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        y += 25

    return frame
def draw_trajectories(image, trajectories):
    """
    Draw movement paths for tracked vehicles.
    """

    for track_id, points in trajectories.items():

        if len(points) < 2:
            continue

        for i in range(1, len(points)):

            cv2.line(
                image,
                points[i - 1],
                points[i],
                (255, 0, 255),
                2
            )

        cv2.putText(
            image,
            f"ID {track_id}",
            points[-1],
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 0),
            2
        )

    return image
def draw_counting_line(image, line_position):

    cv2.line(
        image,
        (0, line_position),
        (image.shape[1], line_position),
        (0, 255, 255),
        3
    )

    cv2.putText(
        image,
        "Counting Line",
        (20, line_position - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2
    )

    return image
def draw_vehicle_count(image, count):

    cv2.putText(
        image,
        f"Vehicle Count : {count}",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    return image
def draw_speed(image, results, speed_estimator):

    if not results:
        return image

    boxes = results[0].boxes

    if boxes.id is None:
        return image

    for box, track_id in zip(boxes.xyxy, boxes.id):

        x1, y1, x2, y2 = map(int, box.tolist())

        track_id = int(track_id)

        speed = speed_estimator.get_speed(track_id)

        cv2.putText(
            image,
            f"{speed:.1f} km/h",
            (x1, y2 + 20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )

    return image
def draw_traffic_status(
    image,
    density,
    avg_speed,
    congestion
):

    cv2.putText(
        image,
        f"Density : {density:.1f} %",
        (20,160),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0,255,255),
        2
    )

    cv2.putText(
        image,
        f"Average Speed : {avg_speed:.1f} km/h",
        (20,200),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255,255,0),
        2
    )

    cv2.putText(
        image,
        f"Traffic : {congestion}",
        (20,240),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,0,255),
        2
    )

    return image
def draw_signal_information(
    image,
    signal,
    green_time
):

    cv2.putText(
        image,
        f"Current Signal : {signal}",
        (20, 280),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        image,
        f"Green Time : {green_time} sec",
        (20, 320),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    return image
def draw_priority_information(
    image,
    lane,
    score
):

    cv2.putText(
        image,
        f"Priority Lane : {lane}",
        (20, 360),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.putText(
        image,
        f"Priority Score : {score:.2f}",
        (20, 400),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 0, 255),
        2
    )

    return image
def draw_emergency_status(
    image,
    controller,
    emergency_manager
):

    if controller.is_emergency():

        emergency = emergency_manager.get_active_emergency()

        text = (
            f"Emergency : "
            f"{emergency['vehicle']} "
            f"({emergency['lane']})"
        )

        color = (0, 0, 255)

    else:

        text = "Emergency : None"

        color = (0, 255, 0)

    cv2.putText(
        image,
        text,
        (20, 440),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

    return image
def draw_scheduler_information(
    image,
    lane,
    waiting_time
):

    cv2.putText(
        image,
        f"Scheduled Lane : {lane}",
        (20, 480),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 255),
        2
    )

    y = 520

    for direction, wait in waiting_time.items():

        cv2.putText(
            image,
            f"{direction}: {wait}",
            (20, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2
        )

        y += 30

    return image