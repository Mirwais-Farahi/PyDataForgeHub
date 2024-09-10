# src/data_analysis.py

import pandas as pd

def correlation_between(df: pd.DataFrame, column1: str, column2: str):
    """
    Calculate the correlation between two columns.
    
    :param df: A pandas DataFrame.
    :param column1: The first column for correlation.
    :param column2: The second column for correlation.
    :return: A float representing the correlation between two columns.
    """
    return df[column1].corr(df[column2])