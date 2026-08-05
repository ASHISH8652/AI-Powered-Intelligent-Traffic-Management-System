from traffic_ai.prediction import SignalForecaster

forecast = SignalForecaster()

result = forecast.forecast(

    lane="North",

    vehicle_count=42,

    congestion="HIGH",

    predicted_queue=28

)

print("=" * 60)

print(f"""
Lane               : {result.lane}

Current Vehicles   : {result.vehicle_count}

Congestion         : {result.congestion}

Predicted Queue    : {result.predicted_queue}

Green Time         : {result.green_time} sec

Confidence         : {result.confidence:.2f}
""")