# src/pydataforgehub.py

import pandas as pd
import data_count as dc
from data_quality import check_null_values
from data_visualization import plot_group_count, plot_time_series
from data_analysis import correlation_between

def main():
    # Create a sample DataFrame
    data = {
        'age': [23, 45, 12, 35, 25, None, 44],
        'salary': [50000, 62000, 48000, 58000, None, 61000, 70000],
        'department': ['HR', 'Engineering', 'HR', 'Engineering', 'HR', 'Finance', 'HR'],
        'date_collected': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-08'],
    }

    df = pd.DataFrame(data)

    # Count occurrences of each value in the 'department' column
    print("\nCount by 'department':")
    print(dc.count_by_column(df, 'department'))

    # Group by 'department' and count the number of records in each group
    print("\nGroup count by 'department':")
    print(dc.group_count(df, ['department']))

    # Count total records
    print("\nTotal records count:")
    print(dc.count_total_records(df))

    # Count records over time (daily)
    print("\nRecords count over time (daily):")
    print(dc.count_over_time(df, 'date_collected', freq='D'))

    # Visualize the group count by department
    print("\nVisualizing group count by 'department':")
    plot_group_count(df, ['department'], plot_type='bar', title='Group Count by Department')

    # Visualize the records collected over time
    print("\nVisualizing records count over time:")
    plot_time_series(df, 'date_collected', freq='D', title='Records Collected Over Time')

    # Check if there are any null values in the dataframe
    print("\nChecking for null values:")
    print(check_null_values(df))

    # Calculate the correlation between 'age' and 'salary'
    print("\nCorrelation between 'age' and 'salary':")
    print(correlation_between(df, 'age', 'salary'))

if __name__ == '__main__':
    main()