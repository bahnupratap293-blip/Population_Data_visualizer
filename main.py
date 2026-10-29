import csv
import matplotlib.pyplot as plt
import pandas as pd

def is_valid_population(value):
    try:
        population = int(value)
        return population > 0
    except (ValueError, TypeError):
        return False


def is_valid_year(value):
    try:
        year = int(value)
        return year > 0
    except (ValueError, TypeError):
        return False
    
# Read the CSV file and handle invalid data
data = []

with open("population.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            city = row["City"].strip()
            year = int(row["Year"])
            population = int(row["Population"])

            if not city:
                print("Skipping row: City is missing")
                continue

            if not is_valid_year(year):
                print("Skipping row: Invalid year", row)
                continue

            if not is_valid_population(population):
                print("Skipping row: Invalid population", row)
                continue

            row["City"] = city
            row["Year"] = year
            row["Population"] = population
            data.append(row)

        except (ValueError, TypeError, KeyError, AttributeError):
            print("Skipping invalid row:", row)

if not data:
    print("No valid population data found.")
    raise SystemExit

# Find the latest year
latest_year = max(row["Year"] for row in data)
earliest_year = min(row["Year"] for row in data)

# Get population of each city in the latest year
latest_data = {}

for row in data:
    city = row["City"]
    year = row["Year"]
    population = row["Population"]

    if year == latest_year:
        latest_data[city] = population

# Calculate total population
total_population = sum(latest_data.values())

# Find the largest city
largest_city = max(latest_data, key=latest_data.get)

# Calculate growth for each city
growth = {}

for city in latest_data:
    old_population = None
    new_population = latest_data[city]

    for row in data:
        if row["City"] == city and row["Year"] == earliest_year:
            old_population = row["Population"]

    if old_population is not None and old_population > 0:
        growth[city] = (
            (new_population - old_population)
            / old_population * 100
        )
# Display population data in table format
print("\nPOPULATION DATA TABLE")
print("-------------------------------")

df = pd.DataFrame(data)
print(df.to_string(index=False))
print("\nPOPULATION DATA SUMMARY")
print("-------------------------------")
print("Latest year:", latest_year)
print("Total population:", total_population)
print("Largest city:", largest_city,
      "(", latest_data[largest_city], ")")
# Detailed Data Analysis
print("\nDETAILED DATA ANALYSIS")
print("-------------------------------")
# Year-wise population records using Pandas
print("\nYEAR-WISE POPULATION TABLE")
print("-------------------------------")

year_table = df.pivot_table(
    index="City",
    columns="Year",
    values="Population",
    aggfunc="first"
)

print(year_table.to_string())
for city in latest_data:
    city_data = [row for row in data if row["City"] == city]
    city_data.sort(key=lambda row: row["Year"])

    first_population = city_data[0]["Population"]
    last_population = city_data[-1]["Population"]
    population_change = last_population - first_population

    if first_population > 0:
        growth_percentage = (population_change / first_population) * 100
    else:
        growth_percentage = 0

    print("\nCity:", city)
    print("Population Change:", population_change)
    print("Growth Percentage:", round(growth_percentage, 2), "%")

print("\nDATA INSIGHTS")
print("-------------------------------")

if growth:
    fastest_city = max(growth, key=growth.get)
    print(f"{fastest_city} has the highest growth rate in the available data.")

print(f"Total population in {latest_year}: {total_population}")

    # Bar chart: Latest population by city
cities = list(latest_data.keys())
populations = list(latest_data.values())

plt.figure(figsize=(8, 5))
plt.bar(cities, populations)
plt.title("City Population Comparison")
plt.xlabel("City")
plt.ylabel("Population")
plt.tight_layout()
plt.savefig("population_comparison.png")
plt.show()

# Line chart: Population trend over years
plt.figure(figsize=(8, 5))

for city in latest_data:
    years = []
    city_populations = []

    for row in data:
        if row["City"] == city:
            years.append(row["Year"])
            city_populations.append(row["Population"])

    points = sorted(zip(years, city_populations))
    years = [point[0] for point in points]
    city_populations = [point[1] for point in points]

    plt.plot(years, city_populations, marker="o", label=city)

plt.title("Population Trend")
plt.xlabel("Year")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("population_trend.png")
plt.show()