from traffic_ai.prediction import ArrivalRatePredictor

predictor = ArrivalRatePredictor()

traffic = [

    18,

    22,

    27,

    31,

    36,

    40,

    45

]

for count in traffic:

    predictor.update(count)

prediction = predictor.predict()

print("=" * 60)

print("History")

print(prediction.history)

print()

print(

    "Average Arrival Rate :",

    prediction.average_arrival_rate,

    "vehicles/min"

)

print()

print(

    "Predicted Next Count :",

    prediction.predicted_next_count

)