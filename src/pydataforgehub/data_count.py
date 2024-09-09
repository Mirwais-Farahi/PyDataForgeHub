# src/data_counter.py

import pandas as pd
import matplotlib.pyplot as plt

class DataCounter:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize DataCounter with a DataFrame.
        
        :param df: A pandas DataFrame containing the dataset.
        """
        self.df = df

    def count_by_column(self, column_name: str):
        """
        Count occurrences of each value in the specified column.
        
        :param column_name: The name of the column to count unique values in.
        :return: A pandas Series with the count of each unique value in the column.
        """
        return self.df[column_name].value_counts()

    def group_count(self, group_by_columns: list):
        """
        Group the data by specified columns and count the number of records in each group.
        
        :param group_by_columns: A list of column names to group by.
        :return: A pandas DataFrame with group counts.
        """
        return self.df.groupby(group_by_columns).size().reset_index(name='record_count')

    def count_total_records(self):
        """
        Count the total number of records in the DataFrame.
        
        :return: An integer representing the total number of records.
        """
        return self.df.shape[0]

    def count_over_time(self, date_column: str, freq: str = 'D'):
        """
        Count the number of records over time based on a date column.
        
        :param date_column: The name of the date column in the DataFrame.
        :param freq: The frequency to group by (e.g., 'D' for daily, 'W' for weekly).
        :return: A pandas DataFrame with counts over time.
        """
        self.df[date_column] = pd.to_datetime(self.df[date_column])
        return self.df.groupby(pd.Grouper(key=date_column, freq=freq)).size().reset_index(name='record_count')

    def count_by_enumerator(self, enumerator_column: str):
        """
        Count the number of records collected by each enumerator.
        
        :param enumerator_column: The name of the enumerator column.
        :return: A pandas DataFrame with enumerator counts.
        """
        return self.df.groupby(enumerator_column).size().reset_index(name='record_count')