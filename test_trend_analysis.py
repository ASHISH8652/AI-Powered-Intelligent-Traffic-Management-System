from traffic_ai.prediction import TrafficTrendAnalyzer

traffic = {

    7:[12,14,15],

    8:[18,20,22],

    9:[31,35,34],

    10:[45,42,47],

    11:[38,36,35],

    12:[25,24,26]

}

analyzer = TrafficTrendAnalyzer()

trend = analyzer.analyze(traffic)

print("="*60)

print("Hourly Average")

for hour,value in trend.hourly_average.items():

    print(f"{hour}:00 -> {value}")

print()

print("Peak Hour :",trend.peak_hour)

print("Peak Traffic :",trend.peak_traffic)

print("Overall Average :",trend.average_traffic)