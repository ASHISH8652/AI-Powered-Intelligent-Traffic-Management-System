"""
Traffic Pattern Analysis
------------------------
Analyze historical traffic trends
and detect peak traffic hours.
"""

from dataclasses import dataclass


@dataclass
class TrafficTrend:

    hourly_average: dict

    peak_hour: int

    peak_traffic: float

    average_traffic: float


class TrafficTrendAnalyzer:

    def analyze(self, traffic_data):

        """
        traffic_data

        Example

        {

            8: [21,22,24],

            9: [31,35,37],

            10:[42,41,40]

        }
        """

        hourly_average = {}

        total = 0
        count = 0

        peak_hour = None
        peak_average = -1

        for hour, values in traffic_data.items():

            avg = sum(values) / len(values)

            hourly_average[hour] = round(avg,2)

            total += sum(values)
            count += len(values)

            if avg > peak_average:

                peak_average = avg
                peak_hour = hour

        overall = round(total/count,2)

        return TrafficTrend(

            hourly_average,

            peak_hour,

            round(peak_average,2),

            overall

        )