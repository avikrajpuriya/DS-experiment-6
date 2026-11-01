import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

df = pd.read_csv("urban_climate.csv")

attributes = [
    "temperature_celsius",
    "humidity_percent",
    "precipitation_mm"
]

for column in attributes:
    data = df[column].dropna()

    density = gaussian_kde(data)
    x = [data.min() + i * (data.max() - data.min()) / 199 for i in range(200)]
    y = density(x)

    plt.figure(figsize=(7, 5))
    plt.plot(x, y)
    plt.xlabel(column)
    plt.ylabel("Density")
    plt.title("Density Plot of " + column)
    plt.grid(True)
    plt.show()