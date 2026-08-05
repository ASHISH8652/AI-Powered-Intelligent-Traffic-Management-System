"""
Utility functions for prediction.
"""


def congestion_level(volume):

    if volume < 1500:
        return "Low"

    elif volume < 3500:
        return "Medium"

    elif volume < 5500:
        return "High"

    else:
        return "Severe"