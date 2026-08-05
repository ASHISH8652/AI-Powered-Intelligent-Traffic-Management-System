from traffic_ai.prediction import CongestionPredictor

predictor = CongestionPredictor()

prediction = predictor.predict(38)

print("=" * 60)

print(f"""
Current Vehicles : {prediction.vehicle_count}

Predicted Vehicles : {prediction.predicted_count}

Congestion : {prediction.congestion_level}

Confidence : {prediction.confidence:.2f}
""")