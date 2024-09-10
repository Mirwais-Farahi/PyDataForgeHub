# src/data_counter.py

import pandas as pd

def count_by_column(df: pd.DataFrame, column_name: str):
    """
    Count occurrences of each value in the specified column.
    
    :param df: A pandas DataFrame.
    :param column_name: The name of the column to count unique values in.
    :return: A pandas Series with the count of each unique value in the column.
    """
    return df[column_name].value_counts()

def group_count(df: pd.DataFrame, group_by_columns: list):
    """
    Group the data by specified columns and count the number of records in each group.
    
    :param df: A pandas DataFrame.
    :param group_by_columns: A list of column names to group by.
    :return: A pandas DataFrame with group counts.
    """
    return df.groupby(group_by_columns).size().reset_index(name='record_count')

def count_total_records(df: pd.DataFrame):
    """
    Count the total number of records in the DataFrame.
    
    :param df: A pandas DataFrame.
    :return: An integer representing the total number of records.
    """
    return df.shape[0]

def count_over_time(df: pd.DataFrame, date_column: str, freq: str = 'D'):
    """
    Count the number of records over time based on a date column.
    
    :param df: A pandas DataFrame.
    :param date_column: The name of the date column in the DataFrame.
    :param freq: The frequency to group by (e.g., 'D' for daily, 'W' for weekly).
    :return: A pandas DataFrame with counts over time.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    return df.groupby(pd.Grouper(key=date_column, freq=freq)).size().reset_index(name='record_count')