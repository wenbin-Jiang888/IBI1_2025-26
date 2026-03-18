import matplotlib.pyplot as plt
import numpy as np
population_data = {
    "UK": [66.7, 69.2],
    "China": [1426, 1410],
    "Italy": [59.4, 58.9],
    "Brazil": [208.6, 212.0],
    "USA": [331.6, 340.1]
}

population_change = {}
print("1. Population change percentage for each country:")
for country, (pop_2020, pop_2024) in population_data.items():
    change_percent = ((pop_2024 - pop_2020) / pop_2020) * 100
    population_change[country] = change_percent
    print(f"   {country}: {change_percent:.2f}%")

# Sort the population change percentages in descending order
sorted_countries = sorted(population_change.items(), key=lambda x: x[1], reverse=True)
print("\n2. Population change percentages sorted in descending order:")
for country, percent in sorted_countries:
    print(f"   {country}: {percent:.2f}%")

max_increase_country = sorted_countries[0][0]
max_decrease_country = sorted_countries[4][0]
print(f"   Country with the largest population increase: {max_increase_country} ({sorted_countries[0][1]:.2f}%)")
print(f"   Country with the largest population decrease: {max_decrease_country} ({sorted_countries[4][1]:.2f}%)")

plt.figure(figsize=(10, 6))
countries = [item[0] for item in sorted_countries]
change_percents = [item[1] for item in sorted_countries]


colors = ['green' if x > 0 else 'red' for x in change_percents]
plt.bar(countries, change_percents, color=colors)
plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)  
plt.title("Population Change Percentage (2020-2024)", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Change Percentage (%)", fontsize=12)
plt.yticks(np.arange(-2, 4.5, step=0.5))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()