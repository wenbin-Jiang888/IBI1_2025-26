# Practical 10: Working with Global Health Data
# IBI1 2025/26
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory (please update to your own path)
os.chdir(r"C:\Users\Lenovo\Desktop\IBI1\IBI1_2025-26\IBI1_2025-26\Practical10")
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Load dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Show first 10 rows, Year and DALYs (third and fourth columns: index 2 and 3)
print("\n--- First 10 rows: Year and DALYs ---")
print(dalys_data.iloc[0:10, [2, 3]])

# ------------------------------
# Afghanistan first 10 years: which year has maximum DALYs?
# Answer: 1990
# ------------------------------
afghanistan = dalys_data.loc[dalys_data["Entity"] == "Afghanistan"].head(10)
max_year_afg = afghanistan.loc[afghanistan["DALYs"].idxmax(), "Year"]
print("\nAfghanistan max DALYs in first 10 years:", max_year_afg)

# ------------------------------
# Zimbabwe data using Boolean index
# First year: 1990, Last year: 2019
# ------------------------------
zimbabwe = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe"]
print("\n--- Zimbabwe DALYs data ---")
print(zimbabwe[["Year", "DALYs"]])
print("Zimbabwe first year:", zimbabwe["Year"].min())
print("Zimbabwe last year:", zimbabwe["Year"].max())

# ------------------------------
# 2019 max and min DALYs countries
# Max: ..., Min: ...
# ------------------------------
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
country_max = data_2019.loc[data_2019["DALYs"].idxmax(), "Entity"]
country_min = data_2019.loc[data_2019["DALYs"].idxmin(), "Entity"]
print("\n2019 Max DALYs country:", country_max)
print("2019 Min DALYs country:", country_min)

# Plot time series for one country (e.g., minimum country)
country_plot = dalys_data.loc[dalys_data["Entity"] == country_min]
plt.figure(figsize=(10, 5))
plt.plot(country_plot["Year"], country_plot["DALYs"], marker='o', linestyle='-', color='blue')
plt.title(f"DALYs Rate Over Time: {country_min}")
plt.xlabel("Year")
plt.ylabel("DALYs Rate")
plt.xticks(rotation=90)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("dalys_trend.png")
plt.show()

# ------------------------------
# Code for question.txt starts here (LINE 60)
# Question: What is the distribution of DALYs across all countries in 2019?
# ------------------------------
plt.figure(figsize=(10, 5))
plt.hist(data_2019["DALYs"], bins=30, color='green', edgecolor='black')
plt.title("Distribution of DALYs Rates Across Countries in 2019")
plt.xlabel("DALYs Rate")
plt.ylabel("Number of Countries")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("dalys_2019_distribution.png")
plt.show()

print("\nAll tasks completed.")