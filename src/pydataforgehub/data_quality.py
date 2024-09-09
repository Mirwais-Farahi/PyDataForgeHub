# src/data_quality.py

import pandas as pd

class DataQualityChecker:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_null_values(self):
        """Check if there are any null values in the dataframe."""
        return self.df.isnull().sum()