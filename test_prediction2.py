from traffic_ai.prediction import PredictionEngine

engine = PredictionEngine()

sample = {

    "holiday":3,
    "temp":290,
    "rain_1h":0,
    "snow_1h":0,
    "clouds_all":75,
    "weather_main":2,
    "weather_description":5,
    "year":2024,
    "month":7,
    "day":15,
    "hour":18,
    "dayofweek":1,
    "is_weekend":0,
    "traffic_previous_hour":4200,
    "traffic_rolling_mean":4100,
    "traffic_rolling_max":4500,
    "traffic_rolling_min":3900,
    "traffic_std":200,
    "traffic_change":100,
    "traffic_growth":80,
    "weather_score":4,
    "temperature_category":2
}

result = engine.run(sample)

print(result)