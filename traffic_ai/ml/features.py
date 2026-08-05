"""
Traffic Feature Engineering
---------------------------
Create ML-ready traffic features.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder


class TrafficFeatureEngineer:

    def __init__(self):

        self.density_encoder = LabelEncoder()

        self.congestion_encoder = LabelEncoder()

    def transform(self, dataframe):

        df = dataframe.copy()

        # -------------------------
        # Weekend Feature
        # -------------------------

        df["is_weekend"] = (

            df["day_of_week"] >= 5

        ).astype(int)

        # -------------------------
        # Peak Hour Feature
        # -------------------------

        df["is_peak_hour"] = (

            ((df["hour"] >= 8) & (df["hour"] <= 10)) |

            ((df["hour"] >= 17) & (df["hour"] <= 20))

        ).astype(int)

        # -------------------------
        # Lane Statistics
        # -------------------------

        lane_columns = [

            "lane_1",

            "lane_2",

            "lane_3",

            "lane_4"

        ]

        df["lane_average"] = (

            df[lane_columns]

            .mean(axis=1)

        )

        df["lane_variance"] = (

            df[lane_columns]

            .var(axis=1)

        )

        # -------------------------
        # Encode Density
        # -------------------------

        df["density_encoded"] = (

            self.density_encoder.fit_transform(

                df["density"]

            )

        )

        # -------------------------
        # Encode Congestion
        # -------------------------

        df["congestion_encoded"] = (

            self.congestion_encoder.fit_transform(

                df["congestion"]

            )

        )

        return df