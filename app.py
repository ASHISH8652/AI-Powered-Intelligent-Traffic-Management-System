"""
==========================================================
🚦 Smart City AI
Traffic Intelligence Platform
Version 2.0
==========================================================
"""

import os
import streamlit as st

# Dashboard Pages
from dashboard.home import home
from dashboard.detection import detection
from dashboard.analytics import analytics
from dashboard.prediction import prediction
from dashboard.monitoring import monitoring
from dashboard.about import about

# Integration
from traffic_ai.system import AISystemManager


# ==========================================================
# Initialize System Manager
# ==========================================================

if "system_manager" not in st.session_state:
    st.session_state.system_manager = AISystemManager()


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
# Load CSS
# ==========================================================

def load_css():

    css_file = "assets/style.css"

    if os.path.exists(css_file):

        with open(css_file) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )


load_css()


# ==========================================================
# Sidebar
# ==========================================================

with st.sidebar:

    logo = "assets/logo.png"

    if os.path.exists(logo):
        st.image(logo, use_container_width=True)

    st.title("🚦 Smart City AI")

    st.caption(
        "Traffic Intelligence Platform\n\nVersion 2.0"
    )

    st.markdown("---")

    pages = {
        "🏠 Home": home,
        "🚗 Vehicle Detection": detection,
        "📊 Analytics": analytics,
        "🤖 Prediction": prediction,
        "📡 Monitoring": monitoring,
        "ℹ About": about
    }

    page = st.radio(
        "Navigation",
        list(pages.keys())
    )

    st.markdown("---")

    st.subheader("System Status")

    st.success("🟢 YOLOv8 Loaded")

    st.success("🟢 Random Forest Loaded")

    st.success("🟢 Analytics Active")

    st.success("🟢 Dashboard Online")

    st.success("🟢 System Online")

    st.markdown("---")

    st.info(
        """
Live AI Modules

✔ Detection

✔ Analytics

✔ Prediction

✔ Monitoring
"""
    )

    st.markdown("---")

    st.caption("Developed by Ashish Kumar Prusty")


# ==========================================================
# Routing
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

c1, c2, c3 = st.columns(3)

with c1:

    st.info(
        """
🚗 Detection

YOLOv8
"""
    )

with c2:

    st.info(
        """
🤖 Prediction

Random Forest
"""
    )

with c3:

    st.info(
        """
📊 Dashboard

Streamlit + Plotly
"""
    )

st.markdown("---")

st.caption(
    "🚦 Smart City AI • Traffic Intelligence Platform • Version 2.0"
)

st.caption(
    "© 2026 Developed by Ashish Kumar Prusty"
)