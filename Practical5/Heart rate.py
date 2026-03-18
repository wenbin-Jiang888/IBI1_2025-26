import matplotlib.pyplot as plt
import numpy as np
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]
patient_count = len(heart_rates)
avg_heart_rate = sum(heart_rates) / patient_count
print(f"1. There are {patient_count} patients in the dataset")
print(f"the average heart rate is: {avg_heart_rate:.2f} bpm" )

low_count = 0    # Low: <60 bpm
normal_count = 0 # Normal: 60-120 bpm
high_count = 0   # High: >120 bpm

for rate in heart_rates:
    if rate < 60:
        low_count += 1
    elif 60 <= rate <= 120:
        normal_count += 1
    else:
        high_count += 1
print("\n2. Heart rate category statistics:")
print(f"   Low (<60 bpm): {low_count} patients")
print(f"   Normal (60-120 bpm): {normal_count} patients")
print(f"   High (>120 bpm): {high_count} patients")

max_count = max(low_count, normal_count, high_count)
if max_count == low_count:
    most_common = "Low"
elif max_count == normal_count:
    most_common = "Normal"
else:
    most_common = "High"
print(f"   The most common heart rate category is: {most_common}")
plt.figure(figsize=(8, 8))
labels = [f'Low({low_count} patients)', f'Normal({normal_count} patients)', f'High({high_count} patients)']
sizes = [low_count, normal_count, high_count]
colors = ['lightcoral', 'lightgreen', 'lightskyblue']
explode = (0.1,0 , 0)  # Highlight the smallist slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.title("Distribution of Heart Rate Categories", fontsize=14)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.tight_layout()
plt.show()