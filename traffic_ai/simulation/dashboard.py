"""
Traffic Dashboard
-----------------
Displays signal status.
"""

import cv2


def draw_intersection_dashboard(
    image,
    signal_state
):

    y = 60

    cv2.putText(
        image,
        "Traffic Signal Dashboard",
        (900,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255,255,255),
        2
    )

    for lane, signal in signal_state.items():

        if signal == "GREEN":

            color = (0,255,0)

        else:

            color = (0,0,255)

        cv2.putText(
            image,
            f"{lane}: {signal}",
            (900,y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            color,
            2
        )

        y += 40

    return image