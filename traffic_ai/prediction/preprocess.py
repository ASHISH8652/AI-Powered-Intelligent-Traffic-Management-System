"""
Prediction Preprocessing
"""

import pandas as pd


def prepare_input(data, feature_columns):

    df = pd.DataFrame([data])

    df = df.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return df