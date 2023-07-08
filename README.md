# Wireline-Plot

# Wireline Plotting Tool

This repository contains a Python script that generates wireline logs plot using matplotlib. The script is designed to read a CSV file containing wireline log data, perform descriptive statistics to determine the appropriate limits, and generate a plot with customizable parameters.

## Instructions

1. **Import the Data**: The wireline log data should be imported into a CSV file. Ensure that the CSV file follows the required format and contains the necessary columns. Modify the `df = pd.read_csv(...)` line in the script to specify the correct file path.

2. **Descriptive Statistics**: Use the descriptive statistics of the data to determine the appropriate limits and depth range for each track. Modify the limits and depth range within the `plot_wireline` function based on the descriptive statistics of your data.

3. **Define Parameters**: Define the parameters for each track using the appropriate section in the script. For example, to plot the Gamma Ray track, define the `GR` variable as `df["GR"]`. Adjust the parameters according to your data.

4. **Check File Location**: Ensure that the `save_path` variable in the script points to the desired location where you want to save the plot. Modify the file path to the desired directory and filename.

5. **Run the Function**: Execute the `plot_wireline` function to generate the wireline log plot. The plot will be saved to the specified file location.

## Example Usage

```python
import pandas as pd
import matplotlib.pyplot as plt

# Import the data into a DataFrame
df = pd.read_csv("path/to/wireline_data.csv")

# Calculate descriptive statistics and adjust limits and depth range

# Define the parameters for each track

# Set the save_path variable to the desired file location

# Call the plot_wireline function
plot_wireline(df, save_path="path/to/save/plot.jpeg")

Make sure to install the necessary dependencies such as pandas and matplotlib before running the script.

For more detailed instructions, please refer to the comments within the script.

Feel free to modify the script and customize it according to your specific requirements. Happy plotting!
