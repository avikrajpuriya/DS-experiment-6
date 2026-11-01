import pandas as pd
import math

df = pd.read_csv("urban_climate.csv")

attributes = [
    "temperature_celsius",
    "humidity_percent",
    "precipitation_mm"
]

for column in attributes:
    data = []

    for value in df[column]:
        if pd.notna(value):
            data.append(value)

    n = len(data)

    total = 0
    for value in data:
        total += value

    mean = total / n

    sum_sq = 0
    for value in data:
        sum_sq += (value - mean) ** 2

    sd = math.sqrt(sum_sq / n)

    sum_cube = 0
    sum_fourth = 0

    for value in data:
        z = (value - mean) / sd
        sum_cube += z ** 3
        sum_fourth += z ** 4

    skewness = sum_cube / n
    kurtosis = (sum_fourth / n) - 3

    print("\nAttribute:", column)
    print("Skewness:", skewness)
    print("Kurtosis:", kurtosis)