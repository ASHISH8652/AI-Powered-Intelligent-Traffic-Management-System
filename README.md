# AI-Powered Intelligent Traffic Management System

A Streamlit-based traffic intelligence platform featuring YOLOv8 vehicle detection, lane analytics, traffic density estimation, and Random Forest traffic prediction.

## Features

- YOLOv8 Vehicle Detection
- Lane Analytics
- Traffic Density Estimation
- Random Forest Traffic Prediction
- Live Streamlit Dashboard
- Smart Signal Recommendation
- Historical Prediction Tracking

## Tech Stack

- Python
- OpenCV
- YOLOv8
- Scikit-Learn
- Streamlit
- Plotly
- Pandas
- NumPy

## Installation

1. Create and activate a Python virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

1. Run the dashboard:

```bash
streamlit run app.py
```

## Environment Variables

The app supports optional environment overrides via a `.env` file or shell environment:

- `MODEL`: path to the trained model file (default: `models/random_forest.pkl`)
- `YOLO`: path to the YOLO model file (default: `models/yolov8n.pt`)
- `LOG_FOLDER`: path to the log folder (default: `logs`)

Create a `.env` file in the project root to customize these values.

## Docker

Build and start the app with Docker Compose:

```bash
docker compose up --build
```

Then open `http://localhost:8501` in your browser.

## Dataset

Uses the Metro Interstate Traffic Volume dataset and supplemental traffic analytics input.

## Model

- Random Forest Regressor for traffic volume prediction
- Model metadata and feature order are persisted for consistent inference

## License

MIT
