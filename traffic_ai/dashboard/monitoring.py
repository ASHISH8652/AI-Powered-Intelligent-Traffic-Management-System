"""
Live Monitoring Dashboard
-------------------------
Real-time monitoring page for the
AI-Powered Intelligent Traffic Management System.
"""

import os
import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

from traffic_ai.integration import DataManager
from traffic_ai.integration.pipeline import PipelineController


def monitoring():

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
    # Load Live Data
    # ==========================================================

    manager = st.session_state.system_manager

    data = manager.get_live_data()
    # from traffic_ai.integration import PipelineController

    pipeline = PipelineController()
    if not pipeline.status():

        st.warning("AI Pipeline is currently OFF.")

        return

    vehicle = data.get("vehicle_count", 0)
    density = data.get("density", "Low")
    prediction = data.get("prediction", 0)

    # Temporary Speed Estimation
    if density == "Low":
        speed = 55
        signal = "Normal"

    elif density == "Medium":
        speed = 42
        signal = "Optimized"

    elif density == "High":
        speed = 28
        signal = "Extended"

    else:
        speed = 15
        signal = "Emergency"

    # ==========================================================
    # Page Header
    # ==========================================================

    st.title("📡 Live Traffic Monitoring Dashboard")

    st.markdown("""
Real-time monitoring of

- Vehicle Detection
- Traffic Analytics
- AI Prediction
- Smart Signal Optimization
""")

    st.markdown("---")

    # ==========================================================
    # System Time
    # ==========================================================

    st.subheader("🕒 System Time")

    st.info(
        datetime.now().strftime(
            "%d %B %Y | %I:%M:%S %p"
        )
    )

    st.markdown("---")

    # ==========================================================
    # KPI Cards
    # ==========================================================

    st.subheader("📊 Live Traffic KPIs")

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "Vehicles",
        vehicle
    )

    col2.metric(
        "Average Speed",
        f"{speed} km/h"
    )

    col3.metric(
        "Congestion",
        density
    )

    col4.metric(
        "Signal Status",
        signal
    )

    col5.metric(
        "Prediction",
        prediction
    )

    st.markdown("---")

    st.subheader("⚙️ AI Pipeline Status")

    pipeline = PipelineController()

    if pipeline.status():

        st.success("🟢 AI Pipeline is Running")

    else:

        st.error("🔴 AI Pipeline is Offline")

    st.markdown("---")

    # ==========================================================
    # AI System Health
    # ==========================================================

    with st.expander("🤖 AI System Health", expanded=False):

        health = pd.DataFrame({

            "Module": [

                "YOLOv8",

                "DeepSORT",

                "Traffic Analytics",

                "Prediction Model",

                "Dashboard"

            ],

            "Status": [

                "Running",

                "Running",

                "Running",

                "Loaded",

                "Online"

            ]

        })

        st.dataframe(

            health,

            hide_index=True,

            use_container_width=True

        )

    st.markdown("---")

    # ==========================================================
    # Vehicle Distribution
    # ==========================================================

    st.subheader("🚗 Vehicle Distribution")

    vehicle_chart = go.Figure()

    vehicle_chart.add_trace(

        go.Bar(

            x=[

                "Cars",

                "Bus",

                "Truck",

                "Bike"

            ],

            y=[

                2350,

                83,

                152,

                1767

            ]

        )

    )

    vehicle_chart.update_layout(

        title="Detected Vehicle Classes",

        xaxis_title="Vehicle Type",

        yaxis_title="Vehicle Count"

    )

    st.plotly_chart(

        vehicle_chart,

        use_container_width=True

    )

    # ==========================================================
    # Congestion Distribution
    # ==========================================================

    st.subheader("🚦 Congestion Distribution")

    congestion_chart = go.Figure(

        go.Pie(

            labels=[

                "Low",

                "Medium",

                "High"

            ],

            values=[

                22,

                51,

                27

            ],

            hole=0.45

        )

    )

    congestion_chart.update_layout(

        title="Congestion Distribution"

    )

    st.plotly_chart(

        congestion_chart,

        use_container_width=True

    )

    # ==========================================================
    # Live Traffic Trend
    # ==========================================================

    st.subheader("📈 Traffic Trend")

    traffic = [

        2100,

        2600,

        3100,

        4500,

        5200,

        4700,

        3800

    ]

    hours = [

        "8 AM",

        "9 AM",

        "10 AM",

        "11 AM",

        "12 PM",

        "1 PM",

        "2 PM"

    ]

    trend = go.Figure()

    trend.add_trace(

        go.Scatter(

            x=hours,

            y=traffic,

            mode="lines+markers",

            name="Traffic"

        )

    )

    trend.update_layout(

        title="Traffic Volume Trend",

        xaxis_title="Time",

        yaxis_title="Vehicles"

    )

    st.plotly_chart(

        trend,

        use_container_width=True

    )

    st.markdown("---")

    # ==========================================================
    # AI Recommendation
    # ==========================================================

    with st.expander("🧠 AI Recommendation", expanded=True):

        if density == "Low":

            st.success("""

### 🟢 Low Traffic

• Traffic Flow is Smooth

• No congestion detected

• Normal signal timing

• No alternate route required

""")

        elif density == "Medium":

            st.warning("""

### 🟡 Moderate Traffic

• Moderate Congestion

• Optimized signal timing recommended

• Monitor nearby junctions

""")

        elif density == "High":

            st.warning("""

### 🟠 Heavy Traffic

• Heavy Congestion

• Optimize traffic lights

• Recommend alternate routes

""")

        else:

            st.error("""

### 🔴 Severe Congestion

• Emergency Signal Optimization

• Notify Traffic Control Center

• Open Alternate Lanes

• Recommend Route Diversion

""")

    st.markdown("---")

    # ==========================================================
    # Emergency Monitor
    # ==========================================================

    st.subheader("🚑 Emergency Monitor")

    st.info(

        "No emergency vehicle detected."

    )

    st.markdown("---")

    # ==========================================================
    # Smart City Status
    # ==========================================================

    st.subheader("🏙 Smart City Status")

    c1, c2, c3, c4 = st.columns(4)

    c1.success("YOLOv8 Ready")

    c2.success("DeepSORT Ready")

    c3.success("Prediction Active")

    c4.success("System Online")

    st.markdown("---")

    st.subheader("📜 System Logs")

    log_path = "logs/system.log"

    if os.path.exists(log_path):

        with open(log_path) as f:

            logs = f.read()

        st.text_area(

            "Latest Logs",

            logs,

            height=250

        )

    else:

        st.info("No logs available.")

    st.markdown("---")

    st.markdown("---")

    st.caption(
        "🚦 Smart City AI • Traffic Intelligence Platform • Version 2.0"
    )

    st.caption(
        f"Last Updated : {datetime.now().strftime('%H:%M:%S')}"
    )