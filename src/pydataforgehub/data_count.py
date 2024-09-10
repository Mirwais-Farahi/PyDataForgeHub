import pandas as pd

def count_total_records(df: pd.DataFrame):
    """
    Count the total number of records in the DataFrame.
    
    :param df: A pandas DataFrame.
    :return: An integer representing the total number of records.
    """
    return df.shape[0]

def count_values(df: pd.DataFrame, column_name: str = None, group_by_columns: list = None):
    """
    Count occurrences of values either in a single column or across multiple group-by columns.
    
    :param df: A pandas DataFrame.
    :param column_name: The name of the column to count unique values in. If None, uses group_by_columns.
    :param group_by_columns: A list of column names to group by. If None, counts unique values in column_name.
    :return: A pandas DataFrame or Series with the count of values.
    """
    if column_name:
        # Count unique values in a single column
        return df[column_name].value_counts()
    elif group_by_columns:
        # Group by specified columns and count the number of records in each group
        return df.groupby(group_by_columns).size().reset_index(name='record_count')
    else:
        raise ValueError("Either column_name or group_by_columns must be provided")

def count_over_time(df: pd.DataFrame, date_column: str, start_date: str = None, end_date: str = None):
    """
    Count the number of records over time based on a date column within a specified date range.
    
    :param df: A pandas DataFrame.
    :param date_column: The name of the date column in the DataFrame.
    :param start_date: The start date for the range in 'YYYY-MM-DD' format. If None, includes all dates from the beginning.
    :param end_date: The end date for the range in 'YYYY-MM-DD' format. If None, includes all dates up to the end.
    :return: A pandas DataFrame with counts over time within the specified date range.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    
    if start_date:
        df = df[df[date_column] >= pd.to_datetime(start_date)]
    if end_date:
        df = df[df[date_column] <= pd.to_datetime(end_date)]
    
    # Count records by date within the range
    return df.groupby(date_column).size().reset_index(name='record_count')

def total_surveys_in_range(df: pd.DataFrame, date_column: str, start_date: str, end_date: str):
    """
    Count the total number of surveys within a specified date range.
    
    :param df: A pandas DataFrame.
    :param date_column: The name of the date column in the DataFrame.
    :param start_date: The start date for the range in 'YYYY-MM-DD' format.
    :param end_date: The end date for the range in 'YYYY-MM-DD' format.
    :return: An integer representing the total number of surveys within the specified date range.
    """
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Filter data based on the date range
    filtered_df = df[(df[date_column] >= pd.to_datetime(start_date)) & (df[date_column] <= pd.to_datetime(end_date))]
    
    # Return the count of records within the filtered range
    return filtered_df.shape[0]