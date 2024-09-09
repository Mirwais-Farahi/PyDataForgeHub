"""Main module."""
# src/pydataforgehub.py

import pandas as pd
from data_count import DataCounter
from data_quality import DataQualityChecker
from data_visualization import DataVisualizer
from data_analysis import DataAnalyzer

def main():

    # Create a sample DataFrame
    data = {
        'age': [23, 45, 12, 35, 25, None, 44],
        'salary': [50000, 62000, 48000, 58000, None, 61000, 70000],
        'department': ['HR', 'Engineering', 'HR', 'Engineering', 'HR', 'Finance', 'HR']
    }

    df = pd.DataFrame(data)

    # Count occurrences of each value in the specified column
    data_counter = DataCounter(df)
    print(data_counter.count_by_column('department'))

    # Check if there are any null values in the dataframe
    data_quality_checker = DataQualityChecker(df)
    print(data_quality_checker.check_null_values())

    # Plot a histogram of the specified column
    data_visualizer = DataVisualizer(df)
    data_visualizer.plot_histogram('age')

    # Calculate the correlation between two columns
    data_analyzer = DataAnalyzer(df)
    print(data_analyzer.correlation_between('age', 'salary'))

if __name__ == '__main__':
    main()