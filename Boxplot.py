# Creating a Box plot for Population Growth based on World Population Prospects 2022

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Population 1950-2018.csv')

# Select the desired columns
columns = ['PopGrowthRate', 'CBR', 'CDR', 'LEx',  'MedianAgePop']

# Colors for each country
colors = ['blue', 'purple', 'green', 'red', 'orange']

# Plotting the box plot for each column
for col, color in zip(columns, colors):
    plt.style.use('seaborn')
    plt.figure()
    plt.boxplot([data[data['Location'] == 'United Kingdom'][col],
                 data[data['Location'] == 'United States of America'][col],
                 data[data['Location'] == 'India'][col],
                 data[data['Location'] == 'Brazil'][col],
                 data[data['Location'] == 'China'][col]],
                labels=['United Kingdom', 'United States of America', 'India', 'Brazil', 'China'],
                patch_artist=True,
                boxprops=dict(facecolor=color, color=color),
                whiskerprops=dict(color=color),
                capprops=dict(color=color),
                medianprops=dict(color='black', linewidth=2),
                flierprops=dict(marker='o', markersize=10, markerfacecolor='white', markeredgecolor=color))
    plt.xlabel('Country', fontsize=12)
    
    # Labeling the Y-axis
    if col == 'PopGrowthRate':
        plt.ylabel('Population Growth Rate (Percentage)', fontsize=12)
    elif col == 'CBR':
        plt.ylabel('Crude Birth Rate (Births Per 1,000 Population)', fontsize=12)
    elif col == 'CDR':
        plt.ylabel(('Crude Death Rate (Deaths Per 1,000 Population'), fontsize=12)
    elif col == 'LEx':
        plt.ylabel('Life Expectancy at Birth of both sexes  (Years)', fontsize=12)
    elif col == 'MedianAgePop':
        plt.ylabel('Median Age Population (Years)', fontsize=12)
    
    plt.grid(True)

# Show the plots
plt.show()
