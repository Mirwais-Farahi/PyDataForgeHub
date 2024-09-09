# src/data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def group_count(self, group_by_columns: list) -> pd.DataFrame:
        """
        Group by specified columns and count the number of records in each group.
        
        :param group_by_columns: A list of columns to group by.
        :return: A DataFrame with group counts.
        """
        group_counts = self.df.groupby(group_by_columns).size().reset_index(name='record_count')
        return group_counts

    def plot_group_count(self, group_by_columns: list, plot_type: str = 'bar', title: str = 'Group Count'):
        """
        Visualize the group counts with a specified plot type (e.g., 'bar', 'pie').
        
        :param group_by_columns: A list of columns to group by.
        :param plot_type: The type of plot to create ('bar', 'pie', etc.).
        :param title: The title of the plot.
        """
        group_counts = self.group_count(group_by_columns)

        if plot_type == 'bar':
            group_counts.plot(kind='bar', x=group_by_columns[-1], y='record_count', title=title)
        elif plot_type == 'pie':
            group_counts.set_index(group_by_columns[-1])['record_count'].plot(kind='pie', title=title)

        plt.show()

    def plot_time_series(self, date_column: str, freq: str = 'D', title: str = 'Records Over Time'):
        """
        Plot the number of records over time.
        
        :param date_column: The name of the date column.
        :param freq: The frequency to group by (e.g., 'D' for daily, 'W' for weekly).
        :param title: The title of the plot.
        """
        time_counts = self.count_over_time(date_column, freq)
        time_counts.plot(kind='line', x=date_column, y='record_count', title=title)
        plt.show()

    def count_over_time(self, date_column: str, freq: str) -> pd.DataFrame:
        """
        Count the number of records over time by resampling.
        
        :param date_column: The name of the date column.
        :param freq: The frequency to group by (e.g., 'D' for daily, 'W' for weekly).
        :return: A DataFrame with counts over time.
        """
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        time_counts = self.df.resample(freq, on=date_column).size().reset_index(name='record_count')
        return time_counts