import streamlit as st
from traffic_ai.dashboard.detection import detection as run_detection

uploaded_file = st.file_uploader(
    "Upload Image or Video",
    type=["jpg","jpeg","png","mp4","avi","mov"]
)
def detection():
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

    run_detection()

    st.markdown("---")

    st.caption(
        "🚦 Smart City AI • Traffic Intelligence Platform • Version 2.0"
    )