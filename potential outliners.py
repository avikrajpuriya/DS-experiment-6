import pandas as pd

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

    data.sort()

    n = len(data)

    q1_position = 0.25 * (n - 1)
    q3_position = 0.75 * (n - 1)

    q1_low = int(q1_position)
    q1_high = q1_low + 1
    q3_low = int(q3_position)
    q3_high = q3_low + 1

    q1_fraction = q1_position - q1_low
    q3_fraction = q3_position - q3_low

    q1 = data[q1_low] + q1_fraction * (data[q1_high] - data[q1_low])
    q3 = data[q3_low] + q3_fraction * (data[q3_high] - data[q3_low])

    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = []

    for value in data:
        if value < lower_limit or value > upper_limit:
            outliers.append(value)

    print("\nAttribute:", column)
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
    print("Lower limit:", lower_limit)
    print("Upper limit:", upper_limit)
    print("Number of potential outliers:", len(outliers))
    print("Potential outlier values:", outliers)