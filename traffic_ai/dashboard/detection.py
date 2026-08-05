import streamlit as st
import tempfile
import os
import cv2

from traffic_ai.detection.inference import TrafficInference
from traffic_ai.integration import DataManager


def detection():
    st.title("🚗 Vehicle Detection")
    st.markdown(
        """
Upload an image or a video and let the AI detect vehicles,
estimate traffic density, and update the monitoring dashboard.
"""
    )
    uploaded_file = st.file_uploader(
    "Upload Image or Video",
    type=["jpg","jpeg","png","mp4","avi","mov"]
)
    st.markdown("---")

    inference = TrafficInference()
    option = st.radio(
        "Choose Input",
        ["Image", "Video"],
        horizontal=True
    )

    if option == "Image":
        uploaded = st.file_uploader(
            "Upload Image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded:
            st.image(uploaded)

            if st.button("Detect Vehicles"):
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".jpg"
                ) as temp:
                    temp.write(uploaded.read())
                    image_path = temp.name

                result = inference.detect_image(image_path)

                st.image(
                    cv2.cvtColor(result, cv2.COLOR_BGR2RGB),
                    use_container_width=True
                )

                os.remove(image_path)

    elif option == "Video":
        uploaded = st.file_uploader(
            "Upload Video",
            type=["mp4", "avi", "mov"]
        )

        if uploaded:
            st.video(uploaded)

            if st.button("Run Detection"):
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp4"
                ) as temp:
                    temp.write(uploaded.read())
                    input_video = temp.name

                output_video = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp4"
                ).name

                inference.detect_video(input_video, output_video)
                st.success("Detection Completed")

                st.video(output_video)
                os.remove(input_video)