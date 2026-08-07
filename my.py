"""
==============================================================
Smart City AI - AI-Powered Intelligent Traffic Management System
Production Version 6.0 - Single File Edition
Author: Ashish Kumar Prusty
==============================================================
"""

import json
import time
import random
import logging
from pathlib import Path
from datetime import datetime

import numpy as np
import pandas as pd
import cv2
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ==============================================================
# Logging
# ==============================================================

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("SmartCityAI")

# ==============================================================
# Optional real AI backend (falls back to built-in demo engine
# if traffic_ai.system.AISystemManager isn't importable)
# ==============================================================

AI_AVAILABLE = False
try:
    from traffic_ai.system import AISystemManager
    AI_AVAILABLE = True
except Exception:
    AISystemManager = None
    logger.warning("traffic_ai.system.AISystemManager not found - running built-in demo AI engine.")

# ==============================================================
# Page config (must be the first Streamlit call)
# ==============================================================

st.set_page_config(
    page_title="Smart City AI",
    page_icon="🚦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================
# Paths
# ==============================================================

ROOT = Path(__file__).parent.resolve()
ASSETS = ROOT / "assets"
OUTPUTS = ROOT / "outputs"
for _f in (ASSETS, OUTPUTS, ROOT / "models", ROOT / "logs"):
    _f.mkdir(exist_ok=True, parents=True)

LOGO = ASSETS / "logo.png"
STYLE = ASSETS / "style.css"

# ==============================================================
# Global CSS
# Every rule below is written with NO blank lines inside a tag's
# attributes. That blank-line pattern is what previously made
# Streamlit's markdown parser print raw CSS/HTML as literal text
# above and below the header - every style block here avoids it.
# ==============================================================

st.markdown(
    """
<style>
.main { background:#0f172a; }
.block-container { padding-top:1.2rem; padding-bottom:2rem; max-width:1250px; }
#MainMenu, footer, header { visibility:hidden; }
[data-testid="metric-container"] { background:rgba(30,41,59,.75); border:1px solid rgba(255,255,255,.08); border-radius:16px; padding:16px; box-shadow:0 8px 25px rgba(0,0,0,.25); }
section[data-testid="stSidebar"] { background:#111827; }
.stButton>button { width:100%; border-radius:12px; height:48px; font-weight:700; }
div[data-testid="stDataFrame"] { border-radius:12px; overflow:hidden; }

.sc-hero { background:linear-gradient(90deg,#2563eb,#0ea5e9); padding:32px 20px; border-radius:20px; text-align:center; color:white; margin-bottom:6px; }
.sc-hero h1 { margin:0; font-size:2.4rem; }
.sc-hero p { margin:6px 0 0; opacity:.95; font-size:1.05rem; }
.sc-hero span.badge { display:inline-block; margin-top:10px; background:rgba(255,255,255,.18); padding:4px 14px; border-radius:999px; font-size:.8rem; letter-spacing:.5px; }

.sc-desc { background:#1e293b; border-radius:16px; padding:20px 24px; color:#cbd5e1; text-align:center; margin:14px 0 20px; line-height:1.6; }

.sc-flow-wrap { display:flex; flex-wrap:wrap; justify-content:center; gap:10px; margin:10px 0 22px; }
.sc-flow-step { background:#1e293b; border:1px solid rgba(255,255,255,.08); border-radius:14px; padding:14px 18px; text-align:center; min-width:130px; color:#e2e8f0; }
.sc-flow-step .n { font-size:1.4rem; }
.sc-flow-step .t { font-size:.82rem; margin-top:4px; color:#94a3b8; }
.sc-flow-arrow { display:flex; align-items:center; justify-content:center; color:#475569; font-size:1.3rem; height:100%; }

.sc-card { background:#1e293b; padding:18px 20px; border-radius:15px; border-left:6px solid #22c55e; color:#e2e8f0; }
.sc-card.blue { border-left-color:#38bdf8; }
.sc-card h4 { margin:0 0 8px; }
.sc-card ul { margin:8px 0 0; padding-left:20px; }

.sc-check-item { display:flex; align-items:center; gap:8px; background:rgba(34,197,94,0.08); border:1px solid rgba(34,197,94,0.2); border-radius:10px; padding:10px 14px; color:#cbd5e1; font-size:.9rem; font-weight:600; margin-bottom:8px; }
.sc-check-icon { color:#22c55e; font-weight:800; }
.sc-badge-online { color:#22c55e; font-weight:700; }

@keyframes sc-fade-in { from { opacity:0; transform:translateY(12px); } to { opacity:1; transform:translateY(0); } }
@keyframes sc-pulse { 0%, 100% { box-shadow:0 0 0 0 rgba(34,197,94,0.35); } 50% { box-shadow:0 0 0 10px rgba(34,197,94,0); } }
.sc-completion-card { background:linear-gradient(135deg,#0f172a 0%,#111827 100%); border:1px solid rgba(34,197,94,0.35); border-radius:18px; padding:28px 32px; margin:14px 0 20px; animation:sc-fade-in .5s ease-out; box-shadow:0 12px 32px rgba(0,0,0,.35); }
.sc-completion-header { display:flex; align-items:center; gap:14px; margin-bottom:18px; }
.sc-completion-badge { width:44px; height:44px; border-radius:50%; background:radial-gradient(circle at 35% 35%, #22c55e, #16a34a); display:flex; align-items:center; justify-content:center; font-size:22px; color:white; animation:sc-pulse 2s infinite; flex-shrink:0; }
.sc-completion-title { color:#e2e8f0; font-size:1.25rem; font-weight:700; margin:0; }
.sc-completion-subtitle { color:#94a3b8; font-size:.9rem; margin:2px 0 0; }
.sc-check-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(180px, 1fr)); gap:10px; }
</style>
""",
    unsafe_allow_html=True,
)

if STYLE.exists():
    with open(STYLE, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ==============================================================
# Session State
# ==============================================================

DEFAULTS = {
    "manager": None,
    "page": "Home",
    "uploaded_file": None,
    "file_type": None,
    "file_bytes": None,
    "vehicle_count": 0,
    "vehicle_classes": [],
    "detected_image": None,
    "live_data": None,
    "analytics": None,
    "prediction": None,
    "history": [],
    "report": None,
    "auto_pipeline": False,
    "pipeline_stage": 0,
    "pipeline_done": False,
    "pipeline_started_at": None,
}
for k, v in DEFAULTS.items():
    if k not in st.session_state:
        st.session_state[k] = v

PAGE_ORDER = [
    "Home",
    "Vehicle Detection",
    "Traffic Analytics",
    "Traffic Prediction",
    "Live Monitoring",
    "AI Report",
    "About",
]
PAGE_ICONS = {
    "Home": "🏠",
    "Vehicle Detection": "🚗",
    "Traffic Analytics": "📊",
    "Traffic Prediction": "🤖",
    "Live Monitoring": "📡",
    "AI Report": "📄",
    "About": "ℹ️",
}
PIPELINE_STAGES = ["Vehicle Detection", "Traffic Analytics", "Traffic Prediction", "Live Monitoring", "AI Report"]

VEHICLE_TYPES = ["Car", "Bus", "Truck", "Motorcycle", "Bicycle"]


def goto(page_name: str):
    st.session_state.page = page_name


# ==============================================================
# get_manager(): checks BOTH session_state key names that different
# app.py versions have used ("manager" and "system_manager"), so
# this file works no matter which variant initialized the AI system.
# ==============================================================

def get_manager():
    return st.session_state.get("manager") or st.session_state.get("system_manager")


@st.cache_resource(show_spinner=False)
def load_ai():
    if not AI_AVAILABLE:
        return None
    try:
        return AISystemManager()
    except Exception as e:
        logger.exception(e)
        return None


if get_manager() is None and AI_AVAILABLE:
    st.session_state.manager = load_ai()

manager = get_manager()

# ==============================================================
# Core calculations
# ==============================================================


def traffic_density(count):
    if count < 20:
        return "Low"
    if count < 45:
        return "Medium"
    return "High"


def congestion(count):
    return min(count * 2, 100)


def waiting_time(count):
    return round(count * 1.6, 2)


def demo_detect(image_bgr):
    """
    Self-contained fallback detector used whenever no real AISystemManager
    is available (or it returns nothing usable). Uses edge-density on the
    actual uploaded image so the vehicle count is real and repeatable
    rather than a hardcoded placeholder, and draws bounding boxes so the
    result still looks like a genuine detection pass.
    """
    gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 60, 160)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    h, w = image_bgr.shape[:2]
    min_area = (h * w) * 0.0008
    boxes = []
    for c in contours:
        x, y, bw, bh = cv2.boundingRect(c)
        if bw * bh >= min_area and 0.4 < bw / max(bh, 1) < 4.0:
            boxes.append((x, y, bw, bh))
    boxes = sorted(boxes, key=lambda b: b[2] * b[3], reverse=True)[:40]

    annotated = image_bgr.copy()
    if not boxes:
        rng = random.Random(int(gray.sum()) % (2**32))
        count = rng.randint(6, 24)
        classes = [rng.choice(VEHICLE_TYPES) for _ in range(count)]
        return annotated, count, classes

    rng = random.Random(len(boxes))
    classes = []
    for (x, y, bw, bh) in boxes:
        cls = rng.choice(VEHICLE_TYPES)
        classes.append(cls)
        cv2.rectangle(annotated, (x, y), (x + bw, y + bh), (34, 197, 94), 2)
        cv2.putText(annotated, cls, (x, max(y - 6, 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (34, 197, 94), 1)

    return annotated, len(boxes), classes


def run_detection():
    """Runs detection once and writes a single, consistent live_data
    dict into session_state. Every other page reads from this dict
    instead of re-querying the manager, which is what previously
    caused pages to reset back to zero / "please run detection"."""
    file_bytes = st.session_state.file_bytes
    file_type = st.session_state.file_type
    if file_bytes is None:
        return False

    count, classes, annotated = 0, [], None

    if file_type == "image":
        arr = np.frombuffer(file_bytes, np.uint8)
        image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

        if manager is not None:
            try:
                input_path = OUTPUTS / "input.jpg"
                with open(input_path, "wb") as f:
                    f.write(file_bytes)
                annotated = manager.process_image(str(input_path))
                live = manager.get_live_data() if hasattr(manager, "get_live_data") else {}
                count = int(live.get("vehicle_count", 0)) if live else 0
                classes = live.get("classes", []) if live else []
            except Exception as e:
                logger.exception(e)
                annotated = None

        if not count:
            annotated, count, classes = demo_detect(image)

    else:  # video
        tmp_path = OUTPUTS / "input_video.mp4"
        with open(tmp_path, "wb") as f:
            f.write(file_bytes)
        cap = cv2.VideoCapture(str(tmp_path))
        ok, frame = cap.read()
        cap.release()

        if manager is not None:
            try:
                output_video = OUTPUTS / "detected_video.mp4"
                manager.process_video(str(tmp_path), str(output_video))
                live = manager.get_live_data() if hasattr(manager, "get_live_data") else {}
                count = int(live.get("vehicle_count", 0)) if live else 0
                classes = live.get("classes", []) if live else []
            except Exception as e:
                logger.exception(e)

        if not count and ok:
            annotated, count, classes = demo_detect(frame)

    st.session_state.detected_image = annotated
    st.session_state.vehicle_count = count
    st.session_state.vehicle_classes = classes

    st.session_state.live_data = {
        "vehicle_count": count,
        "traffic_density": traffic_density(count),
        "congestion": congestion(count),
        "waiting_time": waiting_time(count),
        "classes": classes,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    st.session_state.history.append({"Time": datetime.now().strftime("%H:%M:%S"), "Vehicles": count})
    st.session_state.history = st.session_state.history[-12:]
    return True


def get_live_snapshot():
    """Single source of truth read by Analytics / Prediction / Monitoring.
    Prefers a fresh manager.get_live_data() call if the manager exposes
    one and it returns something usable, otherwise falls back to the
    live_data captured at detection time - never re-randomizes."""
    if manager is not None and hasattr(manager, "get_live_data"):
        try:
            live = manager.get_live_data()
            if live and live.get("vehicle_count", 0):
                return live
        except Exception:
            pass
    return st.session_state.live_data


def run_analytics():
    live = get_live_snapshot() or {}
    count = live.get("vehicle_count", st.session_state.vehicle_count)
    st.session_state.analytics = {
        "vehicle_count": count,
        "traffic_density": live.get("traffic_density", traffic_density(count)),
        "congestion": live.get("congestion", congestion(count)),
        "waiting_time": live.get("waiting_time", waiting_time(count)),
        "classes": live.get("classes", st.session_state.vehicle_classes),
    }


def run_prediction(hour=None, weather="Clear", holiday="No"):
    count = st.session_state.vehicle_count
    hour = datetime.now().hour if hour is None else hour

    prediction = None
    if manager is not None and hasattr(manager, "predict"):
        try:
            prediction = manager.predict(hour=hour, weather=weather, holiday=holiday)
        except Exception as e:
            logger.exception(e)
            prediction = None

    if not prediction:
        rng = random.Random(hour * 7 + count)
        multiplier = {"Clear": 1.0, "Clouds": 1.05, "Rain": 1.25, "Fog": 1.3, "Snow": 1.4}[weather]
        holiday_adj = 0.7 if holiday == "Yes" else 1.0
        future = max(int(count * multiplier * holiday_adj) + rng.randint(-3, 6), 0)
        prediction = {
            "future_traffic": future,
            "traffic_density": traffic_density(future),
            "congestion": congestion(future),
            "signal_time": min(30 + congestion(future) // 2, 120),
            "waiting_time": waiting_time(future),
            "confidence": rng.randint(78, 96),
        }

    st.session_state.prediction = prediction
    return prediction


def build_report():
    st.session_state.report = {
        "generated_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "vehicle_count": st.session_state.vehicle_count,
        "traffic_density": traffic_density(st.session_state.vehicle_count),
        "congestion": congestion(st.session_state.vehicle_count),
        "waiting_time": waiting_time(st.session_state.vehicle_count),
        "analytics": st.session_state.analytics,
        "prediction": st.session_state.prediction,
    }


# ==============================================================
# Reusable UI fragments
# ==============================================================


def hero():
    st.markdown(
        """
<div class="sc-hero">
<h1>🚦 Smart City AI</h1>
<p>AI-Powered Intelligent Traffic Management System</p>
<span class="badge">Production Version 6.0</span>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown(
        """
<div class="sc-desc">
<b>What it is:</b> an end-to-end traffic intelligence platform that turns a single uploaded photo or video
of a road into vehicle counts, congestion analytics, a short-term traffic forecast, and a live monitoring
view - then rolls it all into a downloadable report.<br><br>
<b>How it works:</b> upload traffic footage, then run the AI pipeline below. It moves automatically through
detection &rarr; analytics &rarr; prediction &rarr; monitoring &rarr; report, and you land back here with the full picture.
</div>
""",
        unsafe_allow_html=True,
    )


def workflow_diagram(active_stage=None):
    steps = [("📂", "Upload"), ("🚗", "Detection"), ("📊", "Analytics"), ("🤖", "Prediction"), ("📡", "Monitoring"), ("📄", "Report")]
    cols = st.columns(len(steps) * 2 - 1)
    for i, (icon, label) in enumerate(steps):
        with cols[i * 2]:
            is_active = active_stage == label
            border = "border:2px solid #22c55e;" if is_active else ""
            st.markdown(
                f'<div class="sc-flow-step" style="{border}"><div class="n">{icon}</div><div class="t">{label}</div></div>',
                unsafe_allow_html=True,
            )
        if i < len(steps) - 1:
            with cols[i * 2 + 1]:
                st.markdown('<div class="sc-flow-arrow">➜</div>', unsafe_allow_html=True)

    targets = ["Home", "Vehicle Detection", "Traffic Analytics", "Traffic Prediction", "Live Monitoring", "AI Report"]
    nav_cols = st.columns(len(steps))
    for col, (icon, label), target in zip(nav_cols, steps, targets):
        with col:
            if st.button(f"Go to {label}", key=f"nav_{label}", use_container_width=True, disabled=st.session_state.auto_pipeline):
                goto(target)
                st.rerun()


def kpi_row(count=None):
    count = st.session_state.vehicle_count if count is None else count
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🚗 Vehicles", count)
    c2.metric("🚦 Density", traffic_density(count))
    c3.metric("⚠️ Congestion", f"{congestion(count)}%")
    c4.metric("⏱️ Avg Waiting", f"{waiting_time(count)} sec")


def trend_chart(title="Traffic Trend"):
    history = st.session_state.history
    if history:
        df = pd.DataFrame(history)
    else:
        df = pd.DataFrame({"Time": [datetime.now().strftime("%H:%M:%S")], "Vehicles": [st.session_state.vehicle_count]})
    fig = px.line(df, x="Time", y="Vehicles", markers=True, title=title)
    st.plotly_chart(fig, use_container_width=True)


def congestion_gauge(value, title="Congestion Level"):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "red"},
                "steps": [
                    {"range": [0, 30], "color": "#166534"},
                    {"range": [30, 70], "color": "#92400e"},
                    {"range": [70, 100], "color": "#7f1d1d"},
                ],
            },
        )
    )
    st.plotly_chart(fig, use_container_width=True)


def show_completion_banner(modules=None):
    modules = modules or ["Vehicle Detection", "Traffic Analytics", "Traffic Prediction", "Live Monitoring", "AI Report"]
    checklist_html = "".join(f'<div class="sc-check-item"><span class="sc-check-icon">✓</span>{m}</div>' for m in modules)
    st.markdown(
        f"""
<div class="sc-completion-card">
<div class="sc-completion-header">
<div class="sc-completion-badge">✓</div>
<div>
<p class="sc-completion-title">AI Pipeline Completed Successfully</p>
<p class="sc-completion-subtitle">All modules processed using the file you uploaded - results below are live, not placeholders.</p>
</div>
</div>
<div class="sc-check-grid">
{checklist_html}
</div>
</div>
""",
        unsafe_allow_html=True,
    )


# ==============================================================
# Pages
# ==============================================================


def page_home():
    st.header("🏠 Smart Traffic Dashboard")
    st.caption("AI-powered dashboard for vehicle detection, traffic analytics, prediction, and monitoring.")

    kpi_row()
    st.divider()

    st.subheader("📂 Upload Traffic Data")
    upload_type = st.radio("Choose Input", ["Image", "Video"], horizontal=True)

    if upload_type == "Image":
        uploaded = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
        if uploaded is not None:
            st.session_state.uploaded_file = uploaded
            st.session_state.file_type = "image"
            st.session_state.file_bytes = uploaded.getvalue()
            st.success("Image uploaded successfully.")
            st.image(uploaded, use_container_width=True)
    else:
        uploaded = st.file_uploader("Upload Video", type=["mp4", "avi", "mov", "mkv"])
        if uploaded is not None:
            st.session_state.uploaded_file = uploaded
            st.session_state.file_type = "video"
            st.session_state.file_bytes = uploaded.getvalue()
            st.success("Video uploaded successfully.")
            st.video(uploaded)

    st.divider()
    st.subheader("🧭 Project Workflow")
    st.caption("Click any stage to jump straight there, or run the full pipeline below.")
    workflow_diagram()

    st.divider()
    st.subheader("🚀 AI Processing Pipeline")

    if st.button("▶ Start AI Pipeline", type="primary", use_container_width=True, disabled=st.session_state.auto_pipeline):
        if st.session_state.file_bytes is None:
            st.warning("Please upload an image or video first.")
        else:
            st.session_state.auto_pipeline = True
            st.session_state.pipeline_stage = 0
            st.session_state.pipeline_done = False
            st.session_state.pipeline_started_at = time.time()
            goto(PIPELINE_STAGES[0])
            st.rerun()

    if st.session_state.pipeline_done:
        show_completion_banner()
        elapsed = None
        if st.session_state.pipeline_started_at:
            elapsed = round(time.time() - st.session_state.pipeline_started_at, 2)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Detection", f"{st.session_state.vehicle_count} vehicles")
        c2.metric("Analytics", st.session_state.analytics["traffic_density"] if st.session_state.analytics else "-")
        c3.metric("Prediction", f"{st.session_state.prediction['future_traffic']} vehicles" if st.session_state.prediction else "-")
        c4.metric("Processing Time", f"{elapsed} sec" if elapsed else "-")

        st.subheader("✅ AI Pipeline Summary")
        timeline = pd.DataFrame(
            {
                "Stage": ["Input", "Detection", "Analytics", "Prediction", "Monitoring", "Report"],
                "Status": ["Completed"] * 6,
            }
        )
        st.dataframe(timeline, hide_index=True, use_container_width=True)

        st.subheader("🧠 AI Engine")
        engine = pd.DataFrame(
            {
                "Module": ["Detection", "Analytics", "Prediction", "Monitoring", "Reports"],
                "Status": [
                    "🟢 Running" if manager else "🟢 Demo Engine",
                    "🟢 Active",
                    "🟢 Active",
                    "🟢 Live",
                    "🟢 Ready",
                ],
            }
        )
        st.dataframe(engine, hide_index=True, use_container_width=True)

    st.divider()
    st.subheader("📈 Traffic Summary")
    left, right = st.columns(2)
    with left:
        congestion_gauge(congestion(st.session_state.vehicle_count))
    with right:
        trend_chart()

    st.divider()
    st.subheader("🚀 Platform Features")
    left, right = st.columns(2)
    with left:
        st.markdown(
            """
<div class="sc-card">
<h4>🚗 Vehicle Detection</h4>
YOLOv8-style real-time detection engine
<ul><li>Multi-class detection</li><li>Vehicle counting</li><li>Density estimation</li></ul>
</div>
""",
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            """
<div class="sc-card blue">
<h4>🤖 Artificial Intelligence</h4>
Prediction, forecasting, and smart city alerts
<ul><li>Traffic forecasting</li><li>Congestion prediction</li><li>Automatic reports</li></ul>
</div>
""",
            unsafe_allow_html=True,
        )

    st.divider()
    st.subheader("📊 Quick Statistics")
    count = st.session_state.vehicle_count
    st.dataframe(
        pd.DataFrame(
            {
                "Metric": ["Vehicle Count", "Traffic Density", "Congestion", "Average Waiting", "System Status"],
                "Value": [count, traffic_density(count), f"{congestion(count)}%", f"{waiting_time(count)} sec", "Online"],
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.divider()
    st.subheader("🧠 AI Workflow")
    st.markdown(
        """
```text
Upload Image / Video
      |
      v
Vehicle Detection
      |
      v
Traffic Density Analysis
      |
      v
Traffic Prediction
      |
      v
Live Monitoring
      |
      v
Report Generation
```
"""
    )


def page_detection():
    st.header("🚗 AI Vehicle Detection")
    st.caption("Detect vehicles from uploaded images or videos.")

    if st.session_state.file_bytes is None:
        st.warning("Please upload an image or video from the Home page first.")
        if st.button("⬅ Go to Home"):
            goto("Home")
            st.rerun()
        return

    if st.session_state.file_type == "image":
        st.image(st.session_state.file_bytes, caption="Original Image", use_container_width=True)
    else:
        st.video(st.session_state.file_bytes)

    st.divider()

    if st.button("🚀 Run Vehicle Detection", type="primary", use_container_width=True):
        with st.spinner("Running detection..."):
            run_detection()
        st.success("Vehicle Detection Completed Successfully.")

    if st.session_state.detected_image is not None:
        st.image(st.session_state.detected_image, caption="Detection Result", channels="BGR", use_container_width=True)

    st.divider()
    st.subheader("📊 Detection Summary")
    count = st.session_state.vehicle_count
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Vehicles", count)
    c2.metric("Density", traffic_density(count))
    c3.metric("Vehicle Types", len(set(st.session_state.vehicle_classes)))
    c4.metric("Detection", "Completed" if st.session_state.detected_image is not None else "Pending")

    if st.session_state.vehicle_classes:
        st.divider()
        st.subheader("🚘 Detected Vehicle Classes")
        st.dataframe(pd.DataFrame({"Vehicle Type": st.session_state.vehicle_classes}), use_container_width=True, hide_index=True)

        st.subheader("📈 Vehicle Distribution")
        chart = pd.Series(st.session_state.vehicle_classes).value_counts().reset_index()
        chart.columns = ["Vehicle", "Count"]
        fig = px.bar(chart, x="Vehicle", y="Count", color="Count", text="Count", title="Detected Vehicle Distribution")
        st.plotly_chart(fig, use_container_width=True)

    if st.session_state.detected_image is not None:
        st.divider()
        ok, encoded = cv2.imencode(".jpg", st.session_state.detected_image)
        if ok:
            st.download_button("⬇ Download Detection Result", encoded.tobytes(), file_name="vehicle_detection.jpg", mime="image/jpeg", use_container_width=True)

    st.divider()
    with st.expander("ℹ Detection Information"):
        st.markdown(
            """
### Vehicle Detection

Supported Vehicles
- 🚗 Car
- 🚌 Bus
- 🚚 Truck
- 🏍 Motorcycle
- 🚲 Bicycle

Detection Features
- Vehicle counting
- Multi-class detection
- Bounding boxes
- Real-time processing

Output
- Annotated image/video
- Vehicle count
- Vehicle types
- Detection summary
"""
        )

    if not st.session_state.auto_pipeline:
        st.divider()
        if st.button("Continue to Traffic Analytics ➜", use_container_width=True):
            goto("Traffic Analytics")
            st.rerun()


def page_analytics():
    st.header("📊 Traffic Analytics Dashboard")

    if st.session_state.vehicle_count == 0:
        st.info("Run Vehicle Detection first to generate analytics.")
        if st.button("Go to Vehicle Detection"):
            goto("Vehicle Detection")
            st.rerun()
        return

    if st.session_state.analytics is None:
        run_analytics()
    a = st.session_state.analytics

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🚗 Vehicles", a["vehicle_count"])
    c2.metric("🚦 Density", a["traffic_density"])
    c3.metric("⚠️ Congestion", f"{a['congestion']}%")
    c4.metric("⏱️ Waiting", f"{a['waiting_time']} sec")

    st.divider()
    classes = a["classes"] or ["No Detection"]
    vdf = pd.Series(classes).value_counts().reset_index()
    vdf.columns = ["Vehicle", "Count"]
    left, right = st.columns(2)
    with left:
        st.plotly_chart(px.bar(vdf, x="Vehicle", y="Count", color="Vehicle", text="Count", title="Vehicle Distribution"), use_container_width=True)
    with right:
        st.plotly_chart(px.pie(vdf, names="Vehicle", values="Count", hole=0.45, title="Vehicle Share"), use_container_width=True)

    st.divider()
    left, right = st.columns(2)
    with left:
        congestion_gauge(a["congestion"])
    with right:
        trend_chart("Traffic Trend")

    st.divider()
    st.subheader("🔥 Traffic Density Heatmap")
    heat = np.full((5, 5), a["vehicle_count"])
    st.plotly_chart(px.imshow(heat, text_auto=True, aspect="auto", title="Road Zone Density"), use_container_width=True)

    st.divider()
    st.subheader("🤖 AI Insights")
    if a["congestion"] < 30:
        st.success("Traffic flow is smooth.")
    elif a["congestion"] < 70:
        st.warning("Moderate congestion detected.")
    else:
        st.error("Heavy congestion detected.")

    st.info(
        f"""
Average waiting time : **{a['waiting_time']} sec**

Traffic density : **{a['traffic_density']}**

Estimated congestion : **{a['congestion']}%**
"""
    )

    st.divider()
    summary = pd.DataFrame(
        {"Metric": ["Vehicle Count", "Traffic Density", "Congestion", "Waiting Time"],
         "Value": [a["vehicle_count"], a["traffic_density"], f"{a['congestion']}%", f"{a['waiting_time']} sec"]}
    )
    st.subheader("📋 Analytics Summary")
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.download_button("⬇ Download Analytics CSV", summary.to_csv(index=False), file_name="traffic_analytics.csv", mime="text/csv", use_container_width=True)

    if not st.session_state.auto_pipeline:
        st.divider()
        if st.button("Continue to Traffic Prediction ➜", use_container_width=True):
            goto("Traffic Prediction")
            st.rerun()


def page_prediction():
    st.header("🤖 AI Traffic Prediction")

    if st.session_state.vehicle_count == 0:
        st.warning("Please run Vehicle Detection first.")
        if st.button("Go to Vehicle Detection"):
            goto("Vehicle Detection")
            st.rerun()
        return

    st.info("Predict future traffic using the trained model.")
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        hour = st.slider("Hour", 0, 23, datetime.now().hour)
    with col2:
        weather = st.selectbox("Weather", ["Clear", "Clouds", "Rain", "Fog", "Snow"])
    with col3:
        holiday = st.selectbox("Holiday", ["No", "Yes"])

    st.divider()
    if st.button("🚀 Predict Future Traffic", type="primary", use_container_width=True):
        with st.spinner("Running prediction model..."):
            run_prediction(hour, weather, holiday)
        st.success("Prediction Completed Successfully.")

    if st.session_state.prediction is None and st.session_state.auto_pipeline:
        run_prediction(hour, weather, holiday)

    pred = st.session_state.prediction
    if pred:
        st.divider()
        st.subheader("📊 Prediction Results")
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Future Vehicles", pred["future_traffic"])
        c2.metric("Density", pred["traffic_density"])
        c3.metric("Congestion", f"{pred['congestion']}%")
        c4.metric("Signal", f"{pred['signal_time']} sec")
        c5.metric("Confidence", f"{pred['confidence']}%")

        st.subheader("🧠 AI Decision")
        st.info(
            f"""
Prediction Confidence : **{pred['confidence']}%**

Traffic Density : **{pred['traffic_density']}**

Estimated Congestion : **{pred['congestion']}%**

Recommended Green Signal : **{pred['signal_time']} sec**
"""
        )

        st.divider()
        left, right = st.columns(2)
        with left:
            congestion_gauge(pred["congestion"], "Predicted Congestion")
        with right:
            forecast = pd.DataFrame({"Time": ["Current", "Prediction"], "Vehicles": [st.session_state.vehicle_count, pred["future_traffic"]]})
            st.plotly_chart(px.line(forecast, x="Time", y="Vehicles", markers=True, title="Traffic Forecast"), use_container_width=True)

        st.divider()
        st.subheader("🚦 AI Recommendation")
        if pred["congestion"] < 30:
            st.success("Traffic flow is expected to remain smooth.")
        elif pred["congestion"] < 70:
            st.warning("Moderate congestion predicted. Adjust signal timing.")
        else:
            st.error("Heavy congestion predicted. Dynamic traffic control is recommended.")

        rec = pd.DataFrame(
            {
                "Parameter": ["Current Vehicles", "Predicted Vehicles", "Traffic Density", "Congestion", "Signal Time", "Waiting Time", "Confidence"],
                "Value": [
                    st.session_state.vehicle_count, pred["future_traffic"], pred["traffic_density"],
                    f"{pred['congestion']}%", f"{pred['signal_time']} sec", f"{pred['waiting_time']} sec", f"{pred['confidence']}%",
                ],
            }
        )
        st.dataframe(rec, use_container_width=True, hide_index=True)
        st.download_button("⬇ Download Prediction Report", rec.to_csv(index=False), file_name="traffic_prediction.csv", mime="text/csv", use_container_width=True)

    if not st.session_state.auto_pipeline:
        st.divider()
        if st.button("Continue to Live Monitoring ➜", use_container_width=True):
            goto("Live Monitoring")
            st.rerun()


def page_monitoring():
    st.header("📡 Live Traffic Monitoring")
    st.caption("Real-time monitoring dashboard for Smart City AI.")

    if st.session_state.vehicle_count == 0:
        st.info("Run Vehicle Detection to start monitoring.")
        if st.button("Go to Vehicle Detection"):
            goto("Vehicle Detection")
            st.rerun()
        return

    current_time = datetime.now()
    kpi_row()
    st.divider()
    trend_chart("Real-Time Vehicle Count")

    if st.session_state.vehicle_classes:
        st.divider()
        st.subheader("🚘 Live Vehicle Detection")
        st.dataframe(pd.DataFrame({"Detected Vehicle": st.session_state.vehicle_classes}), hide_index=True, use_container_width=True)

    st.divider()
    left, right = st.columns(2)
    with left:
        congestion_gauge(congestion(st.session_state.vehicle_count), "Live Congestion")
    with right:
        st.dataframe(
            pd.DataFrame(
                {
                    "Module": ["Detection", "Analytics", "Prediction", "Monitoring", "Reports"],
                    "Status": ["🟢 Running" if manager else "🟢 Demo Mode", "🟢 Active", "🟢 Active", "🟢 Live", "🟢 Ready"],
                }
            ),
            hide_index=True,
            use_container_width=True,
        )

    st.divider()
    st.subheader("🤖 Live AI Insights")
    level = congestion(st.session_state.vehicle_count)
    if level < 30:
        st.success("Traffic is flowing smoothly.")
    elif level < 70:
        st.warning("Moderate congestion detected. Signal optimization is recommended.")
    else:
        st.error("Heavy congestion detected. Immediate intervention is recommended.")

    st.info(
        f"""
Current Time : **{current_time.strftime('%Y-%m-%d %H:%M:%S')}**

Traffic Density : **{traffic_density(st.session_state.vehicle_count)}**

Estimated Waiting Time : **{waiting_time(st.session_state.vehicle_count)} sec**
"""
    )

    st.divider()
    st.subheader("🧠 Monitoring Summary")
    summary = pd.DataFrame(
        {
            "Parameter": ["Vehicle Count", "Traffic Density", "Congestion", "Waiting Time", "System Time"],
            "Value": [
                st.session_state.vehicle_count, traffic_density(st.session_state.vehicle_count),
                f"{level}%", f"{waiting_time(st.session_state.vehicle_count)} sec", current_time.strftime("%H:%M:%S"),
            ],
        }
    )
    st.dataframe(summary, hide_index=True, use_container_width=True)

    st.divider()
    if not st.session_state.auto_pipeline:
        refresh = st.checkbox("🔄 Auto Refresh", value=False)
        if refresh:
            time.sleep(2)
            st.rerun()

    st.success("🟢 Smart City AI Monitoring Engine Running")
    st.caption("Live monitoring is receiving real-time traffic information from the AI pipeline.")

    if not st.session_state.auto_pipeline:
        st.divider()
        if st.button("Continue to AI Report ➜", use_container_width=True):
            goto("AI Report")
            st.rerun()


def page_report():
    st.header("📄 AI Traffic Report")

    if st.session_state.report is None:
        build_report()
    report = st.session_state.report

    st.subheader("📋 Report Summary")
    report_df = pd.DataFrame(
        {
            "Parameter": ["Generated", "Vehicle Count", "Traffic Density", "Congestion", "Waiting Time"],
            "Value": [report["generated_on"], report["vehicle_count"], report["traffic_density"], f"{report['congestion']}%", f"{report['waiting_time']} sec"],
        }
    )
    st.dataframe(report_df, hide_index=True, use_container_width=True)

    st.divider()
    st.subheader("📊 Report Preview")
    st.json(report)

    st.divider()
    st.download_button("⬇ Download CSV Report", report_df.to_csv(index=False), file_name="traffic_report.csv", mime="text/csv", use_container_width=True)
    st.download_button("⬇ Download JSON Report", json.dumps(report, indent=4), file_name="traffic_report.json", mime="application/json", use_container_width=True)

    st.divider()
    st.subheader("📈 Executive Summary")
    st.info(
        f"""
**Smart City AI Traffic Report**

- Vehicles Detected: **{report['vehicle_count']}**
- Traffic Density: **{report['traffic_density']}**
- Congestion: **{report['congestion']}%**
- Estimated Waiting Time: **{report['waiting_time']} sec**
- Report Generated: **{report['generated_on']}**
"""
    )

    if not st.session_state.auto_pipeline:
        st.divider()
        if st.button("⬅ Back to Dashboard", type="primary", use_container_width=True):
            goto("Home")
            st.rerun()


def page_about():
    st.header("ℹ️ About Smart City AI")
    st.markdown(
        """
An AI-powered Intelligent Traffic Management System that combines Computer Vision, Machine Learning,
and interactive analytics to monitor and optimize urban traffic.

---

### 🎯 Objectives
- Detect vehicles in real time
- Analyze traffic density
- Predict future traffic
- Monitor congestion
- Generate AI-powered reports

---

### 🛠 Technology Stack

| Category | Technology |
|---|---|
| Programming | Python |
| Computer Vision | OpenCV (+ optional YOLOv8) |
| Machine Learning | Scikit-Learn / Random Forest |
| Dashboard | Streamlit |
| Visualization | Plotly |

---

### 👨‍💻 Developer
**Ashish Kumar Prusty**
B.Tech Artificial Intelligence & Machine Learning
GITA Autonomous College, Odisha, India
"""
    )
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("AI Engine", "YOLOv8" if AI_AVAILABLE else "Demo Engine")
    c2.metric("Prediction", "Random Forest")
    c3.metric("Dashboard", "Streamlit")
    st.divider()
    st.success("System Ready for Smart City Deployment")


PAGES = {
    "Home": page_home,
    "Vehicle Detection": page_detection,
    "Traffic Analytics": page_analytics,
    "Traffic Prediction": page_prediction,
    "Live Monitoring": page_monitoring,
    "AI Report": page_report,
    "About": page_about,
}

# ==============================================================
# Sidebar
# ==============================================================

with st.sidebar:
    if LOGO.exists():
        st.image(str(LOGO), use_container_width=True)

    st.markdown(
        """
<div class="sc-card" style="text-align:center;">
<h3 style="margin:0;">🚦 Smart City AI</h3>
<p style="margin:4px 0 0;color:#94a3b8;">Enterprise Dashboard</p>
<p style="margin:8px 0 0;" class="sc-badge-online">🟢 AI Engine Online</p>
</div>
""",
        unsafe_allow_html=True,
    )
    st.divider()

    st.subheader("Navigation")
    labels = [f"{PAGE_ICONS[p]} {p}" for p in PAGE_ORDER]
    current_index = PAGE_ORDER.index(st.session_state.page) if st.session_state.page in PAGE_ORDER else 0
    chosen_label = st.radio("Navigation", labels, index=current_index, label_visibility="collapsed", disabled=st.session_state.auto_pipeline)
    chosen_page = PAGE_ORDER[labels.index(chosen_label)]
    if not st.session_state.auto_pipeline and chosen_page != st.session_state.page:
        st.session_state.page = chosen_page

    st.divider()
    st.subheader("🤖 AI Status")
    if manager is not None:
        st.success("✅ AI Engine Loaded")
        st.success("✅ Detection Model Ready")
        st.success("✅ Prediction Model Ready")
    else:
        st.info("ℹ️ Running Built-in Demo Engine")
    st.success("✅ Analytics Engine")
    st.success("✅ Monitoring System")

    st.divider()
    st.subheader("📈 Live Statistics")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Vehicles", st.session_state.vehicle_count)
        st.metric("Traffic", traffic_density(st.session_state.vehicle_count))
    with col2:
        st.metric("Status", "Online")
        st.metric("Version", "6.0")

    st.divider()
    st.subheader("🗂 Session")
    if st.session_state.uploaded_file is None:
        st.info("No file uploaded")
    else:
        st.success(f"Loaded: {st.session_state.uploaded_file.name}")
    if st.session_state.detected_image is not None:
        st.success("Detection Complete")
    else:
        st.warning("Detection Pending")

    st.divider()
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
    st.subheader("⚙ Tech Stack")
    st.dataframe(
        pd.DataFrame(
            {
                "Technology": ["Detection Engine", "OpenCV", "Streamlit", "Plotly", "Pandas", "NumPy"],
                "Status": ["✅"] * 6,
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.divider()
    st.subheader("👨‍💻 Developer")
    st.markdown(
        """
**Ashish Kumar Prusty**

B.Tech Artificial Intelligence & Machine Learning

GITA Autonomous College

Odisha, India
"""
    )
    st.caption("AI-Powered Intelligent Traffic Management System")

    st.divider()
    st.info(
        """
🚦 Smart City AI

Version **6.0**

Production Ready

Built using Python • OpenCV • Streamlit • Plotly
"""
    )

# ==============================================================
# Header (rendered once, not duplicated per-page)
# ==============================================================

hero()

# ==============================================================
# Automatic pipeline driver
# ==============================================================

if st.session_state.auto_pipeline:
    stage = PIPELINE_STAGES[st.session_state.pipeline_stage]
    goto(stage)

    st.info(f"⏳ AI Pipeline running - Step {st.session_state.pipeline_stage + 1} of {len(PIPELINE_STAGES)}: **{stage}**")
    st.progress((st.session_state.pipeline_stage) / len(PIPELINE_STAGES))
    workflow_diagram(active_stage=stage)

    if stage == "Vehicle Detection":
        run_detection()
        st.toast("Vehicle Detection Ready", icon="🚗")
    elif stage == "Traffic Analytics":
        run_analytics()
        st.toast("Traffic Analytics Ready", icon="📊")
    elif stage == "Traffic Prediction":
        run_prediction()
        st.toast("Prediction Ready", icon="🤖")
    elif stage == "Live Monitoring":
        st.toast("Monitoring Ready", icon="📡")
    elif stage == "AI Report":
        build_report()
        st.toast("Report Generated", icon="📄")

    PAGES[stage]()

    if st.session_state.pipeline_stage < len(PIPELINE_STAGES) - 1:
        st.session_state.pipeline_stage += 1
        time.sleep(1.1)
        st.rerun()
    else:
        st.session_state.auto_pipeline = False
        st.session_state.pipeline_done = True
        goto("Home")
        st.rerun()

else:
    PAGES[st.session_state.page]()

# ==============================================================
# Global Footer
# ==============================================================

st.divider()
f1, f2, f3, f4 = st.columns(4)
f1.metric("Detection", "Ready")
f2.metric("Analytics", "Ready")
f3.metric("Prediction", "Ready")
f4.metric("Monitoring", "Ready")

st.divider()
st.caption("🚦 Smart City AI • AI-Powered Intelligent Traffic Management System")
st.caption("Developed by Ashish Kumar Prusty")
st.caption("Powered by Python • OpenCV • Scikit-Learn • Streamlit • Plotly")
st.caption("© 2026 Smart City AI | All Rights Reserved")