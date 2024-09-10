# src/data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

def group_count(df: pd.DataFrame, group_by_columns: list):
    """
    Group by specified columns and count the number of records in each group.
    
    :param df: A pandas DataFrame.
    :param group_by_columns: A list of columns to group by.
    :return: A DataFrame with group counts.
    """
    return df.groupby(group_by_columns).size().reset_index(name='record_count')

def plot_group_count(df: pd.DataFrame, group_by_columns: list, plot_type: str = 'bar', title: str = 'Group Count'):
    """
    Visualize the group counts with a specified plot type (e.g., 'bar', 'pie').
    
    :param df: A pandas DataFrame.
    :param group_by_columns: A list of columns to group by.
    :param plot_type: The type of plot to create ('bar', 'pie', etc.).
    :param title: The title of the plot.
    """
    group_counts = group_count(df, group_by_columns)

    if plot_type == 'bar':
        group_counts.plot(kind='bar', x=group_by_columns[-1], y='record_count', title=title)
    elif plot_type == 'pie':
        group_counts.set_index(group_by_columns[-1])['record_count'].plot(kind='pie', title=title)

    plt.show()

def plot_time_series(df: pd.DataFrame, date_column: str, freq: str = 'D', title: str = 'Records Over Time'):
    """
    Plot the number of records over time.
    
    :param df: A pandas DataFrame.
    :param date_column: The name of the date column.
    :param freq: The frequency to group by (e.g., 'D' for daily, 'W' for weekly).
    :param title: The title of the plot.
    """
    # Ensure the date_column is in datetime format
    df[date_column] = pd.to_datetime(df[date_column])

    # Group by the specified frequency (e.g., daily, weekly) and count the number of records
    time_counts = df.set_index(date_column).resample(freq).size().reset_index(name='record_count')

    # Plot the time series
    time_counts.plot(kind='line', x=date_column, y='record_count', title=title)
    plt.show()