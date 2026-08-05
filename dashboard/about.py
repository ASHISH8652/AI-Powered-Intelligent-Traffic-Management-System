"""
About Project Page
"""

import streamlit as st


def about():

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

    st.title("ℹ About Project")

    st.markdown("""

## AI-Powered Intelligent Traffic Management System

This project combines

- YOLOv8 Vehicle Detection

- Multi Object Tracking

- Traffic Density Analysis

- Lane Analytics

- Traffic Flow Analysis

- Machine Learning Prediction

- AI Recommendation System

- Real-time Monitoring Dashboard

to create a Smart City Traffic Management Solution.

""")

    st.markdown("---")

    st.subheader("Technology Stack")

    st.markdown("""

### Artificial Intelligence

- YOLOv8

- Random Forest

- Scikit-Learn

- OpenCV

### Dashboard

- Streamlit

- Plotly

### Programming

- Python

""")

    st.markdown("---")

    st.subheader("Developer")

    st.success(

        "Ashish Kumar Prusty"

    )

    st.info(

        "B.Tech AIML"

    )

    st.markdown("---")

    st.caption(
        "🚦 Smart City AI • Traffic Intelligence Platform • Version 2.0"
    )