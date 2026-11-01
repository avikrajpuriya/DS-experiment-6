import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("urban_climate.csv")

attributes = [
    "temperature_celsius",
    "humidity_percent",
    "precipitation_mm"
]

for column in attributes:

    data = df[column].dropna()

    skewness = data.skew()

    print("Attribute:", column)
    print("Skewness:", skewness)

    if skewness > 0:
        print("Distribution: Positively Skewed")
    elif skewness < 0:
        print("Distribution: Negatively Skewed")
    else:
        print("Distribution: Symmetric")

    print()

    plt.figure(figsize=(7, 5))

    plt.hist(data, bins=30, density=True, alpha=0.6, edgecolor="black")

    x = np.linspace(data.min(), data.max(), 200)

    mean = data.mean()
    std = data.std()

    kde = np.zeros(len(x))

    for value in data:
        kde += np.exp(-0.5 * ((x - value) / std) ** 2)

    kde = kde / (len(data) * std * np.sqrt(2 * np.pi))

    plt.plot(x, kde, linewidth=2)

    plt.xlabel(column)
    plt.ylabel("Density")
    plt.title("Histogram and KDE of " + column)
    plt.show()