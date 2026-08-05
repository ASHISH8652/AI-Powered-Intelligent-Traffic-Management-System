import pandas as pd

from traffic_ai.ml import TrafficFeatureEngineer

df = pd.read_csv(

    "datasets/processed/traffic_ml_dataset.csv"

)

engineer = TrafficFeatureEngineer()

features = engineer.transform(df)

print("=" * 60)

print(features.head())

print()

print(features.columns)