import os

REQUIRED_FILES = [

    "models/random_forest.pkl",

    "models/feature_columns.pkl",

    "models/metadata.json"

]


def verify():

    missing = []

    for file in REQUIRED_FILES:

        if not os.path.exists(file):

            missing.append(file)

    return missing