import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file, skipping the comment section
df = pd.read_csv("server_log.csv", skiprows=5)

# Remove the Timestamp column because we only need service response times
df = df.drop("Timestamp", axis=1)

# Fill missing values in each column with that column's mean
df = df.fillna(df.mean())

# Calculate mean response time for each service
mean_response = df.mean()

# Print cleaned data and averages
print("Cleaned Server Log Data:")
print(df)
print()
print("Mean Response Time for Each Service:")
print(mean_response)

# Create pie chart
plt.pie(mean_response, labels=mean_response.index, autopct="%1.1f%%")
plt.title("Server Response Time Distribution")

# Save graph
plt.savefig("log_response_pie.png")

# Show graph
plt.show()