import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

# Load data from CSV files
file1 = 'Task1/output/activated_small.csv'  # Replace with the path to your first CSV file
file2 = 'Task1/output/people_small.csv'  # Replace with the path to your second CSV file

# Read the CSV files into pandas DataFrames
data1 = pd.read_csv(file1)
data2 = pd.read_csv(file2)

print(data2) # as Activated people haven't been removed yet, this will describe the entire data.

#remove activated people from people list
data2 = pd.merge(data2,data1, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)


# Plot the points from the second file in blue
plt.scatter(data2['x'], data2['y'], color='blue', label='non-activated')

# Plot the points from the first file in red
plt.scatter(data1['x'], data1['y'], color='red', label='activated')

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of activated people over non-activated people')

# Show legend
plt.legend()

# Display the plot
plt.show()
