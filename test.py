import numpy as np
from scipy import stats

# Get user input for dataset
num_points = int(input("Enter the number of data points: "))
x_values = []
y_values = []

for i in range(num_points):
    x = float(input(f"Enter x value for data point {i+1}: "))
    y = float(input(f"Enter y value for data point {i+1}: "))
    x_values.append(x)
    y_values.append(y)

# Convert lists to NumPy arrays
x_values = np.array(x_values)
y_values = np.array(y_values)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(x_values, y_values)

# Print regression results
print("Regression Results:")
print(f"Slope: {slope}")
print(f"Intercept: {intercept}")
print(f"R-squared: {r_value**2}")
