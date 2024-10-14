import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Function to create scatter plots with trendline and R-squared
def create_scatter_plots(input_csv, output_dir, comparison_column):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Columns to exclude
    excluded_columns = ['Delivery Rate_mean', 'Delivery Rate_std_dev']
    excluded_std_dev_columns = [col for col in df.columns if col.endswith('_std_dev')]

    # Combine all columns to exclude
    columns_to_exclude = excluded_columns + excluded_std_dev_columns + [comparison_column]

    # Make sure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Loop through each column except the excluded ones and create scatter plots
    for column in df.columns:
        if column not in columns_to_exclude and pd.api.types.is_numeric_dtype(df[column]):
            # Remove rows where either value is NaN
            valid_data = df[[comparison_column, column]].dropna()
            x = valid_data[comparison_column]
            y = valid_data[column]
            
            # Calculate linear regression
            slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
            line = slope * x + intercept

            # Create scatter plot
            plt.figure()
            plt.scatter(x, y, alpha=0.5, label='Data points')
            plt.plot(x, line, color='red', label=f'Trendline (R² = {r_value**2:.3f})')

            # Add titles and labels
            plt.title(f'{comparison_column} vs {column}')
            plt.xlabel(comparison_column)
            plt.ylabel(column)
            plt.legend()

            # Save the plot
            plot_filename = f'{column}_vs_{comparison_column}.png'
            plot_path = os.path.join(output_dir, plot_filename)
            plt.savefig(plot_path)
            plt.close()
            print(f'Saved scatter plot: {plot_filename}')

# Example usage
if __name__ == "__main__":
    mode = 'human_discriminator'  # Change this to 'human' or 'discriminator'
    input_csv = f'discriminator/scores.csv'  # Path to the input CSV file
    output_dir = f'output_plots/{mode}'  # Directory where the plots will be saved
    os.makedirs(output_dir, exist_ok=True)

    comparison_column = f'{mode}_score'  # Change this to 'human_score' or any other column

    create_scatter_plots(input_csv, output_dir, comparison_column)
