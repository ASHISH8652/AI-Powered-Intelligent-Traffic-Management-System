from traffic_ai.prediction import TrafficReportGenerator

traffic = [

    18,

    21,

    26,

    35,

    42,

    47,

    51,

    45,

    39,

    31

]

generator = TrafficReportGenerator()

report = generator.generate(

    traffic_counts=traffic,

    peak_hour=10

)

print("=" * 60)

print(f"""
Traffic Report

Date               : {report.report_date}

Total Vehicles     : {report.total_vehicles}

Average Traffic    : {report.average_traffic}

Peak Hour          : {report.peak_hour}:00

Peak Traffic       : {report.peak_traffic}

Congestion Level   : {report.congestion_level}

AI Recommendation

{report.recommendation}
""")