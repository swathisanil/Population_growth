#Analyse Crude Birth Rate of five countries

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Population 1950-2018.csv')

# Extract the decade from the Time column
data['Decade'] = (data['Time'] // 10) * 10

# Filter the data for the required columns and locations
locations = ['India', 'China', 'United Kingdom', 'United States of America', 'Brazil']
filtered_data = data[data['Location'].isin(locations)]
filtered_data = filtered_data[['Decade', 'Births', 'Location']]

# Group the data by Decade and Location, and calculate the total births
grouped_data = filtered_data.groupby(['Decade', 'Location'])['Births'].sum().reset_index()

# Plot the grouped bar plot
fig, ax = plt.subplots(figsize=(10, 10))
width = 1.7  # Increased width to 0.5
colors = ['green', 'orange', 'blue', 'red', 'purple']  # Define a custom color palette

# Define the desired labels for legends
legend_labels = {'India': 'India', 'China': 'China', 'United Kingdom': 'UK',
                 'United States of America': 'USA', 'Brazil': 'Brazil'}

for i, loc in enumerate(locations):
    x = grouped_data[grouped_data['Location'] == loc]['Decade']
    y = grouped_data[grouped_data['Location'] == loc]['Births']
    ax.bar(x + (i - 2) * width, y, width=width, label=legend_labels[loc], color=colors[i])  # Assign different colors to bars

ax.set_xlabel('Decade (10 Years Period)')
ax.set_ylabel('Total Number of Births')
ax.set_xticks(grouped_data['Decade'].unique())
ax.legend(loc="upper left")

plt.show()
