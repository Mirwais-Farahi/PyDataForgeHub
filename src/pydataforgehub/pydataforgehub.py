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
        'department': ['HR', 'Engineering', 'HR', 'Engineering', 'HR', 'Finance', 'HR'],
        'date_collected': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07'],
        'enumerator': ['Alice', 'Bob', 'Alice', 'Charlie', 'Alice', 'Charlie', 'Bob']
    }

    df = pd.DataFrame(data)

    # Count occurrences of each value in the 'department' column
    data_counter = DataCounter(df)
    print("\nCount by 'department':")
    print(data_counter.count_by_column('department'))

    # Group by 'department' and 'status' and count the number of records in each group
    print("\nGroup count by 'department' and 'status':")
    print(data_counter.group_count(['department', 'status']))

    # Count total records
    print("\nTotal records count:")
    print(data_counter.count_total_records())

    # Count records over time (daily)
    print("\nRecords count over time (daily):")
    print(data_counter.count_over_time('date_collected', freq='D'))

    # Count surveys collected by each enumerator
    print("\nCount by enumerator:")
    print(data_counter.count_by_enumerator('enumerator'))

    # Create an instance of DataVisualizer
    data_visualizer = DataVisualizer(df)

    # Visualize the group count by department
    print("\nVisualizing group count by 'department':")
    data_visualizer.plot_group_count(['department'], plot_type='bar', title='Group Count by Department')

    # Visualize the records collected over time
    print("\nVisualizing records count over time:")
    data_visualizer.plot_time_series('date_collected', freq='D', title='Records Collected Over Time')

    # Check if there are any null values in the dataframe
    data_quality_checker = DataQualityChecker(df)
    print("\nChecking for null values:")
    print(data_quality_checker.check_null_values())

    # Calculate the correlation between 'age' and 'salary'
    data_analyzer = DataAnalyzer(df)
    print("\nCorrelation between 'age' and 'salary':")
    print(data_analyzer.correlation_between('age', 'salary'))

if __name__ == '__main__':
    main()