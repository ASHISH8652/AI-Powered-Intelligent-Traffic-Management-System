"""
==========================================================
🚦 Smart City AI
Traffic Intelligence Platform
Version 3.0
==========================================================

Author  : Ashish Kumar Prusty
Project : AI-Powered Intelligent Traffic Management System
"""

import os
import time
import traceback
from pathlib import Path

import streamlit as st

# ==========================================================
# Dashboard Pages
# ==========================================================

from dashboard.home import home
from dashboard.detection import detection
from dashboard.analytics import analytics
from dashboard.prediction import prediction
from dashboard.monitoring import monitoring
from dashboard.about import about

# ==========================================================
# AI System
# ==========================================================

from traffic_ai.system import AISystemManager

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="🚦 Smart City AI",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Session Initialization
# ==========================================================

if "initialized" not in st.session_state:
    st.session_state.initialized = True

if "system_manager" not in st.session_state:

    with st.spinner("Initializing AI System..."):

        st.session_state.system_manager = AISystemManager()

# Shortcut Variable

system = st.session_state.system_manager

# ==========================================================
# Helper Functions
# ==========================================================

ROOT = Path(__file__).parent

ASSETS = ROOT / "assets"

LOGO = ASSETS / "logo.png"

STYLE = ASSETS / "style.css"

# ----------------------------------------------------------

def load_css():

    """
    Load custom CSS safely.
    """

    if STYLE.exists():

        with open(STYLE, encoding="utf-8") as f:

            st.markdown(

                f"<style>{f.read()}</style>",

                unsafe_allow_html=True

            )

# ----------------------------------------------------------

def show_banner():

    st.markdown(
        """
        <h1 style='text-align:center;color:#00BFFF;'>
        🚦 Smart City AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "AI Powered Intelligent Traffic Management Platform"
    )

# ----------------------------------------------------------

def health_check():

    checks = {
        "YOLOv8 Model": True,
        "Prediction Model": True,
        "Analytics Engine": True,
        "Monitoring": True,
        "Dashboard": True
    }

    return checks

# ----------------------------------------------------------

load_css()

show_banner()
# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    st.markdown("## 🚦 Smart City AI")

    if LOGO.exists():
        st.image(str(LOGO), use_container_width=True)

    st.markdown(
        """
### Traffic Intelligence Platform

AI Powered Intelligent Traffic Management System

Version **3.0**
"""
    )

    st.divider()

    # ======================================================
    # Navigation
    # ======================================================

    st.subheader("📂 Navigation")

    pages = {

        "🏠 Home": home,

        "🚗 Vehicle Detection": detection,

        "📊 Traffic Analytics": analytics,

        "🤖 Traffic Prediction": prediction,

        "📡 Live Monitoring": monitoring,

        "ℹ About": about,

    }

    page = st.radio(

        "Choose Page",

        options=list(pages.keys()),

        label_visibility="collapsed"

    )

    st.divider()

    # ======================================================
    # AI Status
    # ======================================================

    st.subheader("🤖 AI Modules")

    status = health_check()

    for module, ok in status.items():

        if ok:

            st.success(f"✅ {module}")

        else:

            st.error(f"❌ {module}")

    st.divider()

    # ======================================================
    # Project Statistics
    # ======================================================

    st.subheader("📈 Live Statistics")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(

            "Model",

            "YOLOv8"

        )

        st.metric(

            "Prediction",

            "Random Forest"

        )

    with col2:

        st.metric(

            "Status",

            "Online"

        )

        st.metric(

            "Version",

            "3.0"

        )

    st.divider()

    # ======================================================
    # Feature List
    # ======================================================

    st.subheader("🚀 Features")

    st.markdown(
        """
✅ Vehicle Detection

✅ Traffic Density Analysis

✅ Congestion Analytics

✅ Traffic Prediction

✅ Live Monitoring

✅ AI Dashboard

✅ Report Generation

✅ Smart City Ready
"""
    )

    st.divider()

    # ======================================================
    # Developer
    # ======================================================

    st.subheader("👨‍💻 Developer")

    st.write("**Ashish Kumar Prusty**")

    st.caption(
        "B.Tech AI & ML\n\nGITA Autonomous College"
    )

    st.caption(
        "AI-Powered Intelligent Traffic Management System"
    )

    st.divider()

    # ======================================================
    # Footer
    # ======================================================

    st.info(
        """
🚦 Smart City AI

Version 3.0

Powered by

YOLOv8 • Streamlit • Python
"""
    )
# ==========================================================
# Main Routing
# ==========================================================

try:

    pages[page]()

except Exception as e:

    st.error("⚠️ Application Error")

    st.exception(e)


# ==========================================================
# Footer
# ==========================================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:

    st.info(
        """
🚗 Vehicle Detection

YOLOv8
"""
    )

with col2:

    st.info(
        """
🤖 Traffic Prediction

Random Forest
"""
    )

with col3:

    st.info(
        """
📊 Dashboard

Streamlit + Plotly
"""
    )

st.markdown("---")

st.subheader("📈 System Health")

health1, health2, health3, health4 = st.columns(4)

with health1:
    st.metric(
        "Detection",
        "Ready",
    )

with health2:
    st.metric(
        "Analytics",
        "Ready",
    )

with health3:
    st.metric(
        "Prediction",
        "Ready",
    )

with health4:
    st.metric(
        "Monitoring",
        "Ready",
    )

st.markdown("---")

st.caption(
    "🚦 Smart City AI • AI-Powered Intelligent Traffic Management System"
)

st.caption(
    "Developed using Computer Vision, Machine Learning, Data Analytics and Streamlit"
)

st.caption(
    "© 2026 Ashish Kumar Prusty | GITA Autonomous College | AI & ML"
)
