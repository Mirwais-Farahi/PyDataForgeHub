# src/data_quality.py

import pandas as pd

def check_null_values(df: pd.DataFrame):
    """
    Check if there are any null values in the DataFrame.
    
    :param df: A pandas DataFrame.
    :return: A pandas Series representing the count of null values in each column.
    """
    return df.isnull().sum()