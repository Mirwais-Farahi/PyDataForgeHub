import pandas as pd
import data_count as dc
from data_quality import check_null_values
from data_visualization import plot_group_count, plot_time_series
from data_analysis import correlation_between

def main():
    # Create a sample DataFrame with an additional 'directorate' column
    data = {
        'age': [23, 45, 12, 35, 25, None, 44],
        'salary': [50000, 62000, 48000, 58000, None, 61000, 70000],
        'department': ['HR', 'Engineering', 'HR', 'Engineering', 'HR', 'Finance', 'HR'],
        'directorate': ['A', 'B', 'A', 'B', 'C', 'C', 'A'],  # Added directorate names
        'date_collected': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-08'],
    }

    df = pd.DataFrame(data)

    # Count occurrences of each value in the 'department' column
    print("\nCount by 'department':")
    print(dc.count_values(df, column_name='department'))

    # Group by 'department' and 'directorate' and count the number of records in each group
    print("\nGroup count by 'department' and 'directorate':")
    print(dc.count_values(df, group_by_columns=['department', 'directorate']))

    # Count total records
    print("\nTotal records count:")
    print(dc.count_total_records(df))

    # Count records over time within a specific date range
    print("\nRecords count over time within a date range:")
    print(dc.count_over_time(df, 'date_collected', start_date='2023-01-01', end_date='2023-01-31'))

    # Total number of surveys within a specific date range
    print("\nTotal number of surveys within a date range:")
    print(dc.total_surveys_in_range(df, 'date_collected', start_date='2023-01-01', end_date='2023-01-31'))

    # Visualize the group count by department and directorate
    print("\nVisualizing group count by 'department' and 'directorate':")
    plot_group_count(df, ['department', 'directorate'], plot_type='bar', title='Group Count by Department and Directorate')

    # Visualize the records collected over time
    print("\nVisualizing records count over time:")
    plot_time_series(df, 'date_collected', title='Records Collected Over Time')

    # Check if there are any null values in the dataframe
    print("\nChecking for null values:")
    print(check_null_values(df))

    # Calculate the correlation between 'age' and 'salary'
    print("\nCorrelation between 'age' and 'salary':")
    print(correlation_between(df, 'age', 'salary'))

if __name__ == '__main__':
    main()