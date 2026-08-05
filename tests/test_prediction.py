"""
Prediction Test
"""

from traffic_ai.prediction.inference import PredictionEngine


def test_prediction():

    engine = PredictionEngine()

    sample = {

        "holiday":3,

        "temp":295,

        "rain_1h":0,

        "snow_1h":0,

        "clouds_all":50,

        "weather_main":2,

        "weather_description":4,

        "year":2024,

        "month":7,

        "day":18,

        "hour":16,

        "dayofweek":2,

        "is_weekend":0,

        "traffic_previous_hour":4100,

        "traffic_rolling_mean":4200,

        "traffic_rolling_max":4500,

        "traffic_rolling_min":3900,

        "traffic_std":180,

        "traffic_change":120,

        "traffic_growth":150,

        "weather_score":4.2,

        "temperature_category":1

    }

    result = engine.run(sample)

    print(result)


if __name__ == "__main__":

    test_prediction()