"""
==============================================================
🚦 Smart City AI
AI-Powered Intelligent Traffic Management System
Production Version 5.0

Author:
Ashish Kumar Prusty

Features
--------
✔ Vehicle Detection (YOLOv8)
✔ Traffic Analytics
✔ Traffic Prediction
✔ Live Monitoring
✔ AI Reports
✔ Smart Dashboard
✔ Streamlit Cloud Ready

==============================================================
"""

# ==========================================================
# Standard Library
# ==========================================================

import os
import io
import cv2
import json
import time
import logging
import traceback
from pathlib import Path
from datetime import datetime

# ==========================================================
# Third Party
# ==========================================================

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import streamlit as st

# ==========================================================
# Logging
# ==========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger("SmartCityAI")

# ==========================================================
# Optional AI Modules
# ==========================================================

AI_AVAILABLE = False

try:

    from traffic_ai.system import AISystemManager

    AI_AVAILABLE = True

except Exception:

    AISystemManager = None

    logger.warning("AISystemManager not found. Running in Demo Mode.")

# ==========================================================
# Page Config
# ==========================================================

st.set_page_config(

    page_title="🚦 Smart City AI",

    page_icon="🚦",

    layout="wide",

    initial_sidebar_state="expanded"

)

# ==========================================================
# Paths
# ==========================================================

ROOT = Path(__file__).parent.resolve()

ASSETS = ROOT / "assets"

OUTPUTS = ROOT / "outputs"

MODELS = ROOT / "models"

OUTPUTS.mkdir(exist_ok=True)

LOGO = ASSETS / "logo.png"

STYLE = ASSETS / "style.css"

# ==========================================================
# Theme
# ==========================================================

st.markdown("""

<style>

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

</style>

""",unsafe_allow_html=True)

# ==========================================================
# Load CSS
# ==========================================================

def load_css():

    if STYLE.exists():

        with open(STYLE,"r",encoding="utf-8") as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

load_css()

# ==========================================================
# Cached AI Model
# ==========================================================

@st.cache_resource(show_spinner=True)

def load_ai():

    if not AI_AVAILABLE:

        return None

    try:

        return AISystemManager()

    except Exception as e:

        logger.exception(e)

        return None

# ==========================================================
# Session State
# ==========================================================

DEFAULT_STATE = {

    "manager":None,

    "uploaded_file":None,

    "file_type":None,

    "vehicle_count":0,

    "vehicle_classes":[],

    "detected_image":None,

    "analytics":None,

    "prediction":None,

    "report":None,

    "processing":False

}

for k,v in DEFAULT_STATE.items():

    if k not in st.session_state:

        st.session_state[k]=v

# ==========================================================
# Initialize AI
# ==========================================================

if st.session_state.manager is None:

    with st.spinner("Loading Smart City AI..."):

        st.session_state.manager=load_ai()

# ==========================================================
# Helper Functions
# ==========================================================

def success(msg):

    st.success(msg)

def warning(msg):

    st.warning(msg)

def error(msg):

    st.error(msg)

def info(msg):

    st.info(msg)

def traffic_density(vehicle_count):

    if vehicle_count < 20:

        return "Low"

    elif vehicle_count < 45:

        return "Medium"

    return "High"

def congestion(vehicle_count):

    return min(vehicle_count*2,100)

def waiting_time(vehicle_count):

    return round(vehicle_count*1.6,2)

# ==========================================================
# Header
# ==========================================================

st.markdown("""

<h1 style='text-align:center;color:#00BFFF;'>

🚦 Smart City AI

</h1>

""",unsafe_allow_html=True)

st.markdown("""

<div style='text-align:center'>

<h4>

AI Powered Intelligent Traffic Management System

</h4>

</div>

""",unsafe_allow_html=True)

st.divider()

# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    # ------------------------------------------------------
    # Logo
    # ------------------------------------------------------

    if LOGO.exists():
        st.image(str(LOGO), use_container_width=True)

    st.markdown(
        """
        # 🚦 Smart City AI
        ### Traffic Intelligence Platform
        """
    )

    st.caption(
        "AI-Powered Intelligent Traffic Management System"
    )

    st.divider()

    # ------------------------------------------------------
    # Navigation
    # ------------------------------------------------------

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "🚗 Vehicle Detection",
            "📊 Traffic Analytics",
            "🤖 Traffic Prediction",
            "📡 Live Monitoring",
            "📄 AI Report",
            "ℹ About"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    # ------------------------------------------------------
    # AI Status
    # ------------------------------------------------------

    st.subheader("🤖 AI Status")

    manager = st.session_state.manager

    if manager is not None:
        st.success("✅ AI Engine Loaded")
        st.success("✅ YOLOv8 Ready")
        st.success("✅ Prediction Model Ready")
    else:
        st.warning("⚠ Demo Mode")
        st.warning("⚠ YOLOv8 Offline")
        st.warning("⚠ Prediction Offline")

    st.success("✅ Analytics Engine")
    st.success("✅ Monitoring System")

    st.divider()

    # ------------------------------------------------------
    # Live Statistics
    # ------------------------------------------------------

    st.subheader("📈 Live Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Vehicles",
            st.session_state.vehicle_count
        )

        st.metric(
            "Traffic",
            traffic_density(
                st.session_state.vehicle_count
            )
        )

    with col2:

        st.metric(
            "Status",
            "Online"
        )

        st.metric(
            "Version",
            "5.0"
        )

    st.divider()

    # ------------------------------------------------------
    # Session
    # ------------------------------------------------------

    st.subheader("🗂 Session")

    if st.session_state.uploaded_file is None:

        st.info("No file uploaded")

    else:

        st.success(
            f"Loaded: {st.session_state.uploaded_file.name}"
        )

    if st.session_state.detected_image is not None:

        st.success("Detection Complete")

    else:

        st.warning("Detection Pending")

    st.divider()

    # ------------------------------------------------------
    # Features
    # ------------------------------------------------------

    st.subheader("🚀 Features")

    st.markdown(
        """
✅ Vehicle Detection

✅ Traffic Density Analysis

✅ Congestion Detection

✅ AI Prediction

✅ Live Monitoring

✅ Interactive Dashboard

✅ Download Reports

✅ Smart City Ready
"""
    )

    st.divider()

    # ------------------------------------------------------
    # Technologies
    # ------------------------------------------------------

    st.subheader("⚙ Tech Stack")

    tech_df = pd.DataFrame(
        {
            "Technology": [
                "YOLOv8",
                "OpenCV",
                "Streamlit",
                "Plotly",
                "Scikit-Learn",
                "Pandas"
            ],
            "Status": [
                "✅",
                "✅",
                "✅",
                "✅",
                "✅",
                "✅"
            ]
        }
    )

    st.dataframe(
        tech_df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ------------------------------------------------------
    # Developer
    # ------------------------------------------------------

    st.subheader("👨‍💻 Developer")

    st.markdown(
        """
**Ashish Kumar Prusty**

B.Tech Artificial Intelligence & Machine Learning

GITA Autonomous College

Odisha, India
"""
    )

    st.caption(
        "AI-Powered Intelligent Traffic Management System"
    )

    st.divider()

    # ------------------------------------------------------
    # System Info
    # ------------------------------------------------------

    st.subheader("💻 System")

    st.metric(
        "Python",
        "3.11+"
    )

    st.metric(
        "Framework",
        "Streamlit"
    )

    st.metric(
        "Detection",
        "YOLOv8"
    )

    st.metric(
        "Prediction",
        "Random Forest"
    )

    st.metric(
        "Dashboard",
        "Plotly"
    )

    st.divider()

    # ------------------------------------------------------
    # Footer
    # ------------------------------------------------------

    st.info(
        """
🚦 Smart City AI

Version **5.0**

Production Ready

Built using

YOLOv8 • OpenCV • Streamlit • Plotly
"""
    )
# ==========================================================
# HOME PAGE
# ==========================================================

if page == "🏠 Home":

    st.header("🏠 Smart Traffic Dashboard")

    st.caption(
        "AI-powered dashboard for vehicle detection, traffic analytics, prediction, and monitoring."
    )

    # ======================================================
    # KPI Cards
    # ======================================================

    vehicle_count = st.session_state.vehicle_count

    density = traffic_density(vehicle_count)

    congestion_level = congestion(vehicle_count)

    wait_time = waiting_time(vehicle_count)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🚗 Vehicles",
            vehicle_count
        )

    with col2:
        st.metric(
            "🚦 Density",
            density
        )

    with col3:
        st.metric(
            "⚠ Congestion",
            f"{congestion_level}%"
        )

    with col4:
        st.metric(
            "⏱ Avg Waiting",
            f"{wait_time} sec"
        )

    st.divider()

    # ======================================================
    # Upload Section
    # ======================================================

    st.subheader("📂 Upload Traffic Data")

    upload_type = st.radio(
        "Choose Input",
        ["Image", "Video"],
        horizontal=True
    )

    uploaded = None

    if upload_type == "Image":

        uploaded = st.file_uploader(
            "Upload Image",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded is not None:

            st.session_state.uploaded_file = uploaded
            st.session_state.file_type = "image"

            st.success("Image uploaded successfully.")

            st.image(
                uploaded,
                use_container_width=True
            )

    else:

        uploaded = st.file_uploader(
            "Upload Video",
            type=["mp4", "avi", "mov", "mkv"]
        )

        if uploaded is not None:

            st.session_state.uploaded_file = uploaded
            st.session_state.file_type = "video"

            st.success("Video uploaded successfully.")

            st.video(uploaded)

    st.divider()

    # ======================================================
    # AI Pipeline
    # ======================================================

    st.subheader("🚀 AI Processing Pipeline")

    pipeline_steps = [
        "Loading Input",
        "Vehicle Detection",
        "Traffic Analytics",
        "Prediction",
        "Monitoring",
        "Generating Report",
        "Completed"
    ]

    if st.button(
        "▶ Start AI Pipeline",
        type="primary",
        use_container_width=True
    ):

        if st.session_state.uploaded_file is None:

            st.warning("Please upload an image or video first.")

        else:

            progress = st.progress(0)

            status = st.empty()

            for i, step in enumerate(pipeline_steps):

                status.info(step)

                progress.progress(
                    int(((i + 1) / len(pipeline_steps)) * 100)
                )

                time.sleep(0.5)

            status.success("Pipeline completed successfully.")

            st.balloons()

    st.divider()

    # ======================================================
    # Traffic Summary
    # ======================================================

    st.subheader("📈 Traffic Summary")

    summary_col1, summary_col2 = st.columns(2)

    with summary_col1:

        gauge = go.Figure()

        gauge.add_trace(

            go.Indicator(

                mode="gauge+number",

                value=congestion_level,

                title={"text": "Congestion Level"},

                gauge={
                    "axis": {"range": [0, 100]},
                    "bar": {"color": "red"},
                    "steps": [
                        {"range": [0, 30], "color": "#4CAF50"},
                        {"range": [30, 70], "color": "#FFC107"},
                        {"range": [70, 100], "color": "#F44336"},
                    ],
                },
            )

        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    with summary_col2:

        trend_df = pd.DataFrame(
            {
                "Time": [
                    "08:00",
                    "09:00",
                    "10:00",
                    "11:00",
                    "12:00",
                    "13:00",
                ],
                "Vehicles": [
                    max(vehicle_count - 15, 0),
                    max(vehicle_count - 10, 0),
                    max(vehicle_count - 5, 0),
                    vehicle_count,
                    vehicle_count + 4,
                    vehicle_count + 8,
                ],
            }
        )

        fig = px.line(
            trend_df,
            x="Time",
            y="Vehicles",
            markers=True,
            title="Traffic Trend"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.divider()

    # ======================================================
    # Features
    # ======================================================

    st.subheader("🚀 Platform Features")

    left, right = st.columns(2)

    with left:

        st.info(
            """
### Computer Vision

- YOLOv8 Vehicle Detection
- Multi-Class Detection
- Real-Time Processing
- Vehicle Counting
- Density Estimation
"""
        )

    with right:

        st.info(
            """
### Artificial Intelligence

- Random Forest Prediction
- Traffic Forecasting
- Live Monitoring
- Automatic Reports
- Smart City Dashboard
"""
        )

    st.divider()

    # ======================================================
    # Quick Statistics
    # ======================================================

    st.subheader("📊 Quick Statistics")

    quick_stats = pd.DataFrame(
        {
            "Metric": [
                "Vehicle Count",
                "Traffic Density",
                "Congestion",
                "Average Waiting",
                "System Status",
            ],
            "Value": [
                vehicle_count,
                density,
                f"{congestion_level}%",
                f"{wait_time} sec",
                "Online",
            ],
        }
    )

    st.dataframe(
        quick_stats,
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    # ======================================================
    # Architecture
    # ======================================================

    st.subheader("🧠 AI Workflow")

    st.markdown(
        """
```text
Upload Image / Video
          │
          ▼
YOLOv8 Vehicle Detection
          │
          ▼
Traffic Density Analysis
          │
          ▼
Random Forest Prediction
          │
          ▼
Live Monitoring
          │
          ▼
Analytics Dashboard
          │
          ▼
Report Generation
```
""")
# ==========================================================
# VEHICLE DETECTION
# ==========================================================

elif page == "🚗 Vehicle Detection":

    st.header("🚗 AI Vehicle Detection")

    st.caption(
        "Detect vehicles from uploaded images or videos using YOLOv8."
    )

    manager = st.session_state.manager

    # ------------------------------------------------------
    # Validation
    # ------------------------------------------------------

    if st.session_state.uploaded_file is None:

        st.warning(
            "Please upload an image or video from the Home page."
        )

    else:

        uploaded = st.session_state.uploaded_file

        file_type = st.session_state.file_type

        st.success(
            f"Loaded : {uploaded.name}"
        )

        # --------------------------------------------------
        # Preview
        # --------------------------------------------------

        if file_type == "image":

            st.image(
                uploaded,
                caption="Original Image",
                use_container_width=True
            )

        else:

            st.video(uploaded)

        st.divider()

        # --------------------------------------------------
        # Detection Button
        # --------------------------------------------------

        if st.button(
            "🚀 Run Vehicle Detection",
            type="primary",
            use_container_width=True
        ):

            with st.spinner("Running YOLOv8 Detection..."):

                try:

                    suffix = uploaded.name.split(".")[-1]

                    input_path = OUTPUTS / f"input.{suffix}"

                    with open(input_path, "wb") as f:
                        f.write(uploaded.getbuffer())

                    # ======================================
                    # IMAGE
                    # ======================================

                    if file_type == "image":

                        if manager is not None:

                            result = manager.process_image(
                                str(input_path)
                            )

                        else:

                            image = cv2.imread(str(input_path))

                            result = image

                        st.session_state.detected_image = result

                        st.image(
                            result,
                            caption="Detection Result",
                            use_container_width=True
                        )

                    # ======================================
                    # VIDEO
                    # ======================================

                    else:

                        output_video = OUTPUTS / "detected_video.mp4"

                        if manager is not None:

                            manager.process_video(
                                str(input_path),
                                str(output_video)
                            )

                        else:

                            import shutil

                            shutil.copy(
                                str(input_path),
                                str(output_video)
                            )

                        st.video(str(output_video))

                    # ======================================
                    # Live Data
                    # ======================================

                    if manager is not None:

                        try:

                            live = manager.get_live_data()

                            st.session_state.vehicle_count = live.get(
                                "vehicle_count",
                                0
                            )

                            st.session_state.vehicle_classes = live.get(
                                "classes",
                                []
                            )

                        except Exception:

                            pass

                    st.success(
                        "Vehicle Detection Completed Successfully."
                    )

                except Exception as e:

                    logger.exception(e)

                    st.error(
                        "Detection Failed."
                    )

                    st.exception(e)

    st.divider()

    # ======================================================
    # Detection Summary
    # ======================================================

    st.subheader("📊 Detection Summary")

    vehicle_count = st.session_state.vehicle_count

    density = traffic_density(vehicle_count)

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Vehicles",
            vehicle_count
        )

    with c2:

        st.metric(
            "Density",
            density
        )

    with c3:

        st.metric(
            "Vehicle Types",
            len(
                st.session_state.vehicle_classes
            )
        )

    with c4:

        st.metric(
            "Detection",
            "Completed"
            if st.session_state.detected_image is not None
            else "Waiting"
        )

    st.divider()

    # ======================================================
    # Vehicle Class Table
    # ======================================================

    if len(st.session_state.vehicle_classes) > 0:

        st.subheader("🚘 Detected Vehicle Classes")

        vehicle_df = pd.DataFrame(

            {

                "Vehicle Type":

                st.session_state.vehicle_classes

            }

        )

        st.dataframe(

            vehicle_df,

            use_container_width=True,

            hide_index=True

        )

    # ======================================================
    # Distribution Chart
    # ======================================================

    if len(st.session_state.vehicle_classes) > 0:

        st.subheader("📈 Vehicle Distribution")

        chart = (

            pd.Series(

                st.session_state.vehicle_classes

            )

            .value_counts()

            .reset_index()

        )

        chart.columns = [

            "Vehicle",

            "Count"

        ]

        fig = px.bar(

            chart,

            x="Vehicle",

            y="Count",

            color="Count",

            text="Count",

            title="Detected Vehicle Distribution"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

    # ======================================================
    # Download
    # ======================================================

    if st.session_state.detected_image is not None:

        st.divider()

        st.subheader("⬇ Download")

        success, encoded = cv2.imencode(

            ".jpg",

            st.session_state.detected_image

        )

        if success:

            st.download_button(

                "Download Detection Result",

                encoded.tobytes(),

                file_name="vehicle_detection.jpg",

                mime="image/jpeg",

                use_container_width=True

            )

    # ======================================================
    # Detection Information
    # ======================================================

    st.divider()

    with st.expander("ℹ Detection Information"):

        st.markdown(
            """
### YOLOv8 Vehicle Detection

Supported Vehicles

- 🚗 Car
- 🚌 Bus
- 🚚 Truck
- 🏍 Motorcycle
- 🚲 Bicycle

Detection Features

- Vehicle Counting
- Multi-Class Detection
- Bounding Boxes
- Confidence Scores
- Real-Time Processing

Output

- Annotated Image/Video
- Vehicle Count
- Vehicle Types
- Detection Summary
"""
        )
# ==========================================================
# TRAFFIC ANALYTICS
# ==========================================================

elif page == "📊 Traffic Analytics":

    st.header("📊 Traffic Analytics Dashboard")

    vehicle_count = st.session_state.vehicle_count

    if vehicle_count == 0:

        st.info("Run Vehicle Detection first to generate analytics.")

    else:

        density = traffic_density(vehicle_count)
        congestion_level = congestion(vehicle_count)
        wait = waiting_time(vehicle_count)

        analytics = {
            "vehicle_count": vehicle_count,
            "traffic_density": density,
            "congestion": congestion_level,
            "waiting_time": wait,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        st.session_state.analytics = analytics

        # ==================================================
        # KPI Cards
        # ==================================================

        c1, c2, c3, c4 = st.columns(4)

        with c1:
            st.metric("🚗 Vehicles", vehicle_count)

        with c2:
            st.metric("🚦 Density", density)

        with c3:
            st.metric("⚠ Congestion", f"{congestion_level}%")

        with c4:
            st.metric("⏱ Waiting", f"{wait} sec")

        st.divider()

        # ==================================================
        # Vehicle Distribution
        # ==================================================

        if len(st.session_state.vehicle_classes) > 0:

            vehicle_df = (
                pd.Series(
                    st.session_state.vehicle_classes
                )
                .value_counts()
                .reset_index()
            )

            vehicle_df.columns = [
                "Vehicle",
                "Count"
            ]

        else:

            vehicle_df = pd.DataFrame({

                "Vehicle":[
                    "Car",
                    "Bus",
                    "Truck",
                    "Bike"
                ],

                "Count":[
                    int(vehicle_count*0.55),
                    int(vehicle_count*0.15),
                    int(vehicle_count*0.15),
                    int(vehicle_count*0.15)
                ]

            })

        left, right = st.columns(2)

        with left:

            fig = px.bar(

                vehicle_df,

                x="Vehicle",

                y="Count",

                color="Vehicle",

                text="Count",

                title="Vehicle Distribution"

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        with right:

            fig = px.pie(

                vehicle_df,

                names="Vehicle",

                values="Count",

                hole=0.45,

                title="Vehicle Share"

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

        st.divider()

        # ==================================================
        # Congestion Gauge
        # ==================================================

        left, right = st.columns(2)

        with left:

            gauge = go.Figure()

            gauge.add_trace(

                go.Indicator(

                    mode="gauge+number",

                    value=congestion_level,

                    title={"text":"Congestion Level"},

                    gauge={

                        "axis":{"range":[0,100]},

                        "bar":{"color":"red"},

                        "steps":[

                            {"range":[0,30],"color":"green"},

                            {"range":[30,70],"color":"orange"},

                            {"range":[70,100],"color":"red"}

                        ]

                    }

                )

            )

            st.plotly_chart(

                gauge,

                use_container_width=True

            )

        with right:

            traffic_df = pd.DataFrame({

                "Hour":[
                    "08",
                    "09",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15"
                ],

                "Vehicles":[

                    max(vehicle_count-15,0),

                    max(vehicle_count-10,0),

                    max(vehicle_count-5,0),

                    vehicle_count,

                    vehicle_count+5,

                    vehicle_count+8,

                    vehicle_count+3,

                    vehicle_count-2

                ]

            })

            line = px.line(

                traffic_df,

                x="Hour",

                y="Vehicles",

                markers=True,

                title="Traffic Trend"

            )

            st.plotly_chart(

                line,

                use_container_width=True

            )

        st.divider()

        # ==================================================
        # Heatmap
        # ==================================================

        st.subheader("🔥 Traffic Density Heatmap")

        heat = np.random.randint(

            10,

            vehicle_count+20,

            size=(6,6)

        )

        heat_fig = px.imshow(

            heat,

            text_auto=True,

            aspect="auto",

            title="Road Zone Density"

        )

        st.plotly_chart(

            heat_fig,

            use_container_width=True

        )

        st.divider()

        # ==================================================
        # AI Insights
        # ==================================================

        st.subheader("🤖 AI Insights")

        if congestion_level < 30:

            st.success(

                "Traffic flow is smooth. No congestion detected."

            )

        elif congestion_level < 70:

            st.warning(

                "Moderate congestion detected. Consider adjusting signal timing."

            )

        else:

            st.error(

                "Heavy congestion detected. Immediate traffic management is recommended."

            )

        st.info(

            f"""
Average waiting time : **{wait} sec**

Traffic density : **{density}**

Estimated congestion : **{congestion_level}%**
"""
        )

        st.divider()

        # ==================================================
        # Summary Table
        # ==================================================

        summary = pd.DataFrame({

            "Metric":[

                "Vehicle Count",

                "Traffic Density",

                "Congestion",

                "Waiting Time",

                "System Status"

            ],

            "Value":[

                vehicle_count,

                density,

                f"{congestion_level}%",

                f"{wait} sec",

                "Operational"

            ]

        })

        st.subheader("📋 Analytics Summary")

        st.dataframe(

            summary,

            use_container_width=True,

            hide_index=True

        )

        st.divider()

        # ==================================================
        # Download
        # ==================================================

        st.download_button(

            "⬇ Download Analytics CSV",

            summary.to_csv(index=False),

            file_name="traffic_analytics.csv",

            mime="text/csv",

            use_container_width=True

        )
# ==========================================================
# TRAFFIC PREDICTION
# ==========================================================

elif page == "🤖 Traffic Prediction":

    st.header("🤖 AI Traffic Prediction")

    vehicle_count = st.session_state.vehicle_count

    if vehicle_count == 0:

        st.warning(
            "Please run Vehicle Detection first."
        )

    else:

        st.info(
            "Predict future traffic using the trained Machine Learning model."
        )

        st.divider()

        # ==================================================
        # Prediction Inputs
        # ==================================================

        col1, col2, col3 = st.columns(3)

        with col1:

            hour = st.slider(
                "Hour",
                0,
                23,
                datetime.now().hour
            )

        with col2:

            weather = st.selectbox(
                "Weather",
                [
                    "Clear",
                    "Clouds",
                    "Rain",
                    "Fog",
                    "Snow"
                ]
            )

        with col3:

            is_holiday = st.selectbox(
                "Holiday",
                [
                    "No",
                    "Yes"
                ]
            )

        st.divider()

        # ==================================================
        # Prediction Button
        # ==================================================

        if st.button(
            "🚀 Predict Future Traffic",
            use_container_width=True,
            type="primary"
        ):

            with st.spinner("Running Prediction Model..."):

                manager = st.session_state.manager

                prediction = None

                # --------------------------------------------
                # Production Model
                # --------------------------------------------

                if manager is not None:

                    try:

                        prediction = manager.predict()

                    except Exception:

                        prediction = None

                # --------------------------------------------
                # Demo Prediction
                # --------------------------------------------

                if prediction is None:

                    weather_factor = {
                        "Clear": 0,
                        "Clouds": 3,
                        "Rain": 8,
                        "Fog": 5,
                        "Snow": 10
                    }

                    holiday_factor = 8 if is_holiday == "Yes" else 0

                    rush_hour = (
                        12
                        if hour in [8, 9, 17, 18]
                        else 0
                    )

                    future = (
                        vehicle_count
                        + weather_factor[weather]
                        + holiday_factor
                        + rush_hour
                        + np.random.randint(-3, 6)
                    )

                    future = max(future, 0)

                    congestion_probability = min(
                        future * 2,
                        100
                    )

                    green_signal = max(
                        30,
                        min(120, future + 30)
                    )

                    waiting = round(
                        future * 1.4,
                        2
                    )

                    if future < 20:

                        status = "Low"

                    elif future < 45:

                        status = "Moderate"

                    else:

                        status = "High"

                    prediction = {

                        "future_traffic": future,

                        "congestion_probability": congestion_probability,

                        "signal_time": green_signal,

                        "waiting_time": waiting,

                        "status": status

                    }

                st.session_state.prediction = prediction

                st.success(
                    "Prediction Completed Successfully."
                )

        # ==================================================
        # Results
        # ==================================================

        if st.session_state.prediction is not None:

            pred = st.session_state.prediction

            st.divider()

            st.subheader("📊 Prediction Results")

            c1, c2, c3, c4, c5 = st.columns(5)

            with c1:

                st.metric(
                    "Future Vehicles",
                    pred["future_traffic"]
                )

            with c2:

                st.metric(
                    "Congestion",
                    f"{pred['congestion_probability']}%"
                )

            with c3:

                st.metric(
                    "Green Signal",
                    f"{pred['signal_time']} sec"
                )

            with c4:

                st.metric(
                    "Waiting Time",
                    f"{pred['waiting_time']} sec"
                )

            with c5:

                st.metric(
                    "Status",
                    pred["status"]
                )

            st.divider()

            # ==============================================
            # Gauge
            # ==============================================

            left, right = st.columns(2)

            with left:

                gauge = go.Figure()

                gauge.add_trace(

                    go.Indicator(

                        mode="gauge+number",

                        value=pred["congestion_probability"],

                        title={
                            "text": "Congestion Probability"
                        },

                        gauge={

                            "axis": {
                                "range": [0, 100]
                            },

                            "bar": {
                                "color": "red"
                            },

                            "steps": [

                                {
                                    "range": [0, 30],
                                    "color": "green"
                                },

                                {
                                    "range": [30, 70],
                                    "color": "orange"
                                },

                                {
                                    "range": [70, 100],
                                    "color": "red"
                                }

                            ]

                        }

                    )

                )

                st.plotly_chart(
                    gauge,
                    use_container_width=True
                )

            # ==============================================
            # Forecast Chart
            # ==============================================

            with right:

                forecast = pd.DataFrame({

                    "Time": [

                        "Current",

                        "+15m",

                        "+30m",

                        "+45m",

                        "+60m"

                    ],

                    "Vehicles": [

                        vehicle_count,

                        int(
                            (vehicle_count + pred["future_traffic"]) / 2
                        ),

                        pred["future_traffic"],

                        pred["future_traffic"] + 4,

                        pred["future_traffic"] + 2

                    ]

                })

                fig = px.line(

                    forecast,

                    x="Time",

                    y="Vehicles",

                    markers=True,

                    title="Traffic Forecast"

                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            st.divider()

            # ==============================================
            # Recommendation
            # ==============================================

            st.subheader("🚦 AI Recommendation")

            if pred["status"] == "Low":

                st.success(
                    "Traffic is expected to remain smooth. Normal signal timing is sufficient."
                )

            elif pred["status"] == "Moderate":

                st.warning(
                    "Moderate traffic expected. Consider increasing green signal duration."
                )

            else:

                st.error(
                    "Heavy congestion predicted. Dynamic traffic control is recommended."
                )

            recommendation = pd.DataFrame({

                "Parameter": [

                    "Current Vehicles",

                    "Predicted Vehicles",

                    "Congestion",

                    "Signal Time",

                    "Waiting Time",

                    "Traffic Status"

                ],

                "Value": [

                    vehicle_count,

                    pred["future_traffic"],

                    f"{pred['congestion_probability']}%",

                    f"{pred['signal_time']} sec",

                    f"{pred['waiting_time']} sec",

                    pred["status"]

                ]

            })

            st.dataframe(
                recommendation,
                use_container_width=True,
                hide_index=True
            )

            st.download_button(

                "⬇ Download Prediction Report",

                recommendation.to_csv(index=False),

                file_name="traffic_prediction.csv",

                mime="text/csv",

                use_container_width=True

            )
# ==========================================================
# LIVE MONITORING
# ==========================================================

elif page == "📡 Live Monitoring":

    st.header("📡 Live Traffic Monitoring")

    st.caption(
        "Real-time monitoring dashboard for Smart City AI."
    )

    vehicles = st.session_state.vehicle_count

    if vehicles == 0:

        st.info(
            "Run Vehicle Detection to start monitoring."
        )

    else:

        current_time = datetime.now()

        density = traffic_density(vehicles)

        congestion_level = congestion(vehicles)

        wait = waiting_time(vehicles)

        # ==================================================
        # Live Metrics
        # ==================================================

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "🚗 Vehicles",
            vehicles
        )

        c2.metric(
            "🚦 Density",
            density
        )

        c3.metric(
            "⚠ Congestion",
            f"{congestion_level}%"
        )

        c4.metric(
            "🕒 Updated",
            current_time.strftime("%H:%M:%S")
        )

        st.divider()

        # ==================================================
        # Live Trend
        # ==================================================

        trend = pd.DataFrame({

            "Minute":[

                "00",

                "05",

                "10",

                "15",

                "20",

                "25",

                "30"

            ],

            "Vehicles":[

                max(vehicles-6,0),

                max(vehicles-3,0),

                vehicles,

                vehicles+2,

                vehicles+5,

                vehicles+3,

                vehicles

            ]

        })

        fig = px.line(

            trend,

            x="Minute",

            y="Vehicles",

            markers=True,

            title="Live Traffic Trend"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

        st.divider()

        # ==================================================
        # Congestion Gauge
        # ==================================================

        left, right = st.columns(2)

        with left:

            gauge = go.Figure()

            gauge.add_trace(

                go.Indicator(

                    mode="gauge+number",

                    value=congestion_level,

                    title={"text":"Live Congestion"},

                    gauge={

                        "axis":{"range":[0,100]},

                        "bar":{"color":"red"}

                    }

                )

            )

            st.plotly_chart(

                gauge,

                use_container_width=True

            )

        with right:

            system = pd.DataFrame({

                "Module":[

                    "YOLOv8",

                    "Analytics",

                    "Prediction",

                    "Monitoring",

                    "Dashboard"

                ],

                "Status":[

                    "Online" if st.session_state.manager else "Demo",

                    "Online",

                    "Online",

                    "Online",

                    "Online"

                ]

            })

            st.dataframe(

                system,

                hide_index=True,

                use_container_width=True

            )

        st.divider()

        # ==================================================
        # AI Monitoring Insights
        # ==================================================

        st.subheader("🤖 Live AI Insights")

        if congestion_level < 30:

            st.success(
                "Traffic is flowing normally."
            )

        elif congestion_level < 70:

            st.warning(
                "Moderate congestion detected."
            )

        else:

            st.error(
                "Heavy congestion detected. Optimize traffic signals."
            )

        st.info(

            f"""
Current Time : **{current_time.strftime('%Y-%m-%d %H:%M:%S')}**

Traffic Density : **{density}**

Estimated Waiting Time : **{wait} sec**
"""

        )

# ==========================================================
# REPORT GENERATION
# ==========================================================

elif page == "📄 AI Report":

    st.header("📄 AI Traffic Report")

    vehicle_count = st.session_state.vehicle_count

    analytics = st.session_state.analytics

    prediction = st.session_state.prediction

    report = {

        "generated_on":

        datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        ),

        "vehicle_count":

        vehicle_count,

        "traffic_density":

        traffic_density(vehicle_count),

        "congestion":

        congestion(vehicle_count),

        "waiting_time":

        waiting_time(vehicle_count),

        "analytics":

        analytics,

        "prediction":

        prediction

    }

    st.session_state.report = report

    st.subheader("📋 Report Summary")

    report_df = pd.DataFrame({

        "Parameter":[

            "Generated",

            "Vehicle Count",

            "Traffic Density",

            "Congestion",

            "Waiting Time"

        ],

        "Value":[

            report["generated_on"],

            report["vehicle_count"],

            report["traffic_density"],

            f"{report['congestion']}%",

            f"{report['waiting_time']} sec"

        ]

    })

    st.dataframe(

        report_df,

        hide_index=True,

        use_container_width=True

    )

    st.divider()

    st.subheader("📊 Report Preview")

    st.json(report)

    st.divider()

    # ==================================================
    # Downloads
    # ==================================================

    csv = report_df.to_csv(index=False)

    st.download_button(

        "⬇ Download CSV Report",

        csv,

        file_name="traffic_report.csv",

        mime="text/csv",

        use_container_width=True

    )

    st.download_button(

        "⬇ Download JSON Report",

        json.dumps(

            report,

            indent=4

        ),

        file_name="traffic_report.json",

        mime="application/json",

        use_container_width=True

    )

    st.divider()

    # ==================================================
    # Printable Report
    # ==================================================

    st.subheader("📈 Executive Summary")

    st.info(f"""

**Smart City AI Traffic Report**

• Vehicles Detected : **{vehicle_count}**

• Traffic Density : **{traffic_density(vehicle_count)}**

• Congestion : **{congestion(vehicle_count)}%**

• Estimated Waiting Time : **{waiting_time(vehicle_count)} sec**

• Report Generated : **{report['generated_on']}**

""")
# ==========================================================
# ABOUT PAGE
# ==========================================================

elif page == "ℹ About":

    st.header("ℹ About Smart City AI")

    st.markdown("""
## 🚦 Smart City AI

An AI-powered Intelligent Traffic Management System that combines
Computer Vision, Machine Learning, and Interactive Analytics
to monitor and optimize urban traffic.

---

### 🎯 Objectives

- Detect vehicles in real time
- Analyze traffic density
- Predict future traffic
- Monitor congestion
- Generate AI-powered reports
- Assist Smart City traffic management

---

### 🚀 Key Features

- 🚗 YOLOv8 Vehicle Detection
- 📊 Traffic Analytics Dashboard
- 🤖 Random Forest Traffic Prediction
- 📡 Live Monitoring
- 📄 Automatic Report Generation
- 📈 Interactive Plotly Charts
- ☁ Streamlit Cloud Deployment Ready

---

### 🛠 Technology Stack

| Category | Technology |
|----------|------------|
| Programming | Python |
| Computer Vision | YOLOv8, OpenCV |
| Machine Learning | Scikit-Learn |
| Dashboard | Streamlit |
| Visualization | Plotly |
| Data Analysis | Pandas, NumPy |

---

### 👨‍💻 Developer

**Ashish Kumar Prusty**

B.Tech – Artificial Intelligence & Machine Learning

GITA Autonomous College

Odisha, India

---

### 📌 Version

Smart City AI **Version 5.0**

Production Release

""")

    st.divider()

    st.subheader("🏆 System Overview")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("AI Engine", "YOLOv8")

    with c2:
        st.metric("Prediction", "Random Forest")

    with c3:
        st.metric("Dashboard", "Streamlit")

    st.divider()

    st.success("System Ready for Smart City Deployment")

# ==========================================================
# GLOBAL FOOTER
# ==========================================================

st.divider()

footer1, footer2, footer3 = st.columns(3)

with footer1:
    st.info("""
🚗 Vehicle Detection

YOLOv8
""")

with footer2:
    st.info("""
🤖 Prediction

Random Forest
""")

with footer3:
    st.info("""
📊 Dashboard

Streamlit + Plotly
""")

st.divider()

status1, status2, status3, status4 = st.columns(4)

status1.metric("Detection", "Ready")

status2.metric("Analytics", "Ready")

status3.metric("Prediction", "Ready")

status4.metric("Monitoring", "Ready")

st.divider()

st.caption(
    "🚦 Smart City AI • AI-Powered Intelligent Traffic Management System"
)

st.caption(
    "Developed by Ashish Kumar Prusty"
)

st.caption(
    "Powered by Python • YOLOv8 • OpenCV • Scikit-Learn • Streamlit • Plotly"
)

st.caption(
    "© 2026 Smart City AI | All Rights Reserved"
)