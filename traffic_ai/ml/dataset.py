"""
Traffic ML Dataset Builder
--------------------------
Store traffic analytics for
machine learning training.
"""

import os
import pandas as pd
from datetime import datetime


class TrafficDatasetBuilder:

    def __init__(

        self,

        output_file="datasets/processed/traffic_ml_dataset.csv"

    ):

        self.output_file = output_file

        os.makedirs(

            os.path.dirname(output_file),

            exist_ok=True

        )

        if not os.path.exists(output_file):

            columns = [

                "timestamp",

                "hour",

                "day_of_week",

                "vehicle_count",

                "lane_1",

                "lane_2",

                "lane_3",

                "lane_4",

                "density",

                "arrival_rate",

                "queue_length",

                "signal_time",

                "congestion"

            ]

            pd.DataFrame(

                columns=columns

            ).to_csv(

                output_file,

                index=False

            )

    def append(

        self,

        vehicle_count,

        lane_counts,

        density,

        arrival_rate,

        queue_length,

        signal_time,

        congestion

    ):

        now = datetime.now()

        row = {

            "timestamp": now.strftime(

                "%Y-%m-%d %H:%M:%S"

            ),

            "hour": now.hour,

            "day_of_week": now.weekday(),

            "vehicle_count": vehicle_count,

            "lane_1": lane_counts[0],

            "lane_2": lane_counts[1],

            "lane_3": lane_counts[2],

            "lane_4": lane_counts[3],

            "density": density,

            "arrival_rate": arrival_rate,

            "queue_length": queue_length,

            "signal_time": signal_time,

            "congestion": congestion

        }

        df = pd.DataFrame([row])

        df.to_csv(

            self.output_file,

            mode="a",

            header=False,

            index=False

        )