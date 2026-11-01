import pandas as pd
import numpy as np

df = pd.read_csv("urban_climate.csv")

attributes = [
    "temperature_celsius",
    "humidity_percent",
    "precipitation_mm"
]

for attribute in attributes:

    data = df[attribute].dropna().to_numpy()

    n = len(data)

    total = 0
    for x in data:
        total += x

    mean = total / n

    squared_sum = 0
    for x in data:
        squared_sum += (x - mean) ** 2

    variance = squared_sum / (n - 1)

    standard_deviation = np.sqrt(variance)

    print("\nAttribute:", attribute)
    print("Mean =", mean)
    print("Standard Deviation =", standard_deviation)