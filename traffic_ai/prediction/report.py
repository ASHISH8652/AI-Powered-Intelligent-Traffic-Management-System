"""
Traffic Report Generator
------------------------
Generate historical traffic reports
and AI recommendations.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class TrafficReport:

    report_date: str

    total_vehicles: int

    average_traffic: float

    peak_hour: int

    peak_traffic: int

    congestion_level: str

    recommendation: str


class TrafficReportGenerator:

    def generate(

        self,

        traffic_counts,

        peak_hour

    ):

        total = sum(traffic_counts)

        average = round(

            total / len(traffic_counts),

            2

        )

        peak = max(traffic_counts)

        if average < 20:

            level = "LOW"

            recommendation = (

                "Current infrastructure is sufficient."

            )

        elif average < 40:

            level = "MEDIUM"

            recommendation = (

                "Monitor traffic during peak hours."

            )

        elif average < 60:

            level = "HIGH"

            recommendation = (

                "Increase green signal duration "

                "during rush hours."

            )

        else:

            level = "VERY HIGH"

            recommendation = (

                "Deploy adaptive traffic control "

                "and additional traffic personnel."

            )

        return TrafficReport(

            report_date=datetime.now().strftime(

                "%Y-%m-%d"

            ),

            total_vehicles=total,

            average_traffic=average,

            peak_hour=peak_hour,

            peak_traffic=peak,

            congestion_level=level,

            recommendation=recommendation

        )