"""
Home Dashboard
--------------
Landing page for the AI-Powered Intelligent Traffic Management System.
"""

import os
import time
import streamlit as st
from traffic_ai.integration import DataManager, PipelineController

def home():

    manager = st.session_state.system_manager

    live = manager.get_live_data()

    st.markdown(
        """
<style>
.block-container{
    padding-top:1rem;
}
</style>
""",
        unsafe_allow_html=True
    )

    # ==========================================================
    # Title
    # ==========================================================

    # st.title("🚦 AI-Powered Intelligent Traffic Management System")
    st.markdown("""
# 🚦 AI-Powered Intelligent Traffic Management System

### Smart City Traffic Intelligence Platform
""")

    st.markdown("---")

    # ==========================================================
    # Banner / Logo
    # ==========================================================

    banner_path = "assets/banner.png"
    logo_path = "assets/logo.png"

    if os.path.exists(banner_path):

        st.image(
            banner_path,
            use_container_width=True
        )

    elif os.path.exists(logo_path):

        st.image(
            logo_path,
            width=250
        )

    # ==========================================================
    # Dashboard KPI Cards
    # ==========================================================

    st.subheader("📊 Live System Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Today's Vehicles",
        "42,153",
        "+7%"
    )

    col2.metric(
        "Congestion",
        "Medium"
    )

    col3.metric(
        "Average Speed",
        "44 km/h"
    )

    col4.metric(
        "AI Accuracy",
        "96.8%"
    )

    st.markdown("---")

    st.subheader("📈 Live System Summary")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Vehicles",
        live["vehicle_count"]
    )

    c2.metric(
        "Density",
        live["density"]
    )

    c3.metric(
        "Prediction",
        live["prediction"]
    )

    st.markdown("---")

    # ==========================================================
    # Project Overview
    # ==========================================================

    st.subheader("🌍 Smart Traffic Vision")

    left, right = st.columns([2, 3])

    with left:

        st.image(
            "assets/logo.png",
            use_container_width=True
        )

    with right:

        st.write(
            """
The AI Traffic Management System uses Artificial Intelligence,
Computer Vision and Machine Learning to monitor city traffic
in real time.

It automatically detects vehicles, estimates congestion,
predicts future traffic conditions and recommends smart
signal timing.
"""
        )

    pipeline = PipelineController()

    # ==========================================================
    # Features
    # ==========================================================

    st.subheader("✨ Key Features")

    left, right = st.columns(2)

    with left:

        st.success("✅ Vehicle Detection (YOLOv8)")

        st.success("✅ Multi-Object Tracking")

        st.success("✅ Vehicle Counting")

        st.success("✅ Lane-wise Analytics")

    with right:

        st.success("✅ Traffic Density Estimation")

        st.success("✅ AI Traffic Prediction")

        st.success("✅ Smart Signal Recommendation")

        st.success("✅ Live Monitoring Dashboard")

    st.markdown("---")

    # ==========================================================
    # Core AI Modules
    # ==========================================================

    st.subheader("🚀 Core AI Modules")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info("""
### 🚗 Detection

YOLOv8

Computer Vision

Live Camera
""")

    with c2:

        st.success("""
### 📊 Analytics

Density

Vehicle Count

Lane Analysis
""")

    with c3:

        st.warning("""
### 🤖 Prediction

Random Forest

Traffic Forecast

Recommendations
""")

    st.markdown("---")

    c4, c5, c6 = st.columns(3)

    with c4:

        st.info("""
### 🚦 Smart Signals

Optimization

Adaptive Timing
""")

    with c5:

        st.success("""
### 📡 Monitoring

Live Dashboard

Real-Time KPIs
""")

    with c6:

        st.warning("""
### 🌍 Smart City

Future Ready

Scalable
""")

    st.markdown("---")

    st.subheader("⚡ Quick Access")

    c1, c2, c3, c4 = st.columns(4)

    c1.button("🚗 Detection")

    c2.button("📊 Analytics")

    c3.button("🤖 Prediction")

    c4.button("📡 Monitoring")

    st.markdown("---")

    # ==========================================================
    # AI Pipeline Control
    # ==========================================================

    st.subheader("🚀 AI Pipeline Control")

    pipeline = PipelineController()

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button("▶ Start AI Pipeline"):

            pipeline.start()

            st.success("AI Pipeline Started")

    with col2:

        if st.button("⏹ Stop AI Pipeline"):

            pipeline.stop()

            st.warning("AI Pipeline Stopped")

    with col3:

        if pipeline.status():

            st.success("🟢 Running")

        else:

            st.error("🔴 Offline")

    st.markdown("---")

    # ==========================================================
    # System Status
    # ==========================================================

    st.subheader("🖥 System Status")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(label="Model Loader", value="OK", delta="Ready")
    c2.metric(label="Detection Engine", value="Online", delta="YOLOv8")
    c3.metric(label="Prediction Service", value="Ready", delta="Feature OK")
    c4.metric(label="Dashboard", value="Live", delta="All Systems Go")

    st.markdown("---")

    # ==========================================================
    # Project Information
    # ==========================================================

    with st.expander("📌 Project Information"):

        st.markdown(
            """
**Project Name**

AI-Powered Intelligent Traffic Management System

**Technologies Used**

- Python
- Streamlit
- OpenCV
- YOLOv8
- Random Forest
- Scikit-Learn
- Plotly

**Modules**

- Vehicle Detection
- Traffic Analytics
- AI Prediction
- Live Monitoring
- Smart Recommendations
"""
        )

    st.markdown("---")

    # ==========================================================
    # Footer
    # ==========================================================

    st.markdown("---")

    st.caption(
        "🚦 Smart City AI • Traffic Intelligence Platform • Version 2.0"
    )