import csv

file = open("urban_climate.csv", "r")
data = list(csv.DictReader(file))
file.close()

print("Number of records:", len(data))

columns = [
    "temperature_celsius",
    "humidity_percent",
    "precipitation_mm"
]

for column in columns:

    values = []

    for row in data:
        try:
            values.append(float(row[column]))
        except:
            pass

    n = len(values)

    if n == 0:
        print("No valid data for", column)
        continue

    total = 0

    for x in values:
        total = total + x

    mean = total / n

    for i in range(n):
        for j in range(i + 1, n):
            if values[i] > values[j]:
                values[i], values[j] = values[j], values[i]

    if n % 2 == 0:
        median = (values[n//2 - 1] + values[n//2]) / 2
    else:
        median = values[n//2]

    frequency = {}

    for x in values:
        if x in frequency:
            frequency[x] = frequency[x] + 1
        else:
            frequency[x] = 1

    max_frequency = 0
    mode = []

    for x in frequency:
        if frequency[x] > max_frequency:
            max_frequency = frequency[x]
            mode = [x]
        elif frequency[x] == max_frequency:
            mode.append(x)

    if max_frequency == 1:
        mode = "No mode"

    print("\nAttribute:", column)
    print("Mean =", mean)
    print("Median =", median)
    print("Mode =", mode)


while True:

    city_name = input("\nEnter city name (or type 'exit' to stop): ")

    if city_name.lower() == "exit":
        print("Program ended.")
        break

    for column in columns:

        values = []

        for row in data:
            if row["city"].lower() == city_name.lower():
                try:
                    values.append(float(row[column]))
                except:
                    pass

        if len(values) == 0:
            print("No valid", column, "data found for", city_name)
            continue

        n = len(values)

        total = 0

        for x in values:
            total = total + x

        mean = total / n

        for i in range(n):
            for j in range(i + 1, n):
                if values[i] > values[j]:
                    values[i], values[j] = values[j], values[i]

        if n % 2 == 0:
            median = (values[n//2 - 1] + values[n//2]) / 2
        else:
            median = values[n//2]

        frequency = {}

        for x in values:
            if x in frequency:
                frequency[x] = frequency[x] + 1
            else:
                frequency[x] = 1

        max_frequency = 0
        mode = []

        for x in frequency:
            if frequency[x] > max_frequency:
                max_frequency = frequency[x]
                mode = [x]
            elif frequency[x] == max_frequency:
                mode.append(x)

        if max_frequency == 1:
            mode = "No mode"

        print("\nCity:", city_name)
        print("Attribute:", column)
        print("Observations:", n)
        print("Mean =", mean)
        print("Median =", median)
        print("Mode =", mode)