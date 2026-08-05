from traffic_ai.prediction import QueuePredictor

predictor = QueuePredictor()

prediction = predictor.predict(

    lane="North",

    current_queue=25,

    arrival_rate=5,

    green_time=30

)

print("=" * 60)

print(f"""
Lane              : {prediction.lane}

Current Queue     : {prediction.current_queue}

Incoming Vehicles : {prediction.arriving}

Vehicles Passing  : {prediction.departing}

Predicted Queue   : {prediction.predicted_queue}
""")