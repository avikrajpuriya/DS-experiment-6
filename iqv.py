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

    data = np.sort(data)

    n = len(data)

    # Median of whole data = Q2
    if n % 2 == 0:
        q2 = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        q2 = data[n // 2]

    # Divide data into two 50% halves
    mid = n // 2

    first_half = data[:mid]
    second_half = data[mid:]

    # Median of first 50% = Q1
    n1 = len(first_half)

    if n1 % 2 == 0:
        q1 = (first_half[n1 // 2 - 1] + first_half[n1 // 2]) / 2
    else:
        q1 = first_half[n1 // 2]

    # Median of next 50% = Q3
    n2 = len(second_half)

    if n2 % 2 == 0:
        q3 = (second_half[n2 // 2 - 1] + second_half[n2 // 2]) / 2
    else:
        q3 = second_half[n2 // 2]

    # Interquartile Range
    iqr = q3 - q1

    print("\nAttribute:", attribute)
    print("Q1 =", q1)
    print("Q2 (Median) =", q2)
    print("Q3 =", q3)
    print("Interquartile Range (IQR) =", iqr)