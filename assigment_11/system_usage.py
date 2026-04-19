import pandas as pd
import matplotlib.pyplot as plt
import stats

# Hourly CPU load data for 8 hours
cpu_usage = [25, 30, 85, 92, 40, 38, 75, 30]

# Create hour labels
hours = [1, 2, 3, 4, 5, 6, 7, 8]

# Use pandas
cpu_series = pd.Series(cpu_usage)

# Statistical breakdown
print("Hourly CPU Usage Report")
print("CPU Usage Data:", cpu_usage)
print("Mean:", stats.mean(cpu_usage))
print("Frequencies:", stats.frequencies(cpu_usage))
print("Mode:", stats.mode(cpu_usage))
print("Standard Deviation:", stats.std(cpu_usage))

# Create a bar chart
plt.bar(hours, cpu_series)
plt.title("Hourly CPU Usage Report")
plt.xlabel("Hour")
plt.ylabel("Usage (%)")

# Save the graph
plt.savefig("system_usage_bar.png")

# Show the graph
plt.show()