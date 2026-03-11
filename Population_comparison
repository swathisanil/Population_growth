#Comparison of population of five countries

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Population 1950-2018.csv')

# Select relevant columns for the five locations
columns_to_use = ['Location', 'TPopulation1Jan']
df = data.loc[data['Location'].isin(['India', 'China', 'United Kingdom', 'United States of America', 'Brazil']), columns_to_use]

# Prepare data for the plot
locations = df['Location']
population = df['TPopulation1Jan']
colors = ['blue', 'orange', 'green', 'red', 'purple']

# Create a bar plot
plt.bar(locations, population, color=colors)
plt.xlabel('Locations')
plt.ylabel('Population')
plt.title('Population Comparison')
plt.show()

# Create a horizontal bar plot
plt.barh(locations, population, color=colors)
plt.xlabel('Population')
plt.ylabel('Locations')
plt.title('Population Comparison')
plt.show()
