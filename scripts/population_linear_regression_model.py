#Linear Regression Model

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv('Population5.csv')

# Filters the data based on desired locations ('India', 'China', 'United Kingdom', 'United States of America', 'Brazil') and a specific time period (2010 to 2018) and assigns the filtered data to the variable filtered_data
filtered_data = data[(data['Location'].isin(['India', 'China', 'United Kingdom', 'United States of America', 'Brazil'])) & (data['Time'] >= 2010) & (data['Time'] <= 2018)]

# Split the data into training and testing sets
#Selects the training data from the filtered data by keeping  'Time' values less than or equal to 2013.
#Selects the testing data from the filtered data by keeping  'Time' values between 2013 and 2018.
train_data = filtered_data[filtered_data['Time'] <= 2013]
test_data = filtered_data[(filtered_data['Time'] >= 2013) & (filtered_data['Time'] <= 2018)]

# Select the features (independent variables) and target variable to be used in the analysis.
#Defines the target variable (dependent variable) to be predicted.
features = ['Location', 'Time']
target = 'CBR'

# Convert categorical variables into numerical values using one-hot encoding
train_data_encoded = pd.get_dummies(train_data[features])
test_data_encoded = pd.get_dummies(test_data[features])

#Creates an instance of the StandardScaler class from scikit-learn to perform feature scaling
# Standardize the features
scaler = StandardScaler()
#Applies standardization to the training data by scaling the features to have zero mean and unit variance.
train_data_encoded_scaled = scaler.fit_transform(train_data_encoded)
#Applies the same scaling transformation to the testing data using the parameters learned from the training data.
test_data_encoded_scaled = scaler.transform(test_data_encoded)

# Train the Linear Regression model
#Creates an instance of the LinearRegression class for linear regression modeling.
#Trains the linear regression model using the scaled training data and the target variable.
model = LinearRegression()
model.fit(train_data_encoded_scaled, train_data[target])

# Predict the CBR for the test data
#Generates predictions for the target variable using the trained model and the scaled testing data.
predictions = model.predict(test_data_encoded_scaled)

# Compare the predicted CBR with the original data
# Creates a copy of the testing data and assigns it to comparison_df.
#Adds a new column 'Predicted_CBR' to comparison_df containing the predicted values.
comparison_df = test_data.copy()
comparison_df['Predicted_CBR'] = predictions

# Calculate the Mean Squared Error
#Calculates the mean squared error between the actual target values in the testing data and the predicted values.
mse = mean_squared_error(test_data[target], predictions)

# Create a vertical bar chart
locations = comparison_df['Location']
time = comparison_df['Time']
cbr = comparison_df['CBR']
predicted_cbr = comparison_df['Predicted_CBR']

# Plotting the bar chart
#Creates a figure object for plotting with a specific size
plt.figure(figsize=(10, 6))

# Assign colors and labels for each location
colors = {'United Kingdom': 'blue', 'United States of America': 'red', 'India': 'green', 'China': 'orange', 'Brazil': 'purple'}
labels = {'United Kingdom': 'UK', 'United States of America': 'USA', 'India': 'IND', 'China': 'CHINA', 'Brazil': 'BRZL'}

#Iterates over the locations in locations with their corresponding index and plot the bars
for i, loc in enumerate(locations):
    x = i
    # Plot the original CBR bar Plot at the specified index x with a specific width, alignment, color, and label.
    plt.bar(x, cbr.iloc[i], width=0.4, align='center', color=colors[loc], label='Original CBR' if i == 0 else '')
    # Plot the predicted CBR bar Plots  at the specified index x with a different width, alignment, color, transparency, edge color, linewidth, and label.
    plt.bar(x, predicted_cbr.iloc[i], width=0.6, align='edge', color=colors[loc], alpha=0.6,
            edgecolor='black', linewidth=0.1, label='Predicted CBR' if i == 0 else '')

# Set the labels and title
plt.xlabel('Country')
plt.ylabel('Crude Birth Rate')
plt.title('Comparison of Original Crude Birth Rate and Predicted Crude Birth Rate')
#Sets the x-axis tick labels using the mapped labels
plt.xticks(range(len(locations)), [labels[loc] for loc in locations], rotation=45)
#Adjusts the layout of the plot to prevent overlapping elements
plt.tight_layout()

# Add the legend
plt.legend()

# Show the plot
plt.show()

# Print the output
#Prints the header for the output table
# Iterates over the locations in locations with their corresponding index to print output table
print('Location                    Year     CBR   Predicted_CBR')
for i in range(len(locations)):
    print(f"{locations.iloc[i]:<27} {time.iloc[i]:^5} {cbr.iloc[i]:>7.3f} {predicted_cbr.iloc[i]:>14.5f}")
print('Mean Squared Error:', mse)
